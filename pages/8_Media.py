import streamlit as st

st.set_page_config(page_title="Media | The Lymphie Sanctuary", page_icon="🎙️", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #2C3E35; font-size: 16px; }
    h1, h2, h3 { font-family: 'Nunito', sans-serif; font-weight: 600; color: #1A3B2E; }
    .highlight-box {
        background: linear-gradient(135deg, #F4F9F6 0%, #FFFFFF 100%);
        border-left: 6px solid #2E7D5E;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 0.8rem 0;
    }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("🎙️ Media")

st.markdown("""
### 🎧 Radio Interview — June 2026

I spoke with Access Media about living with lymphoedema and building The Lymphie Sanctuary.
""")

# Working button using st.link_button (native Streamlit, always works)
st.link_button(
    label="🎧 Listen to the Interview (25 min)",
    url="https://accessmedia.nz/player?EID=87547ae2-cca2-4387-8619-ed10b7ff3599&audioOnlyMode=true",
    use_container_width=True
)

st.caption("Click the button above to open the interview in a new tab.")

st.markdown("---")

st.subheader("📋 Interview Highlights")

st.markdown("#### Key Discussion Points")

st.markdown("""
<div class="highlight-box">
<strong>🩺 The "Vague Recall" Clinical Gap</strong><br>
Patients arrive at appointments unable to remember their week; the app provides concrete data for clinical conversations.
</div>

<div class="highlight-box">
<strong>🔒 Data Sovereignty &amp; Privacy-First Architecture</strong><br>
Health data never leaves the user's device; the server stores only email and license keys; built for complete privacy.
</div>

<div class="highlight-box">
<strong>💚 Lived-Experience Design</strong><br>
Every feature shaped by personal lymphoedema management; built by someone who lives the condition daily.
</div>

<div class="highlight-box">
<strong>🧠 The Invisible Cognitive Load</strong><br>
Constant mental management of garments, diet, travel, heat; a full-time job invisible to healthcare providers.
</div>

<div class="highlight-box">
<strong>🚀 Patient-Led Innovation</strong><br>
Faster, more empathetic, more usable solutions emerge when patients design for their own conditions.
</div>

<div class="highlight-box">
<strong>🌱 Self-Compassion as a Feature</strong><br>
Daily gentle reminder that "you are doing enough"; no streaks, no leaderboards, no pressure.
</div>

<div class="highlight-box">
<strong>🌍 Universal Need</strong><br>
Built for NZ but reaching global community; the need transcends borders.
</div>

<div class="highlight-box">
<strong>📈 From Symptom Tracker to Empowerment Platform</strong><br>
Visual trends, flare detection, exportable clinic summaries, therapist-facing tools, anonymised research contribution.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
### About The Lymphie Sanctuary

The Lymphie Sanctuary is a private, 2‑minute daily symptom journal for people managing lymphoedema. Built by a data scientist who lives with the condition. NZ$19.99 once, for life. No subscriptions. No accounts. Your data never leaves your device.

🌿 [thelymphiesanctuary.com](https://thelymphiesanctuary.com)
""")