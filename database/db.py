import psycopg2
from psycopg2.extras import execute_values
from sqlalchemy import create_engine
from config import DB_CONFIG


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def get_engine():
    cfg = DB_CONFIG
    url = (
        f"postgresql+psycopg2://{cfg['user']}:{cfg['password']}"
        f"@{cfg['host']}:{cfg['port']}/{cfg['database']}"
    )
    return create_engine(url)


def upsert_permits(df):
    if df.empty:
        print("No records to upsert.")
        return

    conn = get_connection()
    cur = conn.cursor()
    cols = list(df.columns)
    values = [tuple(row) for row in df.itertuples(index=False)]

    insert_sql = f"""
        INSERT INTO permits ({', '.join(cols)})
        VALUES %s
        ON CONFLICT (job_id) DO UPDATE SET
        {', '.join([f"{c} = EXCLUDED.{c}" for c in cols if c != 'job_id'])},
        ingested_at = NOW()
    """

    execute_values(cur, insert_sql, values)
    conn.commit()
    cur.close()
    conn.close()
    print(f"Upserted {len(values)} records into permits table.")