#!/usr/bin/env python3
"""Regenerate the cache version and file list in sw.js.

Run it in the app folder after changing any file:

    python3 update-sw.py            # update sw.js
    python3 update-sw.py --check    # only report whether sw.js is up to date

The version is the first 10 hex characters of a SHA-256 hash over the
contents of all app files, in this order: index.html, manifest.webmanifest,
then every other file sorted by path. sw.js itself, README.md, this script
and hidden files are not part of the app and are skipped.
Uses only the Python standard library (3.8+).
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SW = ROOT / "sw.js"
SKIP = {"sw.js", "README.md", Path(__file__).name}
FIRST = ["index.html", "manifest.webmanifest"]


def app_files():
    rest = sorted(
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file()
        and not any(part.startswith(".") for part in p.relative_to(ROOT).parts)
        and p.relative_to(ROOT).as_posix() not in SKIP
        and p.relative_to(ROOT).as_posix() not in FIRST
        and p.suffix != ".zip"
    )
    missing = [f for f in FIRST if not (ROOT / f).is_file()]
    if missing:
        sys.exit("Missing: " + ", ".join(missing))
    return FIRST + rest


def main():
    if not SW.is_file():
        sys.exit("sw.js not found next to this script")
    files = app_files()
    h = hashlib.sha256()
    for f in files:
        h.update((ROOT / f).read_bytes())
    version = h.hexdigest()[:10]
    assets = ["./"] + ["./" + f for f in files]

    src = SW.read_text(encoding="utf-8")
    old = re.search(r'const VERSION = "([^"]*)";', src)
    if not old or not re.search(r"const ASSETS = \[.*?\];", src, re.S):
        sys.exit("sw.js does not contain the VERSION / ASSETS lines")

    new = re.sub(r'const VERSION = "[^"]*";', 'const VERSION = "%s";' % version, src, count=1)
    new = re.sub(r"const ASSETS = \[.*?\];", lambda m: "const ASSETS = %s;" % json.dumps(assets), new, count=1, flags=re.S)

    if "--check" in sys.argv:
        if new == src:
            print("sw.js is up to date (version %s)" % version)
            return
        print("sw.js is out of date: %s -> %s" % (old.group(1), version))
        sys.exit(1)

    if new == src:
        print("No change, version %s" % version)
        return
    SW.write_text(new, encoding="utf-8")
    print("sw.js updated: %s -> %s (%d files cached)" % (old.group(1), version, len(assets)))


if __name__ == "__main__":
    main()
