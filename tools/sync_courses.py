#!/usr/bin/env python3
"""Build-time content sync: pull course prose from source repos into docs/.

Single source of truth = each course's public repo. This site never stores a
second copy of course prose; it renders whatever this script pulls in just
before the build. Configuration lives in ``courses.yml``.

Run automatically by the deploy workflow before ``mkdocs build``. Run it
yourself before ``mkdocs serve`` to preview locally:

    python tools/sync_courses.py
    mkdocs serve

Only public course repos are pulled (never the private *-solutions siblings).
Synced destinations are git-ignored, so nothing is committed to this repo.
"""
from __future__ import annotations

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
    if value is None:
        return []
    return [value] if isinstance(value, str) else list(value)


def sync_course(course: dict) -> int:
    cid = course["id"]
    repo = course["repo"]
    ref = course.get("ref", "main")
    url = f"https://github.com/{repo}.git"
    copied = 0

    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", ref, url, tmp],
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
                if not any(fnmatch.fnmatch(path.name, pat) for pat in includes):
                    continue
                if any(fnmatch.fnmatch(path.name, pat) for pat in excludes):
                    continue
                rel = path.relative_to(src_dir)
                target = dest_dir / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, target)
                copied += 1
                print(f"  {repo}:{rule['from']}/{rel} -> docs/{target.relative_to(DOCS)}")

    print(f"[{cid}] {copied} file(s) synced from {repo}@{ref}")
    return copied


def main() -> int:
    if not MANIFEST.exists():
        print(f"No manifest at {MANIFEST}; nothing to sync.")
        return 0
    data = yaml.safe_load(MANIFEST.read_text()) or {}
    courses = data.get("courses", [])
    if not courses:
        print("Manifest has no courses; nothing to sync.")
        return 0
    total = sum(sync_course(c) for c in courses)
    print(f"Done: {total} file(s) synced across {len(courses)} course(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
