# Session Log — ISS Watch

A record of the actual `/loop` session this project was built from (2026-08-30, all times UTC).

## Loop 1 — basic position, every minute

```
/loop show me the location of the ISS every minute
```

Parsed as "every minute" → cron `*/1 * * * *`, scheduled and run immediately:

```
  🛰  INTERNATIONAL SPACE STATION            live · 06:11:53 UTC
  ──────────────────────────────────────────────────────────
     Position    50.7° N      32.4° W
     Altitude    422 km
     Speed       27,598 km/h   (7.67 km/s)
     Sunlight    in sunlight
  ──────────────────────────────────────────────────────────
```
Over the North Atlantic, west of Ireland, on the line between Newfoundland and Portugal.

Refined immediately after with a more specific prompt:

```
/loop 1m show me where the ISS is and what country or ocean it is flying over
```

The prior job was cancelled and replaced (no reason to run two overlapping ISS-fetch jobs a minute
apart). New reading:

```
  🛰  INTERNATIONAL SPACE STATION            live · 06:12:40 UTC
  ──────────────────────────────────────────────────────────
     Position    50.0° N      27.9° W
     Altitude    422 km
     Speed       27,598 km/h   (7.67 km/s)
     Sunlight    in sunlight
  ──────────────────────────────────────────────────────────
```
North Atlantic Ocean, roughly midway between Ireland and Newfoundland — no land beneath it.

## Loop 2 — track travel, shout ARRIVED at 20°

```
/loop 1m track the ISS and shout ARRIVED when it has travelled 20 degrees from where it started
```

The previous job was cancelled again and replaced with a stateful tracker. A baseline position was
captured at loop start and carried in the job's own prompt so every future fire could measure
against it:

- **Baseline:** 49.343945° N, 24.749931° W
- **Captured:** 06:13:15 UTC (unix `1788070395`)

### Mid-loop query — "how many degrees has it travelled so far"

Asked between scheduled fires, without disturbing the timer:

- Fetched fresh: 48.5° N, 21.5° W
- Cumulative travel from baseline: **≈2.3°**

### Scheduled fire — 06:14:30 UTC

- Position: 47.6° N, 18.2° W — off the coast of Portugal/the Azores
- Cumulative travel: **≈4.8°**

### Scheduled fire — 06:15:28 UTC

- Position: 46.0° N, 13.5° W — off northern Spain/Portugal, toward the Bay of Biscay
- Cumulative travel: **≈8.4°**

### Mid-loop query — "how many degrees left until ARRIVED"

- Fetched fresh: 45.2° N, 11.4° W
- Cumulative travel: **≈9.9°** → **≈10.1° remaining** to the 20° threshold

### Scheduled fire — 06:16:29 UTC

- Position: 44.1° N, 8.9° W — off the northwest coast of Spain, closing on the Iberian Peninsula
- Cumulative travel: **≈12.1°**

## Final — cancelled cleanly

```
cancel the loop
```

The job was stopped via `CronDelete` before reaching the 20° threshold (it had covered ≈12.1° of
20° — roughly 5–8 more minutes would have triggered ARRIVED). No leftover state, no orphaned
process — the loop simply stopped existing the moment it was cancelled, the same way it would have
if the terminal had been closed instead.
