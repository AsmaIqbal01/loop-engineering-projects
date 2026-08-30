# Session Log — Sky Watch

A record of the actual setup and first run this project was built from (2026-08-30).

## Step 1 — manual proof, before scheduling anything

Ran the bundled script directly from this folder, to prove the fetch and the danger rule work
before trusting a clock with it:

```bash
python3 .claude/skills/sky-watch/scripts/skywatch.py
```

Output (2026-08-30, next 7 days):

```
  ☄  SKY WATCH — next 7 days, 2026-08-30
  ──────────────────────────────────────────────────────────────
     ⚠  4 flagged POTENTIALLY HAZARDOUS by NASA:
        2026-08-30  2013 JR28  —  101.9× the Moon
        2026-09-01  2011 CT4  —  185.1× the Moon
        2026-09-03  337075 (1998 QC1  —  131.8× the Moon
        2026-09-05  2006 HC2  —  137.7× the Moon

     Closest pass:  2017 RH16  on 2026-08-31
        3,335,900 km  =  8.7× the Moon
        ~16–35 m across, 43,688 km/h

     42 close approaches the next 7 days.
  ──────────────────────────────────────────────────────────────
```

Turned into the one-paragraph watch, per the skill's shape rules (lead with calm or danger, name
the closest pass in Moons, say when):

> All clear for the week ahead: nothing on NASA's hazardous list is actually close. The closest
> pass is 2017 RH16 on August 31st, at 8.7× the Moon's distance — a small rock, 16–35 meters
> across. NASA does flag four other objects as "potentially hazardous" this week (2013 JR28, 2011
> CT4, 1998 QC1, 2006 HC2), but every one of them stays well past 100× the Moon — that label is
> about their orbits over many years, not this particular pass. 42 close approaches total in the
> next seven days, nothing to worry about.

## Step 2 — pushed to GitHub

A cloud Routine clones the repo fresh on every fire — it has no access to this machine, so the
skill, script, and settings had to be committed and pushed to
`github.com/AsmaIqbal01/loop-engineering-projects` before the schedule could work at all.

## Step 3 — the schedule

```
/schedule every day at midnight, run the sky-watch skill for today and write me the forecast
```

"Midnight" resolved to the user's timezone, Asia/Karachi (UTC+5) — `0 19 * * *` UTC.

- **Repo:** `https://github.com/AsmaIqbal01/loop-engineering-projects`
- **Prompt:** reads this project's `AGENTS.md` and `.claude/skills/sky-watch/SKILL.md` inside
  `project-03-sky-watch/`, runs `skywatch.py --days 1` (today only — a daily run reports today, not
  the full week), and writes the one-paragraph forecast in the skill's voice.
- **Routine ID:** `trig_016U5XqxoNeCvXgEancEsoam`
- **Link:** https://claude.ai/code/routines/trig_016U5XqxoNeCvXgEancEsoam

## Step 4 — rehearsed it immediately (did not wait for midnight)

Fired the routine on demand (`RemoteTrigger action:"run"`) right after creating it, per the
course's "prove it fast, then trust it overnight" rule — a schedule is too slow to prove by waiting
for the clock.

Result: the rehearsal **failed to fetch**, and that turned out to be the useful proof. The cloud
sandbox's egress proxy rejected the connection to `api.nasa.gov` with `403 Forbidden` ("organization
policy"), `skywatch.py` exited non-zero after its 3 retries, and the agent did exactly what the
skill demands in that case — no invented forecast, just:

> The watch could not run this time — the fetch to NASA's asteroid feed failed (network access to
> api.nasa.gov was blocked). No forecast was generated.

So the schedule, the prompt, and the failure path are all confirmed working end to end. The one
open item is infrastructure, not code: the cloud environment's outbound network allowlist needs
`api.nasa.gov` added before a real midnight run can succeed. Until that's fixed, every scheduled
fire will correctly report "could not run" rather than a wrong or guessed forecast — which is the
one thing this project is built to never get wrong.
