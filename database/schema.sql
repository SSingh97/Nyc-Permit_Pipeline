CREATE TABLE IF NOT EXISTS permits (
    job_id VARCHAR PRIMARY KEY,
    borough VARCHAR,
    job_type VARCHAR,
    job_status VARCHAR,
    job_status_descrp VARCHAR,
    building_type VARCHAR,
    initial_cost NUMERIC,
    total_sqft NUMERIC,
    existing_no_of_stories INTEGER,
    proposed_no_of_stories INTEGER,
    latest_action_date DATE,
    approved_date DATE,
    fully_permitted_date DATE,
    owner_business_type VARCHAR,
    zip_code VARCHAR,
    ingested_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_borough ON permits(borough);
CREATE INDEX IF NOT EXISTS idx_job_type ON permits(job_type);
CREATE INDEX IF NOT EXISTS idx_latest_action_date ON permits(latest_action_date);
CREATE INDEX IF NOT EXISTS idx_initial_cost ON permits(initial_cost);
