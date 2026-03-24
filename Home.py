import streamlit as st

st.set_page_config(
    page_title="The Lymphie Sanctuary",
    page_icon="🌿",
    layout="centered"
)

# ---------- SIMPLE, RELIABLE CSS (system fonts, no external import) ----------
st.markdown("""
<style>
    /* Global font for everything */
    html, body, [class*="css"], .stApp, .stMarkdown, .stText, .stButton, .stSidebar, .stSidebar * {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
    }

    /* Headings – use serif if you like, but a clean sans-serif works too */
    h1, h2, h3, h4, h5, h6 {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
        font-weight: 600;
        color: #4f6b6a;
    }

    /* Sidebar navigation font */
    [data-testid="stSidebarNav"] * {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
        font-weight: 500;
    }

    /* Disclaimer box – improved spacing */
    .disclaimer-box {
        background-color: #fff3e0;
        border-left: 8px solid #e67e22;
        border-radius: 16px;
        padding: 1rem 1.5rem;  /* less vertical padding */
        margin: 1.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    .disclaimer-text {
        color: #b85e00;
        margin: 0;
        font-weight: 500;
        font-size: 1rem;
        line-height: 1.4;      /* tighter line height */
        letter-spacing: normal;
    }

    .disclaimer-icon {
        font-size: 1.3rem;
        margin-right: 8px;
        vertical-align: middle;
    }

    /* Feature cards – ensure font inherits */
    .feature-card {
        background: white;
        padding: 1.8rem 1.5rem;
        border-radius: 24px;
        box-shadow: 0 8px 20px rgba(79,107,106,0.08);
        border: 1px solid #e2eef0;
        transition: all 0.2s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(79,107,106,0.12);
    }

    .feature-icon {
        font-size: 2.2rem;
        margin-bottom: 1rem;
    }

    .feature-title {
        font-weight: 700;
        font-size: 1.3rem;
        color: #1a3b2e;
        margin-bottom: 0.8rem;
        line-height: 1.3;
    }

    .feature-desc {
        color: #4a6a68;
        font-size: 0.95rem;
        line-height: 1.5;
        flex-grow: 1;
    }

    .cta-section {
        background: linear-gradient(135deg, #a9d7d0 0%, #d8e2e0 100%);
        padding: 2rem;
        border-radius: 24px;
        text-align: center;
        margin: 2rem 0;
        color: #4f6b6a;
    }

    .cta-title {
        font-weight: 700;
        font-size: 1.8rem;
        margin-bottom: 0.8rem;
        color: #2c5a54;
    }

    .cta-sub {
        font-size: 1rem;
        opacity: 0.9;
        margin-bottom: 1.5rem;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
        color: #3a5f5a;
    }

    .stButton > button {
        background-color: #4f6b6a !important;
        color: white !important;
        font-weight: 500 !important;
        border-radius: 40px !important;
        border: none !important;
        font-size: 1rem !important;
        padding: 0.5rem 1.8rem !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover {
        background-color: #3a504f !important;
        transform: scale(1.02);
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        margin-top: 2.5rem;
        padding-top: 1.5rem;
        border-top: 1px solid #d8e2e0;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown("""
<div style="background: linear-gradient(145deg, #1a4d3a, #2E7D5E); padding: 2.5rem 2rem; border-radius: 30px; text-align: center; margin-bottom: 2rem;">
    <h1 style="font-size: 2.8rem; color: white; margin-bottom: 0.5rem; font-weight: 700;">🌿 The Lymphie Sanctuary</h1>
    <p style="font-size: 1.3rem; color: rgba(255,255,255,0.9); max-width: 550px; margin: 0 auto 1rem auto;">Decode Your Symptoms. Reclaim Your Days.</p>
    <div style="display: inline-block; background: rgba(255,255,255,0.15); padding: 0.5rem 1.5rem; border-radius: 50px;">
        <span style="color: white; font-weight: 500;">✨ Trusted by early access lymphies worldwide</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- TOP DISCLAIMER ----------
st.markdown("""
<div class="disclaimer-box">
    <p class="disclaimer-text">
        <span class="disclaimer-icon">⚠️</span>
        <strong>IMPORTANT:</strong> The Lymphie Sanctuary is a self-care companion, not a substitute for clinical diagnostics. 
        Always consult your certified lymphedema therapist or physician before altering your treatment plan.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- INTRODUCTION ----------
st.markdown("""
<p style="font-size:1.1rem; color:#4f6b6a; margin:1rem 0 2rem 0; text-align:center; max-width:700px; margin-left:auto; margin-right:auto;">
    Navigating lymphedema shouldn't require constant guesswork. The Sanctuary provides a calm, secure space to log your daily symptoms, uncover hidden lifestyle triggers, and build a comprehensive health history for you and your care team.
</p>
""", unsafe_allow_html=True)

# ---------- FEATURE GRID (same as before, but now styled by CSS) ----------
st.markdown("""
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
    <div class="feature-card">
        <div class="feature-icon">🕊️</div>
        <div class="feature-title">2-Minute Daily Check-In</div>
        <div class="feature-desc">Respects your limited energy. Track swelling, compression, and mental wellness without overwhelm.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Visual Healing Journey</div>
        <div class="feature-desc">See how stress, humidity, and movement impact your limb volume and pain levels over time.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📄</div>
        <div class="feature-title">Specialist-Ready Reports</div>
        <div class="feature-desc">Generate clean PDF summaries of your symptoms and adherence to share with your care team.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Pinpoint Hidden Triggers</div>
        <div class="feature-desc">Identify whether diet, travel, or weather are quietly impacting your swelling and flares.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <div class="feature-title">Uncompromising Privacy</div>
        <div class="feature-desc">Your health data is encrypted and never, under any circumstances, sold to third parties.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Total Data Ownership</div>
        <div class="feature-desc">Export your raw data to CSV anytime for your own analysis or to contribute to research.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- EMAIL SIGNUP ----------
st.markdown("---")
st.markdown("""
<h3 style="text-align:center; color:#4f6b6a; font-weight:600;">💌 Join the Early Access Community</h3>
<p style="text-align:center; color:#4f6b6a; max-width:500px; margin:0.5rem auto 1.5rem auto;">
    Be the first to experience new features, gain early access to personalized insights, and receive evidence-based lymphedema management strategies. Your inbox is an extension of our sanctuary; we respect your peace and never spam.
</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.link_button(
        "🌿 Join the Early Access Community", 
        "https://docs.google.com/forms/d/1dO0Oryxyeeiuvj2GKqHWYPXDWzAHUKmkh__wlCZ9a1Y/edit",
        use_container_width=True,
        type="primary"
    )
st.caption("You'll be taken to our secure signup page. Your privacy is respected.")

# ---------- ANALYTICS ----------
st.markdown("---")
st.markdown("""
<h3 style="text-align:center; color:#4f6b6a; font-weight:600;">📊 Understand Your Patterns</h3>
<p style="text-align:center; color:#4f6b6a;">See how your symptoms change over time and discover what impacts you most.</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("📊 View Analytics Dashboard", use_container_width=True):
        st.switch_page("pages/2_Analytics.py")

# ---------- REPORT ----------
st.markdown("---")
st.markdown("""
<h3 style="text-align:center; color:#4f6b6a; font-weight:600;">📋 For Your Healthcare Team</h3>
<p style="text-align:center; color:#4f6b6a;">Generate a structured PDF summary of your symptoms, adherence, and triggers to share with your GP or therapist.</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("📄 Generate GP Report", use_container_width=True):
        st.switch_page("pages/3_Report.py")

# ---------- CALL TO ACTION ----------
st.markdown("""
<div class="cta-section">
    <div class="cta-title">Ready to decode your body?</div>
    <div class="cta-sub">Enter The Sanctuary and take the first step toward reclaiming your days.</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🌿 Enter The Sanctuary", use_container_width=True):
        st.switch_page("pages/1_Daily_Log.py")

# ---------- BOTTOM DISCLAIMER ----------
st.markdown("""
<div class="disclaimer-box">
    <p class="disclaimer-text">
        <span class="disclaimer-icon">🔔</span>
        <strong>REMEMBER:</strong> This tool is for informational and self-tracking purposes only. 
        It is not medical advice. Always consult your healthcare provider before making changes to your treatment.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    © 2026 The Lymphie Sanctuary. All rights reserved. | 
    <a href="#" style="color:#64748b; text-decoration:none;">Privacy</a> • 
    <a href="#" style="color:#64748b; text-decoration:none;">Terms</a>
</div>
""", unsafe_allow_html=True)