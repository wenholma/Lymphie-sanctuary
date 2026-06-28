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

def tip(text):
    st.markdown(f"<small style='color: #6B7F74;'>ℹ️ {text}</small>", unsafe_allow_html=True)

# ==============================================================================
# TABS
# ==============================================================================
tab_log, tab_insights = st.tabs(["📝 Daily Log", "🧠 My Insights"])

# ------------------------------------------------------------------------------
# TAB 1: DAILY LOG (single form, always works)
# ------------------------------------------------------------------------------
with tab_log:
    st.markdown("### Your 2‑Minute Check‑In")
    
    with st.form("daily_log_form", clear_on_submit=True):
        # Two columns for the most important sliders (always visible)
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
        
        # Expandable sections for additional details
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
            # Force refresh to show updated insights
            st.rerun()
        except Exception as e:
            st.error(f"❌ Failed to save: {e}")

# ------------------------------------------------------------------------------
# TAB 2: MY INSIGHTS
# ------------------------------------------------------------------------------
with tab_insights:
    st.markdown("## 🧠 My Insights")
    
    if st.session_state.log_df.empty or len(st.session_state.log_df) < 2:
        st.info("📝 Log at least 2 entries to unlock your personal insights. Patterns emerge over time.")
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
    
    with col1:
        if 'Heaviness' in df.columns and not recent.empty:
            avg = recent['Heaviness'].mean()
            val = today['Heaviness']
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta < -0.5:
                    st.metric("Heaviness", f"{val:.0f}/10", delta=f"↓ {abs(delta):.1f} Better", delta_color="inverse")
                elif delta > 0.5:
                    st.metric("Heaviness", f"{val:.0f}/10", delta=f"↑ {delta:.1f} Worse", delta_color="off")
                else:
                    st.metric("Heaviness", f"{val:.0f}/10", delta="→ Stable")
        if 'Pain' in df.columns and not recent.empty:
            avg = recent['Pain'].mean()
            val = today['Pain']
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta < -0.5:
                    st.metric("Pain", f"{val:.0f}/10", delta=f"↓ {abs(delta):.1f} Better", delta_color="inverse")
                elif delta > 0.5:
                    st.metric("Pain", f"{val:.0f}/10", delta=f"↑ {delta:.1f} Worse", delta_color="off")
                else:
                    st.metric("Pain", f"{val:.0f}/10", delta="→ Stable")
    
    with col2:
        if 'Stress' in df.columns and not recent.empty:
            avg = recent['Stress'].mean()
            val = today['Stress']
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta < -0.5:
                    st.metric("Stress", f"{val:.0f}/10", delta=f"↓ {abs(delta):.1f} Calmer", delta_color="inverse")
                elif delta > 0.5:
                    st.metric("Stress", f"{val:.0f}/10", delta=f"↑ {delta:.1f} Higher", delta_color="off")
                else:
                    st.metric("Stress", f"{val:.0f}/10", delta="→ Stable")
        if 'Energy' in df.columns and not recent.empty:
            avg = recent['Energy'].mean()
            val = today['Energy']
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta > 0.5:
                    st.metric("Energy", f"{val:.0f}/10", delta=f"↑ {delta:.1f}")
                elif delta < -0.5:
                    st.metric("Energy", f"{val:.0f}/10", delta=f"↓ {abs(delta):.1f}", delta_color="off")
                else:
                    st.metric("Energy", f"{val:.0f}/10", delta="→ Stable")
    
    with col3:
        if 'Compression Hours' in df.columns and not recent.empty:
            avg = recent['Compression Hours'].mean()
            val = today['Compression Hours']
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta > 1:
                    st.metric("Compression", f"{val:.0f}h", delta=f"↑ {delta:.1f}h")
                elif delta < -1:
                    st.metric("Compression", f"{val:.0f}h", delta=f"↓ {abs(delta):.1f}h", delta_color="off")
                else:
                    st.metric("Compression", f"{val:.0f}h", delta="→ On track")
        if 'Self Compassion' in df.columns and not recent.empty:
            avg = recent['Self Compassion'].mean()
            val = today['Self Compassion']
            if pd.notna(val) and pd.notna(avg):
                delta = val - avg
                if delta > 0.5:
                    st.metric("Self-Compassion", f"{val:.0f}/10", delta=f"↑ Growing 🌱")
                elif delta < -0.5:
                    st.metric("Self-Compassion", f"{val:.0f}/10", delta=f"↓ Be gentle", delta_color="off")
                else:
                    st.metric("Self-Compassion", f"{val:.0f}/10", delta="→ Steady")
    
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
                if poor_sleep['Pain'].mean() > good_sleep['Pain'].mean() + 1:
                    alerts.append(f"💤 **Sleep matters.** Pain averages {poor_sleep['Pain'].mean():.1f}/10 after poor sleep vs {good_sleep['Pain'].mean():.1f}/10 after good sleep.")
        
        if 'Stress' in df.columns and 'Heaviness' in df.columns:
            high_stress = df[df['Stress'] >= 7]
            low_stress = df[df['Stress'] <= 4]
            if len(high_stress) >= 2 and len(low_stress) >= 2:
                if high_stress['Heaviness'].mean() > low_stress['Heaviness'].mean() + 1:
                    alerts.append(f"🧘 **Stress affects swelling.** Heaviness averages {high_stress['Heaviness'].mean():.1f}/10 on high-stress days vs {low_stress['Heaviness'].mean():.1f}/10 on calmer days.")
        
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
    
    # ---- DAILY PRESCRIPTION ----
    if len(df) >= 2:
        st.markdown("---")
        st.markdown("### 🌿 Tomorrow's Focus")
        suggestions = []
        if pd.notna(today.get('Compression Hours', 0)) and today['Compression Hours'] < 12:
            suggestions.append("Wear compression for **12+ hours** tomorrow.")
        if pd.notna(today.get('Stress', 5)) and today['Stress'] >= 7:
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