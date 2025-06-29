#!/usr/bin/env python
import os, yaml, pathlib
from scholarly import scholarly, ProxyGenerator
import logging, time

logging.basicConfig(level=logging.INFO)

def main():
    pg = ProxyGenerator()
    pg.FreeProxies()               # 30-40 public proxies
    scholarly.use_proxy(pg)

    t0 = time.perf_counter()
    user_id = os.environ["SCHOLAR_USER_ID"].strip()
    if not user_id:
        raise SystemExit("SCHOLAR_USER_ID not set")

    # Fetch profile
    logging.info("Fetching profile %s", user_id)
    profile = scholarly.search_author_id(user_id, filled=True)
    logging.info("Fetched in %.1fs", time.perf_counter() - t0)
    total = profile["citedby"]

    # Path to Jekyll data file
    data_path = pathlib.Path("_data/citations.yml")
    data_path.parent.mkdir(parents=True, exist_ok=True)

    # Only rewrite if the number changed
    current = {}
    if data_path.exists():
        current = yaml.safe_load(data_path.read_text()) or {}
    if current.get("total") == total:
        print("Citation count unchanged:", total)
        return

    # Overwrite YAML
    data_path.write_text(yaml.dump({"total": total}, default_flow_style=False))
    print("Updated citation count:", total)

if __name__ == "__main__":
    main()
