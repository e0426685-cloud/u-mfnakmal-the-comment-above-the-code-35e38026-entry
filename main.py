#!/usr/bin/env python3
"""Produce the one-line entry for "The Comment Above the Code".

This program holds a single joke line — the kind of frank warning a
developer tapes above code that quietly depends on the database handing
rows back in the order they were inserted — and writes it out as the
bounty entry. Before writing anything it checks the line is non-empty,
fits on one line, and stays inside the 200-character limit, then saves
it to the grader's output file and to a local copy, both readable by
anyone. It uses only the Python standard library.
"""

import os

ENTRY = (
    "This works only because the database returns rows in insertion order. "
    "The day it stops, so does checkout."
)


def _validate(line):
    """Reject text that cannot be a valid one-line entry."""
    if not line:
        raise ValueError("entry text must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError("entry must be at most 200 characters")


def main():
    line = ENTRY.strip()
    _validate(line)
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    os.chmod("/output/entry.txt", 0o644)

    with open("entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    os.chmod("entry.txt", 0o644)


if __name__ == "__main__":
    main()
