import os, random, time, logging, yaml, pathlib
from scholarly import scholarly, ProxyGenerator

logging.basicConfig(level=logging.INFO)
USER_ID = os.environ["SCHOLAR_USER_ID"].strip()

def fetch_citations_with_retries(user_id, max_attempts=10, wait_max_sec=4):
    """Try up to `max_attempts` proxies before giving up."""
    pg = ProxyGenerator()
    pg.FreeProxies(rand=True, n=max_attempts)   # get exactly that many
    scholarly.use_proxy(pg)

    for attempt in range(1, max_attempts + 1):
        try:
            logging.info("Attempt %d/%d", attempt, max_attempts)
            profile = scholarly.search_author_id(user_id)   # filled=False (lighter)
            return profile["citedby"]
        except AttributeError as e:
            # CAPTCHA or page layout failure
            logging.warning("Blocked/captcha: %s", e)
        except Exception as e:
            logging.warning("Proxy error: %s", e)

        scholarly.use_proxy(pg)                      # rotate to next proxy
        sleep = random.uniform(1, wait_max_sec)
        logging.info("Sleeping %.1fs and trying next proxy…", sleep)
        time.sleep(sleep)

    raise RuntimeError("All proxies failed — Google still blocking us")

def main():
    total = fetch_citations_with_retries(USER_ID)

    data_path = pathlib.Path("_data/citations.yml")
    data_path.parent.mkdir(exist_ok=True)

    current = {}
    if data_path.exists():
        current = yaml.safe_load(data_path.read_text()) or {}

    if current.get("total") == total:
        logging.info("Citation count unchanged: %s", total)
        return

    data_path.write_text(yaml.dump({"total": total}, default_flow_style=False))
    logging.info("Updated citation count to %s", total)

if __name__ == "__main__":
    main()