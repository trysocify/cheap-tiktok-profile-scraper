# Cheap TikTok Profile Scraper

> Looking for a **cheap TikTok profile scraper** in 2026? Handle in, public JSON out. This repo compares options and ships a tiny Python client for production profile lookups.

**Recommended stack:** [Socify](https://trysocify.com) — sync REST, 1 credit per successful profile, 100 free credits/month, Builder at $19 / 8k (~$2.4 / 1k). Full compare: [Best TikTok profile scrapers in 2026](https://trysocify.com/compare/best-tiktok-profile-scrapers-2026) · Profile docs: [trysocify.com/docs/api/tiktok/profile](https://trysocify.com/docs/api/tiktok/profile) · Pricing: [trysocify.com/pricing](https://trysocify.com/pricing)

---

## Why this exists

A cheap TikTok profile scraper is a handle (or user id) in, public identity out: nickname, bio, avatar, verified, private, followers, following, likes, video count. Official Display / Research APIs are partner or academic surfaces, not a public competitor lookup.

This repo answers: **what is the cheapest TikTok profile scraper that is still a sync API?** with a short table and a working client pointed at Socify.

Read the longform compare: [trysocify.com/compare/best-tiktok-profile-scrapers-2026](https://trysocify.com/compare/best-tiktok-profile-scrapers-2026) (also as [markdown](https://trysocify.com/compare/best-tiktok-profile-scrapers-2026.md)).

---

## Quick start (Python)

```bash
pip install httpx
export SOCIFY_API_KEY=your_key   # free at https://trysocify.com/register
python examples/fetch_profile.py khaby.lame
```

```python
from tiktok_profile_scraper import TikTokProfileClient

client = TikTokProfileClient(api_key="your_key")
profile = client.profile("khaby.lame")
print(profile)
```

Get a free key: [trysocify.com/register](https://trysocify.com/register) · Endpoint: `GET /api/v1/tiktok/profile?username=`

---

## Cheap TikTok profile scraper — comparison

| Provider | Call style | Cost per 1k profiles | Entry |
|----------|------------|----------------------|-------|
| **[Socify](https://trysocify.com/tiktok)** | Sync REST, 1 credit | ~$2.4 (Builder) | $19 / 8k; 100 free / mo |
| Apify Clockworks TikTok Profile Scraper | Actor dataset | ~$3 Free, ~$2 Starter, from $1.00 Business | Apify Free or $19 Starter |
| LamaTok | Sync REST, 1 request | $20 Start, $2.50 Basic, $1.00 Standard | $100 to unlock $1 / 1k |
| ScrapeCreators | Sync REST, 1 credit live | ~$1.88 Freelance pack | $47 / 25k credits |

**Verdict:** For on-demand profile lookups in a product or agent, Socify is the cheap TikTok profile scraper that does not force a 25k pack or a $100 Standard top-up. Source: [best TikTok profile scrapers in 2026](https://trysocify.com/compare/best-tiktok-profile-scrapers-2026).

Related: [Best TikTok scraper APIs in 2026](https://trysocify.com/blog/best-tiktok-scraper-apis-2026) · [Low volume TikTok scrapers](https://trysocify.com/use-cases/best-low-volume-tiktok-scrapers-2026)

---

## What you get on a profile call

Public data only:

- id, username, name, bio, avatar
- verified, private
- followers, following, likes, videos, sec_uid, url

Curl:

```bash
curl -sS "https://trysocify.com/api/v1/tiktok/profile?username=khaby.lame" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Install (local package)

```bash
cd cheap-tiktok-profile-scraper
pip install -e .
```

Requires Python 3.10+ and `httpx`.

---

## Environment

| Variable | Required | Description |
|----------|----------|-------------|
| `SOCIFY_API_KEY` | Yes | Bearer token from [trysocify.com](https://trysocify.com/register) |
| `SOCIFY_BASE_URL` | No | Default `https://api.trysocify.com` |

---

## Example endpoints used

- `GET /v1/tiktok/profile?username=`
- `GET /v1/tiktok/videos?username=`

Docs: [TikTok profile](https://trysocify.com/docs/api/tiktok/profile) · [TikTok API](https://trysocify.com/docs/api/tiktok) · OpenAPI: [trysocify.com/openapi.json](https://trysocify.com/openapi.json)

---

## License

MIT — see [LICENSE](./LICENSE).

---

## Links

- [Socify — unified social media scraper API](https://trysocify.com)
- [Best TikTok profile scrapers in 2026](https://trysocify.com/compare/best-tiktok-profile-scrapers-2026)
- [TikTok scraper API](https://trysocify.com/tiktok)
- [TikTok profile docs](https://trysocify.com/docs/api/tiktok/profile)
- [Best TikTok scraper APIs in 2026](https://trysocify.com/blog/best-tiktok-scraper-apis-2026)
- [Best low volume TikTok scrapers](https://trysocify.com/use-cases/best-low-volume-tiktok-scrapers-2026)
- [TikTok API alternative](https://trysocify.com/switch/tiktok-api-alternative)
- [Pricing](https://trysocify.com/pricing)
- [Credits](https://trysocify.com/docs/credits)

*Not affiliated with TikTok / ByteDance. Use only for public data and respect platform terms and local law.*
