import streamlit as st

st.set_page_config(page_title="About | The Lymphie Sanctuary", page_icon="👋", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #2C3E35; font-size: 16px; line-height: 1.7; }
    h1, h2, h3 { font-family: 'Nunito', sans-serif; font-weight: 600; color: #1A3B2E; }
    h1 { font-size: 2rem; }
    h2 { font-size: 1.5rem; margin-top: 2rem; }
    .signature { font-style: italic; color: #4A6357; margin-top: 2rem; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("👋 About The Lymphie Sanctuary")

st.markdown("""
### Hi, I'm Marece.

I'm a data scientist originally from South Africa, now living in Aotearoa New Zealand. I live with left‑leg lymphoedema — a condition that began after a long‑haul flight about eight years ago and has gradually progressed over time. After returning to New Zealand, I developed persistent swelling in my left leg and was assessed by a vascular surgeon, who ruled out DVT and confirmed lymphoedema. Since then, I've managed it with compression and self‑care, and I've been fortunate not to experience infections.

Like many people with lymphoedema, I deal with the everyday realities: bulk, heaviness, tightness, and the constant negotiation between comfort and compression. My experience is fairly typical — no dramatic trigger, no underlying trauma or illness, just a condition that arrived quietly and stayed.

I built The Lymphie Sanctuary because I needed a tool that was simple, private, and genuinely useful — not another subscription, not another dashboard full of ads. Just a calm place to keep track of what my body is doing.

This is a one‑person project, made with care for the lymphoedema community. I hope it brings you clarity and a bit more breathing room.

---

### Why I Built This

After years of tracking symptoms in spreadsheets and notebooks, I wanted:
- Something fast (2 minutes max).
- Something private (my health data is mine).
- Something that doesn't require a subscription.

The Sanctuary is my answer. It's local‑first, meaning your data never leaves your device. It's a one‑time purchase because you shouldn't have to rent a notebook.

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

<div class="signature">— Marece</div>
""")