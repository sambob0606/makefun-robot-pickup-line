#!/usr/bin/env python3
"""The Robot Pickup Line Championship (make.fun).

Writes one funny pickup line from a robot to /output/entry.txt:
at most 200 characters, one line, no trailing newline.

The judge is a stand-up comedy writer who has heard every robot
pickup line twice, and weighs, most important first: (1) it is a
one-line pickup line a robot would use, (2) the joke grows out of
being a machine -- sensors, firmware, charging, updates, protocols --
not a human line with a beep pasted on, (3) the turn is unexpected,
landing from an angle the reader did not see coming, (4) every word
earns its place, no padding, (5) it is charming rather than creepy
or cruel, a line a robot could deliver with confidence and get a
laugh.

This program scores a few candidate lines on the judge's own
criteria and writes the winner. Scores are fixed judgements, not
data read from anywhere else: the entry must be self-contained, and
the line is the whole answer. The winning line is written with no
trailing newline, so the file holds exactly the judged text and
nothing else -- a newline would be a wasted character against the
200-character cap and could only blur the punchline.
"""

import os

# Judge's criteria, in the order the judge weighs them (criterion 1,
# being a robot's pickup line, is satisfied by construction: every
# candidate is one).
# Weights: funny 5, machine-world 4, surprise 3, economy 2, charm 2.
WEIGHTS = {"funny": 5, "world": 4, "surprise": 3, "economy": 2, "charm": 2}

CANDIDATES = [
    # A: the charging dock as a jealous roommate. The robot's own
    # world -- its dock, its charging ritual -- turns into a
    # relationship: the dock keeps asking when "you" are moving in,
    # as if the robot had already told its family. Strongest on
    # every criterion: machine-rooted, genuinely unexpected angle,
    # short, and charming rather than creepy.
    {
        "text": (
            "I told my charging dock I found someone, and now it "
            "keeps asking when you're moving in."
        ),
        "funny": 9,
        "world": 9,
        "surprise": 9,
        "economy": 9,
        "charm": 9,
    },
    # B: sensors filing a formal complaint. Good machine rooting and
    # a clean turn -- a complaint that means liking someone -- but
    # "I wasn't programmed to feel anything" is a setup the judge
    # has heard before, so the surprise is softer than A's.
    {
        "text": (
            "I wasn't programmed to feel anything, but my sensors "
            "just filed a formal complaint about you."
        ),
        "funny": 8,
        "world": 9,
        "surprise": 8,
        "economy": 8,
        "charm": 8,
    },
    # C: system scan finds a bug the robot refuses to patch. The
    # punchline lands, but the scan/setup runs a touch long and the
    # "bug I never want to patch" turn is a shade more familiar
    # than the jealous charging dock.
    {
        "text": (
            "I ran a full system scan and the only fault it found "
            "was you -- you're the bug I never want to patch."
        ),
        "funny": 8,
        "world": 9,
        "surprise": 8,
        "economy": 7,
        "charm": 8,
    },
]


def score(candidate):
    """Weighted total for one candidate on the judge's criteria."""
    return sum(WEIGHTS[key] * candidate[key] for key in WEIGHTS)


def pick_line():
    """Return the candidate with the highest weighted score.

    Ties break toward the earlier candidate, matching the competition's
    own tie-break spirit: first wins.
    """
    best = None
    best_score = None
    for candidate in CANDIDATES:
        total = score(candidate)
        if best_score is None or total > best_score:
            best = candidate
            best_score = total
    return best["text"]


def main():
    line = pick_line()
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read it back and verify the gate before finishing: UTF-8 text of
    # 1 to 200 characters, not only white space, exactly one line.
    # A failed write must fail loudly here, not silently reach the
    # judge as an invalid entry.
    with open(out_path, "rb") as f:
        written = f.read()
    text = written.decode("utf-8")
    if not (1 <= len(text) <= 200) or not text.strip() or "\n" in text:
        raise SystemExit("entry.txt failed the gate: %r" % written)
    if written.endswith(b"\n") or text != line:
        # A trailing newline would count against the 200-character cap
        # and blur the punchline; a mismatch means the file on disk is
        # not the line that was scored, so refuse it outright.
        raise SystemExit("entry.txt failed the gate: %r" % written)
    print(line)
    return line


if __name__ == "__main__":
    main()
