import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import random

sys.path.append('.')
from utils.database import save_log, load_all_logs, get_premium_status

st.set_page_config(page_title="Daily Lymphie Log | The Lymphie Sanctuary", page_icon="📝", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #2C3E35; font-size: 16px; }
    h1, h2, h3, h4 { font-family: 'Nunito', sans-serif; font-weight: 600; color: #1A3B2E; }
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: #F4F9F6;
        border-radius: 20px;
        padding: 0.4rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'Nunito', sans-serif;
        font-weight: 600;
        font-size: 0.9rem;
        border-radius: 16px;
        padding: 0.6rem 1.2rem;
    }
    .stTabs [aria-selected="true"] {
        background: #2E7D5E !important;
        color: white !important;
    }
    .stButton > button { font-family: 'Nunito', sans-serif !important; background-color: #2E7D5E !important; color: white !important; border-radius: 60px !important; padding: 0.9rem 2.2rem !important; border: none !important; font-weight: 700 !important; font-size: 1.1rem !important; min-height: 48px; }
    .stWarning { border-radius: 16px !important; border-left: 6px solid #2E7D5E !important; background: linear-gradient(135deg, #F4F9F6 0%, #EAF3EE 100%) !important; padding: 1rem 1.5rem !important; }
    @media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("🌿 Daily Lymphie Log")
st.caption("Your private daily intelligence companion.")

# ------------------------------------------------------------------------------
# LICENSE GATE
# ------------------------------------------------------------------------------
premium = get_premium_status()
if not premium:
    st.warning("🔑 **Lifetime Access required.** Purchase your one-time license key on the Settings page.")
    if st.button("⚙️ Go to Settings & License to Unlock", type="primary"):
        st.switch_page("pages/1_Settings.py")
    st.stop()

# ------------------------------------------------------------------------------
# PRIVACY NOTICE
# ------------------------------------------------------------------------------
st.info("""
🔒 **Your data stays on this device.** We never see, store, or access your health data.
⚠️ Personal tracking only — not medical advice.
""")

# ------------------------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------------------------
if "log_df" not in st.session_state:
    logs = load_all_logs()
    if logs:
        st.session_state.log_df = pd.DataFrame(logs)
    else:
        st.session_state.log_df = pd.DataFrame(columns=[
            "Date", "Time", "Heaviness", "Pain", "Limb Appearance", "Measurement Taken",
            "Affected Areas", "Compression Type", "Compression Hours", "Self Care",
            "Professional Treatment", "Movement & Exercise",
            "Dietary Triggers", "Environmental Triggers", "Health Triggers", "Stress",
            "Sleep Quality", "Energy", "Mobility", "Self Compassion", "Biggest Challenge",
            "Small Win", "Temperature", "Humidity", "Tags"
        ])

def safe_get(series, key, default=None):
    """Safely get a value from a pandas Series, returning default if key is missing."""
    if series is None or key not in series.index:
        return default
    val = series[key]
    if pd.isna(val):
        return default
    return val

# ==============================================================================
# TABS
# ==============================================================================
tab_log, tab_insights = st.tabs(["📝 Daily Log", "🧠 My Insights"])

# ------------------------------------------------------------------------------
# TAB 1: DAILY LOG
# ------------------------------------------------------------------------------
with tab_log:
    st.markdown("### Your 2‑Minute Check‑In")
    st.info("""
    ✨ **Here's the magic:** Fill in as much or as little as you like. After you save, jump over to the **🧠 My Insights** tab to see your personal trends, pattern alerts, flare risk, and a clinical summary ready for your therapist.
    """)

    with st.form("daily_log_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            entry_date = st.date_input("Date", value=datetime.now().date(), key="d_date")
            heaviness = st.slider("Heaviness / Tightness (0–10)", 0, 10, 0, key="d_heaviness")
            pain = st.slider("Pain / Discomfort (0–10)", 0, 10, 0, key="d_pain")
            stress = st.slider("Stress (0–10)", 0, 10, 0, key="d_stress")
        with col2:
            entry_time = st.time_input("Time", value=datetime.now().time().replace(second=0, microsecond=0), key="d_time", step=300)
            compression_hours = st.slider("Compression Hours", 0, 24, 0, key="d_comp_hours")
            energy = st.slider("Energy (0–10)", 0, 10, 5, key="d_energy")
            mobility = st.slider("Mobility (0–10)", 0, 10, 5, key="d_mobility")

        with st.expander("👁️ Appearance & Measurements", expanded=False):
            appearance = st.selectbox("How did the limb look today?", [
                "Baseline / Normal", "Slight puffiness (pitting)",
                "Noticeable swelling (firm)", "Marked swelling / skin stretched"
            ], key="d_appearance")
            measurement = st.radio("Measurements taken?", 
                ["No", "Yes — full measurement", "Yes — partial measurement", "Not applicable"],
                horizontal=True, key="d_measurement")

        with st.expander("📍 Affected Areas", expanded=False):
            affected_areas = st.multiselect("Select all areas with symptoms today",
                ["Left arm", "Right arm", "Left leg", "Right leg", "Trunk", "Head/neck", "Genital area", "Other"],
                key="d_areas")

        with st.expander("🧦 Compression & Self‑Care", expanded=False):
            compression = st.multiselect("Compression worn today",
                ["None", "Light support (OTC)", "Circular knit (standard)", "Flat knit (custom)",
                 "Bandages / wraps", "Night garment", "Kinesio taping", "Not applicable"],
                key="d_compression")
            self_care = st.multiselect("Home self‑care performed today",
                ["None", "Self MLD", "Dry brushing", "Elevation", "Lymphatic breathing / breathwork",
                 "Rebounding (mini trampoline)", "Lymphatic yoga / stretching", "Walking with compression",
                 "Skin care / moisturising", "Cold / warm therapy", "Diaphragmatic breathing", "Not applicable"],
                key="d_selfcare")

        with st.expander("🏥 Professional Treatments & Movement", expanded=False):
            prof_treatment = st.multiselect("Professional treatments received today",
                ["None", "Therapist MLD — Vodder", "Therapist MLD — Földi", "Therapist MLD — Casley-Smith",
                 "Therapist MLD — other", "DLT/CDT", "Deep Oscillation Therapy",
                 "Lymphastim / IPC", "Low Level Laser Therapy", "Bowen Therapy / NST",
                 "Reflexology / RLD", "Vacuflex", "Myofascial Release", "Craniosacral Therapy",
                 "Acupuncture", "Sound Therapy", "Other professional treatment", "Not applicable"],
                key="d_professional")
            movement = st.multiselect("Movement & exercise today",
                ["None", "Gentle walking", "Swimming / aqua therapy", "Aqua Lymphatic Therapy",
                 "Lymphatic yoga", "Pilates", "Rebounding", "Guided exercise programme",
                 "Breathwork for lymphatic flow", "Other movement", "Not applicable"],
                key="d_movement")

        with st.expander("🍽️ Lifestyle & Triggers", expanded=False):
            diet_triggers = st.multiselect("Dietary triggers",
                ["High-salt meal", "High sugar", "Alcohol", "Caffeine", "Processed foods",
                 "Dehydration", "Food intolerance", "None / not applicable"], key="d_diet")
            env_triggers = st.multiselect("Environmental triggers",
                ["Heat exposure", "Cold exposure", "Long travel / flying", "Long standing",
                 "Long sitting", "Vigorous exercise", "Tight clothing", "None / not applicable"], key="d_env")
            health_triggers = st.multiselect("Health triggers",
                ["Infection", "Menstrual cycle", "New medication", "Fatigue", "Poor sleep",
                 "Stress spike", "Recent illness", "None / not applicable"], key="d_health")

        with st.expander("🧘 Wellness Context", expanded=False):
            sleep_quality = st.selectbox("Sleep quality last night",
                ["Very good (8h+)", "Good (7–8h)", "Fair (5–7h)", "Poor (<5h)"], key="d_sleep")
            self_compassion = st.slider("Self-compassion (0–10)", 0, 10, 5, key="d_selfcomp")

        with st.expander("📝 Reflections & Tags", expanded=False):
            challenge = st.text_area("Biggest challenge today?", max_chars=1000, height=80, key="d_challenge")
            win = st.text_area("Small win today? 🌱", max_chars=1000, height=80, key="d_win")
            tags = st.text_input("Tags (optional)", placeholder="e.g., flare, new garment", key="d_tags")

        with st.expander("🌤️ Environment (optional)", expanded=False):
            c1, c2 = st.columns(2)
            with c1:
                temp = st.number_input("Temperature (°C)", value=None, step=0.5, min_value=-20.0, max_value=55.0, key="d_temp")
            with c2:
                humidity = st.number_input("Humidity (%)", value=None, min_value=0, max_value=100, key="d_humidity")

        submitted = st.form_submit_button("💾 Save Today's Entry", use_container_width=True)

    if submitted:
        new_entry = {
            "Date": entry_date.strftime("%Y-%m-%d"), "Time": entry_time.strftime("%H:%M"),
            "Heaviness": heaviness, "Pain": pain, "Limb Appearance": appearance,
            "Measurement Taken": measurement, "Affected Areas": ", ".join(affected_areas) if affected_areas else "",
            "Compression Type": ", ".join(compression) if compression else "",
            "Compression Hours": compression_hours, "Self Care": ", ".join(self_care) if self_care else "",
            "Professional Treatment": ", ".join(prof_treatment) if prof_treatment else "",
            "Movement & Exercise": ", ".join(movement) if movement else "",
            "Dietary Triggers": ", ".join(diet_triggers) if diet_triggers else "",
            "Environmental Triggers": ", ".join(env_triggers) if env_triggers else "",
            "Health Triggers": ", ".join(health_triggers) if health_triggers else "",
            "Stress": stress, "Sleep Quality": sleep_quality, "Energy": energy,
            "Mobility": mobility, "Self Compassion": self_compassion,
            "Biggest Challenge": challenge, "Small Win": win,
            "Temperature": temp if temp is not None else "",
            "Humidity": humidity if humidity is not None else "", "Tags": tags
        }
        try:
            save_log(new_entry)
            logs = load_all_logs()
            st.session_state.log_df = pd.DataFrame(logs)
            st.success(f"✅ Entry saved! ({len(logs)} total entries logged)")
            st.balloons()
            st.info("👉 Jump to the **🧠 My Insights** tab to see your updated trends, patterns, and clinical summary.")
            st.rerun()
        except Exception as e:
            st.error(f"❌ Failed to save: {e}")

# ------------------------------------------------------------------------------
# TAB 2: MY INSIGHTS
# ------------------------------------------------------------------------------
with tab_insights:
    st.markdown("## 🧠 My Insights")
    st.info("""
    📊 **What you'll see here (once you've logged a few entries):**
    - **Trend arrows** comparing today's values to your weekly average.
    - **Pattern alerts** revealing your personal triggers and what helps.
    - **Flare risk assessment** based on recent data.
    - **Tomorrow's focus** – a small, personalised action to try.
    - **Weekly clinical summary** ready to share with your therapist.
    """)

    if st.session_state.log_df.empty or len(st.session_state.log_df) < 2:
        st.warning("📝 Log at least 2 entries to unlock your personal insights. Patterns emerge over time.")
        st.stop()

    df = st.session_state.log_df.copy()
    numeric_cols = ['Heaviness', 'Pain', 'Stress', 'Energy', 'Mobility', 'Self Compassion', 'Compression Hours']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    today = df.iloc[0]
    recent = df.iloc[1:8] if len(df) > 1 else df.iloc[1:]

    # ---- TREND CARDS ----
    st.markdown("### 📈 Today vs. Your Weekly Average")
    col1, col2, col3 = st.columns(3)

    # Helper to safely show metric
    def show_metric(col, label, metric_col, higher_better=False):
        if metric_col not in df.columns or recent.empty:
            return
        avg = recent[metric_col].mean()
        val = today[metric_col]
        if pd.isna(val) or pd.isna(avg):
            return
        delta = val - avg
        if higher_better:
            if delta > 0.5:
                col.metric(label, f"{val:.0f}{'h' if 'Hours' in metric_col else '/10'}", delta=f"↑ {delta:.1f}")
            elif delta < -0.5:
                col.metric(label, f"{val:.0f}{'h' if 'Hours' in metric_col else '/10'}", delta=f"↓ {abs(delta):.1f}", delta_color="off")
            else:
                col.metric(label, f"{val:.0f}{'h' if 'Hours' in metric_col else '/10'}", delta="→ Stable")
        else:
            if delta < -0.5:
                col.metric(label, f"{val:.0f}{'h' if 'Hours' in metric_col else '/10'}", delta=f"↓ {abs(delta):.1f} Better", delta_color="inverse")
            elif delta > 0.5:
                col.metric(label, f"{val:.0f}{'h' if 'Hours' in metric_col else '/10'}", delta=f"↑ {delta:.1f} Worse", delta_color="off")
            else:
                col.metric(label, f"{val:.0f}{'h' if 'Hours' in metric_col else '/10'}", delta="→ Stable")

    with col1:
        show_metric(col1, "Heaviness", "Heaviness")
        show_metric(col1, "Pain", "Pain")
    with col2:
        show_metric(col2, "Stress", "Stress")
        show_metric(col2, "Energy", "Energy", higher_better=True)
    with col3:
        show_metric(col3, "Compression", "Compression Hours", higher_better=True)
        show_metric(col3, "Self-Compassion", "Self Compassion", higher_better=True)

    # ---- PATTERN ALERTS ----
    if len(df) >= 3:
        st.markdown("---")
        st.markdown("### 🔍 Pattern Alerts")
        alerts = []

        if 'Compression Hours' in df.columns and 'Heaviness' in df.columns:
            high_comp = df[df['Compression Hours'] >= 12]
            low_comp = df[df['Compression Hours'] < 12]
            if len(high_comp) >= 2 and len(low_comp) >= 2:
                high_avg = high_comp['Heaviness'].mean()
                low_avg = low_comp['Heaviness'].mean()
                if low_avg > high_avg + 1:
                    alerts.append(f"🔑 **Compression is working.** Heaviness averages {low_avg:.1f}/10 with <12h compression vs {high_avg:.1f}/10 with 12+h.")

        if 'Sleep Quality' in df.columns and 'Pain' in df.columns:
            poor_sleep = df[df['Sleep Quality'].str.contains('Poor', na=False)]
            good_sleep = df[df['Sleep Quality'].str.contains('Good|Very good', na=False)]
            if len(poor_sleep) >= 2 and len(good_sleep) >= 2:
                poor_avg = poor_sleep['Pain'].mean()
                good_avg = good_sleep['Pain'].mean()
                if poor_avg > good_avg + 1:
                    alerts.append(f"💤 **Sleep matters.** Pain averages {poor_avg:.1f}/10 after poor sleep vs {good_avg:.1f}/10 after good sleep.")

        if 'Stress' in df.columns and 'Heaviness' in df.columns:
            high_stress = df[df['Stress'] >= 7]
            low_stress = df[df['Stress'] <= 4]
            if len(high_stress) >= 2 and len(low_stress) >= 2:
                high_avg = high_stress['Heaviness'].mean()
                low_avg = low_stress['Heaviness'].mean()
                if high_avg > low_avg + 1:
                    alerts.append(f"🧘 **Stress affects swelling.** Heaviness averages {high_avg:.1f}/10 on high-stress days vs {low_avg:.1f}/10 on calmer days.")

        if alerts:
            for alert in alerts:
                st.info(alert)
        else:
            st.caption("Keep logging! Patterns emerge after more entries.")

    # ---- FLARE RISK ----
    if len(df) >= 5:
        st.markdown("---")
        st.markdown("### ⚠️ Flare Risk Assessment")
        risk_score = 0
        risk_factors = []
        recent_5 = df.head(5)

        if 'Heaviness' in df.columns and recent_5['Heaviness'].mean() >= 7:
            risk_score += 3
            risk_factors.append("Heaviness averaging 7+ this week")
        if 'Sleep Quality' in df.columns:
            poor_count = recent_5['Sleep Quality'].str.contains('Poor', na=False).sum()
            if poor_count >= 3:
                risk_score += 2
                risk_factors.append(f"Poor sleep on {poor_count} of 5 nights")
        if 'Stress' in df.columns and recent_5['Stress'].mean() >= 7:
            risk_score += 2
            risk_factors.append(f"Average stress {recent_5['Stress'].mean():.1f}/10")
        if 'Compression Hours' in df.columns and recent_5['Compression Hours'].mean() < 10:
            risk_score += 2
            risk_factors.append(f"Compression averaging {recent_5['Compression Hours'].mean():.0f}h")

        if risk_score >= 5:
            st.error(f"⚠️ Elevated flare risk. Score: {risk_score}/10")
        elif risk_score >= 3:
            st.warning(f"🟡 Moderate risk. Score: {risk_score}/10")
        else:
            st.success(f"✅ Low risk. Score: {risk_score}/10")
        for factor in risk_factors:
            st.markdown(f"- {factor}")

    # ---- TOMORROW'S FOCUS ----
    if len(df) >= 2:
        st.markdown("---")
        st.markdown("### 🌿 Tomorrow's Focus")
        suggestions = []
        comp_today = safe_get(today, 'Compression Hours', 0)
        stress_today = safe_get(today, 'Stress', 5)
        if comp_today < 12:
            suggestions.append("Wear compression for **12+ hours** tomorrow.")
        if stress_today >= 7:
            suggestions.append("Try **5 minutes of diaphragmatic breathing** before bed.")
        if suggestions:
            random.shuffle(suggestions)
            st.info(suggestions[0])
        else:
            st.success("You're doing well. Keep your current routine. 🌿")

    # ---- WEEKLY CLINICAL SUMMARY ----
    if len(df) >= 7:
        st.markdown("---")
        st.markdown("### 📋 Weekly Clinical Summary")
        recent_7 = df.head(7)
        summary = f"**This week ({len(recent_7)} entries):** "
        if 'Heaviness' in df.columns:
            summary += f"Heaviness averaged {recent_7['Heaviness'].mean():.1f}/10. "
        if 'Pain' in df.columns:
            summary += f"Pain averaged {recent_7['Pain'].mean():.1f}/10. "
        if 'Compression Hours' in df.columns:
            summary += f"Compression averaged {recent_7['Compression Hours'].mean():.0f}h/day. "
        st.info(summary)
        st.caption("Share this with your therapist at your next appointment.")