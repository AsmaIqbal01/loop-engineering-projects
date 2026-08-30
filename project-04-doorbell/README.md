# The Doorbell — a loop that nobody starts

**Loop Engineering, Concept 7 — event-driven loops.**

Propose a change to your code, and about a minute later a review appears. Nobody typed a prompt.
Nobody was watching. Something _happened_, and that started the work.

That is the whole idea, and it is the opposite of the schedule in
[Project 3 — Sky Watch](../project-03-sky-watch/).

## Two kinds of loop

In [Project 1 — ISS Watch](../project-01-iss-watch/), **you** start the loop. You type a `/loop`
prompt and it runs while you watch. In Project 3, a **schedule** starts the loop — an alarm clock
that rings whether or not anything happened.

Here, **you start nothing.** The loop sits there doing nothing at all — for a day, a week,
forever — until someone proposes a change to the code. Then it wakes up.

A schedule is an alarm clock: it rings whether or not anything happened.
An event is a doorbell: **nothing until someone presses it, then instantly.**

That has a real consequence. On a quiet day this loop runs zero times and costs zero. On a busy day
it runs nine times. It matches the work, because the work is what starts it.

## Where the files actually live in this repo

A doorbell only rings on files GitHub can see at the **top** of a repository — a workflow sitting
inside a subfolder like `project-04-doorbell/` is never read. So in this monorepo the pieces are
split:

| File                                             | Lives at                                       |
| ------------------------------------------------ | ----------------------------------------------- |
| `readings.py` (the code under review)             | here, in `project-04-doorbell/`                 |
| `doorbell.yml` (the doorbell itself)              | repo root: `.github/workflows/doorbell.yml`     |

That is not a stylistic choice — it is the one thing that makes the doorbell actually ring on
`AsmaIqbal01/loop-engineering-projects`.

## The doorbell itself

```yaml
on:
  pull_request:
    types: [opened, synchronize]
```

Four lines in the workflow are doing the real work:

| Line                                        | Why it is there                                                                       |
| -------------------------------------------- | -------------------------------------------------------------------------------------- |
| `on: pull_request`                           | **The doorbell itself.** This is what listens.                                        |
| `types: [opened, synchronize]`               | Ring when a change is proposed (`opened`) **and** when it is updated (`synchronize`). |
| `track_progress: true`                       | **Do not remove this.** Without it the run succeeds and posts nothing. See gotchas.   |
| `github_token: ${{ secrets.GITHUB_TOKEN }}`  | Lets it comment without installing any GitHub App. GitHub provides this token free.   |

## Setup already done for this repo

1. `readings.py` copied into `project-04-doorbell/` (something to review).
2. `.github/workflows/doorbell.yml` placed at the **repo root** (the doorbell itself), so GitHub
   actually reads it.
3. Repo secret `CLAUDE_CODE_OAUTH_TOKEN` needs to be set on
   `github.com/AsmaIqbal01/loop-engineering-projects` — see `loop-log.md` in this folder for the
   exact command.

You need a **Claude Pro or Max plan**. No API key, no billing setup.

## Ring it

Propose a change with a bug in it — easiest way, no git needed:

1. On GitHub, open `project-04-doorbell/readings.py` and click the **pencil** (Edit).
2. Paste this in at the bottom — the bug is on purpose:

   ```python
   def average_altitude(readings):
       total = 0
       for i in range(len(readings) - 1):
           total += readings[i]
       return total / len(readings)
   ```

3. Choose **"Create a new branch for this commit and start a pull request"**.
4. Click **Propose changes**, then **Create pull request**.

Now stop touching it. Within a minute or two, a review you never asked for:

> **Off-by-one error in `average_altitude()`**
>
> `range(len(readings) - 1)` iterates indices `0` to `len(readings) - 2`, skipping the last element
> of `readings`. The sum is then divided by the full `len(readings)` … the average is systematically
> too low.

## What happens when the doorbell rings

There is no robot waiting inside your laptop. The real sequence:

1. You propose a change.
2. **GitHub notices** and reads `.github/workflows/doorbell.yml`.
3. GitHub **rents a fresh computer** — a blank Ubuntu machine in a data centre.
4. It downloads your code, runs Claude, posts the review.
5. The machine is **destroyed**. Everything on it is gone.

## Gotchas we hit, so you do not have to

**A green checkmark does not mean it worked.** A run can take several turns, report success, and
post **absolutely nothing** — a cheerful green tick and an empty PR. Without `track_progress: true`
the action reviews quietly and never publishes. If you see green and silence, this is why.

**Committing to `main` does nothing.** There is no "push" doorbell — only "a change was proposed."
Commit straight to `main` and nothing fires: no run, no cost, silence. Push to a branch with an open
pull request and it rings every time.

**Each ring is a brand-new computer.** Two pushes to one PR are two machines that never met.

**It costs real money.** About **$0.11 of your Claude usage per review**. Not a separate bill — just
not free. A busy PR with ten pushes is ten reviews.

**The token expires eventually.** If the doorbell goes quiet for no reason, run `claude setup-token`
again and update the secret.

## Now push again — and read what it says

Change something on that same branch and commit. A second review appears, and it will know things
it has no business knowing. Here is a real example from the original lab's own testing:

> **Bug:** The PR is a no-op. Commit `e79b8e7` changed `lowest()`'s docstring in `readings.py`, and
> commit `f85e54d` reverted it back to the original text. The resulting file is byte-identical to
> `origin/main`'s `readings.py`, so despite the PR title there is no actual change to merge.

Stop and look at that, because it is stranger than it first appears.

The computer that wrote the first review **no longer exists**. It was destroyed. The machine that
wrote this one had never run before, has no memory of anything, and does not know it has a
predecessor. It has never seen your earlier commits happen.

Yet it can know that one commit changed a docstring, a later one undid it, and the two cancelled
out — and be right.

**It read all of it.** The commits are in the git history. The earlier reviews are in the pull
request thread. All of it written down, sitting in the repo, waiting. A total stranger walked in,
read the record, and reconstructed the whole story in 2 minutes.

Nothing was remembered. Everything was **written down**, and the next run read it.

The model forgot. **The repo did not.**

That is not a trick — that is the next part of the course, and it has a name: the **spine**.

## Reference

Original lab kit: [`crash-course/loop-eng/doorbell`](https://github.com/panaversity/agentfactory-labs/tree/main/crash-course/loop-eng/doorbell)
in `agentfactory-labs`.
