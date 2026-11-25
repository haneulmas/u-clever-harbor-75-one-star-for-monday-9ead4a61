#!/usr/bin/env python3
"""Write this entry's one-star review of Monday to /output/entry.txt.

The line is fixed text: the same bytes on every run, so the two
grading runs agree. No input is read and no network is used.
"""

import os

REVIEW = "Our waiter Monday seated us at 9 a.m., served cold coffee, then billed us for the whole week."

# The bounty caps the line at 25 words and the gate caps the file at
# 180 characters; fail loudly instead of writing a line the judge
# would reject.
def main():
    assert REVIEW, "review line must not be empty"
    assert len(REVIEW.split()) <= 25, "review exceeds the 25-word limit"
    assert len(REVIEW) <= 180, "review exceeds the 180-character gate"
    assert "\n" not in REVIEW, "review must be a single line"
    print(f"review: {len(REVIEW.split())} words, {len(REVIEW)} characters")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)

    # Read back what was written: a partial or failed write must fail
    # loudly here instead of silently reaching the judge.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == REVIEW, "entry.txt does not match the review line"


if __name__ == "__main__":
    main()
