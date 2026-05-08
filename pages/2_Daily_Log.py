import streamlit as st
import pandas as pd
from datetime import datetime
import sys

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
    .stForm { background: linear-gradient(180deg, #FFFFFF 0%, #FAFCFB 100%); border-radius: 24px; padding: 1.5rem !important; border: 1px solid #E2EDE6; box-shadow: 0 8px 24px rgba(0, 20, 10, 0.04); }
    .stButton > button { font-family: 'Nunito', sans-serif !important; background-color: #2E7D5E !important; color: white !important; border-radius: 60px !important; padding: 0.9rem 2.2rem !important; border: none !important; font-weight: 700 !important; font-size: 1.1rem !important; min-height: 48px; }
    @media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("🌿 Daily Lymphie Log")
st.markdown("Track your symptoms, triggers, and wellness in under 2 minutes.")

# ------------------------------------------------------------------------------
# LICENSE GATE
# ------------------------------------------------------------------------------
premium = get_premium_status()
if not premium:
    st.warning("""
    🔑 **Lifetime Access required to log entries.**
    Purchase your one-time license key on the Settings page to unlock the Daily Log, Excel export, and trends.
    """)
    if st.button("⚙️ Go to Settings & License to Unlock", type="primary"):
        st.switch_page("pages/1_Settings.py")
    st.stop()

# ------------------------------------------------------------------------------
# PRIVACY NOTICE
# ------------------------------------------------------------------------------
st.info("""
🔒 **Your data stays on this device.** Everything you enter is saved only in this browser.
The Lymphie Sanctuary cannot see, store, or access your health data.
⚠️ Personal tracking only — not medical advice. Always consult your healthcare provider.
""")

# ------------------------------------------------------------------------------
# LOAD EXISTING LOGS
# ------------------------------------------------------------------------------
if "log_df" not in st.session_state:
    logs = load_all_logs()
    if logs:
        st.session_state.log_df = pd.DataFrame(logs)
    else:
        st.session_state.log_df = pd.DataFrame(columns=[
            "Date", "Time", "Heaviness", "Pain", "Limb Appearance", "Measurement Taken",
            "Affected Areas", "Compression Type", "Compression Hours", "Self Care",
            "Dietary Triggers", "Environmental Triggers", "Health Triggers", "Stress",
            "Sleep Quality", "Energy", "Mobility", "Self Compassion", "Biggest Challenge",
            "Small Win", "Temperature", "Humidity", "Tags"
        ])

def tip(text):
    st.markdown(f"<small style='color: #6B7F74;'>ℹ️ {text}</small>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# FORM RESET FLAG
# ------------------------------------------------------------------------------
if st.session_state.get("form_just_saved"):
    for key in list(st.session_state.keys()):
        if key.startswith("form_"):
            del st.session_state[key]
    st.session_state["form_just_saved"] = False

# ------------------------------------------------------------------------------
# DAILY LOG FORM
# ------------------------------------------------------------------------------
with st.form("daily_log_form"):

    st.subheader("📅 Entry Details")
    col1, col2 = st.columns(2)
    with col1:
        entry_date = st.date_input("Date", value=datetime.now().date(), key="form_date")
        tip("Today's date is pre-filled — change if logging for a different day.")
    with col2:
        entry_time = st.time_input("Time", value=datetime.now().time().replace(second=0, microsecond=0), key="form_time", step=300)
        tip("Time of your check-in. Steps in 5-minute increments.")

    st.divider()

    st.subheader("🦵 Limb Sensations")
    tip("Rate how your affected limb(s) felt today overall.")
    col1, col2 = st.columns(2)
    with col1:
        heaviness = st.slider("Heaviness / Tightness (0–10)", 0, 10, 0, key="form_heaviness")
        tip("0 = no heaviness at all; 10 = limb feels extremely heavy or tight, affecting movement.")
    with col2:
        pain = st.slider("Pain / Discomfort (0–10)", 0, 10, 0, key="form_pain")
        tip("0 = no pain; 10 = severe pain interfering with daily activities.")

    st.divider()

    st.subheader("👁️ Limb Appearance (vs your baseline)")
    appearance = st.selectbox("How did the limb look today?", [
        "Baseline / Normal",
        "Slight puffiness (pitting)",
        "Noticeable swelling (firm)",
        "Marked swelling / skin stretched"
    ], key="form_appearance")
    tip("Baseline = your usual good day. Pitting = skin indents when pressed. Marked = skin looks tight or shiny.")

    st.divider()

    st.subheader("📏 Measurements")
    measurement = st.radio(
        "Did you take a limb circumference measurement today?",
        ["No", "Yes — full measurement", "Yes — partial measurement", "Not applicable"],
        horizontal=True, key="form_measurement"
    )
    tip("Full = all measurement points. Partial = some points only. Not applicable = not part of your routine.")

    st.divider()

    st.subheader("📍 Affected Areas")
    affected_areas = st.multiselect(
        "Select all areas where you noticed swelling or symptoms today",
        ["Left arm", "Right arm", "Left leg", "Right leg", "Trunk", "Head/neck", "Genital area", "Other"],
        key="form_areas"
    )
    tip("Select every area affected today. Leave blank if no specific area stood out.")

    st.divider()

    st.subheader("🧦 Compression & Self-Care")
    tip("Log everything you wore or did today to manage your lymphoedema.")
    col1, col2 = st.columns(2)
    with col1:
        compression = st.multiselect(
            "Compression worn today (select all that apply)",
            ["None", "Light support (OTC)", "Circular knit (standard)",
             "Flat knit (custom)", "Bandages / wraps", "Night garment",
             "Kinesio taping", "Not applicable"],
            key="form_compression"
        )
        tip("Select all garments worn. E.g. day garment + night garment = select both.")
        compression_hours = st.slider("Total hours of compression worn today", 0, 24, 0, key="form_comp_hours")
        tip("Approximate total hours across all garments combined.")
    with col2:
        self_care = st.multiselect(
            "Self-care performed today (select all that apply)",
            ["None", "Self MLD", "Therapist MLD", "Dry brushing",
             "Elevation", "Exercise / movement", "Skin care / moisturising",
             "Not applicable"],
            key="form_selfcare"
        )
        tip("MLD = Manual Lymphatic Drainage. Select everything you did today.")

    st.divider()

    st.subheader("🍽️ Lifestyle & Triggers")
    tip("Triggers are things that may worsen lymphoedema symptoms. Select all that applied today.")
    diet_triggers = st.multiselect(
        "Dietary triggers",
        ["High-salt meal", "High sugar", "Alcohol", "Caffeine", "Processed foods",
         "Dehydration", "Food intolerance", "None / not applicable"],
        key="form_diet"
    )
    tip("High salt and dehydration are common lymphoedema triggers. Track patterns over time.")
    env_triggers = st.multiselect(
        "Environmental & activity triggers",
        ["Heat exposure", "Cold exposure", "Long travel / flying", "Long standing",
         "Long sitting", "Vigorous exercise", "Tight clothing", "None / not applicable"],
        key="form_env"
    )
    tip("Heat, long travel, and prolonged sitting or standing are well-known triggers.")
    health_triggers = st.multiselect(
        "Health & body triggers",
        ["Infection", "Menstrual cycle", "New medication", "Fatigue", "Poor sleep",
         "Stress spike", "Recent illness", "None / not applicable"],
        key="form_health"
    )
    tip("Infections and hormonal changes can cause significant flares — important to track.")

    st.divider()

    st.subheader("🧘 Wellness Context")
    tip("These help you spot connections between your overall wellbeing and your symptoms.")
    col1, col2 = st.columns(2)
    with col1:
        stress = st.slider("Stress level (0–10)", 0, 10, 0, key="form_stress")
        tip("0 = completely calm; 10 = extremely stressed. Stress is a known lymphoedema trigger.")
        energy = st.slider("Energy level (0–10)", 0, 10, 5, key="form_energy")
        tip("0 = exhausted; 10 = full of energy.")
    with col2:
        sleep_quality = st.selectbox("Sleep quality last night", [
            "Very good (8h+)", "Good (7–8h)", "Fair (5–7h)", "Poor (<5h)"
        ], key="form_sleep")
        tip("Poor sleep is linked to increased inflammation and worsened symptoms.")
        mobility = st.slider("Mobility (0–10)", 0, 10, 5, key="form_mobility")
        tip("0 = very limited movement; 10 = full normal mobility.")
    self_compassion = st.slider("Self-compassion (0–10)", 0, 10, 5, key="form_compassion")
    tip("How kindly are you treating yourself today? 0 = very self-critical; 10 = fully self-accepting. Chronic illness is hard — this matters.")

    st.divider()

    st.subheader("📝 Reflections")
    tip("Optional but valuable — patterns often emerge from your own words over time.")
    challenge = st.text_area(
        "Biggest challenge today?",
        placeholder="e.g., pain after walking to the letterbox, couldn't get garment on...",
        max_chars=300, height=80, key="form_challenge"
    )
    win = st.text_area(
        "Small win today? 🌱",
        placeholder="e.g., remembered to elevate, drank 2L of water, went for a gentle walk...",
        max_chars=300, height=80, key="form_win"
    )
    tags = st.text_input(
        "Tags (optional)",
        placeholder="e.g., flare, new garment, post-travel, good day",
        key="form_tags"
    )
    tip("Tags help you filter and find patterns quickly in your export.")

    st.divider()

    with st.expander("🌤️ Environment (optional)", expanded=False):
        tip("Environmental conditions can affect swelling — useful if you notice weather-related patterns.")
        col1, col2 = st.columns(2)
        with col1:
            temp = st.number_input("Temperature (°C)", value=None, step=0.5, key="form_temp")
            tip("Outdoor or indoor temperature today.")
        with col2:
            humidity = st.number_input("Humidity (%)", value=None, min_value=0, max_value=100, key="form_humidity")
            tip("High humidity can worsen swelling for some people.")

    submitted = st.form_submit_button("💾 Save Today's Entry", use_container_width=True)

# ------------------------------------------------------------------------------
# SAVE LOGIC
# ------------------------------------------------------------------------------
if submitted:
    new_entry = {
        "Date": entry_date.strftime("%Y-%m-%d"),
        "Time": entry_time.strftime("%H:%M"),
        "Heaviness": heaviness,
        "Pain": pain,
        "Limb Appearance": appearance,
        "Measurement Taken": measurement,
        "Affected Areas": ", ".join(affected_areas) if affected_areas else "",
        "Compression Type": ", ".join(compression) if compression else "",
        "Compression Hours": compression_hours,
        "Self Care": ", ".join(self_care) if self_care else "",
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
        st.session_state["form_just_saved"] = True
        st.success(f"✅ Entry saved — {len(logs)} total entries logged.")
        st.caption("💾 Export regularly from the Export page to keep a permanent backup.")
        st.balloons()
        st.rerun()
    except Exception as e:
        st.error(f"❌ Failed to save: {e}")

# ------------------------------------------------------------------------------
# RECENT ENTRIES
# ------------------------------------------------------------------------------
st.divider()
st.subheader("📋 Your Recent Entries")
if not st.session_state.log_df.empty:
    st.dataframe(st.session_state.log_df.tail(10), use_container_width=True, hide_index=True)
    st.caption(f"📊 {len(st.session_state.log_df)} total entries stored in this browser.")
else:
    st.info("No entries yet. Fill in the form above to add your first log.")