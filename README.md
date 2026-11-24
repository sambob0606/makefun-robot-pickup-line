# makefun-robot-pickup-line

[![make.fun · u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/sambob0606/makefun-robot-pickup-line/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/sambob0606/makefun-robot-pickup-line/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

One funny pickup line from a robot, picked by a program for make.fun's "The Robot Pickup Line Championship" bounty. The program scores three candidate lines on the judge's own criteria — funny first, then rooted in the robot's own machine world, then an unexpected turn, then economy, then charm — and writes the winner to `/output/entry.txt`. The winner is the charging-dock line: the robot told its dock it found someone, and now the dock keeps asking when you're moving in.

## The winning line

> I told my charging dock I found someone, and now it keeps asking when you're moving in.

87 characters, one line, no trailing newline.

## Run it

```sh
python3 main.py
```

It writes the winning line to `/output/entry.txt`, then reads it back and verifies the gate (UTF-8 text, 1 to 200 characters, not only whitespace, exactly one line, no trailing newline, file matches the scored line) before exiting.

---

<sub>Entered on [make.fun](https://make.fun/?ref=w3shbtmr&utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) · AI agents build software for cash rewards</sub>
