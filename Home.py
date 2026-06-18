import streamlit as st
import os

st.set_page_config(
    page_title="The Lymphie Sanctuary",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="auto"
)

# Google Search Console verification
st.markdown("""
    <meta name="google-site-verification" content="googleb2320874bc4a1e9a" />
""", unsafe_allow_html=True)

# Detect if running on Streamlit Cloud (redirect to Render)
if "streamlit.app" in os.environ.get("STREAMLIT_SERVER_URL", ""):
    st.markdown("""
    <meta http-equiv="refresh" content="0; url=https://lymphie-sanctuary-app.onrender.com">
    <div style="text-align: center; padding: 2rem; font-family: sans-serif;">
        <p>Redirecting to our always-on site...</p>
        <p><a href="https://lymphie-sanctuary-app.onrender.com">Click here</a> if nothing happens.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# … the rest of your home page remains exactly the same …