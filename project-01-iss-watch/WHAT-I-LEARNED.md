# What I Learned — Project 1: ISS Watch

## What an in-session heartbeat actually is

A `/loop` isn't a background service — it's a heartbeat that only beats while the session is
alive. Claude schedules a job that re-fires a prompt on a timer (in my case, every minute), and
each beat runs the same script fresh: no cached position, no guessing, just a new call to the
tracker every single time. That's the point of a heartbeat loop — it's cheap, it's simple, and it
only exists as long as something is there to keep the pulse going.

## Why the loop died when I closed the terminal (and why that's the point)

The job lives in the session's memory, not on disk. The moment the terminal closes, that memory is
gone, and so is the job — there's no process running quietly in the background, no state file
picking back up later. At first that feels like a limitation. It isn't. It's the honest boundary of
what an in-session loop *is*: a kitchen timer, not an oven you can walk away from. If I wanted the
ISS watched overnight, I'd need a different mechanism entirely (a durable, cloud-scheduled job) —
and seeing this one die cleanly is what makes that next step make sense instead of feeling like
overkill.

## How I extended it beyond the basic project

The base project just reports position on a timer forever, until you get bored and cancel it. I
added a second loop with an actual goal: capture a baseline position when the loop starts, then on
every fire compute the great-circle angular distance from that baseline (haversine, handling the
180°/-180° longitude wraparound so it doesn't miscount near the date line). Once cumulative travel
hits 20°, the loop shouts **ARRIVED**, reports the total degrees covered, and cancels itself — no
manual stop needed. I also queried it mid-loop a couple of times ("how many degrees has it
travelled so far", "how many degrees left") without disturbing the timer, which confirmed the
baseline was being held steady across fires rather than drifting to whatever the last reading was.

## Fixed-timer loop vs. conditional loop

A fixed-timer loop only knows about *time* — fire every N minutes, forever, until a human says
stop. It has no idea whether anything meaningful has happened; it just keeps ticking.

A conditional loop still runs on a timer, but it also carries **state** across each fire (the
baseline position, in this case) and a **condition** it's watching for. It knows the difference
between "nothing has changed yet, keep going" and "the condition is met, stop now." That's a small
change mechanically, but it's a big one conceptually — it's the difference between a loop that
watches and a loop that *waits for something to happen*.
