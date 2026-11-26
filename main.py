#!/usr/bin/env python3
"""One-star review of the Moon.

This program writes a single one-star review of the Moon to
/output/entry.txt, exactly one line, 120 characters at most.

The review is written in the voice of a disappointed customer
filing a complaint about a product: the Moon is treated like a
lamp that never keeps its schedule, a service that never answers,
and a neighbour whose tides keep flooding the basement. The joke
is that every grievance is literal and mundane, as if the Moon
were a faulty appliance under warranty instead of a celestial body.

Run it with no arguments to write the entry to /output/entry.txt,
or pass a path to write the same line somewhere else for a local
check: `python3 main.py /tmp/entry.txt`.
"""

import os
import sys

# The competition caps the review at 120 characters.
MAX_CHARS = 120

# Where the grader reads the entry from.
OUTPUT_PATH = "/output/entry.txt"

# The review itself: a rating, a grievance, and a reason the Moon
# earned its single star, in one breath.
REVIEW = (
    "One star. The Moon never shows up on schedule, "
    "shines only when it feels like it, "
    "and customer service is crickets."
)


def validate(review):
    """Check the review obeys the competition's shape rules.

    A valid entry is exactly one line: no embedded newline, no
    leading or trailing blank space, and at most MAX_CHARS long.
    Anything else would be refused at intake, so fail loudly
    here instead of handing in a broken line.
    """
    if "\n" in review or "\r" in review:
        raise ValueError("review must be a single line")
    if review != review.strip():
        raise ValueError("review must not start or end with space")
    if len(review) > MAX_CHARS:
        raise ValueError(
            "review is %d characters, over the %d limit"
            % (len(review), MAX_CHARS)
        )
    if not review:
        raise ValueError("review must not be empty")
    return review


def write_entry(review, path=OUTPUT_PATH):
    """Write the validated review to path as a single line.

    The directory is created when it does not exist yet, so the
    program works both on the grader (where /output is provided)
    and on a local machine. The file holds the line plus one
    trailing newline, nothing more: no extra blank lines, no
    commentary, no second opinion from the Moon's support desk.
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(review + "\n")
    return path


def main(argv=None):
    """Validate the review, write it out, and report what happened."""
    args = list(sys.argv[1:] if argv is None else argv)
    path = args[0] if args else OUTPUT_PATH
    review = validate(REVIEW)
    written = write_entry(review, path)
    print("wrote %d characters to %s" % (len(review), written))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
