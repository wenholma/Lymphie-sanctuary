import streamlit as st
import pandas as pd
from datetime import datetime
import sys

sys.path.append('.')
from utils.database import save_log, load_all_logs

st.set_page_config(page_title="Daily Lymphie Log", page_icon="📝", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

# ------------------------------------------------------------------------------
# CUSTOM CSS — PHASE 2
# ------------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #2C3E35;
        font-size: 16px;
    }
    h1, h2, h3, h4 {
        font-family: 'Nunito', sans-serif;
        font-weight: 600;
        color: #1A3B2E;
    }

    /* Form container — soft card */
    .stForm {
        background: linear-gradient(180deg, #FFFFFF 0%, #FAFCFB 100%);
        border-radius: 24px;
        padding: 1.5rem !important;
        border: 1px solid #E2EDE6;
        box-shadow: 0 8px 24px rgba(0, 20, 10, 0.04);
    }

    /* Buttons */
    .stButton > button {
        font-family: 'Nunito', sans-serif !important;
        background-color: #2E7D5E !important;
        color: white !important;
        border-radius: 60px !important;
        padding: 0.9rem 2.2rem !important;
        border: none !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 14px rgba(46, 125, 94, 0.15);
        transition: all 0.2s ease;
        min-height: 48px;
    }
    .stButton > button:hover {
        background-color: #1E5F45 !important;
        box-shadow: 0 6px 20px rgba(46, 125, 94, 0.25);
        transform: scale(1.02);
    }

    /* Warning banner */
    .stWarning {
        border-radius: 16px !important;
        border-left: 6px solid #2E7D5E !important;
        background: linear-gradient(135deg, #F4F9F6 0%, #EAF3EE 100%) !important;
        padding: 1rem 1.5rem !important;
    }

    /* Sliders */
    .stSlider > div {
        padding-top: 0.5rem;
    }

    /* Divider */
    hr {
        border-color: #E2EDE6 !important;
        margin: 1.5rem 0 !important;
    }

    @media (prefers-reduced-motion: reduce) {
        * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------------------
st.title("🌿 Daily Lymphie Log")
st.markdown("Track your symptoms, triggers, and wellness in under 2 minutes.")

# ---------- Legal Disclaimer ----------
st.warning("""
🔒 **Your data stays on this device.**  
This app works like a digital notebook — everything you enter is saved only in your browser.  
**The Lymphie Sanctuary does not store, transmit, or have access to your health data.**  
⚠️ This tool is for personal tracking only. It is not medical advice. Always consult your healthcare provider.
""")

# ---------- Storage Key ----------
STORAGE_KEY = "lymphie_logs"

# ---------- Initialize session state ----------
if "log_df" not in st.session_state:
    logs = load_all_logs()
    if logs:
        st.session_state.log_df = pd.DataFrame(logs)
        st.success(f"✅ Loaded {len(logs)} previous entries from storage.")
    else:
        columns = [
            "Date", "Time", "Heaviness", "Pain", "Limb Appearance",
            "Measurement Taken", "Affected Areas", "Compression Type", "Compression Hours",
            "Self Care", "Dietary Triggers", "Environmental Triggers",
            "Health Triggers", "Stress", "Sleep Quality", "Energy",
            "Mobility", "Self Compassion", "Biggest Challenge", "Small Win",
            "Temperature", "Humidity", "Tags"
        ]
        st.session_state.log_df = pd.DataFrame(columns=columns)

def info_icon(text):
    st.markdown(f"<small style='color: gray;'>ℹ️ {text}</small>", unsafe_allow_html=True)

# ---------- Form ----------
with st.form("daily_log_form"):
    st.subheader("📅 Entry Details")
    col1, col2 = st.columns(2)
    with col1:
        entry_date = st.date_input("Date", value=datetime.now().date(), key="form_date")
    with col2:
        entry_time = st.time_input("Time", value=datetime.now().time().replace(second=0, microsecond=0), key="form_time")

    st.divider()

    st.subheader("🦵 Limb Sensations")
    col1, col2 = st.columns(2)
    with col1:
        heaviness = st.slider("Heaviness / Tightness (0–10)", 0, 10, 5, key="form_heaviness")
        info_icon("0 = none; 10 = affects movement or comfort")
    with col2:
        pain = st.slider("Pain / Discomfort (0–10)", 0, 10, 5, key="form_pain")
        info_icon("0 = none; 10 = interferes with daily activities")

    st.divider()

    st.subheader("👁️ Limb Appearance (vs baseline)")
    appearance_options = [
        "Baseline / Normal",
        "Slight puffiness (pitting)",
        "Noticeable swelling (firm)",
        "Marked swelling / skin stretched"
    ]
    appearance = st.selectbox("How did the limb look today?", appearance_options, key="form_appearance")
    info_icon("Baseline = your usual good day; marked = tight, shiny skin")

    st.divider()

    st.subheader("📏 Measurements")
    measure_options = ["Yes — full measurement", "Yes — partial measurement", "No", "Not applicable"]
    measurement = st.radio("Did you take a limb circumference measurement today?", measure_options, horizontal=True, key="form_measurement")

    st.divider()

    st.subheader("📍 Affected Areas")
    area_options = ["Left arm", "Right arm", "Left leg", "Right leg", "Trunk", "Head/neck", "Genital area", "Other"]
    affected_areas = st.multiselect("Select all that apply", area_options, key="form_areas")
    info_icon("Select all areas where you noticed swelling or symptoms today.")

    st.divider()

    st.subheader("🧦 Compression & Self-Care")
    col1, col2 = st.columns(2)
    with col1:
        compression_options = [
            "Not applicable", "None", "Light support (OTC)", "Circular knit (standard)",
            "Flat knit (custom)", "Bandages / wraps", "Night garment", "Kinesio taping"
        ]
        compression = st.selectbox("Compression worn today", compression_options, key="form_compression")
        compression_hours = st.slider("Hours of compression worn today", 0, 24, 8, key="form_comp_hours")
    with col2:
        selfcare_options = [
            "No", "Yes — Self MLD", "Yes — Therapist MLD", 
            "Yes — Dry brushing", "Yes — Both", "Not applicable"
        ]
        self_care = st.selectbox("Self-MLD / Dry brushing performed?", selfcare_options, key="form_selfcare")

    st.divider()

    st.subheader("🍽️ Lifestyle & Triggers")
    diet_options = [
        "High-salt meal", "High sugar", "Alcohol", "Caffeine", 
        "Processed foods", "Dehydration", "Food intolerance", "Not applicable"
    ]
    diet_triggers = st.multiselect("Dietary triggers", diet_options, key="form_diet")

    env_options = [
        "Heat exposure", "Cold exposure", "Long travel", "Long standing", 
        "Long sitting", "Vigorous exercise", "Tight clothing", "Not applicable"
    ]
    env_triggers = st.multiselect("Environmental triggers", env_options, key="form_env")

    health_options = [
        "Infection", "Menstrual cycle", "New medication", "Fatigue", 
        "Poor sleep", "Stress spike", "Recent illness", "Not applicable"
    ]
    health_triggers = st.multiselect("Health triggers", health_options, key="form_health")

    st.divider()

    st.subheader("🧘 Wellness Context")
    col1, col2 = st.columns(2)
    with col1:
        stress = st.slider("Stress (0–10)", 0, 10, 5, key="form_stress")
        energy = st.slider("Energy (0–10)", 0, 10, 5, key="form_energy")
    with col2:
        sleep_options = ["Poor (<5h)", "Fair (5–7h)", "Good (7–8h)", "Very good (8+h)"]
        sleep_quality = st.selectbox("Sleep quality", sleep_options, key="form_sleep")
        mobility = st.slider("Mobility (0–10)", 0, 10, 5, key="form_mobility")
    self_compassion = st.slider("Self-compassion (0–10)", 0, 10, 5, key="form_compassion")

    st.divider()

    st.subheader("📝 Reflections")
    challenge = st.text_area("Biggest challenge today?", placeholder="e.g., pain after walking...", max_chars=300, height=70, key="form_challenge")
    win = st.text_area("Small win today?", placeholder="e.g., remembered to elevate...", max_chars=300, height=70, key="form_win")
    tags = st.text_input("Tags (optional)", placeholder="e.g., flare, new garment", key="form_tags")

    st.divider()

    with st.expander("🌤️ Environment (optional)", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            temp = st.number_input("Temperature (°C)", value=None, step=0.1, key="form_temp")
        with col2:
            humidity = st.number_input("Humidity (%)", value=None, min_value=0, max_value=100, key="form_humidity")

    submitted = st.form_submit_button("💾 Save Entry", width='stretch')

# ---------- Save ----------
if submitted:
    new_entry = {
        "Date": entry_date.strftime("%Y-%m-%d"),
        "Time": entry_time.strftime("%H:%M"),
        "Heaviness": heaviness,
        "Pain": pain,
        "Limb Appearance": appearance,
        "Measurement Taken": measurement,
        "Affected Areas": ", ".join(affected_areas) if affected_areas else "",
        "Compression Type": compression,
        "Compression Hours": compression_hours,
        "Self Care": self_care,
        "Dietary Triggers": ", ".join(diet_triggers) if diet_triggers else "",
        "Environmental Triggers": ", ".join(env_triggers) if env_triggers else "",
        "Health Triggers": ", ".join(health_triggers) if health_triggers else "",
        "Stress": stress,
        "Sleep Quality": sleep_quality,
        "Energy": energy,
        "Mobility": mobility,
        "Self Compassion": self_compassion,
        "Biggest Challenge": challenge,
        "Small Win": win,
        "Temperature": temp if temp is not None else "",
        "Humidity": humidity if humidity is not None else "",
        "Tags": tags
    }
    
    try:
        save_log(new_entry)
        logs = load_all_logs()
        st.session_state.log_df = pd.DataFrame(logs)
        st.success(f"✅ Entry saved! ({len(logs)} total entries)")
        st.balloons()
    except Exception as e:
        st.error(f"❌ Failed to save: {e}")

# ---------- Recent entries ----------
st.divider()
st.subheader("📋 Your Recent Entries")

if not st.session_state.log_df.empty:
    st.dataframe(st.session_state.log_df.tail(10), width='stretch', hide_index=True)
    st.caption(f"📊 {len(st.session_state.log_df)} total entries stored.")
else:
    st.info("No entries yet. Use the form above to add your first log.")