import streamlit as st

st.set_page_config(page_title="The Lymphie Sanctuary", page_icon="🌿", layout="centered")

# Custom CSS (minimal version – you can keep your previous styling if you prefer)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Lato:wght@300;400;500;700&display=swap');
    html, body, [class*="css"] { font-family: 'Lato', sans-serif; background-color: #f7fbfa; }
    .hero { background: linear-gradient(145deg, #1a4d3a, #2E7D5E); padding: 3rem 2rem; border-radius: 40px; margin-bottom: 2rem; text-align: center; color: white; }
    .hero h1 { font-size: 3.5rem; margin-bottom: 1rem; }
    .hero p { font-size: 1.3rem; max-width: 600px; margin: 0 auto; }
    .privacy-badge { background-color: #fff3e0; border-left: 8px solid #e67e22; padding: 1.5rem; border-radius: 16px; margin: 2rem 0; }
    .feature-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin: 2rem 0; }
    .feature-card { background: white; padding: 1.8rem; border-radius: 24px; box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
    .feature-icon { font-size: 2.5rem; margin-bottom: 1rem; }
    .feature-title { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; }
    .cta-section { background: linear-gradient(135deg, #a9d7d0, #d8e2e0); padding: 2rem; border-radius: 30px; text-align: center; margin: 2rem 0; }
    .stButton > button { background-color: #4f6b6a !important; color: white !important; border-radius: 40px !important; padding: 0.6rem 2rem !important; }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <h1>🌿 The Lymphie Sanctuary</h1>
    <p>Your Private Digital Symptom Journal</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Lymphedema management is enough work already. Stop the guesswork with a secure, 2‑minute daily log that stays entirely on your own device.
""")

# Privacy promise
st.markdown("""
<div class="privacy-badge">
    <strong>🔒 No Accounts. No Databases. No Data‑Mining.</strong><br>
    Unlike traditional health apps, The Sanctuary is <strong>Local‑First</strong>. Your measurements, photos, and notes are stored only in your browser's private memory. We don't see your data, we don't store it, and we can’t sell it. It belongs to you.
</div>
""", unsafe_allow_html=True)

# Features
st.subheader("How It Works")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🕊️</div>
        <div class="feature-title">2-Minute Daily Check‑In</div>
        Track swelling, compression, and mental energy without the overwhelm.
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Visual Trends</div>
        Spot patterns between your diet, weather, and limb volume over time.
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📥</div>
        <div class="feature-title">Lifetime Export</div>
        Turn your logs into a clean CSV file to share with your CLT or doctor.
    </div>
    """, unsafe_allow_html=True)

# Lifetime Access section
st.markdown("""
<div class="cta-section">
    <h3>Ready to own your data?</h3>
    <p>Get Lifetime Access to the Export & Trends toolkit for a one‑time payment of <strong>$25</strong>.<br>No subscriptions, no hidden fees. Just a tool for life.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🌿 Get My Lifetime Key", use_container_width=True):
        st.switch_page("pages/6_Settings.py")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("📝 Start Your First Log (Free)", use_container_width=True):
        st.switch_page("pages/1_Daily_Log.py")

st.markdown("---")
st.caption("© 2026 The Lymphie Sanctuary. All rights reserved. | [Privacy Policy](pages/4_Privacy.py) | [Terms of Service](pages/5_Terms.py)")