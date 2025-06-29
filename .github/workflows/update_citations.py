#!/usr/bin/env python
import os, yaml, pathlib
from scholarly import scholarly

def main():
    user_id = os.environ["SCHOLAR_USER_ID"].strip()
    if not user_id:
        raise SystemExit("SCHOLAR_USER_ID not set")

    # Fetch profile
    profile = scholarly.search_author_id(user_id, filled=True)
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
