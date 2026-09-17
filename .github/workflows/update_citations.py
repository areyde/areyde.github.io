#!/usr/bin/env python
"""
update_citations.py  ·  GitHub Actions helper for Jekyll

• Fetches total citation count from Google Scholar
• Retries through a small pool of free HTTPS proxies
• Updates _data/citations.yml only when the number changes
"""

import logging
import os
import pathlib
import random
import time

import requests
import yaml
from scholarly import ProxyGenerator, scholarly

# ──────────────────────────── configuration ──────────────────────────── #

MAX_ATTEMPTS      = 10          # how many different proxies to try
WAIT_MAX_SEC      = 4           # max random sleep between retries
PROXY_SOURCE_URL = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
CITATION_YAML     = pathlib.Path("_data/citations.yml")
SCHOLAR_USER_ID   = os.environ["SCHOLAR_USER_ID"].strip()

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
)

# ──────────────────────────── helpers ────────────────────────────────── #

def fetch_free_proxies(n: int) -> list[str]:
    """Return up to `n` random HTTPS proxy strings (“host:port”)."""
    logging.info("Fetching free proxy list…")
    resp = requests.get(PROXY_SOURCE_URL, timeout=10)
    resp.raise_for_status()
    proxies = [line.strip() for line in resp.text.splitlines() if line.strip()]
    random.shuffle(proxies)
    return proxies[:n]

def fetch_metrics_with_retries(
    user_id: str,
    max_attempts: int = MAX_ATTEMPTS,
    wait_max_sec: int = WAIT_MAX_SEC,
) -> tuple[int, int]:

    proxies = fetch_free_proxies(max_attempts)

    for attempt, proxy_str in enumerate(proxies, 1):
        try:
            logging.info(
                "Attempt %d/%d via %s",
                attempt,
                max_attempts,
                proxy_str,
            )

            proxy = ProxyGenerator()

            # This is an HTTP proxy. Leaving https=None makes scholarly
            # use the same HTTP proxy for HTTPS CONNECT requests.
            if not proxy.SingleProxy(http=proxy_str):
                raise RuntimeError("Proxy setup failed")

            scholarly.use_proxy(proxy)

            # First lightweight profile fetch.
            profile = scholarly.search_author_id(user_id)

            # Fetch ONLY the Scholar indices, not the entire profile.
            profile = scholarly.fill(profile, sections=["indices"])

            total = profile["citedby"]
            h_index = profile["hindex"]

            logging.info(
                "Success! Total citations = %s, h-index = %s",
                total,
                h_index,
            )

            return total, h_index

        except Exception as e:
            logging.warning(
                "Attempt %d failed via %s – %s",
                attempt,
                proxy_str,
                e,
            )

        sleep = random.uniform(1, wait_max_sec)
        logging.info("Sleeping %.1fs before next proxy…", sleep)
        time.sleep(sleep)

    raise RuntimeError("All proxies failed – Google still blocking us")

# ──────────────────────────── main routine ───────────────────────────── #

def main() -> None:
    total, h_index = fetch_metrics_with_retries(SCHOLAR_USER_ID)

    # Prepare new data
    new_data = {"total": total, "h_index": h_index}

    # Ensure _data directory exists
    CITATION_YAML.parent.mkdir(parents=True, exist_ok=True)

    # Load current file if exists
    old_data = {}
    if CITATION_YAML.exists():
        old_data = yaml.safe_load(CITATION_YAML.read_text()) or {}

    # Check if anything actually changed
    if old_data.get("total") == total and old_data.get("h_index") == h_index:
        logging.info("Citation data unchanged – nothing to commit.")
        return

    # Save updated YAML
    CITATION_YAML.write_text(
        yaml.dump(new_data, sort_keys=False, default_flow_style=False)
    )
    logging.info("Updated _data/citations.yml → %s", new_data)

if __name__ == "__main__":
    main()
