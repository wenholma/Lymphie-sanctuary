import streamlit as st
import sys
import time

sys.path.append('.')
from utils.database import get_premium_status, set_premium_status

st.set_page_config(page_title="Settings & License | The Lymphie Sanctuary", page_icon="⚙️", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #2C3E35; font-size: 16px; }
    h1, h2, h3, h4 { font-family: 'Nunito', sans-serif; font-weight: 600; color: #1A3B2E; }
    .stButton > button { font-family: 'Nunito', sans-serif !important; background-color: #2E7D5E !important; color: white !important; border-radius: 60px !important; padding: 0.9rem 2.2rem !important; border: none !important; font-weight: 700 !important; font-size: 1.1rem !important; min-height: 48px; }
    .stButton > button[kind="secondary"] { background-color: #FFFFFF !important; color: #2E7D5E !important; border: 2px solid #2E7D5E !important; }
    .stTextInput > div > div > input { border-radius: 12px !important; border: 2px solid #E2EDE6 !important; padding: 0.8rem 1rem !important; font-size: 1rem !important; min-height: 48px; }
    .green-box { background: linear-gradient(135deg, #EAF3EE 0%, #D4E8DC 100%); border-left: 6px solid #2E7D5E; padding: 1.4rem 1.8rem; border-radius: 20px; margin: 2rem 0 1.5rem 0; }
    @media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("⚙️ Settings & License")

STRIPE_PAYMENT_LINK = "https://buy.stripe.com/28E4gz4iyfkhfCu0L60oM00"
premium = get_premium_status()

# ------------------------------------------------------------------------------
# NEW USER FLOW GUIDE
# ------------------------------------------------------------------------------
if not premium:
    st.info("""
    **New here?** Here's the simple flow:
    **1.** Click "Purchase" below → pay via Stripe → check your email for a license key
    **2.** Copy and paste the key from your email into the box below → click "Activate"
    **3.** Go to Daily Log and start tracking!
    """)

# ------------------------------------------------------------------------------
# PRIVACY BLURB
# ------------------------------------------------------------------------------
st.markdown("""
<div style="background: #F4F9F6; padding: 0.8rem 1rem; border-radius: 12px; margin-bottom: 1rem; font-size: 0.9rem;">
    🔒 Your health data stays on your device. We only store your email + license key.
    <a href="/Privacy" target="_self">Privacy Policy →</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="green-box">
    <strong>📱 Use The Sanctuary like an app.</strong><br>
    Tap <strong>Share → Add to Home Screen</strong> on your phone. It'll appear on your home screen and open like a native app — no App Store needed.<br><br>
    <strong>🔒 Local‑first by design.</strong> Your logs never leave your device.<br>
    No accounts. No servers. No tracking. You're not the product — you're the owner.<br><br>
    <strong>📥 Export regularly:</strong> Save your logs as a beautifully formatted Excel file. We recommend downloading a backup weekly.<br><br>
    <small>⚠️ This tool is for personal tracking only. It is not medical advice. Always consult your healthcare provider.</small>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# LIFETIME ACCESS
# ------------------------------------------------------------------------------
st.subheader("🔑 Lifetime Access")

if premium:
    st.success("✅ Lifetime Access active — thank you for supporting The Lymphie Sanctuary.")
    with st.expander("📱 Using a new device?"):
        st.markdown("""
        Your license key works on any device.
        1. Open The Lymphie Sanctuary on your new device
        2. Go to **Settings & License**
        3. Paste your license key and click **Activate**
        """)
    with st.expander("📧 Lost your license key?"):
        st.markdown("""
        Your key was emailed to you after purchase — search your inbox (including **junk/spam**) for **"Lymphie Sanctuary"**.

        Still can't find it? Email **info@thelymphiesanctuary.com** with the email address you used to purchase and I'll resend it within 2–3 days.

        *Only your email and license key are stored on our secure server — no health data, ever.*
        """)
    if st.button("Remove License (for testing)", type="secondary"):
        set_premium_status(False)
        st.rerun()

else:
    st.info("🔓 Activate your Lifetime Access key to unlock the Daily Log, Excel export, and trends.")

    st.markdown("### 💳 Purchase Lifetime Access — $9.99 USD")
    st.markdown(f"""
    <div style="text-align: center; margin: 1.5rem 0;">
        <a href="{STRIPE_PAYMENT_LINK}" target="_blank" style="background-color: #2E7D5E; color: white; padding: 0.9rem 2.2rem; border-radius: 60px; text-decoration: none; font-weight: 700; font-size: 1.1rem; display: inline-block; font-family: 'Nunito', sans-serif;">
            💳 Purchase Lifetime Key ($9.99 USD)
        </a>
    </div>
    <p style="text-align: center; font-size: 0.9rem; color: #6B7F74;">
        Secure payment via Stripe. Your license key will arrive by email — check junk/spam if it doesn't appear within a few minutes.
    </p>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("**Already purchased?** Copy and paste your license key from your email below.")
    st.caption("💡 Tip: Copy and paste directly from the email — don't type it manually to avoid errors.")

    license_key = st.text_input(
        "License Key",
        placeholder="LKEY-XXXX-YYYY-ZZZZ",
        key="license_key_input"
    )

    if st.button("🔓 Activate License Key", type="primary", key="activate_btn"):
        if license_key:
            # Clean the key — strip spaces, force uppercase, remove accidental newlines
            key = license_key.strip().upper().replace(" ", "").replace("\n", "").replace("\r", "")

            # Test key shortcut
            if key == "TEST-1234-ABCD-5678" or key == "TEST1234ABCD5678":
                set_premium_status(True)
                st.success("✅ License activated! You now have lifetime access.")
                st.balloons()
                time.sleep(2)
                st.rerun()