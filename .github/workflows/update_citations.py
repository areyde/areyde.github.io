#!/usr/bin/env python
import os, yaml, pathlib
from scholarly import scholarly, ProxyGenerator
import logging, time

logging.basicConfig(level=logging.INFO)

def get_citations_with_retries(user_id, attempts=8, wait=3):
    pg = ProxyGenerator()
    pg.FreeProxies(rand=True, n=20)
    scholarly.use_proxy(pg)

    for n in range(1, attempts+1):
        try:
            prof = scholarly.search_author_id(user_id)
            return prof["citedby"]
        except (AttributeError, ProxyGeneratorError) as e:
            # CAPTCHA or bad proxy
            print(f"Attempt {n}/{attempts} failed: {e!r}")
            scholarly.use_proxy(pg)          # switch to next proxy
            time.sleep(random.uniform(1, wait))

    raise RuntimeError("All proxies failed or Google blocked us")

def main():
    user_id = os.environ["SCHOLAR_USER_ID"].strip()
    total = get_citations_with_retries(user_id)

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
