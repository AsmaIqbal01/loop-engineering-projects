# The Doorbell

This project has one job: when someone proposes a change to `readings.py` in this repo, review it
for bugs — automatically, without anyone starting the review by hand.

**The loop is not a skill or a script in this folder — it is
`../.github/workflows/doorbell.yml` at the repo root.** GitHub only reads workflow files that sit
at the top of a repository, so the doorbell itself lives outside `project-04-doorbell/`, one level
up from here. This folder holds only `readings.py`, the file the doorbell watches.

The one thing to hold onto: this is an **event-driven** loop, not a scheduled one (contrast
[Project 3 — Sky Watch](../project-03-sky-watch/AGENTS.md)). It runs zero times on a quiet day and
several times on a busy one, because a pull request is what starts it, not a clock. A fresh,
memory-less machine runs each review, and the only continuity between runs is what is written down
in the git history and the PR thread — never assume state carries over between reviews.
