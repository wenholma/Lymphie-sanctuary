import streamlit as st

st.set_page_config(page_title="About", page_icon="👋", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif; color: #2C3E35; font-size: 16px;
    }
    h1, h2, h3 {
        font-family: 'Nunito', sans-serif; font-weight: 600; color: #1A3B2E;
    }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("👋 About The Lymphie Sanctuary")

st.markdown("""
### Hi, I'm Marece

I'm a data scientist living with a chronic condition. I built The Lymphie Sanctuary because I needed a tool that was simple, private, and actually helpful — not another subscription with a dashboard of ads.

This is a one‑person project, made with care for the lymphoedema community. I hope it brings you clarity and a bit more breathing room.

---

### Why I Built This

After years of tracking symptoms in spreadsheets and notebooks, I wanted:
- Something fast (2 minutes max).
- Something private (my health data is mine).
- Something that doesn't require a subscription.

The Sanctuary is my answer. It's local-first, meaning your data never leaves your device. It's a one-time purchase because you shouldn't have to rent a notebook.

---

### The Philosophy

**Gentle. Private. Yours.**

No leaderboards. No social sharing. No streaks to shame you. Just a quiet place to notice patterns in your own time.

---

### Support & Feedback

This app is actively developed based on user feedback. If you have ideas, bugs to report, or just want to say hi:

📧 **info@thelymphiesanctuary.com**

I read every email (though replies may take 2–3 days).

---

### Thank You

To everyone managing lymphoedema — you're doing enough already. I hope The Sanctuary makes tracking one small part of your day a little easier.

— Marece
""")