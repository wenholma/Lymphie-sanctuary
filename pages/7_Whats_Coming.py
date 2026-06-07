import streamlit as st

st.set_page_config(page_title="What's Coming | The Lymphie Sanctuary", page_icon="🚀", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #2C3E35; font-size: 16px; }
    h1, h2, h3, h4 { font-family: 'Nunito', sans-serif; font-weight: 600; color: #1A3B2E; }
    .feature-box {
        background: linear-gradient(135deg, #F4F9F6 0%, #FFFFFF 100%);
        border-left: 6px solid #2E7D5E;
        padding: 1.2rem 1.5rem;
        border-radius: 16px;
        margin: 1.2rem 0;
    }
    .highlight { color: #2E7D5E; font-weight: 700; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("🚀 What's Coming to The Lymphie Sanctuary")

st.markdown("""
<div style="text-align: center; font-size: 1.1rem; color: #4A6357; margin-bottom: 2rem;">
    <em>Exciting new features are on the way — built with the same care, privacy, and lymphie-love as everything else.</em>
</div>
""", unsafe_allow_html=True)

# Feature 1
st.markdown("""
<div class="feature-box">
    <h3>📈 Visual Trends Dashboard</h3>
    <p>See your symptom patterns over weeks and months with <span class="highlight">gentle area charts</span> — heaviness, pain, triggers, and more. No more scrolling through raw entries; your story appears at a glance.</p>
</div>
""", unsafe_allow_html=True)

# Feature 2
st.markdown("""
<div class="feature-box">
    <h3>🧾 Clinical PDF Report</h3>
    <p>Walk into your next appointment with a <span class="highlight">beautiful one‑page summary</span> designed for your therapist or doctor. Includes averages, trends, and your win log — all formatted and ready to share.</p>
</div>
""", unsafe_allow_html=True)

# Feature 3
st.markdown("""
<div class="feature-box">
    <h3>🦵 Multi‑Limb Support</h3>
    <p>Track <span class="highlight">both legs, both arms, or any combination</span> — because lymphoedema doesn't always play by the rules. Each limb gets its own data, all in one app.</p>
</div>
""", unsafe_allow_html=True)

# Feature 4
st.markdown("""
<div class="feature-box">
    <h3>💡 Gentle Insights</h3>
    <p>Your own personal <span class="highlight">pattern detective</span>. The app will suggest connections: <em>"Your heaviness scores increase 2 days after high‑sodium meals"</em> — all calculated privately on your device.</p>
</div>
""", unsafe_allow_html=True)

# Feature 5
st.markdown("""
<div class="feature-box">
    <h3>📅 Appointment Log</h3>
    <p>Record what was discussed at each visit — <span class="highlight">new exercises, garment changes, treatment plans</span>. Keep your complete lymphoedema story in one place.</p>
</div>
""", unsafe_allow_html=True)

# Feature 6
st.markdown("""
<div class="feature-box">
    <h3>📲 PWA Install (No App Store Needed)</h3>
    <p>Soon you'll see a <span class="highlight">"Install" button</span> right in your browser — The Lymphie Sanctuary will feel just like a native app on your home screen. No store, no fees, no hassle.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem;">
    <p style="font-size: 1.1rem; font-weight: 600; color: #1A3B2E;">Which feature are you most excited about? Let me know!</p>
    <p style="font-size: 0.95rem; color: #4A6357;">📧 <strong>info@thelymphiesanctuary.com</strong></p>
    <p style="font-size: 0.9rem; color: #6B7F74;">Your feedback shapes what comes next 🌿</p>
</div>
""", unsafe_allow_html=True)