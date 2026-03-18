import streamlit as st

st.set_page_config(
    page_title="The Lymphie Sanctuary",
    page_icon="🌿",
    layout="centered"
)

# Custom CSS for a professional, clean look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .disclaimer-box {
        background-color: #fef2e0;
        border-left: 6px solid #e67e22;
        padding: 1.2rem 1.8rem;
        border-radius: 12px;
        margin: 1.8rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.03);
    }
    
    .disclaimer-text {
        color: #9a5b13;
        margin: 0;
        font-weight: 500;
        font-size: 0.95rem;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin: 2.5rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 1.8rem 1.5rem;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.02);
        border: 1px solid #e9eef2;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.06);
        border-color: #d0dde6;
    }
    
    .feature-icon {
        font-size: 2.2rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1a3b2e;
        margin-bottom: 0.8rem;
    }
    
    .feature-desc {
        color: #475569;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    .cta-section {
        background: linear-gradient(135deg, #2E7D5E 0%, #1e5f45 100%);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        margin: 2.5rem 0;
        color: white;
    }
    
    .cta-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .cta-sub {
        font-size: 1.1rem;
        opacity: 0.9;
        margin-bottom: 2rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .stButton > button {
        background-color: white !important;
        color: #2E7D5E !important;
        font-weight: 600 !important;
        padding: 0.6rem 2rem !important;
        border-radius: 40px !important;
        border: none !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #f8fafc !important;
        box-shadow: 0 6px 14px rgba(0,0,0,0.15) !important;
        transform: scale(1.02);
    }
    
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION (MORE STRIKING) ----------
st.markdown("""
<div style="
    background: linear-gradient(145deg, #1a4d3a 0%, #2E7D5E 50%, #3a9b7a 100%);
    padding: 3.5rem 2rem;
    border-radius: 30px;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 20px 30px -10px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.2);
">
    <h1 style="
        font-size: 4.5rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0.5rem;
        text-shadow: 0 4px 12px rgba(0,0,0,0.2);
        letter-spacing: -0.02em;
    ">
        🌿 The Lymphie Sanctuary
    </h1>
    <div style="
        font-size: 1.8rem;
        color: rgba(255,255,255,0.95);
        font-weight: 400;
        max-width: 700px;
        margin: 1rem auto;
        text-shadow: 0 2px 6px rgba(0,0,0,0.15);
        line-height: 1.4;
    ">
        Understand your body. Take control.<br>Live better with lymphedema.
    </div>
    <div style="
        margin-top: 2rem;
        display: inline-block;
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(5px);
        padding: 0.8rem 2rem;
        border-radius: 60px;
        border: 1px solid rgba(255,255,255,0.3);
    ">
        <span style="color: white; font-weight: 500; font-size: 1.1rem;">
            ✨ Trusted by early access lymphies worldwide
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- PROMINENT DISCLAIMER (TOP) ----------
st.markdown("""
<div class="disclaimer-box">
    <p class="disclaimer-text">
        ⚠️ <strong>Important:</strong> This tool is for informational and self-tracking purposes only. 
        It is not medical advice. Always consult your healthcare provider before making any changes 
        to your treatment, compression, or self-care routine.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- INTRO ----------
st.markdown("""
<p style="font-size:1.2rem; color:#334155; margin:1.5rem 0 2rem 0; text-align:center; max-width:800px; margin-left:auto; margin-right:auto;">
    The Sanctuary is a gentle, data-informed space where you can track your symptoms, 
    identify triggers, and discover patterns that help you and your healthcare team make better decisions.
</p>
""", unsafe_allow_html=True)

# ---------- FEATURE GRID (using columns for responsiveness) ----------
st.markdown('<div class="feature-grid">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🕊️</div>
        <div class="feature-title">2-Minute Daily Check-In</div>
        <div class="feature-desc">Scientifically-grounded questions on symptoms, compression, triggers, and wellness. No fluff.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Visualize Your Patterns</div>
        <div class="feature-desc">See how stress, diet, activity, and compression affect your swelling and pain over days, weeks, months.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📄</div>
        <div class="feature-title">GP-Ready Reports</div>
        <div class="feature-desc">Generate a one-page summary of your trends to discuss with your doctor or therapist.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Second row of features
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Discover Your Triggers</div>
        <div class="feature-desc">Our algorithms rank what impacts you most: salt, long flights, stress? Know with confidence.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <div class="feature-title">Privacy First</div>
        <div class="feature-desc">Your data stays yours. We never sell or share. Transparent, ethical, built for you.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Export to CSV</div>
        <div class="feature-desc">Download your raw data anytime for your own analysis or to share with specialists.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- EMAIL SIGNUP SECTION ----------
st.markdown("---")
st.markdown("""
<h3 style="text-align:center; color:#1a3b2e; font-weight:600;">💌 Join the Sanctuary Community</h3>
<p style="text-align:center; color:#475569; max-width:600px; margin:0.5rem auto 2rem auto;">
    Be the first to know when we launch new features, and get early access to personalised insights. No spam, ever.
</p>
""", unsafe_allow_html=True)

# Center the button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.link_button(
        "📧 Sign up for updates", 
        "https://thelymphiesanctuary.kit.com/landing-pages/9219430",
        use_container_width=True,
        type="primary"
    )
st.caption("You'll be taken to our secure signup page. Your privacy is respected.")

# ---------- CALL TO ACTION ----------
st.markdown("""
<div class="cta-section">
    <div class="cta-title">Ready to understand your body?</div>
    <div class="cta-sub">Join hundreds of lymphies using data to take control.</div>
</div>
""", unsafe_allow_html=True)

# Center the button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🌿 Start Your First Log", use_container_width=True):
        st.switch_page("pages/Daily_Log.py")

# ---------- BOTTOM DISCLAIMER ----------
st.markdown("""
<div class="disclaimer-box">
    <p class="disclaimer-text">
        ⚠️ <strong>Remember:</strong> The Lymphie Sanctuary is a self-tracking tool, not medical advice. 
        Always consult a qualified healthcare professional for medical guidance specific to your situation.
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