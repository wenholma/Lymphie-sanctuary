import streamlit as st
import sys
import time

sys.path.append('.')
from utils.database import get_premium_status, set_premium_status

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="centered")

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

STRIPE_PAYMENT_LINK = "https://buy.stripe.com/test_4gM28s6GmfbO2S6cUc0sU00"
premium = get_premium_status()

# ------------------------------------------------------------------------------
# STEP-BY-STEP FOR NEW USERS
# ------------------------------------------------------------------------------
if not premium:
    st.info("""
    **New here?** Here's the simple flow:
    **1.** Click "Purchase" below → pay via Stripe → check your email for a license key
    **2.** Paste the key in the box below → click "Activate"
    **3.** Go to Daily Log and start tracking!
    """)

# ------------------------------------------------------------------------------
# PRIVACY BLURB
# ------------------------------------------------------------------------------
st.markdown("""
<div style="background: #F4F9F6; padding: 0.8rem 1rem; border-radius: 12px; margin-bottom: 1rem; font-size: 0.9rem;">
    🔒 Your health data stays on your device. We only store email + license key.
    <a href="/Privacy" target="_self">Privacy Policy</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="green-box">
    <strong>📱 Use The Sanctuary like an app.</strong><br>
    Tap <strong>Share → Add to Home Screen</strong> on your phone. It'll appear on your home screen and open like a native app—no App Store needed.<br><br>
    <strong>🔒 Local‑first by design.</strong> Your logs never leave your device.<br>
    No accounts. No servers. No tracking. You're not the product — you're the owner.<br><br>
    <strong>📥 Export regularly:</strong> Save your logs as a beautifully formatted Excel file. We recommend downloading a backup weekly.<br><br>
    <small>⚠️ This tool is for personal tracking only. It is not medical advice. Always consult your healthcare provider.</small>
</div>
""", unsafe_allow_html=True)

st.subheader("🔑 Lifetime Access")

if premium:
    st.success("✅ Lifetime Access active — thank you for supporting The Lymphie Sanctuary.")
    with st.expander("📱 Using a new device?"):
        st.markdown("Your license is tied to your email, not this device. 1. On your new device, open The Lymphie Sanctuary. 2. Go to Settings. 3. Paste your license key and click Activate.")
    with st.expander("📧 Lost your license key?"):
        st.markdown("""
        Your license key was emailed to you after purchase. **Search your inbox** for "Lymphie Sanctuary" to find it.
        Still can't find it? Email **info@thelymphiesanctuary.com** with the email address you used to purchase, and I'll look up your key and resend it.
        *Note: Only your email and license key are stored on a secure server to enable key validation. No health data or personal logs are ever stored.*
        """)
    if st.button("Remove License (for testing)", type="secondary"):
        set_premium_status(False)
        st.rerun()
else:
    st.info("🔓 Activate your Lifetime Access key to unlock Excel export and trends.")
    st.markdown("### 💳 Purchase Lifetime Access — $0.50 USD (Test)")
    st.markdown(f"""
    <div style="text-align: center; margin: 1.5rem 0;">
        <a href="{STRIPE_PAYMENT_LINK}" target="_blank" style="background-color: #2E7D5E; color: white; padding: 0.9rem 2.2rem; border-radius: 60px; text-decoration: none; font-weight: 700; font-size: 1.1rem; display: inline-block; font-family: 'Nunito', sans-serif;">
            💳 Purchase Lifetime Key ($0.50 USD Test)
        </a>
    </div>
    <p style="text-align: center; font-size: 0.9rem; color: #6B7F74;">Test payment via Stripe. You'll receive your license key by email.</p>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("**Already purchased?** Paste your license key below.")
    
    license_key = st.text_input("License Key", placeholder="e.g., LKEY-XXXX-YYYY-ZZZZ", key="license_key_input")
    
    if st.button("🔓 Activate License Key", type="primary", key="activate_btn"):
        if license_key:
            key = license_key.strip()
            if key == "TEST-1234-ABCD-5678":
                set_premium_status(True)
                st.success("✅ License activated! You now have lifetime access.")
                st.balloons()
                time.sleep(2)
                st.rerun()
            try:
                import requests
                response = requests.post(
                    "https://lymphie-webhook.onrender.com/validate",
                    json={"license_key": key},
                    timeout=10
                )
                if response.status_code == 200 and response.json().get("valid"):
                    set_premium_status(True)
                    st.success("✅ License activated! You now have lifetime access.")
                    st.balloons()
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("❌ Invalid license key. Please check your email and try again.")
            except Exception as e:
                st.error("❌ Could not validate key. Please check your internet connection and try again.")
        else:
            st.warning("Please enter a license key.")

# ------------------------------------------------------------------------------
# DATA MANAGEMENT (collapsed)
# ------------------------------------------------------------------------------
st.divider()
with st.expander("🗂️ Data Management (advanced)", expanded=False):
    st.markdown("All logs are stored **only in this browser's storage**.")
    col1, col2 = st.columns(2)
    with col1: st.warning("⚠️ Clearing browser cache will erase all logs.")
    with col2: st.info("📥 Export regularly from the **Export** page to keep a backup.")
    if st.button("🗑️ Delete ALL Local Data", type="secondary"):
        st.session_state['confirm_delete'] = True
    if st.session_state.get('confirm_delete', False):
        st.error("⚠️ This cannot be undone. Are you sure?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Yes, delete everything"):
                from utils.database import delete_all_logs
                delete_all_logs()
                set_premium_status(False)
                if "log_df" in st.session_state: del st.session_state.log_df
                st.session_state['confirm_delete'] = False
                st.success("All data has been erased.")
                st.rerun()
        with col2:
            if st.button("❌ Cancel"): st.session_state['confirm_delete'] = False; st.rerun()

# ------------------------------------------------------------------------------
# GO TO DAILY LOG
# ------------------------------------------------------------------------------
st.divider()
st.markdown("### 📝 Ready to start logging?")
if st.button("Go to Your Daily Log", width='stretch'):
    st.switch_page("pages/2_Daily_Log.py")

# ------------------------------------------------------------------------------
# FAQS (collapsed)
# ------------------------------------------------------------------------------
st.divider()
with st.expander("❓ Frequently Asked Questions", expanded=False):
    with st.container():
        st.markdown("**📱 How do I use this on my phone daily?**")
        st.markdown("iPhone: Tap Share → Add to Home Screen. Android: Tap ⋮ → Add to Home Screen.")
        st.markdown("**🔑 How do license keys work?**")
        st.markdown("Sent to your email after purchase. Tied to you, not your device. Valid forever.")
        st.markdown("**💾 What happens if I clear my browser cache?**")
        st.markdown("Your logs will be permanently deleted. Export Excel backup weekly.")

st.divider()
st.caption("📧 Need help? Contact: **info@thelymphiesanctuary.com**")