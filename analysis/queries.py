import pandas as pd
from database.db import get_engine


def run_query(sql):
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(sql, conn)


def permits_by_borough():
    return run_query("""
        SELECT borough,
               COUNT(*) AS total_permits
        FROM permits
        WHERE borough IS NOT NULL
        GROUP BY borough
        ORDER BY total_permits DESC
    """)


def permits_by_job_type():
    return run_query("""
        SELECT job_type,
               COUNT(*) AS total
        FROM permits
        WHERE job_type IS NOT NULL
        GROUP BY job_type
        ORDER BY total DESC
    """)


def monthly_permit_volume():
    return run_query("""
        SELECT DATE_TRUNC('month', latest_action_date) AS month,
               COUNT(*) AS permits
        FROM permits
        WHERE latest_action_date IS NOT NULL
        GROUP BY month
        ORDER BY month
    """)


def approval_lag_by_borough():
    return run_query("""
        SELECT borough,
               ROUND(AVG(approved_date - latest_action_date)::numeric, 1)
               AS avg_days_to_approval
        FROM permits
        WHERE approved_date IS NOT NULL
          AND latest_action_date IS NOT NULL
          AND approved_date > latest_action_date
        GROUP BY borough
        ORDER BY avg_days_to_approval DESC
    """)