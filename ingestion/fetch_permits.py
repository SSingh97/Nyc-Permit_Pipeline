import requests
import pandas as pd
from config import API_BASE_URL, API_LIMIT


def fetch_batch(offset=0, limit=API_LIMIT):
    params = {
        "$limit": limit,
        "$offset": offset,
    }
    response = requests.get(API_BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    return pd.DataFrame(response.json())


def fetch_all(max_records=25000):
    all_batches = []
    offset = 0

    while offset < max_records:
        print(f"Fetching records {offset} to {offset + API_LIMIT}...")
        try:
            batch = fetch_batch(offset=offset)
        except Exception as e:
            print(f"Error at offset {offset}: {e}")
            break

        if batch.empty:
            print("No more records.")
            break

        all_batches.append(batch)
        offset += API_LIMIT

    if not all_batches:
        return pd.DataFrame()

    combined = pd.concat(all_batches, ignore_index=True)
    print(f"Total raw records fetched: {len(combined)}")
    return combined