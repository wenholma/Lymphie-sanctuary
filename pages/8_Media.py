import streamlit as st

st.set_page_config(page_title="Media | The Lymphie Sanctuary", page_icon="🎙️", layout="centered")

from utils.nav import mobile_nav
mobile_nav()
from utils.styles import apply_styles
apply_styles()
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    :root {
        --teal: #0F766E;
        --ink: #0F1F1B;
        --tint: #EAF6F1;
        --body-text: #22302B;
        --muted-text: #647A73;
        --mint: #4FE3BC;
    }
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--body-text);
        font-size: 16px;
        background-color: #FAFCFA;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Nunito', sans-serif;
        font-weight: 600;
        color: var(--ink);
    }
    .stCaption, .stMarkdown p, li, div {
        color: var(--body-text);
    }
    .stCaption { color: var(--muted-text); }
    .highlight-box {
        background: linear-gradient(135deg, var(--tint) 0%, #FFFFFF 100%);
        border-left: 6px solid var(--teal);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 0.8rem 0;
    }
    .stButton button, .stDownloadButton button, .stForm button[type="submit"] {
        background-color: var(--teal) !important;
        color: white !important;
        font-weight: 700 !important;
        font-family: 'Nunito', sans-serif !important;
        border: none !important;
        border-radius: 60px !important;
        padding: 0.9rem 2.2rem !important;
        font-size: 1.1rem !important;
        min-height: 48px !important;
        box-shadow: 0 2px 8px rgba(15, 118, 110, 0.25) !important;
        transition: all 0.2s ease !important;
        letter-spacing: 0.3px !important;
        cursor: pointer !important;
    }
    .stButton button:hover, .stDownloadButton button:hover, .stForm button[type="submit"]:hover {
        background-color: #0D5F58 !important;
        box-shadow: 0 4px 16px rgba(15, 118, 110, 0.35) !important;
        transform: translateY(-2px);
    }
    .stButton button:active, .stDownloadButton button:active {
        transform: scale(0.97);
        box-shadow: 0 1px 4px rgba(15, 118, 110, 0.2) !important;
    }
    a { color: var(--teal); text-decoration: none; font-weight: 500; }
    a:hover { color: #0D5F58; text-decoration: underline; }
    .brand-footer {
        text-align: center;
        padding: 1.5rem 0 0.5rem 0;
        font-size: 0.85rem;
        color: var(--muted-text);
        border-top: 1px solid #e0e8e0;
        margin-top: 2rem;
    }
    .brand-footer a { color: var(--teal); font-weight: 500; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("🎙️ Media")

st.markdown("""
### Radio Interview — June 2026

In June 2026 I spoke with Access Media about what it's actually like to live with lymphoedema,
why I built The Lymphie Sanctuary, and what patient-led innovation can do for chronic illness care.

If you've ever sat in a clinic appointment and genuinely couldn't remember your week —
or felt the invisible weight of managing something no one else can see —
this one's for you.
""")

# Working button using st.link_button (native Streamlit, always works)
st.link_button(
    label="🎧 Listen to the Interview (25 min)",
    url="https://accessmedia.nz/player?EID=87547ae2-cca2-4387-8619-ed10b7ff3599&audioOnlyMode=true",
    use_container_width=True
)

st.caption("Click the button above to open the interview in a new tab.")

st.markdown("---")

st.subheader("📋 Interview Highlights")

st.markdown("""
<div class="highlight-box">
<strong>🩺 The "Vague Recall" Clinical Gap</strong><br>
Patients arrive at appointments unable to remember their week; the app provides concrete data for clinical conversations.
</div>

<div class="highlight-box">
<strong>🔒 Data Sovereignty &amp; Privacy-First Architecture</strong><br>
Health data never leaves the user's device; the server stores only email and license keys; built for complete privacy.
</div>

<div class="highlight-box">
<strong>💚 Lived-Experience Design</strong><br>
Every feature shaped by personal lymphoedema management; built by someone who lives the condition daily.
</div>

<div class="highlight-box">
<strong>🧠 The Invisible Cognitive Load</strong><br>
Constant mental management of garments, diet, travel, heat; a full-time job invisible to healthcare providers.
</div>

<div class="highlight-box">
<strong>🚀 Patient-Led Innovation</strong><br>
Faster, more empathetic, more usable solutions emerge when patients design for their own conditions.
</div>

<div class="highlight-box">
<strong>🌱 Self-Compassion as a Feature</strong><br>
Daily gentle reminder that "you are doing enough"; no streaks, no leaderboards, no pressure.
</div>

<div class="highlight-box">
<strong>🌍 Universal Need</strong><br>
Built for NZ but reaching global community; the need transcends borders.
</div>

<div class="highlight-box">
<strong>📈 From Symptom Tracker to Empowerment Platform</strong><br>
Visual trends, flare detection, exportable clinic summaries, therapist-facing tools, anonymised research contribution.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
### About The Lymphie Sanctuary

The Lymphie Sanctuary is a private, 2‑minute daily symptom journal for people managing lymphoedema. Built by a data scientist who lives with the condition. NZ$19.99 once, for life. No subscriptions. No accounts. Your data never leaves your device.

🌿 [thelymphiesanctuary.com](https://thelymphiesanctuary.com)
""")

# ─── BRAND FOOTER ────────────────────────────────────────────────
st.divider()
st.markdown("""
<div class="brand-footer">
    Does your workplace support staff with lymphoedema?
    <a href="https://www.lymphatwork.com" target="_blank">Lymphoedema at Work →</a>
</div>
""", unsafe_allow_html=True)