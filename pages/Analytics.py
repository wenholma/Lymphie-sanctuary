import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")

st.title("📊 Your Sanctuary Insights")
st.markdown("Discover patterns in your symptoms over time.")

# Check if we have data
if "log_df" not in st.session_state or st.session_state.log_df.empty:
    st.warning("No data yet. Complete a few daily logs to see insights!")
    st.stop()

df = st.session_state.log_df.copy()

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort by date
df = df.sort_values('Date')

# Sidebar filters
st.sidebar.header("Filter Data")
date_range = st.sidebar.selectbox(
    "Time Range",
    ["Last 7 days", "Last 30 days", "Last 90 days", "All time"]
)

# Apply date filter
if date_range == "Last 7 days":
    cutoff = datetime.now() - timedelta(days=7)
    df = df[df['Date'] >= cutoff]
elif date_range == "Last 30 days":
    cutoff = datetime.now() - timedelta(days=30)
    df = df[df['Date'] >= cutoff]
elif date_range == "Last 90 days":
    cutoff = datetime.now() - timedelta(days=90)
    df = df[df['Date'] >= cutoff]

if df.empty:
    st.warning(f"No data in selected range. Try a different filter.")
    st.stop()

# ---------- METRICS ROW ----------
st.subheader("Summary")
col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_heaviness = df['Heaviness'].mean()
    st.metric("Avg Heaviness", f"{avg_heaviness:.1f}/10")

with col2:
    avg_pain = df['Pain'].mean()
    st.metric("Avg Pain", f"{avg_pain:.1f}/10")

with col3:
    # Compression adherence
    compression_days = df[df['Compression Type'] != 'None'].shape[0]
    total_days = df.shape[0]
    adherence = (compression_days / total_days) * 100
    st.metric("Compression Adherence", f"{adherence:.0f}%")

with col4:
    # Days with data
    st.metric("Days Logged", total_days)

# ---------- SYMPTOM TRENDS ----------
st.subheader("Symptom Trends Over Time")

# Create figure with secondary y-axis
fig = go.Figure()

# Add Heaviness trace
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Heaviness'],
    mode='lines+markers',
    name='Heaviness',
    line=dict(color='#4f6b6a', width=3),
    marker=dict(size=6)
))

# Add Pain trace
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Pain'],
    mode='lines+markers',
    name='Pain',
    line=dict(color='#a9d7d0', width=3),
    marker=dict(size=6)
))

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Severity (0-10)",
    hovermode='x unified',
    template='simple_white',
    height=400
)

st.plotly_chart(fig, use_container_width=True)

# ---------- COMPRESSION IMPACT ----------
st.subheader("Compression Impact")

# Group by compression type
compression_impact = df.groupby('Compression Type')[['Heaviness', 'Pain']].mean().reset_index()

if not compression_impact.empty:
    fig2 = px.bar(
        compression_impact,
        x='Compression Type',
        y=['Heaviness', 'Pain'],
        barmode='group',
        title="Average Symptoms by Compression Type",
        color_discrete_sequence=['#4f6b6a', '#a9d7d0']
    )
    fig2.update_layout(template='simple_white', height=400)
    st.plotly_chart(fig2, use_container_width=True)

# ---------- WEEKLY PATTERN ----------
st.subheader("Day of Week Pattern")

# Add day of week
df['DayOfWeek'] = df['Date'].dt.day_name()

# Order days
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekly = df.groupby('DayOfWeek')[['Heaviness', 'Pain']].mean().reindex(day_order).reset_index()

fig3 = px.line(
    weekly,
    x='DayOfWeek',
    y=['Heaviness', 'Pain'],
    title="Average Symptoms by Day of Week",
    color_discrete_sequence=['#4f6b6a', '#a9d7d0']
)
fig3.update_layout(template='simple_white', height=400)
st.plotly_chart(fig3, use_container_width=True)

# ---------- RAW DATA ----------
with st.expander("View Raw Data"):
    st.dataframe(df, use_container_width=True)