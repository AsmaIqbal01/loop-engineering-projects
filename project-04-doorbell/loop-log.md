# Session Log — The Doorbell

A record of the actual setup for this project, built from the [original lab
kit](https://github.com/panaversity/agentfactory-labs/tree/main/crash-course/loop-eng/doorbell)
(2026-08-30).

## Step 1 — copied the kit into this repo, split across two locations

Unlike Projects 1 and 3, the doorbell's workflow cannot live inside `project-04-doorbell/` — GitHub
only reads workflow files at the repo root. So the kit was split on copy:

- `readings.py` → `project-04-doorbell/readings.py` (the file under review)
- `doorbell.yml` → `.github/workflows/doorbell.yml` at the **repo root** (the doorbell itself)
- `README.md`, `AGENTS.md`, `CLAUDE.md` → `project-04-doorbell/` (this project's docs; the original
  lab kit had no `AGENTS.md`/`CLAUDE.md`/skill of its own — this project's copies were written to
  match the pattern already used by [Project 3](../project-03-sky-watch/))

## Step 2 — pushed to GitHub

A GitHub Actions workflow only fires from what is actually on `github.com`, not from this local
checkout — so `.github/workflows/doorbell.yml` and `project-04-doorbell/` had to be committed and
pushed to `github.com/AsmaIqbal01/loop-engineering-projects` before any pull request could trigger
it.

## Step 3 — the secret

The doorbell needs one repo secret before it can call Claude from GitHub's rented machine:

```bash
claude setup-token
```

opens the browser, takes a **code** pasted into the terminal, and returns a **token** — the token
(not the code) is what goes into:

```bash
gh secret set CLAUDE_CODE_OAUTH_TOKEN --repo AsmaIqbal01/loop-engineering-projects
```

or, without the CLI: **GitHub → the repo →
Settings → Secrets and variables → Actions → New repository secret**, name
`CLAUDE_CODE_OAUTH_TOKEN` (must match exactly — that's what `doorbell.yml` looks for), value = the
token from `claude setup-token`.

This step needs the user's own Claude Pro/Max login and repo admin access, so `claude setup-token`
was run by the user directly (via `!`, so it had real browser access), and the secret was confirmed
present on the repo (`gh secret list` showed `CLAUDE_CODE_OAUTH_TOKEN`, set 2026-08-30T07:21:49Z).

## Step 4 — first ring (confirmed working, 2026-08-30)

Created branch `doorbell-test`, added the exact off-by-one `average_altitude()` from the README to
`project-04-doorbell/readings.py`, pushed, and opened
[PR #1](https://github.com/AsmaIqbal01/loop-engineering-projects/pull/1) against `main`.

The `Doorbell` workflow fired automatically on `pull_request: opened` (run
`33299085531`), finished in 21 seconds, and posted a real comment — not just a green
checkmark — correctly identifying the bug:

> **Bug:** `average_altitude()` in `project-04-doorbell/readings.py:18` uses
> `range(len(readings) - 1)`, which iterates only over indices `0` to `len(readings) - 2`,
> skipping the last element of the list. This is an off-by-one error — the loop should use
> `range(len(readings))`. As written, `average_altitude(READINGS)` sums only the first 4 of 5
> readings but still divides by `len(readings)` (5), producing an incorrect average.

Confirmed end to end: `on: pull_request` fired, `track_progress: true` made the review actually
post (not just a silent success), and the workflow read the PR's own commit hash (`63d697a`) out of
the diff to cite it — exactly the "the model forgot, the repo did not" behavior the README predicts,
even on this very first ring.
