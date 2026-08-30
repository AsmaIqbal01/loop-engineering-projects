# Loop Engineering Projects

Projects built while working through the **Loop Engineering** crash course — each one explores a
different way to give Claude a loop: in-session heartbeats, conditional stopping points, and
(later) durable, cloud-scheduled jobs that outlive a single terminal session.

## Projects

| # | Project | What it explores |
| - | ------- | ----------------- |
| 1 | [ISS Watch](./project-01-iss-watch) | An in-session `/loop` that tracks the ISS's live position every minute, extended with a conditional stopping point (shout ARRIVED after 20° of travel). Key lesson: in-session loops die when the terminal closes. |
| 2 | [Portfolio Rebuild](./project-02-portfolio) | A loop that rebuilds a live portfolio against a 20-check mechanical spec plus a 6-promise judgment review, stopping only when both pass. Live sites: original at [asmaiqbal.vercel.app](https://asmaiqbal.vercel.app), rebuild at [site-ten-nu-27.vercel.app](https://site-ten-nu-27.vercel.app) — deployed as a separate project, the original untouched. |

More projects will be added here as the course progresses.
