# NYC Construction Permit Analytics Pipeline

End-to-end data pipeline that ingests live permit data from the NYC 
Department of Buildings Open Data API, transforms and loads it into 
PostgreSQL, and serves analytics through a Streamlit dashboard.

![Dashboard Preview](dashboard_preview.png)

## Architecture

NYC Open Data API → Python ETL → PostgreSQL → Streamlit + Plotly

## Stack

- Python (Pandas, SQLAlchemy, psycopg2, requests)
- PostgreSQL
- Streamlit + Plotly
- NYC Open Data API (no auth required)

## Setup

1. Clone the repo
2. Create a virtual environment and install dependencies:
   pip install -r requirements.txt
3. Create a PostgreSQL database called nyc_permits
4. Copy .env.example to .env and fill in your credentials
5. Run the schema: psql -U postgres -d nyc_permits -f database/schema.sql
6. Run the pipeline: python pipeline.py
7. Launch the dashboard: streamlit run dashboard/app.py

## What It Does

- Fetches 25,000 permit records from NYC DOB in paginated batches
- Cleans and validates all fields including dates and categorical data
- Upserts into PostgreSQL with conflict handling so re-runs are safe
- Exposes analytical queries covering volume, job type, borough trends,
  and approval timelines
- Renders an interactive dashboard with Plotly charts

## Analytical Questions Answered

- Which boroughs have the most permit activity?
- What job types dominate NYC construction?
- How has permit volume trended since 1990?
- How long does approval take by borough?
