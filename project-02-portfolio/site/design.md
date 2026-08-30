# The design decision

The page is a terminal that ships: dark, monospace-accented, structured like a build log
that resolves into two clean, green-lit results — because "I write specs before code, and I
ship things that run in production" is literally the sentence she leads with, and every
section is built to look like the second half of that sentence actually happening.

## Why this person

Asma's own material already names the two things this page has to hold together: the spec
(process, discipline, tests-before-ship) and the production result (a live pipeline, a
tests-passing count, a recognition badge). A generic "AI portfolio" template would pick one
mood — polished-corporate or hacker-dark — and lose the other half. Her actual numbers
(489 tests, 106/106 tests, "live since July 2026") are the kind of fact a build log prints,
not the kind a mood board decorates with, so the page is built to print them the same way.

## How the page carries it out

- The nav bar reads like a status line (`asmaiqbal.dev — status: online`), not a logo.
- The hero headline is typeset as two stacked commands — "I write specs before code." /
  "I ship things that run in production." — with the accent green marking only the verbs
  that are actually true right now (write, ship), never used as pure decoration elsewhere.
- Each project card is framed like a completed CI run: a status tag, the pipeline
  (`Gmail → Gemini → HubSpot → Discord`), and the test count rendered in monospace, because
  that count is the one fact on the page that is genuinely load-bearing, not a headline.
- Skills render as a single inline row of terminal-style tags, not a decorative cloud —
  it reads as `$ stack --list`, echoing the same idea at a smaller scale.
- At 390px, the two-line hero commands stack to one column, the status-line nav collapses
  to name + a single "menu" affordance region, and the project "CI run" cards go full width
  so the pipeline arrow and test count stay legible instead of shrinking to noise.

## Tokens
```css
:root {
  --bg: #0a0a0a;
  --bg-raised: #131313;
  --fg: #f2f2f2;
  --fg-muted: #c9cdd3;
  --accent: #00ff88;
  --border: #262626;
  --overlay: #00000066;

  --text-xs: 0.75rem;
  --text-sm: 0.9rem;
  --text-base: 1.05rem;
  --text-lg: 1.3rem;
  --text-xl: clamp(2rem, 5vw, 3.2rem);
  --text-2xl: clamp(2.6rem, 8vw, 5.6rem);

  --space-1: 0.4rem;
  --space-2: 0.8rem;
  --space-3: 1.4rem;
  --space-4: 2.2rem;
  --space-5: 3.5rem;
  --space-6: 6rem;

  --measure: 47ch;
}
```

Computed contrast (WCAG, sRGB relative luminance):
- `--fg` (`#f2f2f2`) on `--bg` (`#0a0a0a`) ≈ **17.7:1**
- `--accent` (`#00ff88`) on `--bg` (`#0a0a0a`) ≈ **14.8:1**

Both clear the 4.5:1 floor with room to spare — `#00ff88` is her own brand accent from the
live site, kept because it was already legible there, not chosen decoratively here.
