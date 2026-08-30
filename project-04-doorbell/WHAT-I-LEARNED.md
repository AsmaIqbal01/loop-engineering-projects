# What I Learned — Project 4: The Doorbell

## A doorbell is a different mechanism than a schedule, not a faster one

[Project 3](../project-03-sky-watch/WHAT-I-LEARNED.md) taught that a schedule is a cron job that
spawns a fresh cloud session on a timer, whether or not anything happened. The doorbell is the
other primitive: it spawns a fresh session only when GitHub sees a `pull_request` event. Nothing
in between is the same clock ticking faster — a schedule always fires; a doorbell may never fire at
all, or fire nine times in an hour. The trigger is the whole difference.

## The workflow has to live where GitHub can see it

This lab's own README says it outright: GitHub only reads workflow files sitting at the **top** of
a repository, never inside a subfolder. Because this repo is a monorepo of several course
projects, `doorbell.yml` cannot live inside `project-04-doorbell/` alongside the code it
reviews — it has to sit at `.github/workflows/doorbell.yml`, one level above every project folder.
`readings.py` (the thing being watched) and `doorbell.yml` (the watcher) are necessarily split
across two different places in the tree, and that split is not optional.

## The token is what an unattended loop needs that an attended one doesn't

Project 1's `/loop` ran on a laptop already logged into Claude Code — no token needed. This loop
runs on a rented, blank Ubuntu machine that has never heard of the user, so it needs its own way to
prove it's allowed to call Claude: `CLAUDE_CODE_OAUTH_TOKEN`, generated once with
`claude setup-token` and stored as a GitHub Actions secret. Every unattended loop in this course —
schedule or event — needs credentials of its own for exactly this reason.

## A green checkmark is not proof of anything

The lab flags this as the gotcha most people hit: a run can finish, report success, and post
nothing at all if `track_progress: true` is missing from the workflow. A green tick only means the
job didn't crash — it says nothing about whether the review actually got written anywhere a human
would see it. The lesson generalizes past this one project: for any unattended loop, "it ran" and
"it did the job" are two separate claims, and only the second one matters.

## Only a proposed change rings the bell

Committing straight to `main` produces no event this workflow listens for — `pull_request` fires on
`opened` and `synchronize`, not on pushes to the default branch. The loop isn't watching the repo in
general; it's watching one specific kind of event, and anything outside that shape is invisible to
it, no matter how real the change is.

## Nothing is remembered between runs — everything has to be written down

Each ring of the doorbell is a brand-new machine with no memory of the last one. What makes a
second review able to reference the first — or notice that two commits on a branch cancelled each
other out — is not memory at all. It's that git history and the PR comment thread are both
persistent, readable records, and a stranger machine can reconstruct the whole story from them in
minutes. The model forgets by design; the repo is what carries continuity across event-driven runs.
This is the seam the course calls **the spine**, and it's the natural next question after this
project: if agents have no memory of their own, what has to be written down for the *next* one to
pick up where this one left off?
