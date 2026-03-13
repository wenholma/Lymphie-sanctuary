import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from datetime import date, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob
from fpdf import FPDF
from PIL import Image
import os

# --------------------------------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="The Lymphie Sanctuary - Daily Body Log (Prototype v2)",
    layout="wide"
)

st.title("The Lymphie Sanctuary - Daily Body Log")
st.caption("Designed in Aotearoa New Zealand for personal tracking only - not medical advice, diagnosis, or treatment.")
st.markdown("---")

# --------------------------------------------------------------------------
# INITIALISE DATABASE
# --------------------------------------------------------------------------
engine = create_engine("sqlite:///lymphie_logs_v2.db", echo=False)

# --------------------------------------------------------------------------
# LOAD EXISTING ENTRIES
# --------------------------------------------------------------------------
try:
    logs_df = pd.read_sql("daily_logs", con=engine)
except Exception:
    logs_df = pd.DataFrame()

# --------------------------------------------------------------------------
# DAILY ENTRY FORM
# --------------------------------------------------------------------------
with st.form("daily_log_form", clear_on_submit=False):
    st.subheader("Daily Entry Form")

    log_date = st.date_input("Date of Entry", date.today())
    heaviness = st.slider("Overall Limb Sensation (Heaviness/Tightness)", 0, 10, 5)
    pain = st.slider("Overall Limb Pain (Aching/Discomfort)", 0, 10, 3)

    appearance = st.radio("Limb Appearance (vs baseline)",
                          ["Baseline / Normal",
                           "Slight puffiness (pitting)",
                           "Noticeable swelling (firm)",
                           "Marked swelling / skin stretched"])

    measurement_taken = st.radio("Did you take a limb measurement today?",
                                 ["Yes", "No"])

    areas = st.multiselect("Affected Area(s)",
                           ["Left arm", "Right arm", "Left leg", "Right leg",
                            "Trunk", "Head/Neck", "Genitalia", "Other"])

    compression_type = st.selectbox("Compression type worn (most of day)",
                                    ["None", "Light support OTC", "Circular knit standard",
                                     "Flat knit custom", "Bandages / wraps",
                                     "Night garment", "Kinesio taping"])

    hours_worn = st.number_input("Approx hours compression worn", 0, 24, 0)

    self_mld = st.radio("Self-MLD or dry brushing performed today?", ["No", "Yes"])

    st.markdown("Lifestyle and Potential Triggers")

    dietary = st.multiselect("Dietary triggers",
                             ["High salt meal", "High sugar / refined carbs",
                              "Alcohol (>1 drink)", "Caffeine (>2 cups)"])

    environmental = st.multiselect("Environmental / Activity triggers",
                                   ["Heat exposure", "Long travel > 2h",
                                    "Repetitive movement of affected limb",
                                    "Injury / skin break", "Tight clothing / jewellery"])

    health = st.multiselect("Health triggers",
                            ["Infection (fever/heat/redness)",
                             "Menstrual cycle (if applicable)",
                             "New medication / dose change",
                             "Fatigue"])

    st.markdown("Wellness Context")

    stress = st.slider("Stress level", 0, 10, 4)
    sleep = st.radio("Sleep quality",
                     ["Poor (<5h, restless)", "Fair (5-7h)",
                      "Good (7-8h)", "Very good (8+h)"])

    energy = st.slider("Energy level", 0, 10, 6)
    mobility = st.slider("Mobility / Ease of movement", 0, 10, 7)
    compassion = st.slider("Self-compassion - I listened to my body today", 0, 10, 7)

    st.markdown("Reflection")

    challenge = st.text_area("Biggest challenge today")
    small_win = st.text_area("Small win / What helped today")

    st.markdown("Environment")

    temperature = st.number_input("Temperature (C)", -10.0, 50.0, 22.0)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 40.0)

    tags = st.text_input("Tags / keywords for this entry (optional)")

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
# DASHBOARD
# --------------------------------------------------------------------------
st.markdown("---")
st.subheader("Your Recent Entries")

if logs_df.empty:
    st.info("No entries yet - fill out the form above.")
else:
    logs_df["Date"] = pd.to_datetime(logs_df["Date"])
    logs_df = logs_df.sort_values("Date")
    st.dataframe(logs_df.tail(7), use_container_width=True)

# --------------------------------------------------------------------------
# SYMPTOM TRENDS
# --------------------------------------------------------------------------
if not logs_df.empty:
    st.markdown("Symptom Trends")

    df_plot = logs_df.copy()
    df_plot["Date"] = pd.to_datetime(df_plot["Date"], errors="coerce")
    df_plot = df_plot.sort_values("Date").dropna(subset=["Date"])

    numeric_cols = ["Heaviness", "Pain", "Stress", "Energy", "Mobility", "Compassion"]
    df_plot[numeric_cols] = df_plot[numeric_cols].apply(pd.to_numeric, errors="coerce")

    metrics = {
        "Heaviness": "#2E8B8B",
        "Pain": "#e08b2e",
        "Stress": "#8b2e72",
        "Energy": "#2b7a0b",
        "Mobility": "#7258b4",
        "Compassion": "#33a1fd"
    }

    cols = st.columns(3)
    for i, (label, color) in enumerate(metrics.items()):
        with cols[i % 3]:
            fig, ax = plt.subplots()
            ax.plot(df_plot["Date"], df_plot[label], marker="o", color=color, linewidth=2)
            ax.set_title(label)
            ax.set_ylim(0, 10)
            ax.set_ylabel("Score (0-10)")
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
            ax.xaxis.set_major_locator(mdates.AutoDateLocator())
            fig.autofmt_xdate(rotation=30)
            plt.tight_layout()
            st.pyplot(fig)

# --------------------------------------------------------------------------
# WEEKLY SNAPSHOT
# --------------------------------------------------------------------------
st.markdown("---")
st.markdown("Weekly Snapshot")
st.caption("Lower scores = less symptom intensity.")

if not logs_df.empty:
    df_plot["Week"] = df_plot["Date"].dt.to_period("W").apply(lambda r: r.start_time)
    week_avg = (df_plot.groupby("Week")[numeric_cols].mean()
                .round(1).reset_index().sort_values("Week"))

    if len(week_avg) >= 2:
        now, prev = week_avg.iloc[-1], week_avg.iloc[-2]
        st.subheader(f"Week starting {now['Week'].strftime('%d %b %Y')}")
        cols = st.columns(len(numeric_cols))

        for i, m in enumerate(numeric_cols):
            change = now[m] - prev[m]
            arrow = "Down" if change < 0 else "Up" if change > 0 else "No change"
            cols[i].metric(label=m,
                           value=f"{now[m]:.1f}",
                           delta=f"{arrow} {abs(change):.1f}",
                           delta_color="inverse")
    else:
        st.info("Not enough weekly data for comparison yet.")

# --------------------------------------------------------------------------
# MONTHLY SNAPSHOT
# --------------------------------------------------------------------------
st.markdown("Monthly Snapshot")

if not logs_df.empty:
    df_plot["Month"] = df_plot["Date"].dt.to_period("M").apply(lambda r: r.start_time)
    month_avg = (df_plot.groupby("Month")[numeric_cols].mean()
                 .round(1).reset_index().sort_values("Month"))

    if len(month_avg) >= 2:
        now_m, prev_m = month_avg.iloc[-1], month_avg.iloc[-2]
        st.subheader(f"Month of {now_m['Month'].strftime('%B %Y')}")
        cols = st.columns(len(numeric_cols))

        for i, m in enumerate(numeric_cols):
            change = now_m[m] - prev_m[m]
            arrow = "Down" if change < 0 else "Up" if change > 0 else "No change"
            cols[i].metric(label=m,
                           value=f"{now_m[m]:.1f}",
                           delta=f"{arrow} {abs(change):.1f}",
                           delta_color="inverse")
    else:
        st.info("No monthly comparison yet.")

# --------------------------------------------------------------------------
# REFLECTIONS
# --------------------------------------------------------------------------
if not logs_df.empty:
    st.markdown("---")
    st.markdown("Daily Reflections")

    if "Challenge" in df_plot.columns and "SmallWin" in df_plot.columns:
        reflections = df_plot[["Date", "Challenge", "SmallWin"]]\
            .sort_values("Date", ascending=False).tail(10)
        reflections["Date"] = reflections["Date"].dt.strftime("%d %b %Y")

        for _, row in reflections.iterrows():
            with st.expander(f"{row['Date']}"):
                st.markdown(f"**Biggest Challenge:**  {row['Challenge'] or '-'}")
                st.markdown(f"**What Helped / Small Win:**  {row['SmallWin'] or '-'}")
    else:
        st.info("No reflections recorded yet.")

# --------------------------------------------------------------------------
# QUALITATIVE INSIGHTS
# --------------------------------------------------------------------------
st.markdown("---")
st.markdown("Qualitative Insights")

if not logs_df.empty:
    text_data = " ".join(df_plot["Challenge"].dropna().astype(str)) + " " + \
                " ".join(df_plot["SmallWin"].dropna().astype(str))

    if text_data.strip() == "":
        st.info("No reflections yet for text-based analysis.")
    else:
        clean_words = [w for w in text_data.split() if w.lower() not in STOPWORDS]
        wc = WordCloud(width=800, height=350,
                       background_color="white",
                       colormap="viridis",
                       max_words=100).generate(" ".join(clean_words))

        st.image(wc.to_array(), caption="Most frequent words in reflections")

        blob = TextBlob(text_data)
        polarity = blob.sentiment.polarity
        tone = "positive" if polarity > 0.05 else "negative" if polarity < -0.05 else "neutral"
        st.caption(f"Average reflection tone: {tone} ({polarity:.2f})")

        st.markdown("Keyword Filter")
        key = st.text_input("Enter a keyword to find related reflections:")

        if key:
            mask = (df_plot["Challenge"].str.contains(key, case=False, na=False) |
                    df_plot["SmallWin"].str.contains(key, case=False, na=False))
            hits = df_plot.loc[mask, ["Date", "Challenge", "SmallWin"]]
            st.dataframe(hits.sort_values("Date", ascending=False),
                         use_container_width=True)

# --------------------------------------------------------------------------
# EXPORT SUMMARY TO PDF
# --------------------------------------------------------------------------
st.markdown("---")
st.markdown("Export Your Summary")

# Always show the button
if st.button("Generate PDF"):

    if logs_df.empty:
        st.warning("No data to export yet.")
    else:
        df_plot["Week"] = df_plot["Date"].dt.to_period("W").apply(lambda r: r.start_time)
        df_plot["Month"] = df_plot["Date"].dt.to_period("M").apply(lambda r: r.start_time)

        numeric_cols = ["Heaviness", "Pain", "Stress", "Energy", "Mobility", "Compassion"]

        weekly_df = (df_plot.groupby("Week")[numeric_cols]
                     .mean().round(1).reset_index().sort_values("Week"))

        monthly_df = (df_plot.groupby("Month")[numeric_cols]
                      .mean().round(1).reset_index().sort_values("Month"))

        reflections_df = df_plot[["Date", "Challenge", "SmallWin"]].dropna(how="all")

        class SanctuaryPDF(FPDF):
            def header(self):
                if os.path.exists("logo.png"):
                    self.image("logo.png", x=10, y=8, w=25)
                self.set_xy(40, 12)
                self.set_text_color(46, 139, 139)
                self.set_font("Helvetica", "B", 16)
                self.cell(0, 12, "The Lymphie Sanctuary - Daily Summary", ln=True)
                self.set_draw_color(222, 229, 234)
                self.line(10, 28, 200, 28)
                self.ln(10)

            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 9)
                self.set_text_color(120, 120, 120)
                self.cell(0, 8, f"Page {self.page_no()}", align="C")

        def generate_pdf(weekly_df, monthly_df, reflections_df):
            pdf = SanctuaryPDF()
            pdf.set_auto_page_break(auto=True, margin=18)
            pdf.add_page()
            pdf.set_font("Helvetica", "", 11)
            pdf.set_text_color(43, 43, 43)

            pdf.multi_cell(
                0,
                7,
                f"Generated on {datetime.now().strftime('%A, %d %b %Y')}\n\n"
                "This summary captures your recent personal-tracking insights. "
                "Scores range 0 (low) to 10 (high). Lower = less symptom intensity.\n",
            )
            pdf.ln(3)

            def add_section(title, color=(46, 139, 139)):
                pdf.set_text_color(*color)
                pdf.set_font("Helvetica", "B", 13)
                pdf.cell(0, 8, title, ln=True)
                pdf.set_text_color(43, 43, 43)
                pdf.set_font("Helvetica", "", 11)

            add_section("Weekly Averages")
            if not weekly_df.empty:
                for _, row in weekly_df.tail(1).iterrows():
                    pdf.cell(0, 7, f"Week of {row['Week'].strftime('%d %b %Y')}", ln=True)
                    pdf.multi_cell(
                        0,
                        6,
                        " | ".join(f"{c}: {row[c]}" for c in weekly_df.columns if c != "Week"),
                    )
            pdf.ln(4)

            add_section("Monthly Averages")
            if not monthly_df.empty:
                for _, row in monthly_df.tail(1).iterrows():
                    pdf.cell(0, 7, f"Month of {row['Month'].strftime('%B %Y')}", ln=True)
                    pdf.multi_cell(
                        0,
                        6,
                        " | ".join(f"{c}: {row[c]}" for c in monthly_df.columns if c != "Month"),
                    )
            pdf.ln(4)

            add_section("Recent Reflections")
            if not reflections_df.empty:
                for _, r in reflections_df.tail(5).iterrows():
                    pdf.multi_cell(
                        0,
                        6,
                        f"{r['Date'].strftime('%d %b %Y')} - "
                        f"Challenge: {r['Challenge'] or '-'}  |  "
                        f"Small Win: {r['SmallWin'] or '-'}",
                    )
                    pdf.ln(1)
            else:
                pdf.cell(0, 6, "No reflections yet", ln=True)

            pdf.ln(5)
            pdf.set_text_color(120, 120, 120)
            pdf.set_font("Helvetica", "I", 9)
            pdf.multi_cell(
                0,
                6,
                "Disclaimer: This log is for personal tracking only and not medical advice, "
                "diagnosis, or treatment. Consult a qualified health professional for any concerns.",
            )

            return bytes(pdf.output(dest="S"))

        pdf_bytes = generate_pdf(weekly_df, monthly_df, reflections_df)

        st.download_button(
            label="Download Summary PDF",
            data=pdf_bytes,
            file_name="Lymphie_Sanctuary_Summary.pdf",
            mime="application/pdf"
        )
