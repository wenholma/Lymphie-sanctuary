import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
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

# Convert Compression Hours to numeric, filling NaN with 0
df['Compression Hours'] = pd.to_numeric(df['Compression Hours'], errors='coerce').fillna(0)

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
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    avg_heaviness = df['Heaviness'].mean()
    st.metric("Avg Heaviness", f"{avg_heaviness:.1f}/10")

with col2:
    avg_pain = df['Pain'].mean()
    st.metric("Avg Pain", f"{avg_pain:.1f}/10")

with col3:
    # Compression adherence (wore compression >0 hours)
    compression_days = df[df['Compression Hours'] > 0].shape[0]
    total_days = df.shape[0]
    adherence = (compression_days / total_days) * 100
    st.metric("Compression Adherence", f"{adherence:.0f}%")

with col4:
    # Average compression hours on days worn
    avg_hours = df[df['Compression Hours'] > 0]['Compression Hours'].mean()
    st.metric("Avg Hours (when worn)", f"{avg_hours:.1f}h")

with col5:
    st.metric("Days Logged", total_days)

# ---------- DUAL-AXIS CHART: Symptoms vs Compression Hours ----------
st.subheader("💪 Compression Impact: Symptoms vs. Hours Worn")

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add Heaviness trace (left y-axis)
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Heaviness'],
        name="Heaviness",
        mode='lines+markers',
        line=dict(color='#4f6b6a', width=3),
        marker=dict(size=8)
    ),
    secondary_y=False,
)

# Add Pain trace (left y-axis)
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Pain'],
        name="Pain",
        mode='lines+markers',
        line=dict(color='#a9d7d0', width=3),
        marker=dict(size=8)
    ),
    secondary_y=False,
)

# Add Compression Hours trace (right y-axis) - only show bars when >0
compression_data = df[df['Compression Hours'] > 0]
if not compression_data.empty:
    fig.add_trace(
        go.Bar(
            x=compression_data['Date'],
            y=compression_data['Compression Hours'],
            name="Compression Hours",
            marker=dict(color='#f1e4d3', line=dict(color='#4f6b6a', width=1)),
            opacity=0.7
        ),
        secondary_y=True,
    )

# Set axes titles
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Symptom Severity (0-10)", secondary_y=False)
fig.update_yaxes(title_text="Compression Hours", secondary_y=True)

# Update layout
fig.update_layout(
    title="See how symptoms decrease when compression hours increase",
    hovermode='x unified',
    template='simple_white',
    height=500,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

st.plotly_chart(fig, use_container_width=True)

# Add insight text
st.info("💡 **Insight**: Look for patterns where symptom lines drop when compression bars rise — that's your proof it's working!")

# ---------- COMPRESSION EFFICACY ANALYSIS ----------
st.subheader("📊 Compression Efficacy")

# Calculate average symptoms by compression hours ranges
df['Compression Range'] = pd.cut(
    df['Compression Hours'], 
    bins=[-1, 0, 4, 8, 12, 24], 
    labels=['None', '1-4 hours', '5-8 hours', '9-12 hours', '12+ hours']
)

efficacy = df.groupby('Compression Range')[['Heaviness', 'Pain']].mean().reset_index()

if not efficacy.empty:
    fig2 = go.Figure()
    
    fig2.add_trace(go.Bar(
        name='Heaviness',
        x=efficacy['Compression Range'],
        y=efficacy['Heaviness'],
        marker_color='#4f6b6a'
    ))
    
    fig2.add_trace(go.Bar(
        name='Pain',
        x=efficacy['Compression Range'],
        y=efficacy['Pain'],
        marker_color='#a9d7d0'
    ))
    
    fig2.update_layout(
        title="Average Symptoms by Compression Duration",
        xaxis_title="Compression Hours",
        yaxis_title="Symptom Severity (0-10)",
        barmode='group',
        template='simple_white',
        height=400
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Find best range
    best_range = efficacy.loc[efficacy[['Heaviness', 'Pain']].mean(axis=1).idxmin(), 'Compression Range']
    st.success(f"✨ **Your optimal compression duration**: {best_range} shows the lowest symptom scores.")

# ---------- SYMPTOM TRENDS (original) ----------
st.subheader("Symptom Trends Over Time")

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Heaviness'],
    mode='lines+markers',
    name='Heaviness',
    line=dict(color='#4f6b6a', width=3),
    marker=dict(size=6)
))

fig3.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Pain'],
    mode='lines+markers',
    name='Pain',
    line=dict(color='#a9d7d0', width=3),
    marker=dict(size=6)
))

fig3.update_layout(
    xaxis_title="Date",
    yaxis_title="Severity (0-10)",
    hovermode='x unified',
    template='simple_white',
    height=400
)

st.plotly_chart(fig3, use_container_width=True)

# ---------- WEEKLY PATTERN ----------
st.subheader("Day of Week Pattern")

df['DayOfWeek'] = df['Date'].dt.day_name()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekly = df.groupby('DayOfWeek')[['Heaviness', 'Pain']].mean().reindex(day_order).reset_index()

fig4 = px.line(
    weekly,
    x='DayOfWeek',
    y=['Heaviness', 'Pain'],
    title="Average Symptoms by Day of Week",
    color_discrete_sequence=['#4f6b6a', '#a9d7d0']
)
fig4.update_layout(template='simple_white', height=400)
st.plotly_chart(fig4, use_container_width=True)

# ---------- RAW DATA ----------
with st.expander("View Raw Data"):
    st.dataframe(df, use_container_width=True)