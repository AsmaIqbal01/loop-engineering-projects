# Session Log — Paper Watch

A record of the actual setup and first run this project was built from (2026-08-30).

## Step 1 — manual proof, before scheduling anything

Ran the bundled script directly from this folder, to prove the fetch and the spine work before
trusting a schedule with it:

```bash
python .claude/skills/paper-watch/scripts/paperwatch.py --topic "AI agents"
```

First run — 20 new papers, newest first (2026-08-27 down to 2026-08-24), including titles like
*WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution* and *The
Compaction Cliff in Long-Running AI Agent Memory*. Ran the exact same command again immediately
after:

```
  📄  FRESH ON ARXIV  ·  "AI agents"
      nothing new since last run  ✓
  ------------------------------------------------------------
   You're all caught up.
   That is the spine working — it remembered what it already showed you.
```

The spine worked as designed: same command, same topic, second call correctly reported nothing
new because `progress.md` remembered the first call's 20 papers.

Along the way, fixed a real Windows-only bug: `progress.md` was being written in the OS default
encoding (`cp1252`), which mangled the em dash in the file header. Harmless on Windows since
read and write used the same broken encoding — but it would have broken a **cloud** run, where
Python defaults to UTF-8 and can't decode that byte. Patched `read_spine()`/`write_spine()` to
open the file with `encoding="utf-8"` explicitly, and added a UTF-8 stdout reconfigure so the
card's `📄`/`·` render correctly on any platform. Regenerated `progress.md` clean and reran to
confirm the spine still worked after the fix.

## Step 2 — pushed to GitHub

A cloud Routine clones the repo fresh on every fire — it has no access to this machine, so the
skill, script, `AGENTS.md`, `CLAUDE.md`, and the seeded `progress.md` had to be committed and
pushed to `github.com/AsmaIqbal01/loop-engineering-projects` before the schedule could work at
all.

## Step 3 — the schedule

```
every day at 9am, run the paper-watch skill for topic "AI agents", read progress.md first,
write results back to progress.md, then commit and push if it changed
```

"9am" resolved to the user's timezone, Asia/Karachi (UTC+5) — `0 4 * * *` UTC.

- **Repo:** `https://github.com/AsmaIqbal01/loop-engineering-projects`
- **Prompt:** `cd`s into `project-05-paper-watch/`, runs
  `paperwatch.py --topic "AI agents"` (reads `progress.md` first, writes it last), then commits
  and pushes `progress.md` only if the script actually changed it — a "nothing new" run stays a
  no-op in git, same as the skill intends.
- **Routine ID:** `trig_01K3ojLGp2xhssUcaL5z6H4U`
- **Link:** https://claude.ai/code/routines/trig_01K3ojLGp2xhssUcaL5z6H4U

## Step 4 — rehearsed it immediately (did not wait for 9am)

Fired the routine on demand (`RemoteTrigger action:"run"`) right after creating it, per the
course's "prove it fast, then trust it overnight" rule — a schedule is too slow to prove by
waiting for the clock.

Result: the rehearsal **failed to fetch**, and that turned out to be the useful proof — the same
class of failure Project 3's Sky Watch hit with `api.nasa.gov`. The cloud sandbox's egress proxy
rejected the connection to `export.arxiv.org` with `403 Forbidden` ("organization policy"),
`paperwatch.py` exited non-zero after its 3 retries, and the agent did exactly what the skill
demands in that case — no invented papers, just:

> The proxy is rejecting connections to export.arxiv.org due to organization egress policy —
> this isn't a transient rate-limit issue, it's a network policy denial. This confirms the
> failure is real; I won't fabricate results. No changes to progress.md, so nothing to commit.

It then confirmed via `git status` that `progress.md` was untouched and correctly skipped commit
and push, rather than pushing a false "nothing new."

So the schedule, the prompt, and the failure path are all confirmed working end to end. The one
open item is infrastructure, not code: the cloud environment's outbound network allowlist needs
`export.arxiv.org` added before a real 9am run can succeed. Until that's fixed, every scheduled
fire will correctly report "could not run" rather than a made-up paper list — which is the one
thing this project is built to never get wrong.
