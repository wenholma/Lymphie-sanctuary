import streamlit as st

st.set_page_config(
    page_title="The Lymphie Sanctuary",
    page_icon="🌿",
    layout="centered"
)

# Custom CSS for a gentle, welcoming feel
st.markdown("""
<style>
    .big-title {
        font-size: 3rem;
        font-weight: 700;
        color: #2E7D5E;
        margin-bottom: 0;
    }
    .disclaimer-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 1rem;
        border-radius: 5px;
        margin: 1.5rem 0;
        font-weight: 500;
    }
    .disclaimer-text {
        color: #856404;
        margin: 0;
    }
    .feature-card {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E7D5E;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<p class="big-title">🌿 The Lymphie Sanctuary</p>', unsafe_allow_html=True)
st.markdown("### Your daily companion for understanding and managing lymphoedema")

# ---------- PROMINENT DISCLAIMER (Top) ----------
st.markdown("""
<div class="disclaimer-box">
    <p class="disclaimer-text">
        ⚠️ <strong>IMPORTANT DISCLAIMER:</strong> This tool is for informational and self-tracking purposes only. 
        It is not medical advice. Always consult your healthcare provider before making any changes 
        to your treatment, compression, or self-care routine.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- Intro ----------
st.write("")
st.write(
    "The Sanctuary is a gentle, data-informed space where you can track your symptoms, "
    "identify triggers, and discover patterns that help you and your healthcare team make better decisions."
)

# ---------- Features ----------
st.markdown('<div class="feature-card">', unsafe_allow_html=True)
st.markdown("**🕊️ 2-minute daily check-in**")
st.markdown("Simple, guided questions about your symptoms, compression, and potential triggers.")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="feature-card">', unsafe_allow_html=True)
st.markdown("**📊 Visual insights**")
st.markdown("See how your symptoms change over time and what might be influencing them.")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="feature-card">', unsafe_allow_html=True)
st.markdown("**📄 GP-ready summaries**")
st.markdown("Export a one-page report to take to your appointments.")
st.markdown("</div>", unsafe_allow_html=True)

# ---------- Email Signup Section ----------
st.markdown("---")
st.markdown("### 💌 Join the Sanctuary Community")
st.markdown(
    "Be the first to know when we launch new features, and get early access to personalised insights. "
    "No spam, ever."
)

# Kit signup button
st.link_button(
    "📧 Sign up for updates", 
    "https://thelymphiesanctuary.kit.com/landing-pages/9219430",
    use_container_width=True,
    type="primary"
)

st.caption("You'll be taken to our secure signup page. Your privacy is respected.")

# ---------- Call to Action ----------
st.markdown("---")
st.markdown("### Ready to begin?")
if st.button("🌿 Go to today's log", type="primary", use_container_width=True):
    st.switch_page("pages/Daily_Log.py")

# ---------- PROMINENT DISCLAIMER (Bottom) ----------
st.markdown("---")
st.markdown("""
<div class="disclaimer-box">
    <p class="disclaimer-text">
        ⚠️ <strong>REMEMBER:</strong> The Lymphie Sanctuary is a self-tracking tool, not medical advice. 
        Always consult a qualified healthcare professional for medical guidance specific to your situation.
    </p>
</div>
""", unsafe_allow_html=True)

st.caption("© 2026 The Lymphie Sanctuary. All rights reserved.")