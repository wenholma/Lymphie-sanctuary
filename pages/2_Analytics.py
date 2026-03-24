import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")

# CSS for centering and sidebar fix
st.markdown("""
<style>
    /* Center main page headings and metrics */
    h1, h2, h3, .stSubheader, .stMetric {
        text-align: center;
    }
    /* Remove the "keyboard_double_" fallback text in the sidebar collapse button */
    [data-testid="stSidebarCollapseButton"] svg + span {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align: center;">📊 Your Sanctuary Insights</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;">Discover patterns in your symptoms over time.</p>', unsafe_allow_html=True)

if "log_df" not in st.session_state or st.session_state.log_df.empty:
    st.warning("No data yet. Complete a few daily logs to see insights!")
    st.stop()

df = st.session_state.log_df.copy()
df['Date'] = pd.to_datetime(df['Date'])
df['Compression Hours'] = pd.to_numeric(df['Compression Hours'], errors='coerce').fillna(0)
df = df.sort_values('Date')

# Date range picker (remains left‑aligned in sidebar – fine)
st.sidebar.header("Select Date Range")
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
col1, col2 = st.sidebar.columns(2)
with col1:
    start_date = st.date_input("Start", value=min_date, min_value=min_date, max_value=max_date)
with col2:
    end_date = st.date_input("End", value=max_date, min_value=min_date, max_value=max_date)

if start_date > end_date:
    st.sidebar.error("Start date cannot be after end date.")
    st.stop()

filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
if filtered_df.empty:
    st.warning(f"No data in selected date range. Please adjust your selection.")
    st.stop()

total_days = len(filtered_df)
st.success(f"Showing data from {start_date} to {end_date} ({total_days} days)")

# ---------- Metrics (centered via CSS) ----------
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    avg_heaviness = filtered_df['Heaviness'].mean()
    st.metric("Avg Heaviness", f"{avg_heaviness:.1f}/10")
with col2:
    avg_pain = filtered_df['Pain'].mean()
    st.metric("Avg Pain", f"{avg_pain:.1f}/10")
with col3:
    compression_days = filtered_df[filtered_df['Compression Hours'] > 0].shape[0]
    adherence = (compression_days / total_days) * 100
    st.metric("Compression Adherence", f"{adherence:.0f}%")
with col4:
    avg_hours = filtered_df[filtered_df['Compression Hours'] > 0]['Compression Hours'].mean()
    st.metric("Avg Hours (when worn)", f"{avg_hours:.1f}h")
with col5:
    st.metric("Days Logged", total_days)

# ---------- Dual‑axis chart ----------
st.subheader("💪 Compression Impact: Symptoms vs. Hours Worn")
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Heaviness'],
                         name="Heaviness", mode='lines+markers',
                         line=dict(color='#4f6b6a', width=3), marker=dict(size=8)),
              secondary_y=False)
fig.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Pain'],
                         name="Pain", mode='lines+markers',
                         line=dict(color='#a9d7d0', width=3), marker=dict(size=8)),
              secondary_y=False)

comp_data = filtered_df[filtered_df['Compression Hours'] > 0]
if not comp_data.empty:
    fig.add_trace(go.Bar(x=comp_data['Date'], y=comp_data['Compression Hours'],
                         name="Compression Hours",
                         marker=dict(color='#f1e4d3', line=dict(color='#4f6b6a', width=1)), opacity=0.7),
                  secondary_y=True)

fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Symptom Severity (0-10)", secondary_y=False)
fig.update_yaxes(title_text="Compression Hours", secondary_y=True)
fig.update_layout(title="See how symptoms decrease when compression hours increase",
                  hovermode='x unified', template='simple_white', height=500,
                  legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
fig.update_xaxes(tickformat="%Y-%m-%d")
st.plotly_chart(fig, use_container_width=True)
st.info("💡 **Insight**: Look for patterns where symptom lines drop when compression bars rise — that's your proof it's working!")

# ---------- Compression efficacy ----------
st.subheader("📊 Compression Efficacy")
filtered_df['Compression Range'] = pd.cut(
    filtered_df['Compression Hours'],
    bins=[-1, 0, 4, 8, 12, 24],
    labels=['None', '1-4 hours', '5-8 hours', '9-12 hours', '12+ hours']
)
efficacy = filtered_df.groupby('Compression Range')[['Heaviness', 'Pain']].mean().reset_index()
if not efficacy.empty:
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(name='Heaviness', x=efficacy['Compression Range'], y=efficacy['Heaviness'], marker_color='#4f6b6a'))
    fig2.add_trace(go.Bar(name='Pain', x=efficacy['Compression Range'], y=efficacy['Pain'], marker_color='#a9d7d0'))
    fig2.update_layout(title="Average Symptoms by Compression Duration",
                       xaxis_title="Compression Hours", yaxis_title="Symptom Severity (0-10)",
                       barmode='group', template='simple_white', height=400)
    st.plotly_chart(fig2, use_container_width=True)
    best_range = efficacy.loc[efficacy[['Heaviness', 'Pain']].mean(axis=1).idxmin(), 'Compression Range']
    st.success(f"✨ **Your optimal compression duration**: {best_range} shows the lowest symptom scores.")

# ---------- Simple symptom trends ----------
st.subheader("Symptom Trends Over Time")
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Heaviness'],
                          mode='lines+markers', name='Heaviness',
                          line=dict(color='#4f6b6a', width=3), marker=dict(size=6)))
fig3.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Pain'],
                          mode='lines+markers', name='Pain',
                          line=dict(color='#a9d7d0', width=3), marker=dict(size=6)))
fig3.update_layout(xaxis_title="Date", yaxis_title="Severity (0-10)",
                   hovermode='x unified', template='simple_white', height=400)
fig3.update_xaxes(tickformat="%Y-%m-%d")
st.plotly_chart(fig3, use_container_width=True)

# ---------- Day of week pattern ----------
st.subheader("Day of Week Pattern")
filtered_df['DayOfWeek'] = filtered_df['Date'].dt.day_name()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekly = filtered_df.groupby('DayOfWeek')[['Heaviness', 'Pain']].mean().reindex(day_order).reset_index()
fig4 = px.line(weekly, x='DayOfWeek', y=['Heaviness', 'Pain'],
               title="Average Symptoms by Day of Week",
               color_discrete_sequence=['#4f6b6a', '#a9d7d0'])
fig4.update_layout(template='simple_white', height=400)
st.plotly_chart(fig4, use_container_width=True)

# ---------- Raw data expander ----------
with st.expander("View Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)