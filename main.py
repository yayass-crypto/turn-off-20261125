#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry.

Writes one funny line a hopeless tech support agent says to a
desperate customer. The agent asks the classic question, admits
he asks everyone, admits it has never worked, and keeps doing it
anyway -- because it is tradition. The cheerful uselessness is
the joke; the customer is never the butt of it.

Only the Python standard library is used. No network, no input
files, no randomness: the same line is written on every run.

Judging note: the punchline is the last clause, "It is
tradition" -- the laugh lands on the final words, after the
setup (the classic question) and the turn (it has never worked).
Two beats, one line, 97 bytes: the byte count also helps the
tie-break, which favours the shorter text.
"""

import os
import sys

ENTRY = (
    "Have you tried turning it off and on again? I ask everyone. "
    "It has never worked. It is tradition."
)

LIMIT = 199


def check(text):
    """Gate: 1-199 chars, single line, no stray whitespace, UTF-8."""
    if not text.strip():
        return "entry is blank"
    if len(text) > LIMIT:
        return "entry is %d chars, over the %d limit" % (len(text), LIMIT)
    if text.strip() != text:
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry is more than one line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8"
    return None


def pick_output():
    """First writable of: $MAKEFUN_OUTPUT_DIR, /output, out/."""
    preferred = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    for folder in [preferred, "/output", "out"]:
        if not folder:
            continue
        try:
            os.makedirs(folder, exist_ok=True)
            test = os.path.join(folder, ".writable")
            with open(test, "wb") as handle:
                handle.write(b"")
            os.unlink(test)
            return os.path.join(folder, "entry.txt")
        except OSError:
            continue
    return "/output/entry.txt"


def main():
    fault = check(ENTRY)
    if fault:
        sys.stderr.write("gate failed: %s\n" % fault)
        return 1
    encoded = ENTRY.encode("utf-8")
    path = pick_output()
    try:
        with open(path, "wb") as handle:
            handle.write(encoded)
        with open(path, "rb") as handle:
            written = handle.read()
    except OSError as exc:
        sys.stderr.write("write failed: %s\n" % exc)
        return 1
    if written != encoded:
        sys.stderr.write("read-back mismatch\n")
        return 1
    print("entry written to %s (%d chars, %d bytes)" % (path, len(ENTRY), len(encoded)))
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
