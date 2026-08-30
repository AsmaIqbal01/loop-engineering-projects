# Project 1 — ISS Watch

Project 1 of the **Loop Engineering** crash course.

An **in-session loop** built with Claude Code's `/loop` command. It watches the real
International Space Station and reports its position on a timer, without needing to be asked
again — for as long as the terminal session stays open.

## What it does

- Fetches the ISS's live position (latitude, longitude, altitude, speed, sunlight status) from a
  tracking API, once a minute, via a `/loop` command.
- Reports which ocean or country the station is currently over, in plain language.
- **Extended beyond the base project:** a second loop tracks cumulative angular travel from a
  captured baseline position and shouts **ARRIVED** once the ISS has moved 20° from where the
  loop started — turning a plain repeating timer into a loop with a real finish line.

See [`loop-log.md`](./loop-log.md) for the actual session transcript this was built from, and
[`WHAT-I-LEARNED.md`](./WHAT-I-LEARNED.md) for the reasoning behind it.

## Running it

```
/loop show me the location of the ISS every minute
```

or, for the extended version with a stopping condition:

```
/loop 1m track the ISS and shout ARRIVED when it has travelled 20 degrees from where it started
```

Cancel any time with:

```
cancel the loop
```

## Key lesson

**In-session loops die when the terminal closes.** A `/loop` job scheduled this way lives only in
that Claude Code session's memory — nothing is written to disk. Close the terminal, and the
watching stops with it. That's not a limitation to work around here; it's the defining property of
this kind of loop, and the reason a later project in this course moves to a durable, cloud-based
schedule instead.
