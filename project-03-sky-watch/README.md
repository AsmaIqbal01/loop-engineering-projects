# Project 3 — Sky Watch

Project 3 of the **Loop Engineering** crash course.

A **scheduled cloud loop**, built with Claude Code's `/schedule` command. It checks NASA's
near-Earth-object feed once a day and reports what asteroids are passing close to Earth — before
they pass, not after — whether or not anyone is watching when it fires.

## What it does

- Fetches the next several days of asteroid close-approach data from NASA's NeoWs feed, via the
  bundled `skywatch.py` script (never from memory — the script owns the data, the date window, and
  the danger rule).
- Reports the closest pass in "times the Moon's distance," and flags anything NASA classifies as
  potentially hazardous — while keeping the flag and the actual distance separate, since a flagged
  object can still miss by 180× the Moon.
- If the fetch fails, it says so and stops. It never invents an "all clear" — a false one is the
  one answer a watch must never give.

See [`loop-log.md`](./loop-log.md) for the actual manual run and the routine this was built from,
and [`WHAT-I-LEARNED.md`](./WHAT-I-LEARNED.md) for the reasoning behind it.

## Running it by hand

```bash
python3 .claude/skills/sky-watch/scripts/skywatch.py
```

or, inside Claude Code:

```
what asteroids are coming this week?
```

## The schedule

```
/schedule every day at midnight, run the sky-watch skill for today and write me the forecast
```

This creates a **cloud Routine** — it runs on Anthropic's servers on a cron schedule, so it fires
at midnight (Asia/Karachi) whether or not this laptop is on. A daily run reports **today**
(`--days 1`), not the full week — a week's worth every morning would just repeat five-sixths of
what it said yesterday.

## Key lesson

**A watch looks forward, and a schedule doesn't stop on its own.** Unlike an in-session `/loop`
(see [Project 1](../project-01-iss-watch)), which dies the moment the terminal closes, this
routine lives in Anthropic's cloud, tied to this repo — it keeps firing every midnight until it is
explicitly cancelled. And unlike an event-driven loop that only speaks up when something happens,
a watch reports in on schedule regardless: most mornings the correct output is "all clear," and
that is the loop working, not the loop having nothing to do.
