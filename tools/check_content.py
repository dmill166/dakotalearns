#!/usr/bin/env python3
"""Publish-lock + accessibility gate for built content.

Runs AFTER ``tools/sync_courses.py`` and BEFORE ``mkdocs build`` so it sees
every publishable page at once: the site-native docs AND the course prose
synced in from each course repo. Hard-exits non-zero if any check fails, so
the deploy workflow refuses to publish a page that isn't ready.

Two check groups (they ride together — the a11y checks land with the
publish-lock gate, per cs-teaching/a11y.md "Enforce it"):

Publish-lock (oneshot_build_requirements.md A2 / gate 1)
    Fail if any page still carries ``author_status: dakota-voice-draft``.
    The marker is an HTML comment — greppable, renders invisibly — so a
    voice-core draft can never silently ship as if Dakota finalized it.
    (``draft: true`` front-matter is inert for non-blog pages, which is why
    this is a content grep and not a front-matter flag; see §10.)

Marker coverage (provenance convention, locked 2026-07-09)
    Every published page must carry at least one valid ``author_status``
    marker (``dakota-authored`` / ``dakota-voice-draft`` /
    ``assistant-mechanical`` / ``assistant-shared``). There is
    deliberately NO exempt class: these are Dakota's public works, and
    every page gets at least a light voice pass and his hand before it
    counts as his (his call, 2026-07-09). An unmarked page used to pass
    silently — "unmarked" meant "invisible to this gate," not
    "voice-verified" — so unmarked is now a hard fail, and a marker with
    an unrecognized value fails too (typo protection). ``docs/blog/`` is
    excluded: the blog is Dakota's voice by definition, and blog drafts
    are already held back by ``draft: true``. Canonical convention doc:
    ``cs-teaching/voice_provenance.md`` (this implementation is
    deliberately vendored per repo — zero cross-repo CI dependency).

Accessibility (cs-teaching/a11y.md)
    * Every ``mermaid`` diagram must carry an ``accDescr`` (its text
      alternative; ``accTitle`` alone does not describe the figure).
    * Every raw ``<img>`` must carry an ``alt`` attribute (``alt=""`` is
      allowed for a provably decorative image).

Run it yourself before a local strict build:

    python tools/sync_courses.py \
        --local computer-science-1=~/dev/computer-science-1
    python tools/check_content.py
    mkdocs build --strict
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml  # provided by MkDocs (PyYAML); no extra dependency needed

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# The one author_status value that must never reach a published page.
DRAFT_MARKER = "author_status: dakota-voice-draft"

# The provenance values a published page may carry. Every page outside
# docs/blog/ must carry at least one (marker-coverage convention,
# locked 2026-07-09; no exempt class — Dakota, same day); any other
# value after ``author_status:`` is a typo and fails the gate.
VALID_STATUSES = (
    "dakota-authored",
    "dakota-voice-draft",
    "assistant-mechanical",
    "assistant-shared",
)
STATUS_MARKER = re.compile(
    r"author_status:\s*([A-Za-z-]+)"
)

# Naming rule: site-native pages never mention a university course
# code — our courses are named by subject; codes belong only in
# reviewed alignment contexts. The CODES ARE DATA, not code: each
# course's ``alignment_codes`` list in ``courses.yml`` feeds this
# check, so onboarding a course extends the gate automatically.
# Exclusions: docs/blog/ (Dakota's historical posts),
# docs/disclaimers.md (carries the quoted example explaining the
# rule), docs/courses/ (synced course prose — its mentions are
# governed by each course repo's baseline ratchet, integrity_scan
# check v).
MANIFEST = ROOT / "courses.yml"
NAME_EXEMPT_PARTS = ("blog", "courses")
NAME_EXEMPT_FILES = ("disclaimers.md",)


def load_name_token() -> re.Pattern | None:
    """Build the forbidden-course-code pattern from courses.yml.

    Returns:
        A compiled alternation of every course's alignment_codes, or
        None when the manifest is missing or lists no codes (the
        naming check is then skipped rather than guessed at).
    """
    if not MANIFEST.is_file():
        return None
    manifest = yaml.safe_load(MANIFEST.read_text()) or {}
    patterns = []
    for course in manifest.get("courses", []):
        patterns += course.get("alignment_codes", [])
    if not patterns:
        return None
    return re.compile("|".join(patterns), re.IGNORECASE)


# A raw <img ...> tag (may span lines: [^>] also matches newlines).
IMG_TAG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
# Opening fence of a mermaid block, e.g. ```mermaid (optionally indented).
MERMAID_OPEN = re.compile(r"^\s*```+\s*mermaid\b")
# Any closing code fence.
FENCE_CLOSE = re.compile(r"^\s*```+\s*$")


class Violation:
    """One failed check, anchored to a file and 1-indexed line."""

    def __init__(self, path: Path, line: int, message: str) -> None:
        self.path = path
        self.line = line
        self.message = message

    def format(self) -> str:
        """Render as a clickable ``path:line — message`` report line."""
        rel = self.path.relative_to(ROOT)
        return f"  {rel}:{self.line} — {self.message}"


def _line_of(text: str, index: int) -> int:
    """Return the 1-indexed line number of a character offset."""
    return text.count("\n", 0, index) + 1


def check_publish_lock(path: Path, text: str) -> list[Violation]:
    """Fail on any surviving dakota-voice-draft marker in the page.

    Returns:
        One violation per draft-marker line; empty means the page
        passes.
    """
    found = []
    for i, line in enumerate(text.splitlines(), start=1):
        if DRAFT_MARKER in line:
            found.append(
                Violation(
                    path,
                    i,
                    "unpromoted voice-core draft (author_status: "
                    "dakota-voice-draft) — promote to dakota-authored "
                    "before publishing",
                )
            )
    return found


def check_marker_coverage(path: Path, text: str) -> list[Violation]:
    """Fail an unmarked page, and any marker with an invalid value.

    "Unmarked" must mean "impossible," not "invisible to the gate": a
    page with no ``author_status`` marker at all is a hard fail, as is a
    marker whose value isn't in ``VALID_STATUSES`` (typo protection).

    Returns:
        One violation for a missing marker plus one per invalid
        value; empty means the page passes.
    """
    found = []
    matches = STATUS_MARKER.findall(text)
    if not matches:
        found.append(
            Violation(
                path,
                1,
                "page carries no author_status marker — add "
                "dakota-authored / dakota-voice-draft / assistant-*, "
                "per cs-teaching/voice_provenance.md",
            )
        )
    for value in matches:
        if value not in VALID_STATUSES:
            found.append(
                Violation(
                    path,
                    1,
                    f"unrecognized author_status value {value!r} — "
                    f"expected one of {', '.join(VALID_STATUSES)}",
                )
            )
    return found


def check_no_course_codes(
    path: Path, text: str, token: re.Pattern
) -> list[Violation]:
    """Fail any site-native page mentioning a university course code.

    Args:
        path: The page being checked.
        text: The page's content.
        token: Compiled alternation of every course's alignment codes
            (from courses.yml via load_name_token).

    Returns:
        One violation per mentioning line; empty means the page
        passes.
    """
    found = []
    for i, line in enumerate(text.splitlines(), start=1):
        match = token.search(line)
        if match:
            found.append(
                Violation(
                    path,
                    i,
                    f"mentions university course code "
                    f"{match.group(0)!r} — our courses are named by "
                    "subject; codes live only in reviewed alignment "
                    "contexts (see the naming rule)",
                )
            )
    return found


def check_mermaid_accdescr(path: Path, text: str) -> list[Violation]:
    """Fail on any mermaid diagram missing an accDescr text alternative.

    Returns:
        One violation per diagram without an accDescr, anchored to
        its opening fence; empty means the page passes.
    """
    found = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if MERMAID_OPEN.match(lines[i]):
            open_line = i + 1
            has_accdescr = False
            i += 1
            while i < len(lines) and not FENCE_CLOSE.match(lines[i]):
                if "accDescr" in lines[i]:
                    has_accdescr = True
                i += 1
            if not has_accdescr:
                found.append(
                    Violation(
                        path,
                        open_line,
                        "mermaid diagram has no accDescr (required text "
                        "alternative — see cs-teaching/a11y.md)",
                    )
                )
        i += 1
    return found


def check_img_alt(path: Path, text: str) -> list[Violation]:
    """Fail on any raw <img> tag lacking an alt attribute.

    Returns:
        One violation per alt-less <img> tag; empty means the page
        passes.
    """
    found = []
    for match in IMG_TAG.finditer(text):
        if not re.search(r"\balt\s*=", match.group(0), re.IGNORECASE):
            found.append(
                Violation(
                    path,
                    _line_of(text, match.start()),
                    "<img> tag has no alt attribute (use alt=\"\" if "
                    "the image is purely decorative)",
                )
            )
    return found


def scan(docs: Path) -> list[Violation]:
    """Run every check over every markdown page under ``docs``.

    Returns:
        All violations found across the tree; empty means the gate
        passes.
    """
    violations: list[Violation] = []
    name_token = load_name_token()
    for path in sorted(docs.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        violations += check_publish_lock(path, text)
        rel_parts = path.relative_to(docs).parts
        if "blog" not in rel_parts:
            violations += check_marker_coverage(path, text)
        if (name_token is not None
                and not any(p in rel_parts for p in NAME_EXEMPT_PARTS)
                and path.name not in NAME_EXEMPT_FILES):
            violations += check_no_course_codes(path, text, name_token)
        violations += check_mermaid_accdescr(path, text)
        violations += check_img_alt(path, text)
    return violations


def main() -> int:
    """Scan the docs tree and report violations.

    Returns:
        Process exit code: 0 when the gate passes (or there is no
        docs directory to scan), 1 when any check fails.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--docs",
        type=Path,
        default=DOCS,
        help="docs directory to scan (default: the site's docs/)",
    )
    args = parser.parse_args()

    if not args.docs.is_dir():
        print(f"No docs directory at {args.docs}; nothing to check.")
        return 0

    violations = scan(args.docs)
    if not violations:
        print("Content gate: PASS — no draft markers or a11y gaps found.")
        return 0

    print(f"Content gate: FAIL — {len(violations)} issue(s):\n")
    for v in violations:
        print(v.format())
    print(
        "\nFix the issues above (promote drafts, add accDescr/alt) and "
        "re-run. This gate blocks the site build on purpose."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
