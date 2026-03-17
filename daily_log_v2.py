import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from datetime import date, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from fpdf import FPDF
import os

# --------------------------------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="The Lymphie Sanctuary - Daily Body Log (Prototype v3)",
    layout="wide"
)

st.markdown(
    """
    <h1 style='color:#2E8B8B; font-weight:700;'>
        🌿 THE LYMPHIE SANCTUARY
    </h1>
    <h3 style='margin-top:-10px; color:#444;'>Daily Body Log (Prototype v3)</h3>
    <p style='color:#666; font-size:15px;'>
        A calm space to track your lymphatic wellbeing.<br>
        Not medical advice, diagnosis, or treatment.
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------------------------------
# INITIALISE NEW DATABASE
# --------------------------------------------------------------------------
engine = create_engine("sqlite:///lymphie_logs_v3.db", echo=False)

# --------------------------------------------------------------------------
# LOAD EXISTING ENTRIES
# --------------------------------------------------------------------------
try:
    logs_df = pd.read_sql("daily_logs", con=engine)
except Exception:
    logs_df = pd.DataFrame()

# --------------------------------------------------------------------------
# DAILY ENTRY FORM — NEW QUESTIONNAIRE
# --------------------------------------------------------------------------
with st.form("daily_log_form", clear_on_submit=False):
    st.subheader("Daily Entry Form")

    # --- Core Symptoms ---
    log_date = st.date_input("Date of Entry", date.today())
    heaviness = st.slider("Limb heaviness / tightness", 0, 10, 5)
    pain = st.slider("Limb pain / discomfort", 0, 10, 3)

    appearance = st.radio(
        "Limb appearance (vs baseline)",
        [
            "Baseline / normal",
            "Slight puffiness (pitting)",
            "Noticeable swelling (firm)",
            "Marked swelling / skin stretched"
        ]
    )

    measurement_taken = st.radio("Did you take a limb measurement today?", ["Yes", "No"])

    areas = st.multiselect(
        "Affected area(s)",
        ["Left arm", "Right arm", "Left leg", "Right leg", "Trunk", "Head/Neck", "Genitalia", "Other"]
    )

    # --- Compression ---
    compression_type = st.selectbox(
        "Compression worn (most of day)",
        [
            "None",
            "Light support OTC",
            "Circular knit standard",
            "Flat knit custom",
            "Bandages / wraps",
            "Night garment",
            "Kinesio taping"
        ]
    )
    hours_worn = st.number_input("Approx hours compression worn", 0, 24, 0)

    self_mld = st.radio("Self-MLD or dry brushing performed today?", ["No", "Yes"])

    # --- Triggers ---
    st.markdown("### Lifestyle & Potential Triggers")

    dietary = st.multiselect(
        "Dietary triggers",
        ["High salt meal", "High sugar / refined carbs", "Alcohol (>1 drink)", "Caffeine (>2 cups)"]
    )

    environmental = st.multiselect(
        "Environmental / activity triggers",
        ["Heat exposure", "Long travel > 2h", "Repetitive limb movement", "Injury / skin break", "Tight clothing / jewellery"]
    )

    health = st.multiselect(
        "Health triggers",
        ["Infection (fever/heat/redness)", "Menstrual cycle", "New medication / dose change", "Fatigue"]
    )

    # --- Wellness ---
    st.markdown("### Wellness Context")

    stress = st.slider("Stress level", 0, 10, 4)
    sleep = st.radio("Sleep quality", ["Poor (<5h)", "Fair (5–7h)", "Good (7–8h)", "Very good (8+h)"])
    energy = st.slider("Energy level", 0, 10, 6)
    mobility = st.slider("Mobility / ease of movement", 0, 10, 7)
    compassion = st.slider("Self-compassion today", 0, 10, 7)

    # --- Reflection ---
    st.markdown("### Reflection")

    challenge = st.text_area("Biggest challenge today")
    small_win = st.text_area("Small win / what helped today")

    # --- Environment ---
    st.markdown("### Environment")

    temperature = st.number_input("Temperature (°C)", -10.0, 50.0, 22.0)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 40.0)

    tags = st.text_input("Tags / keywords (optional)")

    submitted = st.form_submit_button("Save Entry", type="primary")

    if submitted:
        new_row = pd.DataFrame([{
            "Date": log_date,
            "Heaviness": heaviness,
            "Pain": pain,
            "Appearance": appearance,
            "MeasurementTaken": measurement_taken,
            "Areas": ", ".join(areas),
            "CompressionType": compression_type,
            "HoursWorn": hours_worn,
            "SelfMLD": self_mld,
            "DietaryTriggers": ", ".join(dietary),
            "EnvironmentalTriggers": ", ".join(environmental),
            "HealthTriggers": ", ".join(health),
            "Stress": stress,
            "Sleep": sleep,
            "Energy": energy,
            "Mobility": mobility,
            "Compassion": compassion,
            "Challenge": challenge,
            "SmallWin": small_win,
            "Temperature": temperature,
            "Humidity": humidity,
            "Tags": tags,
            "Timestamp": datetime.now()
        }])

        logs_df = pd.concat([logs_df, new_row], ignore_index=True)
        logs_df.to_sql("daily_logs", con=engine, if_exists="replace", index=False)

        st.success("Entry saved successfully!")

# --------------------------------------------------------------------------
# RECENT ENTRIES
# --------------------------------------------------------------------------
st.markdown("---")
st.subheader("Your Recent Entries")

if logs_df.empty:
    st.info("No entries yet — fill out the form above.")
else:
    logs_df["Date"] = pd.to_datetime(logs_df["Date"])
    logs_df = logs_df.sort_values("Date")
    st.dataframe(logs_df.tail(7), use_container_width=True)

# --------------------------------------------------------------------------
# CLEANED-UP CHARTS (Option B)
# --------------------------------------------------------------------------
if not logs_df.empty:
    st.markdown("---")
    st.subheader("Symptom Trends")

    df_plot = logs_df.copy()
    df_plot["Date"] = pd.to_datetime(df_plot["Date"], errors="coerce")
    df_plot = df_plot.sort_values("Date").dropna(subset=["Date"])

    numeric_cols = ["Heaviness", "Pain", "Stress", "Energy", "Mobility", "Compassion"]
    df_plot[numeric_cols] = df_plot[numeric_cols].apply(pd.to_numeric, errors="coerce")

    chart_colors = {
        "Heaviness": "#2E8B8B",
        "Pain": "#e08b2e",
        "Stress": "#8b2e72",
        "Energy": "#2b7a0b",
        "Mobility": "#7258b4",
        "Compassion": "#33a1fd"
    }

    cols = st.columns(3)
    for i, (label, color) in enumerate(chart_colors.items()):
        with cols[i % 3]:
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(df_plot["Date"], df_plot[label], marker="o", color=color, linewidth=2)
            ax.set_title(label, fontsize=12, color="#333")
            ax.set_ylim(0, 10)
            ax.set_ylabel("Score (0–10)")
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
            ax.xaxis.set_major_locator(mdates.AutoDateLocator())
            fig.autofmt_xdate(rotation=30)
            plt.tight_layout()
            st.pyplot(fig)

# --------------------------------------------------------------------------
# WEEKLY SNAPSHOT
# --------------------------------------------------------------------------
st.markdown("---")
st.subheader("Weekly Snapshot")
st.caption("Lower scores = less symptom intensity.")

if not logs_df.empty:
    df_plot["Week"] = df_plot["Date"].dt.to_period("W").apply(lambda r: r.start_time)
    week_avg = (
        df_plot.groupby("Week")[numeric_cols]
        .mean().round(1).reset_index().sort_values("Week")
    )

    if len(week_avg) >= 2:
        now, prev = week_avg.iloc[-1], week_avg.iloc[-2]
        st.markdown(f"### Week starting {now['Week'].strftime('%d %b %Y')}")
        cols = st.columns(len(numeric_cols))

        for i, m in enumerate(numeric_cols):
            change = now[m] - prev[m]
            arrow = "↓" if change < 0 else "↑" if change > 0 else "→"
            cols[i].metric(label=m, value=f"{now[m]:.1f}", delta=f"{arrow} {abs(change):.1f}")
    else:
        st.info("Not enough weekly data yet.")

# --------------------------------------------------------------------------
# MONTHLY SNAPSHOT
# --------------------------------------------------------------------------
st.markdown("---")
st.subheader("Monthly Snapshot")

if not logs_df.empty:
    df_plot["Month"] = df_plot["Date"].dt.to_period("M").apply(lambda r: r.start_time)
    month_avg = (
        df_plot.groupby("Month")[numeric_cols]
        .mean().round(1).reset_index().sort_values("Month")
    )

    if len(month_avg) >= 2:
        now_m, prev_m = month_avg.iloc[-1], month_avg.iloc[-2]
        st.markdown(f"### Month of {now_m['Month'].strftime('%B %Y')}")
        cols = st.columns(len(numeric_cols))

        for i, m in enumerate(numeric_cols):
            change = now_m[m] - prev_m[m]
            arrow = "↓" if change < 0 else "↑" if change > 0 else "→"
            cols[i].metric(label=m, value=f"{now_m[m]:.1f}", delta=f"{arrow} {abs(change):.1f}")
    else:
        st.info("Not enough monthly data yet.")

# --------------------------------------------------------------------------
# REFLECTIONS
# --------------------------------------------------------------------------
if not logs_df.empty:
    st.markdown("---")
    st.subheader("Daily Reflections")

    reflections = df_plot[["Date", "Challenge", "SmallWin"]].sort_values("Date", ascending=False).tail(10)
    reflections["Date"] = reflections["Date"].dt.strftime("%d %b %Y")

    for _, row in reflections.iterrows():
        with st.expander(f"{row['Date']}"):
            st.markdown(f"**Biggest Challenge:** {row['Challenge'] or '-'}")
            st.markdown(f"**Small Win / What Helped:** {row['SmallWin'] or '-'}")

# --------------------------------------------------------------------------
# EXPORT SUMMARY TO PDF — OPTION C (Short + Full Summary)
# --------------------------------------------------------------------------
st.markdown("---")
st.subheader("Export Your Summary")

if st.button("Generate PDF"):

    if logs_df.empty:
        st.warning("No data to export yet.")
    else:
        df_plot["Week"] = df_plot["Date"].dt.to_period("W").apply(lambda r: r.start_time)
        df_plot["Month"] = df_plot["Date"].dt.to_period("M").apply(lambda r: r.start_time)

        weekly_df = (
            df_plot.groupby("Week")[numeric_cols]
            .mean().round(1).reset_index().sort_values("Week")
        )

        monthly_df = (
            df_plot.groupby("Month")[numeric_cols]
            .mean().round(1).reset_index().sort_values("Month")
        )

        reflections_df = df_plot[["Date", "Challenge", "SmallWin"]].dropna(how="all")

        class SanctuaryPDF(FPDF):
            def header(self):
                if os.path.exists("logo.png"):
                    self.image("logo.png", x=10, y=8, w=25)
                self.set_xy(40, 12)
                self.set_text_color(46, 139, 139)
                self.set_font("Helvetica", "B", 16)
                self.cell(0, 12, "The Lymphie Sanctuary — Summary", ln=True)
                self.set_draw_color(220, 220, 220)
                self.line(10, 28, 200, 28)
                self.ln(10)

            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 9)
                self.set_text_color(120, 120, 120)
                self.cell(0, 8, f"Page {self.page_no()}", align="C")

        def generate_pdf():
            pdf = SanctuaryPDF()
            pdf.set_auto_page_break(auto=True, margin=18)
            pdf.add_page()
            pdf.set_font("Helvetica", "", 11)
            pdf.set_text_color(40, 40, 40)

            # --- Short Summary ---
            pdf.set_font("Helvetica", "B", 13)
            pdf.set_text_color(46, 139, 139)
            pdf.cell(0, 8, "Short Summary", ln=True)
            pdf.set_font("Helvetica", "", 11)
            pdf.set_text_color(40, 40, 40)

            latest = logs_df.iloc[-1]
            pdf.multi_cell(
                0, 6,
                f"Date: {latest['Date']}\n"
                f"Heaviness: {latest['Heaviness']} | Pain: {latest['Pain']}\n"
                f"Appearance: {latest['Appearance']}\n"
                f"Compression: {latest['CompressionType']} ({latest['HoursWorn']}h)\n"
                f"Triggers: {latest['DietaryTriggers']}, {latest['EnvironmentalTriggers']}, {latest['HealthTriggers']}\n"
                f"Challenge: {latest['Challenge'] or '-'}\n"
                f"Small Win: {latest['SmallWin'] or '-'}\n"
            )
            pdf.ln(5)

            # --- Full Summary ---
            pdf.set_font("Helvetica", "B", 13)
            pdf.set_text_color(46, 139, 139)
            pdf.cell(0, 8, "Full Summary", ln=True)
            pdf.set_font("Helvetica", "", 11)
            pdf.set_text_color(40, 40, 40)

            # Weekly
            pdf.ln(2)
            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 7, "Weekly Averages", ln=True)
            pdf.set_font("Helvetica", "", 11)
            if not weekly_df.empty:
                row = weekly_df.iloc[-1]
                pdf.multi_cell(
                    0, 6,
                    f"Week of {row['Week'].strftime('%d %b %Y')}\n"
                    + " | ".join(f"{c}: {row[c]}" for c in numeric_cols)
                )
            pdf.ln(4)

            # Monthly
            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 7, "Monthly Averages", ln=True)
            pdf.set_font("Helvetica", "", 11)
            if not monthly_df.empty:
                row = monthly_df.iloc[-1]
                pdf.multi_cell(
                    0, 6,
                    f"Month of {row['Month'].strftime('%B %Y')}\n"
                    + " | ".join(f"{c}: {row[c]}" for c in numeric_cols)
                )
            pdf.ln(4)

            # Reflections
            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 7, "Recent Reflections", ln=True)
            pdf.set_font("Helvetica", "", 11)
            if not reflections_df.empty:
                for _, r in reflections_df.tail(5).iterrows():
                    pdf.multi_cell(
                        0, 6,
                        f"{r['Date'].strftime('%d %b %Y')} — "
                        f"Challenge: {r['Challenge'] or '-'} | "
                        f"Small Win: {r['SmallWin'] or '-'}"
                    )
                    pdf.ln(1)
            else:
                pdf.cell(0, 6, "No reflections yet.", ln=True)

            # Disclaimer
            pdf.ln(5)
            pdf.set_text_color(120, 120, 120)
            pdf.set_font("Helvetica", "I", 9)
            pdf.multi_cell(
                0, 6,
                "This log is for personal tracking only and not medical advice, "
                "diagnosis, or treatment."
            )

            return bytes(pdf.output(dest="S"))

        pdf_bytes = generate_pdf()

        st.download_button(
            label="Download Summary PDF",
            data=pdf_bytes,
            file_name="Lymphie_Sanctuary_Summary.pdf",
            mime="application/pdf"
        )

