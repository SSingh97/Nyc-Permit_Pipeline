from ingestion.fetch_permits import fetch_all
from transformation.clean_permits import clean
from database.db import upsert_permits


def run():
    print("=== NYC Permit Pipeline Starting ===")

    print("\n[1/3] Fetching from NYC Open Data API...")
    raw = fetch_all(max_records=25000)

    if raw.empty:
        print("No data fetched. Exiting.")
        return

    print("\n[2/3] Cleaning and transforming...")
    cleaned = clean(raw)

    print("\n[3/3] Loading into PostgreSQL...")
    upsert_permits(cleaned)

    print("\n=== Pipeline Complete ===")


if __name__ == "__main__":
    run()