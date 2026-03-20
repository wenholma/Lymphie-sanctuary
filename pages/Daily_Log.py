import streamlit as st
import pandas as pd
from datetime import datetime

# -------------------- Page config --------------------
st.set_page_config(page_title="Daily Lymphie Log", layout="centered")
st.title("🌿 Daily Lymphie Log")
st.markdown("Track your symptoms, triggers, and wellness in under 2 minutes.")

# -------------------- Initialize session state --------------------
if "log_df" not in st.session_state:
    # Create an empty DataFrame with the expected columns
    columns = [
        "Date", "Time", "Heaviness", "Pain", "Limb Appearance",
        "Measurement Taken", "Affected Areas", "Compression Type", "Compression Hours",
        "Self Care", "Dietary Triggers", "Environmental Triggers",
        "Health Triggers", "Stress", "Sleep Quality", "Energy",
        "Mobility", "Self Compassion", "Biggest Challenge", "Small Win",
        "Temperature", "Humidity", "Tags"
    ]
    st.session_state.log_df = pd.DataFrame(columns=columns)

# -------------------- Helper for info icons --------------------
def info_icon(text):
    st.markdown(f"<small style='color: gray;'>ℹ️ {text}</small>", unsafe_allow_html=True)

# -------------------- Main Form --------------------
with st.form("daily_log_form"):
    st.subheader("📅 Entry Details")
    col1, col2 = st.columns(2)
    with col1:
        entry_date = st.date_input("Date", value=datetime.now().date())
    with col2:
        entry_time = st.time_input("Time", value=datetime.now().time().replace(second=0, microsecond=0))

    st.subheader("🦵 Limb Sensations")
    col1, col2 = st.columns(2)
    with col1:
        heaviness = st.slider("Heaviness / Tightness (0–10)", 0, 10, 5,
                              help="Internal sensation of fullness, pressure, or weight.")
        info_icon("0 = none; 10 = affects movement or comfort")
    with col2:
        pain = st.slider("Pain / Discomfort (0–10)", 0, 10, 5,
                        help="Aching, throbbing, burning, or discomfort.")
        info_icon("0 = none; 10 = interferes with daily activities")

    st.subheader("👁️ Limb Appearance (vs baseline)")
    appearance_options = [
        "Baseline / Normal",
        "Slight puffiness (pitting)",
        "Noticeable swelling (firm)",
        "Marked swelling / skin stretched"
    ]
    appearance = st.selectbox("How did the limb look today?", appearance_options,
                              help="Baseline = your usual stable appearance on a good day.")
    info_icon("Baseline = your usual good day; pitting = mild indentation; marked = tight, shiny skin")

    st.subheader("📏 Measurements")
    measure_options = ["Yes — full measurement", "Yes — partial measurement", "No", "Not applicable"]
    measurement = st.radio("Did you take a limb circumference measurement today?", measure_options, horizontal=True)

    st.subheader("📍 Affected Areas")
    area_options = ["Left arm", "Right arm", "Left leg", "Right leg", "Trunk", "Head/neck", "Genital area", "Other"]
    affected_areas = st.multiselect("Select all that apply", area_options,
                                    help="Trunk = chest, abdomen, back; Select 'Other' and use Tags field below to specify.")
    info_icon("Select all areas where you noticed swelling or symptoms today. Use Tags for 'Other' details.")

    st.subheader("🧦 Compression & Self-Care")
    col1, col2 = st.columns(2)
    with col1:
        compression_options = [
            "Not applicable", "None", "Light support (OTC)", "Circular knit (standard)",
            "Flat knit (custom)", "Bandages / wraps", "Night garment", "Kinesio taping"
        ]
        # FIX 1: This is already a selectbox (single-select)
        compression = st.selectbox("Compression worn today", compression_options,
                                   help="OTC = over-the-counter; Circular knit = seamless, off-the-shelf; Flat knit = custom-made; Bandages/wraps = multilayer; Night garment = for sleep; Kinesio taping = lymphatic taping.")
        
        # FIX 1: Clarified wording
        compression_hours = st.slider(
            "Hours of compression worn today", 
            min_value=0, 
            max_value=24, 
            value=8,
            help="How many hours did you wear compression today? 0 = none."
        )
        
    with col2:
        # FIX 1: Added "Yes – Therapist MLD" option
        selfcare_options = [
            "No", 
            "Yes — Self MLD", 
            "Yes — Therapist MLD", 
            "Yes — Dry brushing", 
            "Yes — Both", 
            "Not applicable"
        ]
        self_care = st.selectbox("Self-MLD / Dry brushing performed?", selfcare_options,
                                 help="Self-MLD = gentle skin stretching; Dry brushing = soft brush to stimulate lymph flow; Therapist MLD = professional treatment.")

    st.subheader("🍽️ Lifestyle & Triggers")
    st.markdown("**Dietary triggers** (select all that apply)")
    diet_options = [
        "High-salt meal", "High sugar / refined carbs", "Alcohol", "Caffeine",
        "Large meal late at night", "Processed foods", "Dehydration (low water intake)",
        "Food intolerance flare (e.g., gluten, dairy)", "Not applicable"
    ]
    diet_triggers = st.multiselect(
        "Dietary triggers",
        diet_options,
        label_visibility="collapsed",
        help="Select all that apply. The list stays open so you can choose multiple."
    )

    st.markdown("**Environmental / activity triggers** (select all that apply)")
    env_options = [
        "Heat exposure", "Cold exposure", "Long travel (>2 hours sitting)",
        "Long standing (>1 hour)", "Long sitting (>1 hour)", "Vigorous exercise",
        "Repetitive movement of affected limb", "Tight clothing / jewellery",
        "Heavy lifting", "Injury / skin break", "Insect bite", "Sunburn", "Not applicable"
    ]
    env_triggers = st.multiselect(
        "Environmental triggers",
        env_options,
        label_visibility="collapsed",
        help="Select all that apply. The list stays open so you can choose multiple."
    )

    st.markdown("**Health triggers** (select all that apply)")
    health_options = [
        "Infection (fever, redness, heat, streaking)", "Menstrual cycle / hormonal changes",
        "New medication / dose change", "Fatigue / exhaustion", "Poor sleep",
        "Stress spike", "Recent illness (cold, flu, virus)", "Dehydration",
        "Constipation", "Not applicable"
    ]
    health_triggers = st.multiselect(
        "Health triggers",
        health_options,
        label_visibility="collapsed",
        help="Select all that apply. The list stays open so you can choose multiple."
    )

    st.subheader("🧘 Wellness Context")
    col1, col2 = st.columns(2)
    with col1:
        stress = st.slider("Stress (0–10)", 0, 10, 5, help="0 = no stress; 10 = extremely stressed")
        energy = st.slider("Energy (0–10)", 0, 10, 5, help="0 = no energy; 10 = full energy")
    with col2:
        sleep_options = ["Poor (<5h, restless)", "Fair (5–7h)", "Good (7–8h)", "Very good (8+h)"]
        sleep_quality = st.selectbox("Sleep quality", sleep_options)
        mobility = st.slider("Mobility (0–10)", 0, 10, 5, help="0 = unable to move limb; 10 = full mobility")
    self_compassion = st.slider("Self-compassion (0–10)", 0, 10, 5,
                                help="How kind were you to yourself today? 0 = not at all; 10 = very compassionate")

    # ---------- FIX 2: Improved Reflection Text Fields ----------
    st.subheader("📝 Reflections")
    
    challenge = st.text_area(
        "What was your biggest challenge today?",
        placeholder="e.g., pain after walking, emotional struggle, difficult appointment...",
        max_chars=500,
        height=100,
        help="Describe in a few sentences (max 500 characters). This helps us understand your journey."
    )
    # Show character count
    if challenge:
        st.caption(f"Characters: {len(challenge)}/500")
    
    win = st.text_area(
        "What was a small win or something that helped today?",
        placeholder="e.g., remembered to elevate, had a good chat, wore compression all day...",
        max_chars=500,
        height=100,
        help="What made today a bit better? (max 500 characters). Every small win counts."
    )
    # Show character count
    if win:
        st.caption(f"Characters: {len(win)}/500")

    st.subheader("🌤️ Environment (optional)")
    col1, col2 = st.columns(2)
    with col1:
        # FIX 3: Temperature restriction
        temp = st.number_input(
            "Temperature (°C)", 
            value=None, 
            step=0.1, 
            format="%.1f",
            min_value=-50.0,
            max_value=60.0,
            help="Please enter a realistic temperature between -50°C and 60°C."
        )
    with col2:
        humidity = st.number_input("Humidity (%)", value=None, min_value=0, max_value=100, step=1)

    tags = st.text_input("Tags (optional)", placeholder="e.g., post-flight, flare, new garment, other areas")

    # Submit button
    submitted = st.form_submit_button("Save Entry")

# -------------------- Handle form submission --------------------
if submitted:
    # Collect all data into a dictionary
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
    # Append to session state dataframe
    st.session_state.log_df = pd.concat(
        [st.session_state.log_df, pd.DataFrame([new_entry])],
        ignore_index=True
    )
    st.success("Entry saved! You can view all entries below.")

# -------------------- Display past entries --------------------
st.subheader("📋 Your Recent Entries")
if not st.session_state.log_df.empty:
    st.dataframe(st.session_state.log_df.tail(10), use_container_width=True)

    # Download button
    csv = st.session_state.log_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download All Entries as CSV",
        data=csv,
        file_name=f"lymphie_log_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
else:
    st.info("No entries yet. Use the form above to add your first log.")

# -------------------- Footer disclaimer --------------------
st.divider()
st.caption(
    "⚠️ This tool is for informational and self-tracking purposes only. "
    "It is not medical advice. Always consult your healthcare provider "
    "before making changes to your treatment."
)