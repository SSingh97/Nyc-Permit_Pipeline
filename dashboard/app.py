import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import plotly.express as px
from analysis.queries import (
    permits_by_borough,
    permits_by_job_type,
    monthly_permit_volume,
    approval_lag_by_borough,
)

st.set_page_config(page_title="NYC Permit Analytics", layout="wide")
st.title("NYC Construction Permit Analytics")
st.caption("Live data from NYC Department of Buildings via Open Data API")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Permits by Borough")
    df = permits_by_borough()
    fig = px.bar(df, x="borough", y="total_permits",
                 color="borough", text="total_permits")
    st.plotly_chart(fig, width="stretch")

with col2:
    st.subheader("Permits by Job Type")
    jt = permits_by_job_type()
    fig2 = px.pie(jt, names="job_type", values="total")
    st.plotly_chart(fig2, width="stretch")

st.subheader("Monthly Permit Volume")
monthly = monthly_permit_volume()
monthly["month"] = monthly["month"].astype(str)
fig3 = px.line(monthly, x="month", y="permits", markers=True)
st.plotly_chart(fig3, width="stretch")

st.subheader("Avg Days to Approval by Borough")
lag = approval_lag_by_borough()
if not lag.empty:
    fig4 = px.bar(lag, x="borough", y="avg_days_to_approval", color="borough")
    st.plotly_chart(fig4, width="stretch")
else:
    st.info("No approval lag data available in current dataset.")