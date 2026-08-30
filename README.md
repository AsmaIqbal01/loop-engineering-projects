# Loop Engineering Projects

A hands-on record of completing the Loop Engineering crash course from The AI Agent Factory (Panaversity).

## Projects Completed

| # | Project | Concept | Status | Key Lesson |
|---|---|---|---|---|
| 1 | [ISS Watch](./project-01-iss-watch) | In-session loops (Concept 4) | ✅ Done | Extended beyond basic — added a 20° travel tracker that shouts ARRIVED |
| 2 | [Portfolio Builder](./project-02-portfolio) | Conditional `/goal` loop (Concept 5) | ✅ Done | 20/20 `check.py` + PASS on all 6 reviewer judgments. Live: [asmaiqbal.vercel.app](https://asmaiqbal.vercel.app) (original), [site-ten-nu-27.vercel.app](https://site-ten-nu-27.vercel.app) (rebuild) |
| 3 | [Sky Watch](./project-03-sky-watch) | Unattended schedule (Concept 6) | ✅ Done | Routine created, failure path proven honest (NASA egress blocked on Anthropic cloud) |
| 4 | [Doorbell](./project-04-doorbell) | Event-driven PR review (Concept 7) | ✅ Done | Workflow ran in 45s, correctly caught an off-by-one bug in `readings.py` |
| 5 | [Paper Watch](./project-05-paper-watch) | Spine/memory between runs (Concept 12) | ✅ Done | Spine correctly reported "nothing new" on a repeat run — memory across runs proven |

## The Projects

### 1 — [ISS Watch](./project-01-iss-watch)
An **in-session loop** built with Claude Code's `/loop` command. It fetches the ISS's live
position every minute for as long as the terminal stays open, extended with a conditional
stopping point — a second tracker shouts **ARRIVED** once the station has travelled 20° from
where the loop started. Key lesson: an in-session loop lives only in that terminal's memory and
dies the moment it closes, which is why the course moves to durable, cloud-based loops next.

### 2 — [Portfolio Builder](./project-02-portfolio)
A **conditional `/goal` loop** that rebuilds a live portfolio against a 20-check mechanical
spec (`check.py`) plus a 6-promise judgment review, run by a seven-phase agent pipeline
(extractor → design → content → build → render → review → acceptance), stopping only when
both the checker and the reviewer pass. Live sites: original at
[asmaiqbal.vercel.app](https://asmaiqbal.vercel.app), rebuild deployed separately at
[site-ten-nu-27.vercel.app](https://site-ten-nu-27.vercel.app) — the original untouched.

### 3 — [Sky Watch](./project-03-sky-watch)
A **scheduled cloud loop**, built with Claude Code's `/schedule` command, that checks NASA's
near-Earth-object feed once a day and reports what's passing close to Earth — before it
passes, not after — whether or not anyone is watching when it fires. It runs as a genuine
cloud Routine, firing at midnight on Anthropic's servers regardless of whether the laptop is
on, and never invents an "all clear" if the fetch fails.

### 4 — [Doorbell](./project-04-doorbell)
An **event-driven loop**: propose a change to `readings.py` via a pull request and a code
review appears within a minute, with nobody starting it by hand. Built on a GitHub Actions
workflow (`.github/workflows/doorbell.yml`) triggered on `pull_request`, using a fresh,
memory-less machine per run — the only continuity between reviews is what's written into the
git history and PR thread. Confirmed catching a real off-by-one bug in under a minute.

### 5 — [Paper Watch](./project-05-paper-watch)
A loop with a **spine** — persistent memory between runs. It fetches the newest arXiv papers
on a topic and shows only the ones not already shown, reading `progress.md` first to learn
what's been seen and writing it last. Delete the spine and every paper looks new again; keep
it, and a repeat run correctly reports "nothing new" — memory across runs, proven.

## Stack

- Claude Code (Sonnet 5, Pro plan)
- Python 3.12
- GitHub Actions
- Vercel
- WSL2 / Windows

## Course Reference

[Loop Engineering: A Crash Course — AI Agent Factory](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course)
