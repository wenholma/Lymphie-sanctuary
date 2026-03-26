import streamlit as st

st.set_page_config(page_title="The Lymphie Sanctuary", page_icon="🌿", layout="centered")

# Custom CSS (same as before – keeps the look)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3 {
        color: #2E7D5E;
    }
    .main-header {
        background: linear-gradient(145deg, #2E7D5E, #1e5f45);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        color: white;
    }
    .main-header h1 {
        color: white;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    .privacy-badge {
        background-color: #f0f7f4;
        border-left: 8px solid #2E7D5E;
        padding: 1.2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        height: 100%;
        transition: transform 0.2s;
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .feature-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #1a3b2e;
    }
    .cta-section {
        background: #eaf7f2;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
    }
    .cta-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2E7D5E;
        margin-bottom: 1rem;
    }
    .stButton > button {
        background-color: #2E7D5E !important;
        color: white !important;
        border-radius: 40px !important;
        padding: 0.6rem 2rem !important;
        border: none !important;
        font-weight: 500 !important;
    }
    .stButton > button:hover {
        background-color: #1e5f45 !important;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #ddd;
        font-size: 0.9rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🌿 The Lymphie Sanctuary</h1>
    <p>Your Private Digital Symptom Journal</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Lymphedema management is enough work already. Stop the guesswork with a secure, 2‑minute daily log that stays entirely on your own device.
""")

# --- Grounding sentence (emotional warmth) ---
st.markdown("*This is a quiet place to notice patterns — not to judge your body.*")

# Privacy badge
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

# Call to action
st.markdown("""
<div class="cta-section">
    <div class="cta-title">Ready to own your data?</div>
    <p>Get Lifetime Access to the Export & Trends toolkit for a one‑time payment of <strong>$25</strong>. No subscriptions, no hidden fees. Just a tool for life.</p>
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