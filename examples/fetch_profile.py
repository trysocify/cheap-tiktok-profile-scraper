#!/usr/bin/env python3
"""Fetch a public TikTok profile with a cheap TikTok profile scraper (Socify).

Usage:
  export SOCIFY_API_KEY=...
  python examples/fetch_profile.py khaby.lame

Signup: https://trysocify.com/register
Docs:   https://trysocify.com/docs/api/tiktok/profile
Guide:  https://trysocify.com/compare/best-tiktok-profile-scrapers-2026
"""

from __future__ import annotations

import json
import sys

from tiktok_profile_scraper import TikTokProfileClient


def main() -> None:
    username = sys.argv[1] if len(sys.argv) > 1 else "tiktok"
    with TikTokProfileClient() as client:
        data = client.profile(username)
    print(json.dumps(data, indent=2, default=str))


if __name__ == "__main__":
    main()
