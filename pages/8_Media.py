import streamlit as st

st.set_page_config(page_title="Media | The Lymphie Sanctuary", page_icon="🎙️", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #2C3E35; font-size: 16px; }
    h1, h2, h3 { font-family: 'Nunito', sans-serif; font-weight: 600; color: #1A3B2E; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("🎙️ Media")

st.markdown("""
### Radio Interview — June 2026

I spoke about living with lymphoedema and building The Lymphie Sanctuary.

<div style="text-align: center; margin: 2rem 0;">
    <a href="https://accessmedia.nz/player?EID=87547ae2-cca2-4387-8619-ed10b7ff3599&audioOnlyMode=true" 
       target="_blank" 
       style="background-color: #2E7D5E; color: white; padding: 0.9rem 2.2rem; border-radius: 60px; text-decoration: none; font-weight: 700; font-size: 1.1rem; display: inline-block; font-family: 'Nunito', sans-serif;">
        🎧 Listen to the Interview (25 min)
    </a>
</div>

*Click the button above to open the interview in a new tab.*

---

### About The Lymphie Sanctuary

The Lymphie Sanctuary is a private, 2‑minute daily symptom journal for people managing lymphoedema. Built by a data scientist who lives with the condition. NZ$19.99 once, for life. No subscriptions. No accounts. Your data never leaves your device.

🌿 [thelymphiesanctuary.com](https://thelymphiesanctuary.com)
""")