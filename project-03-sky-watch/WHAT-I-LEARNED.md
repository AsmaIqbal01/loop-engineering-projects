# What I Learned — Project 3: Sky Watch

## A schedule is not a bigger `/loop`

The temptation is to think of a cloud Routine as just a `/loop` that survives a closed terminal.
It isn't — it's a different mechanism entirely. A `/loop` is a heartbeat kept alive by the running
session's memory; the moment the session ends, so does the loop. A Routine is a cron job that
spawns a brand-new, isolated cloud session on every fire, with its own fresh git checkout of the
repo. There's no persistent process to keep alive and nothing local to depend on — which is exactly
why it can run at midnight with the laptop asleep in a bag.

## The forecast has to come from the repo, not from me

The whole point of `skywatch.py` is that asteroid positions aren't guessable — NASA's feed is the
only source of truth, so the script re-fetches it fresh on every single run, scheduled or by hand.
The one failure mode the skill explicitly forbids is inventing a calm "all clear" when the fetch
actually failed. A watch that lies quiet is worse than a watch that says "I don't know" — a false
all-clear is the one answer this kind of loop must never give.

## Match the window to the cadence

The skill's script defaults to a 7-day look-ahead, which is right for a by-hand "what's coming
this week?" But a *daily* schedule asking for the full week every morning would just repeat five
of the previous six days' data. The fix is `--days 1`: report today, because tomorrow's run will
report tomorrow. Cadence and window have to match, or the loop becomes noise.

## Cloud routines need the code to actually be in GitHub

A local folder isn't enough. The Routine's cloud session clones the repo fresh from
`origin` on every fire — it has no access to this machine, so anything the schedule needs to run
(the skill, the script, the settings) has to be committed and pushed first. Setting this project up
meant treating "push to GitHub" as part of the setup, not an afterthought.

## "All clear" is the loop working, not the loop having nothing to say

Most days, the correct report is calm: nothing hazardous, closest pass tens of times farther than
the Moon. An event-driven loop (like [the Doorbell](../../../crash-course/loop-eng/doorbell) in
this course) would stay silent on a day like that, because nothing happened. A *scheduled* watch
reports anyway — the quiet morning and the loud one get the same fire, the same script run, the
same honesty. That's what makes it a watch instead of an alarm.

## The one nuance worth internalizing

NASA's "potentially hazardous" flag describes an object's *orbit* over many years — it can come
within ~7.5 million km and is over ~140 m wide — not a claim about *this specific pass*. An object
can carry the flag and still cruise by at 180× the Moon's distance. The script and the write-up
both have to show the flag **and** the real distance side by side, or a routine flyby turns into a
false scare.
