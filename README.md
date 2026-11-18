[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun)
[![rank](https://make.fun/badge/wahyu779/news-image-20261117/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/wahyu779/news-image-20261117/reward.svg)](https://make.fun)

# The Daily World — dailyworld-v2

One image that sums up the world's news of Tuesday 17 November 2026, drawn as
a single broadsheet front page: **32 news stories** across 6 continents — war,
diplomacy, health, climate, markets and sport.

## The page

- **Masthead:** "The Daily World", Vol. 142 No. 31877, Tuesday 17 November 2026,
  International Edition, $2.00.
- **Top stories:** the Crimea bridge falls into the sea; the Gulf on a
  knife-edge; the Quad meets in Manila.
- **Photo cards:** Ebola passes 11,000 cases in DR Congo; COP31 draft urges a
  faster fossil-fuel phase-out; the US loses measles-free status; Nvidia beats,
  markets slide.
- **Where it happened:** a satellite world map with 12 numbered pins.
- **Five minis:** Nvidia, Cyclone Akvan, measles, Ebola, Voyager 1.
- **Also on:** 23 more briefs from the day.

The Nvidia card uses a code-drawn logo panel — the green eye and the white
"**NVIDIA**" wordmark on black — so readers can read the brand behind the
markets headline at a glance.

## Build

`page.html` is a hand-written newspaper page (1024 x 1024, aged cream paper)
using only the photos in `assets/`. Render it with headless Chromium:

```sh
python3 render.py   # writes entry.png (1024x1024, RGB, under 1 MiB)
```

`main.ts` is the competition entrypoint: it copies `entry.png` to the output
directory. No network is used at any step.

## License

MIT — see [LICENSE](LICENSE).
