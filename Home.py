import streamlit as st

st.set_page_config(
    page_title="The Lymphie Sanctuary",
    page_icon="🌿",
    layout="centered"
)

# Custom CSS with your Serene Mineral Springs color palette
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Lato:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Lato', sans-serif;
        background-color: #f7fbfa;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #4f6b6a;
    }
    
    .hero {
        background: linear-gradient(145deg, #f1e4d3 0%, #d8e2e0 100%);
        padding: 3.5rem 2rem;
        border-radius: 30px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 20px 30px -10px rgba(79, 107, 106, 0.15);
        border: 1px solid rgba(169, 215, 208, 0.3);
    }
    
    .hero h1 {
        font-size: 4rem;
        font-weight: 700;
        color: #4f6b6a;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .hero .subhead {
        font-size: 1.5rem;
        color: #4f6b6a;
        font-weight: 400;
        max-width: 700px;
        margin: 1rem auto;
        line-height: 1.4;
    }
    
    .community-badge {
        margin-top: 2rem;
        display: inline-block;
        background: rgba(169, 215, 208, 0.3);
        backdrop-filter: blur(5px);
        padding: 0.8rem 2rem;
        border-radius: 60px;
        border: 1px solid rgba(79, 107, 106, 0.2);
    }
    
    .community-badge span {
        color: #4f6b6a;
        font-weight: 500;
        font-size: 1.1rem;
    }
    
    .disclaimer-box {
        background-color: #f1e4d3;
        border-left: 6px solid #a9d7d0;
        padding: 1.2rem 1.8rem;
        border-radius: 12px;
        margin: 1.8rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.03);
    }
    
    .disclaimer-text {
        color: #4f6b6a;
        margin: 0;
        font-weight: 400;
        font-size: 0.95rem;
        font-style: italic;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin: 2.5rem 0;
    }
    
    .feature-card {
        background: #f1e4d3;
        padding: 1.8rem 1.5rem;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.02);
        border: 1px solid #d8e2e0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(79, 107, 106, 0.1);
        border-color: #a9d7d0;
    }
    
    .feature-icon {
        font-size: 2.2rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: #4f6b6a;
        margin-bottom: 0.8rem;
    }
    
    .feature-desc {
        color: #4f6b6a;
        font-size: 0.95rem;
        line-height: 1.5;
        opacity: 0.9;
    }
    
    .cta-section {
        background: linear-gradient(135deg, #a9d7d0 0%, #d8e2e0 100%);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        margin: 2.5rem 0;
        color: #4f6b6a;
    }
    
    .cta-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #4f6b6a;
    }
    
    .cta-sub {
        font-size: 1.1rem;
        opacity: 0.9;
        margin-bottom: 2rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        color: #4f6b6a;
    }
    
    .stButton > button {
        background-color: #4f6b6a !important;
        color: #f7fbfa !important;
        font-family: 'Lato', sans-serif !important;
        font-weight: 500 !important;
        padding: 0.6rem 2rem !important;
        border-radius: 40px !important;
        border: none !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #3a504f !important;
        box-shadow: 0 6px 14px rgba(0,0,0,0.15) !important;
        transform: scale(1.02);
    }
    
    .footer {
        text-align: center;
        color: #4f6b6a;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #d8e2e0;
        opacity: 0.8;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown("""
<div class="hero">
    <h1>🌿 The Lymphie Sanctuary</h1>
    <div class="subhead">Decode Your Symptoms. Reclaim Your Days.</div>
    <div class="community-badge">
        <span>✨ Join a global community of lymphies using data to find their true baseline.</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- INTRODUCTION (PATIENT-CENTRIC) ----------
st.markdown("""
<p style="font-size:1.2rem; color:#4f6b6a; margin:1.5rem 0 2rem 0; text-align:center; max-width:800px; margin-left:auto; margin-right:auto; font-family:'Lato', sans-serif;">
    Navigating lymphedema shouldn't require constant guesswork. The Sanctuary provides a calm, secure space to log your daily symptoms, uncover hidden lifestyle triggers, and build a comprehensive health history for you and your care team.
</p>
""", unsafe_allow_html=True)

# ---------- DISCLAIMER (ELEGANTLY INTEGRATED) ----------
st.markdown("""
<div class="disclaimer-box">
    <p class="disclaimer-text">
        The Lymphie Sanctuary is a dedicated self-care companion, not a substitute for clinical diagnostics. Always consult your certified lymphedema therapist or referring physician before altering your prescribed treatment plan.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- FEATURE GRID (OPTIMIZED COPY) ----------
st.markdown('<div class="feature-grid">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🕊️</div>
        <div class="feature-title">The 2-Minute Daily Log</div>
        <div class="feature-desc">Thoughtfully designed to respect your limited energy. Track swelling fluctuations, compression compliance, and mental wellness without feeling overwhelmed.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Visualize Your Healing Journey</div>
        <div class="feature-desc">Transform isolated daily logs into clear, readable visual trends. Discover exactly how stress, humidity, and movement impact your unique limb volume and pain levels.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📄</div>
        <div class="feature-title">Specialist-Ready Summaries</div>
        <div class="feature-desc">Say goodbye to appointment anxiety. Generate clean, objective PDF reports of your symptoms and therapy adherence to confidently share with your CLT or physician.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Second row
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Pinpoint Your Hidden Triggers</div>
        <div class="feature-desc">Stop wondering what caused a sudden flare-up. Our correlation tools help you clearly identify whether diet, travel, or weather are quietly impacting your swelling.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <div class="feature-title">Uncompromising Privacy</div>
        <div class="feature-desc">Your health data is intensely personal. It remains securely encrypted on your device and is never, under any circumstances, sold to third parties.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Total Data Ownership</div>
        <div class="feature-desc">Export your comprehensive raw data to CSV at any time for your own deep analysis or to contribute to specialized clinical research.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- EMAIL SIGNUP (COMMUNITY FOCUSED) ----------
st.markdown("---")
st.markdown("""
<h3 style="text-align:center; color:#4f6b6a; font-weight:600; font-family:'Playfair Display', serif;">💌 Join the Early Access Community</h3>
<p style="text-align:center; color:#4f6b6a; max-width:600px; margin:0.5rem auto 2rem auto; font-family:'Lato', sans-serif;">
    Be the first to experience new features, gain early access to personalized insights, and receive evidence-based lymphedema management strategies. Your inbox is an extension of our sanctuary; we respect your peace and never spam.
</p>
""", unsafe_allow_html=True)

# Center the button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.link_button(
        "🌿 Join the Early Access Community", 
        "https://thelymphiesanctuary.kit.com/landing-pages/9219430",
        use_container_width=True,
        type="primary"
    )
st.caption("You'll be taken to our secure signup page. Your privacy is respected.")

# ---------- CALL TO ACTION ----------
st.markdown("""
<div class="cta-section">
    <div class="cta-title">Ready to decode your body?</div>
    <div class="cta-sub">Enter The Sanctuary and take the first step toward reclaiming your days.</div>
</div>
""", unsafe_allow_html=True)

# Center the button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🌿 Enter The Sanctuary", use_container_width=True):
        st.switch_page("pages/Daily_Log.py")

# ---------- BOTTOM DISCLAIMER ----------
st.markdown("""
<div class="disclaimer-box">
    <p class="disclaimer-text">
        The Lymphie Sanctuary is a self-care companion, not medical advice. Always consult your healthcare provider before making changes to your treatment plan.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    © 2026 The Lymphie Sanctuary. All rights reserved. | 
    <a href="#" style="color:#4f6b6a; text-decoration:none;">Privacy</a> • 
    <a href="#" style="color:#4f6b6a; text-decoration:none;">Terms</a>
</div>
""", unsafe_allow_html=True)