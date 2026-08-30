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

## Step 3 — the secret (still pending — user action required)

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

This step needs the user's own Claude Pro/Max login and repo admin access, so it was left for the
user to run rather than done from this session.

## Step 4 — first ring (not yet run)

Plan: open `project-04-doorbell/readings.py` on GitHub, paste in the off-by-one
`average_altitude()` bug from the README, and open it as a pull request via "Create a new branch
for this commit and start a pull request." Expect a review comment within a minute or two naming
the off-by-one bug, *if* `track_progress: true` held and the secret is valid. Will log the actual
result here once the user opens that PR.
