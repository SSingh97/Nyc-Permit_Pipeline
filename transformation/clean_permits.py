import pandas as pd


COLUMNS_TO_KEEP = [
    "job__",
    "borough",
    "job_type",
    "permit_status",
    "filing_status",
    "bldg_type",
    "zip_code",
    "filing_date",
    "issuance_date",
    "expiration_date",
    "owner_s_business_type",
]

RENAME_MAP = {
    "job__": "job_id",
    "permit_status": "job_status",
    "filing_status": "job_status_descrp",
    "bldg_type": "building_type",
    "filing_date": "latest_action_date",
    "issuance_date": "approved_date",
    "expiration_date": "fully_permitted_date",
    "owner_s_business_type": "owner_business_type",
}


def parse_date(series):
    parsed = pd.to_datetime(series, format="%m/%d/%Y", errors="coerce")
    result = []
    for val in parsed:
        if pd.isna(val):
            result.append(None)
        else:
            result.append(val.date())
    return result


def clean(df):
    available = [c for c in COLUMNS_TO_KEEP if c in df.columns]
    df = df[available].copy()
    df = df.rename(columns=RENAME_MAP)

    df = df.dropna(subset=["job_id"])
    df["job_id"] = df["job_id"].astype(str).str.strip()
    df = df.drop_duplicates(subset=["job_id"])

    for col in ["latest_action_date", "approved_date", "fully_permitted_date"]:
        if col in df.columns:
            df[col] = parse_date(df[col])

    if "borough" in df.columns:
        df["borough"] = df["borough"].str.strip().str.title()

    print(f"Clean records ready to load: {len(df)}")
    return df