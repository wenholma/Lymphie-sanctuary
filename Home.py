import streamlit as st

st.set_page_config(
    page_title="The Lymphie Sanctuary",
    page_icon="🌿",
    layout="centered"
)

# Simple test - just the hero section
st.markdown("""
<div style="
    background: linear-gradient(145deg, #1a4d3a 0%, #2E7D5E 50%, #3a9b7a 100%);
    padding: 4rem 2rem;
    border-radius: 40px;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 25px 40px -15px rgba(0,0,0,0.4);
">
    <h1 style="font-size: 4.5rem; font-weight: 800; color: white; margin-bottom: 0.5rem;">
        🌿 The Lymphie Sanctuary
    </h1>
    <div style="font-size: 2rem; color: white; max-width: 700px; margin: 1rem auto;">
        Decode Your Symptoms. Reclaim Your Days.
    </div>
    <div style="margin-top: 2.5rem; display: inline-block; background: rgba(255,255,255,0.2); padding: 0.8rem 2.5rem; border-radius: 60px;">
        <span style="color: white; font-weight: 600;">✨ Trusted by early access lymphies worldwide</span>
    </div>
</div>
""", unsafe_allow_html=True)  # ← This MUST be here

st.write("If you see a beautiful green gradient box above with white text, the fix worked!")