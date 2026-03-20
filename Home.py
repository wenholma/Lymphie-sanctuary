import streamlit as st

st.set_page_config(
    page_title="The Lymphie Sanctuary",
    page_icon="🌿",
    layout="centered"
)

# Custom CSS
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
    
    .disclaimer-box {
        background-color: #fff3e0;
        border-left: 8px solid #e67e22;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 15px rgba(230, 126, 34, 0.15);
        border: 1px solid rgba(230, 126, 34, 0.2);
    }
    
    .disclaimer-text {
        color: #b85e00;
        margin: 0;
        font-weight: 600;
        font-size: 1.1rem;
        line-height: 1.6;
        text-shadow: 0 1px 2px rgba(255,255,255,0.5);
    }
    
    .disclaimer-icon {
        font-size: 1.5rem;
        margin-right: 10px;
        vertical-align: middle;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 2rem 1.8rem;
        border-radius: 24px;
        box-shadow: 0 10px 30px rgba(79, 107, 106, 0.08);
        border: 1px solid #e2eef0;
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .feature-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 35px rgba(79, 107, 106, 0.15);
        border-color: #a9d7d0;
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1.2rem;
    }
    
    .feature-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a3b2e;
        margin-bottom: 1rem;
        line-height: 1.3;
    }
    
    .feature-desc {
        color: #4a6a68;
        font-size: 1rem;
        line-height: 1.6;
        opacity: 1;
        flex-grow: 1;
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
        color: #64748b;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #d8e2e0;
        opacity: 0.8;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SIMPLIFIED HERO SECTION ----------
st.markdown("""
<div style="background: linear-gradient(145deg, #1a4d3a, #2E7D5E); padding: 3rem 2rem; border-radius: 30px; text-align: center; margin-bottom: 2rem;">
    <h1 style="font-size: 3.5rem; color: white; margin-bottom: 1rem;">🌿 The Lymphie Sanctuary</h1>
    <p style="font-size: 1.5rem; color: white; opacity: 0.95; max-width: 600px; margin: 0 auto 1.5rem auto;">Decode Your Symptoms. Reclaim Your Days.</p>
    <div style="display: inline-block; background: rgba(255,255,255,0.2); padding: 0.8rem 2rem; border-radius: 50px;">
        <span style="color: white; font-weight: 600;">✨ Trusted by early access lymphies worldwide</span>
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
<p style="font-size:1.2rem; color:#4f6b6a; margin:1.5rem 0 2rem 0; text-align:center; max-width:800px; margin-left:auto; margin-right:auto; font-family:'Lato', sans-serif;">
    Navigating lymphedema shouldn't require constant guesswork. The Sanctuary provides a calm, secure space to log your daily symptoms, uncover hidden lifestyle triggers, and build a comprehensive health history for you and your care team.
</p>
""", unsafe_allow_html=True)

# ---------- FEATURE GRID ----------
st.markdown("""
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 3rem 0;">
    <div style="background: white; padding: 2rem 1.8rem; border-radius: 24px; box-shadow: 0 10px 30px rgba(79,107,106,0.08); border: 1px solid #e2eef0;">
        <div style="font-size: 2.5rem; margin-bottom: 1.2rem;">🕊️</div>
        <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: #1a3b2e; margin-bottom: 1rem;">2-Minute Daily Check-In</div>
        <div style="color: #4a6a68; font-size: 1rem; line-height: 1.6;">Respects your limited energy. Track swelling, compression, and mental wellness without overwhelm.</div>
    </div>
    <div style="background: white; padding: 2rem 1.8rem; border-radius: 24px; box-shadow: 0 10px 30px rgba(79,107,106,0.08); border: 1px solid #e2eef0;">
        <div style="font-size: 2.5rem; margin-bottom: 1.2rem;">📊</div>
        <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: #1a3b2e; margin-bottom: 1rem;">Visual Healing Journey</div>
        <div style="color: #4a6a68; font-size: 1rem; line-height: 1.6;">See how stress, humidity, and movement impact your limb volume and pain levels over time.</div>
    </div>
    <div style="background: white; padding: 2rem 1.8rem; border-radius: 24px; box-shadow: 0 10px 30px rgba(79,107,106,0.08); border: 1px solid #e2eef0;">
        <div style="font-size: 2.5rem; margin-bottom: 1.2rem;">📄</div>
        <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: #1a3b2e; margin-bottom: 1rem;">Specialist-Ready Reports</div>
        <div style="color: #4a6a68; font-size: 1rem; line-height: 1.6;">Generate clean PDF summaries of your symptoms and adherence to share with your care team.</div>
    </div>
    <div style="background: white; padding: 2rem 1.8rem; border-radius: 24px; box-shadow: 0 10px 30px rgba(79,107,106,0.08); border: 1px solid #e2eef0;">
        <div style="font-size: 2.5rem; margin-bottom: 1.2rem;">🔍</div>
        <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: #1a3b2e; margin-bottom: 1rem;">Pinpoint Hidden Triggers</div>
        <div style="color: #4a6a68; font-size: 1rem; line-height: 1.6;">Identify whether diet, travel, or weather are quietly impacting your swelling and flares.</div>
    </div>
    <div style="background: white; padding: 2rem 1.8rem; border-radius: 24px; box-shadow: 0 10px 30px rgba(79,107,106,0.08); border: 1px solid #e2eef0;">
        <div style="font-size: 2.5rem; margin-bottom: 1.2rem;">🔒</div>
        <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: #1a3b2e; margin-bottom: 1rem;">Uncompromising Privacy</div>
        <div style="color: #4a6a68; font-size: 1rem; line-height: 1.6;">Your health data is encrypted and never, under any circumstances, sold to third parties.</div>
    </div>
    <div style="background: white; padding: 2rem 1.8rem; border-radius: 24px; box-shadow: 0 10px 30px rgba(79,107,106,0.08); border: 1px solid #e2eef0;">
        <div style="font-size: 2.5rem; margin-bottom: 1.2rem;">📈</div>
        <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: #1a3b2e; margin-bottom: 1rem;">Total Data Ownership</div>
        <div style="color: #4a6a68; font-size: 1rem; line-height: 1.6;">Export your raw data to CSV anytime for your own analysis or to contribute to research.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- EMAIL SIGNUP ----------
st.markdown("---")
st.markdown("""
<h3 style="text-align:center; color:#4f6b6a; font-weight:600; font-family:'Playfair Display', serif;">💌 Join the Early Access Community</h3>
<p style="text-align:center; color:#4f6b6a; max-width:600px; margin:0.5rem auto 2rem auto; font-family:'Lato', sans-serif;">
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
<h3 style="text-align:center; color:#4f6b6a; font-weight:600; font-family:'Playfair Display', serif;">📊 Understand Your Patterns</h3>
<p style="text-align:center; color:#4f6b6a; max-width:600px; margin:0.5rem auto 2rem auto; font-family:'Lato', sans-serif;">
    See how your symptoms change over time and discover what impacts you most.
</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("📊 View Analytics Dashboard", use_container_width=True):
        st.switch_page("pages/2_Analytics.py")

# ---------- REPORT ----------
st.markdown("---")
st.markdown("""
<h3 style="text-align:center; color:#4f6b6a; font-weight:600; font-family:'Playfair Display', serif;">📋 For Your Healthcare Team</h3>
<p style="text-align:center; color:#4f6b6a; max-width:600px; margin:0.5rem auto 2rem auto; font-family:'Lato', sans-serif;">
    Generate a structured PDF summary of your symptoms, adherence, and triggers to share with your GP or therapist.
</p>
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