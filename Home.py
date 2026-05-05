import streamlit as st

st.set_page_config(
    page_title="The Lymphie Sanctuary",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="auto"
)

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #2C3E35;
        font-size: 16px;
        line-height: 1.6;
    }
    h1, h2, h3, h4 {
        font-family: 'Nunito', sans-serif;
        font-weight: 600;
        color: #1A3B2E;
        letter-spacing: -0.02em;
    }
    h1 { font-size: 2.2rem; }
    h2 { font-size: 1.6rem; }
    h3 { font-size: 1.3rem; }

    .hero {
        text-align: center;
        padding: 2.5rem 1rem 1.5rem 1rem;
        background: linear-gradient(180deg, #F4F9F6 0%, #FFFFFF 100%);
        border-radius: 24px;
        margin-bottom: 2rem;
    }
    .hero .welcome {
        font-family: 'Nunito', sans-serif;
        font-size: 1rem;
        color: #6B7F74;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.5rem;
    }
    .hero h1 {
        font-size: 2.6rem;
        font-weight: 700;
        color: #1A3B2E;
        margin-bottom: 0.3rem;
    }
    .hero .subhead {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: #4A6357;
        font-weight: 400;
        margin-bottom: 0.2rem;
    }
    .hero .tagline {
        color: #6B7F74;
        font-style: italic;
        margin-top: 0.3rem;
        font-size: 0.95rem;
    }

    .center-text { text-align: center; }

    .green-box {
        background: linear-gradient(135deg, #EAF3EE 0%, #D4E8DC 100%);
        border-left: 6px solid #2E7D5E;
        padding: 1.4rem 1.8rem;
        border-radius: 20px;
        margin: 2rem 0 1.5rem 0;
        box-shadow: 0 4px 12px rgba(46, 125, 94, 0.06);
    }
    .green-box strong {
        color: #1A3B2E;
        font-family: 'Nunito', sans-serif;
        font-size: 1.05rem;
    }

    .feature-card {
        background: linear-gradient(180deg, #FFFFFF 0%, #FAFCFB 100%);
        border-radius: 24px;
        padding: 2rem 1.4rem;
        box-shadow: 0 8px 24px rgba(0, 20, 10, 0.04);
        text-align: center;
        border: 1px solid #E2EDE6;
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(0, 20, 10, 0.08);
    }
    .feature-icon { font-size: 2rem; margin-bottom: 0.8rem; }
    .feature-title {
        font-family: 'Nunito', sans-serif;
        font-weight: 700;
        font-size: 1.2rem;
        color: #1A3B2E;
        margin-bottom: 0.4rem;
    }
    .feature-desc { color: #4A6357; font-size: 0.95rem; line-height: 1.5; }

    .cta-block {
        background: linear-gradient(135deg, #EAF3EE 0%, #D4E8DC 100%);
        padding: 2.5rem 2rem;
        border-radius: 28px;
        text-align: center;
        margin: 2.5rem 0 1rem 0;
        border: 1px solid #C2D9CD;
        box-shadow: 0 8px 24px rgba(46, 125, 94, 0.08);
    }
    .cta-title {
        font-family: 'Nunito', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #1A3B2E;
        margin-bottom: 0.3rem;
    }
    .price-large {
        font-family: 'Nunito', sans-serif;
        font-size: 2.6rem;
        font-weight: 700;
        color: #1E5F45;
        margin: 0.3rem 0;
    }
    .price-sub { color: #4A6357; margin-bottom: 1.5rem; font-size: 1rem; }

    .stButton > button {
        font-family: 'Nunito', sans-serif !important;
        background-color: #2E7D5E !important;
        color: white !important;
        border-radius: 60px !important;
        padding: 0.9rem 2.2rem !important;
        border: none !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 14px rgba(46, 125, 94, 0.15);
        transition: all 0.2s ease;
        min-height: 48px;
    }
    .stButton > button:hover {
        background-color: #1E5F45 !important;
        box-shadow: 0 6px 20px rgba(46, 125, 94, 0.25);
        transform: scale(1.02);
    }

    .streamlit-expanderHeader {
        font-family: 'Nunito', sans-serif;
        font-weight: 600;
        color: #1A3B2E;
        font-size: 1rem;
    }

    .footer {
        text-align: center;
        margin-top: 4rem;
        padding-top: 1.5rem;
        border-top: 1px solid #DDE9E2;
        font-size: 0.85rem;
        color: #6B7F74;
    }
    .footer a { color: #2E7D5E; text-decoration: none; }

    @media (prefers-reduced-motion: reduce) {
        * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# HERO
# ------------------------------------------------------------------------------
st.markdown("""
<div class="hero">
    <div class="welcome">Welcome to</div>
    <h1>🌿 The Lymphie Sanctuary</h1>
    <div class="subhead">A digital notebook for managing your lymphoedema.</div>
    <div class="tagline">Your private daily symptom journal.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="center-text">

### Stop guessing. Start noticing.
A **2‑minute check‑in** that helps you see connections between your body, your care, and your life.  
No accounts. No judgement. Just clarity.

</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
Your daily log helps you check in with **9 key lymphoedema symptoms** each day, so you can start building a clear record of what affects you.
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **🦵 Limb sensations**  
    Heaviness, tightness, pain — simple 0–10 scales.

    **👁️ Appearance vs baseline**  
    Note changes in swelling or skin texture.

    **📍 Affected areas**  
    Mark exactly where you felt symptoms.
    """)
with col2:
    st.markdown("""
    **🧦 Compression & self‑care**  
    Log what you wore and for how long.

    **🍽️ Triggers & wellness**  
    Diet, stress, sleep, energy — all in one place.

    **📝 Reflections**  
    Space for wins, challenges, and notes.
    """)

st.markdown("---")
st.subheader("✨ Everything included for life")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📋</div>
        <div class="feature-title">9 Key Symptoms</div>
        <div class="feature-desc">Track heaviness, pain, appearance, triggers, compression, and more — all in one place.</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📥</div>
        <div class="feature-title">Excel Export & Backup</div>
        <div class="feature-desc">One‑click download, beautifully formatted for your care team.</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌱</div>
        <div class="feature-title">Gentle & Private</div>
        <div class="feature-desc">No ads. No tracking. No external servers. Just you and your data.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("📖 How The Sanctuary Works")

st.markdown("""
<div style="background: linear-gradient(135deg, #F4F9F6 0%, #EAF3EE 100%); padding: 1.5rem 2rem; border-radius: 20px; margin: 1rem 0; border: 1px solid #C2D9CD;">

<h4 style="margin-top: 0;">Your simple 4‑step journey 🌿</h4>

**Step 1 — You're here.** This is the Home page. When you're ready, go to **Settings** to make your one‑time purchase.

**Step 2 — Unlock.** Pay <strong>$9.99 once</strong> via Stripe on the Settings page. Check your email for your license key, paste it in, and activate. No subscriptions. No recurring charges. Ever.

**Step 3 — Log.** Head to **Daily Log** and spend 2 minutes checking in with your body. Track 9 key lymphoedema symptoms with simple sliders and checkboxes.

**Step 4 — Export.** Go to **Export** anytime to download a beautifully formatted Excel file. Share it with your CLT, doctor, or keep it for your own records.

</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **💾 Your Data Lives Here**
    
    - Everything saves to **this browser only**
    - Like a private notebook on your phone
    - We never see, store, or touch your logs
    - Clear your cache? Data is gone — so export regularly
    
    *You're in complete control. Always.*
    """)
with col2:
    st.markdown("""
    **🔑 Your License Stays With You**
    
    - Tied to your **email**, not your device
    - Use it on your phone, tablet, or computer
    - Lost it? Search your inbox for "Lymphie Sanctuary"
    - One purchase = lifetime access on any device
    
    *No accounts. No passwords. Just a key.*
    """)

with st.expander("❓ What happens if I get a new phone or clear my cache?"):
    st.markdown("""
    **If you clear your browser cache:** Your logs are removed. ✅ **Export an Excel backup regularly** (one click from Export page).
    **If you get a new phone:** 1. On new device, go to **Settings** → paste your license key. 2. Keep a copy of your exported Excel file to reference previous logs.
    **Bottom line:** You own your data. Export regularly for peace of mind.
    """)
with st.expander("🔒 Why no accounts or passwords?"):
    st.markdown("Traditional apps store your health data on their servers. That means they can see it, sell it, or lose it in a breach. **The Sanctuary is local‑first.** Your logs never leave your device.")
with st.expander("📱 How do I use this daily like an app?"):
    st.markdown("**iPhone:** Tap Share → Add to Home Screen → Name it 'Sanctuary'. **Android:** Tap ⋮ → Add to Home Screen.")
with st.expander("📧 Lost your license key?"):
    st.markdown("""
    Search your inbox for "Lymphie Sanctuary" to find your license key email.
    
    Still can't find it? Email **info@thelymphiesanctuary.com** with the email you used to purchase, and I'll resend your key.
    """)

# ------------------------------------------------------------------------------
# PRIVACY BLURB
# ------------------------------------------------------------------------------
st.markdown("""
<div style="background: #F4F9F6; padding: 1.2rem 1.5rem; border-radius: 16px; margin: 1.5rem 0; border: 1px solid #C2D9CD; font-size: 0.95rem;">
    <strong>🔒 We separate your health logs from your purchase.</strong><br>
    Your logs stay only on your device. We only store your email and license key so we can deliver and validate your purchase.<br>
    In plain terms: <em>We know you bought a license. We have no idea what you log in it.</em><br>
    <a href="/Privacy" target="_self">Privacy details →</a>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# CTA
# ------------------------------------------------------------------------------
st.markdown("""
<div class="cta-block">
    <div class="cta-title">Ready to own your data?</div>
    <div class="price-large">$9.99 USD</div>
    <div class="price-sub">One‑time payment. Lifetime access. <a href="/Terms" target="_self">Simple, transparent terms.</a></div>
</div>
""", unsafe_allow_html=True)

# Medical disclaimer — unmissable
st.markdown("""
<div style="text-align: center; margin: 1rem 0 0.5rem 0; font-weight: 600; color: #1A3B2E; font-size: 1rem;">
    ⚠️ This is a personal tracking tool, not medical advice.
</div>
""", unsafe_allow_html=True)

# New purchaser banner
st.info("🎉 **Just purchased?** Go to **Settings** → paste your license key → you're in!")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌿 Get Lifetime Key & Start Logging", width='stretch'):
        st.switch_page("pages/1_Settings.py")

st.markdown("""
<div class="footer">
    © 2026 The Lymphie Sanctuary. All rights reserved.<br>
    <a href="/Privacy" target="_self">Privacy Policy</a> · 
    <a href="/Terms" target="_self">Terms of Service</a> · 
    <a href="/About" target="_self">About</a>
</div>
""", unsafe_allow_html=True)