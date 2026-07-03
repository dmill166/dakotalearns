#!/usr/bin/env python3
"""Build-time content sync: pull course prose from source repos into docs/.

Single source of truth = each course's public repo. This site never stores a
second copy of course prose; it renders whatever this script pulls in just
before the build. Configuration lives in ``courses.yml``.

Run automatically by the deploy workflow before ``mkdocs build``. Run it
yourself before ``mkdocs serve`` to preview locally:

    python tools/sync_courses.py
    mkdocs serve

To preview UNPUSHED local course work, point a course id at a local clone —
files come from that working tree instead of a fresh GitHub clone:

    python tools/sync_courses.py \
        --local computer-science-1=~/dev/computer-science-1

Page dates: for every synced ``*.md`` page, the source repo's real git history
is stamped into front-matter as ``date_published`` (first commit) and
``date_updated`` (last commit) — the site repo has no history for synced files,
so a build-time plugin would wrongly show the build date. The theme override
(``overrides/main.html``) renders the line. A page opts out with
``page_dates: false`` in its front-matter; uncommitted files simply get no
dates. Clones are full-history (dates need the log), not ``--depth 1``.

Only public course repos are pulled (never the private *-solutions siblings).
Synced destinations are git-ignored, so nothing is committed to this repo.
"""
from __future__ import annotations

import argparse
import fnmatch
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml  # provided by MkDocs (PyYAML); no extra dependency needed

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MANIFEST = ROOT / "courses.yml"


def _as_list(value) -> list[str]:
    """Normalize a manifest value (None, string, or list) to a list."""
    if value is None:
        return []
    return [value] if isinstance(value, str) else list(value)


def _git_dates(repo: Path, rel: str) -> tuple[str | None, str | None]:
    """(first_commit_date, last_commit_date) as YYYY-MM-DD, or (None, None)."""
    out = subprocess.run(
        ["git", "-C", str(repo), "log", "--follow", "--format=%as", "--", rel],
        capture_output=True,
        text=True,
    ).stdout.split()
    if not out:
        return None, None
    return out[-1], out[0]


def _inject_dates(target: Path, src_repo: Path, rel: str) -> None:
    """Stamp date_published/date_updated into a synced page's front-matter."""
    if target.suffix != ".md":
        return
    text = target.read_text(encoding="utf-8")
    head = text[:1000]
    if "page_dates: false" in head:
        return  # page opted out
    published, updated = _git_dates(src_repo, rel)
    if not published:
        return  # uncommitted file — no history to report
    # Each key is stamped independently: a hand-set date_published in the
    # source front-matter is honored (e.g. backdating a migrated page)
    # while date_updated keeps tracking real git history — and vice versa.
    lines = []
    if "date_published:" not in head:
        lines.append(f"date_published: {published}")
    if "date_updated:" not in head:
        lines.append(f"date_updated: {updated}")
    if not lines:
        return  # page carries both dates itself
    block = "\n".join(lines) + "\n"
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end == -1:
            return  # malformed front-matter; leave the page alone
        text = text[:end + 1] + block + text[end + 1:]
    else:
        text = f"---\n{block}---\n\n{text}"
    target.write_text(text, encoding="utf-8")


def sync_course(course: dict, local: dict[str, Path]) -> int:
    """Copy one course's content into docs/ per its manifest rules.

    Clones the course repo (full history, for date stamping) — or uses a
    local working tree if `local` maps this course id to a path — then
    applies each sync rule's include/exclude globs and stamps page dates.
    Returns the number of files copied.
    """
    cid = course["id"]
    repo = course["repo"]
    ref = course.get("ref", "main")
    url = f"https://github.com/{repo}.git"
    copied = 0

    with tempfile.TemporaryDirectory() as tmp:
        if cid in local:
            src_root = local[cid]
            print(
                f"[{cid}] using LOCAL working tree {src_root} "
                "(preview mode)"
            )
        else:
            subprocess.run(
                ["git", "clone", "--branch", ref, url, tmp],
                check=True,
            )
            src_root = Path(tmp)

        for rule in course.get("sync", []):
            src_dir = src_root / rule["from"]
            dest_dir = DOCS / rule["to"]
            includes = _as_list(rule.get("include", "*"))
            excludes = _as_list(rule.get("exclude"))

            if not src_dir.is_dir():
                print(f"  (skip) {repo}:{rule['from']} — not present")
                continue

            # Clean the destination so a removal in the source is reflected.
            if dest_dir.exists():
                shutil.rmtree(dest_dir)

            for path in sorted(src_dir.rglob("*")):
                if not path.is_file():
                    continue
                included = (
                    fnmatch.fnmatch(path.name, pat) for pat in includes
                )
                if not any(included):
                    continue
                if any(fnmatch.fnmatch(path.name, pat) for pat in excludes):
                    continue
                rel = path.relative_to(src_dir)
                target = dest_dir / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, target)
                repo_rel = str(path.relative_to(src_root))
                _inject_dates(target, src_root, repo_rel)
                copied += 1
                dest_rel = target.relative_to(DOCS)
                print(f"  {repo}:{rule['from']}/{rel} -> docs/{dest_rel}")

    print(f"[{cid}] {copied} file(s) synced from {repo}@{ref}")
    return copied


def main() -> int:
    """Parse CLI args, read the manifest, and sync every course."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--local",
        action="append",
        default=[],
        metavar="ID=PATH",
        help="sync course ID from a local clone at PATH instead of GitHub "
        "(preview unpushed work); repeatable",
    )
    args = parser.parse_args()
    local: dict[str, Path] = {}
    for spec in args.local:
        cid, _, p = spec.partition("=")
        local[cid] = Path(p).expanduser().resolve()

    if not MANIFEST.exists():
        print(f"No manifest at {MANIFEST}; nothing to sync.")
        return 0
    data = yaml.safe_load(MANIFEST.read_text()) or {}
    courses = data.get("courses", [])
    if not courses:
        print("Manifest has no courses; nothing to sync.")
        return 0
    total = sum(sync_course(c, local) for c in courses)
    print(f"Done: {total} file(s) synced across {len(courses)} course(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
