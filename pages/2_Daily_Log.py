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

from utils.styles import apply_styles
apply_styles()

st.title("🌿 Daily Lymphie Log")
st.caption("Two minutes. Your patterns. Your story.")

# ─── LICENSE GATE ──────────────────────────────────────────────────
premium = get_premium_status()
if not premium:
    st.warning("🔑 **Lifetime Access required.** Purchase your one-time license key on the Settings page.")
    if st.button("⚙️ Go to Settings & License to Unlock", type="primary"):
        st.switch_page("pages/1_Settings.py")
    st.stop()

# ─── PRIVACY NOTICE ──────────────────────────────────────────────
st.markdown("""
<div class="green-box">
    🔒 Everything you log stays on this device only. We never see it, store it, or touch it.<br>
    This is a personal tracking tool — not medical advice. Always work with your therapist or GP.
</div>
""", unsafe_allow_html=True)

# ─── LOAD DATA ────────────────────────────────────────────────────
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

# ─── TABS ──────────────────────────────────────────────────────────
tab_log, tab_insights = st.tabs(["📝 Daily Log", "🧠 My Insights"])

# ─── TAB 1: DAILY LOG ────────────────────────────────────────────
with tab_log:
    st.markdown("### Your Daily Check-In")
    st.markdown("*Two minutes. As much or as little as you like. No pressure.*")

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

# ─── TAB 2: MY INSIGHTS ──────────────────────────────────────────
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

    # Helper to find a column regardless of naming convention
    def get_col(df, *possible_names):
        for name in possible_names:
            if name in df.columns:
                return name
        return None

    heaviness_col = get_col(df, 'Heaviness', 'heaviness')
    pain_col = get_col(df, 'Pain', 'pain')
    stress_col = get_col(df, 'Stress', 'stress')
    energy_col = get_col(df, 'Energy', 'energy')
    mobility_col = get_col(df, 'Mobility', 'mobility')
    compassion_col = get_col(df, 'Self Compassion', 'Self-Compassion (0-10)', 'self_compassion')
    comp_hours_col = get_col(df, 'Compression Hours', 'compression_hours')
    sleep_col = get_col(df, 'Sleep Quality', 'sleep_quality')

    # Convert numeric columns
    for col in [heaviness_col, pain_col, stress_col, energy_col, mobility_col, compassion_col, comp_hours_col]:
        if col and col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    today = df.iloc[0]
    recent = df.iloc[1:8] if len(df) > 1 else df.iloc[1:]

    # ─── TREND CARDS ──────────────────────────────────────────────
    st.markdown("### 📈 Today vs. Your Weekly Average")

    col1, col2, col3 = st.columns(3)

    with col1:
        if heaviness_col and not recent.empty:
            avg = recent[heaviness_col].mean()
            val = today[heaviness_col]
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta < -0.5:
                    st.metric("Heaviness", f"{val:.0f}/10", delta=f"↓ {abs(delta):.1f} Better", delta_color="inverse")
                elif delta > 0.5:
                    st.metric("Heaviness", f"{val:.0f}/10", delta=f"↑ {delta:.1f} Worse", delta_color="off")
                else:
                    st.metric("Heaviness", f"{val:.0f}/10", delta="→ Stable")
        if pain_col and not recent.empty:
            avg = recent[pain_col].mean()
            val = today[pain_col]
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta < -0.5:
                    st.metric("Pain", f"{val:.0f}/10", delta=f"↓ {abs(delta):.1f} Better", delta_color="inverse")
                elif delta > 0.5:
                    st.metric("Pain", f"{val:.0f}/10", delta=f"↑ {delta:.1f} Worse", delta_color="off")
                else:
                    st.metric("Pain", f"{val:.0f}/10", delta="→ Stable")

    with col2:
        if stress_col and not recent.empty:
            avg = recent[stress_col].mean()
            val = today[stress_col]
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta < -0.5:
                    st.metric("Stress", f"{val:.0f}/10", delta=f"↓ {abs(delta):.1f} Calmer", delta_color="inverse")
                elif delta > 0.5:
                    st.metric("Stress", f"{val:.0f}/10", delta=f"↑ {delta:.1f} Higher", delta_color="off")
                else:
                    st.metric("Stress", f"{val:.0f}/10", delta="→ Stable")
        if energy_col and not recent.empty:
            avg = recent[energy_col].mean()
            val = today[energy_col]
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta > 0.5:
                    st.metric("Energy", f"{val:.0f}/10", delta=f"↑ {delta:.1f}")
                elif delta < -0.5:
                    st.metric("Energy", f"{val:.0f}/10", delta=f"↓ {abs(delta):.1f}", delta_color="off")
                else:
                    st.metric("Energy", f"{val:.0f}/10", delta="→ Stable")

    with col3:
        if comp_hours_col and not recent.empty:
            avg = recent[comp_hours_col].mean()
            val = today[comp_hours_col]
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta > 1:
                    st.metric("Compression", f"{val:.0f}h", delta=f"↑ {delta:.1f}h")
                elif delta < -1:
                    st.metric("Compression", f"{val:.0f}h", delta=f"↓ {abs(delta):.1f}h", delta_color="off")
                else:
                    st.metric("Compression", f"{val:.0f}h", delta="→ On track")
        if compassion_col and not recent.empty:
            avg = recent[compassion_col].mean()
            val = today[compassion_col]
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta > 0.5:
                    st.metric("Self-Compassion", f"{val:.0f}/10", delta=f"↑ Growing 🌱")
                elif delta < -0.5:
                    st.metric("Self-Compassion", f"{val:.0f}/10", delta=f"↓ Be gentle", delta_color="off")
                else:
                    st.metric("Self-Compassion", f"{val:.0f}/10", delta="→ Steady")

    # ─── PATTERN ALERTS ───────────────────────────────────────────
    if len(df) >= 3:
        st.markdown("---")
        st.markdown("### 🔍 Pattern Alerts")
        alerts = []

        if comp_hours_col and heaviness_col and comp_hours_col in df.columns and heaviness_col in df.columns:
            high_comp = df[df[comp_hours_col] >= 12]
            low_comp = df[df[comp_hours_col] < 12]
            if len(high_comp) >= 2 and len(low_comp) >= 2:
                high_avg = high_comp[heaviness_col].mean()
                low_avg = low_comp[heaviness_col].mean()
                if low_avg > high_avg + 1:
                    alerts.append(f"🔑 **Compression is working.** Heaviness averages {low_avg:.1f}/10 with <12h compression vs {high_avg:.1f}/10 with 12+h.")

        if sleep_col and pain_col and sleep_col in df.columns and pain_col in df.columns:
            poor_sleep = df[df[sleep_col].astype(str).str.contains('Poor', na=False)]
            good_sleep = df[df[sleep_col].astype(str).str.contains('Good|Very good', na=False)]
            if len(poor_sleep) >= 2 and len(good_sleep) >= 2:
                poor_avg = poor_sleep[pain_col].mean()
                good_avg = good_sleep[pain_col].mean()
                if poor_avg > good_avg + 1:
                    alerts.append(f"💤 **Sleep matters.** Pain averages {poor_avg:.1f}/10 after poor sleep vs {good_avg:.1f}/10 after good sleep.")

        if stress_col and heaviness_col and stress_col in df.columns and heaviness_col in df.columns:
            high_stress = df[df[stress_col] >= 7]
            low