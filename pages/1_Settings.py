import streamlit as st
import sys
import time

sys.path.append('.')
from utils.database import get_premium_status, set_premium_status

st.set_page_config(page_title="Settings & License | The Lymphie Sanctuary", page_icon="⚙️", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

from utils.styles import apply_styles
apply_styles()

st.title("⚙️ Settings & License")
st.caption("Your licence, your privacy, your control.")

STRIPE_PAYMENT_LINK = "https://buy.stripe.com/6oUdR97uK6NL1LE79u0oM01"
premium = get_premium_status()

# ─── LICENSE ACTIVATION ──────────────────────────────────────────
st.subheader("🔑 Lifetime Access")

if premium:
    st.success("✅ Lifetime Access active — thank you for supporting The Lymphie Sanctuary.")

    with st.expander("📱 Using a new device?"):
        st.markdown("""
        Your license key works on any device.
        1. Open The Lymphie Sanctuary on your new device.
        2. Go to **Settings & License**.
        3. Paste your license key and click **Activate**.
        """)

    with st.expander("📧 Lost your license key?"):
        st.markdown("""
        Your key was emailed to you after purchase.

        Search your inbox — including your **junk/spam folder** — for **"Lymphie Sanctuary"**.

        Still can't find it? Email **info@thelymphiesanctuary.com** with the email address you used to purchase and I'll resend it within 2–3 days.

        *Only your email and license key are stored on our secure server — no health data, ever.*
        """)

    if st.button("Remove License (for testing)", type="secondary"):
        set_premium_status(False)
        st.rerun()

else:
    # Prominent activation box at the top
    st.markdown("""
    <div class="activation-box">
        <h3 style="margin-top: 0; color: #1A3B2E;">🔑 Already purchased?</h3>
        <p style="margin-bottom: 0.5rem; font-weight: 600;">Enter your license key here to unlock everything.</p>
    </div>
    """, unsafe_allow_html=True)

    license_key = st.text_input(
        "License Key",
        placeholder="LKEY-XXXX-YYYY-ZZZZ",
        key="license_key_input"
    )

    st.markdown("""
    <div style="background: #F4F9F6; padding: 0.8rem 1.2rem; border-radius: 12px; margin-bottom: 0.5rem; font-size: 0.85rem; color: #4A6357; border: 1px solid #C2D9CD;">
        💡 <strong>Best method:</strong> Open your email and copy-paste the key directly into the box above.<br>
        ✍️ <strong>Typing manually?</strong> Use ALL CAPS with a dash after every 4 characters: <code style="font-size: 1rem; letter-spacing: 1px;">LKEY-XXXX-YYYY-ZZZZ</code><br>
        📱 <strong>On a phone:</strong> Double-tap Shift to lock CAPS → type 4 letters/numbers → tap dash → repeat.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔓 Activate License Key", type="primary", key="activate_btn"):
        if license_key:
            key = license_key.strip().upper().replace(" ", "").replace("\n", "").replace("\r", "")

            # All keys validated against the server — no test bypass
            with st.spinner("Validating your license key — please wait..."):
                try:
                    import requests
                    response = requests.post(
                        "https://lymphie-webhook.onrender.com/validate",
                        json={"license_key": key},
                        timeout=30
                    )
                    if response.status_code == 200 and response.json().get("valid"):
                        set_premium_status(True)
                        st.success("✅ License activated! You now have lifetime access.")
                        st.balloons()
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.error("""
❌ License key not recognised. Please try:
- Copying and pasting directly from your email
- Checking your junk/spam folder for the correct key
- Emailing info@thelymphiesanctuary.com if the problem continues
                        """)
                except Exception:
                    st.error("""
❌ Could not reach the validation server. Please check your internet connection and try again.
If the problem continues, email info@thelymphiesanctuary.com.
                    """)
        else:
            st.warning("Please enter your license key.")

    st.divider()

    # Purchase section — now below the activation box
    st.markdown("### 💳 Don't have a key yet?")
    st.markdown(f"""
    <div style="text-align: center; margin: 1.5rem 0;">
        <a href="{STRIPE_PAYMENT_LINK}" target="_blank" style="background-color: #0F766E; color: white; padding: 0.9rem 2.2rem; border-radius: 60px; text-decoration: none; font-weight: 700; font-size: 1.1rem; display: inline-block; font-family: 'Nunito', sans-serif; box-shadow: 0 2px 8px rgba(15,118,110,0.25);">
            💳 Purchase Lifetime Key — NZ$19.99
        </a>
    </div>
    <p style="text-align: center; font-size: 0.9rem; color: #6B7F74;">
        Secure one-time payment via Stripe. No subscription. No recurring charges. Ever.<br>
        Your license key will arrive by email within a few minutes.<br>
        <strong>Check your junk/spam folder</strong> if it doesn't appear in your inbox.
    </p>
    """, unsafe_allow_html=True)

    # New user flow guide — now at the bottom
    st.info("""
    **New here?** Here's the simple flow:\n
    **1.** Click "Purchase" above → pay via Stripe → check your email for a license key\n
    **2.** Copy and paste the key from your email into the box at the top → click "Activate"\n
    **3.** Go to Daily Log and start tracking!
    """)

# ─── PRIVACY & INFO ──────────────────────────────────────────────
st.divider()
st.markdown("""
<div style="background: #F4F9F6; padding: 0.8rem 1rem; border-radius: 12px; margin-bottom: 1rem; font-size: 0.9rem;">
    🔒 Your health data stays on your device. We only store your email + license key.
    <a href="/Privacy" target="_self">Privacy Policy →</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="green-box">
    <strong>📱 Use The Sanctuary like an app.</strong><br>
    <strong>iPhone:</strong> Tap the Share button (box with arrow) at the bottom of Safari → tap <strong>Add to Home Screen</strong>.<br>
    <strong>Android:</strong> Tap the three dots ⋮ in Chrome → tap <strong>Add to Home Screen</strong>.<br><br>
    <strong>🔒 Local‑first by design.</strong> Your logs never leave your device.
    No accounts. No servers. No tracking. You're not the product — you're the owner.<br><br>
    <strong>📥 Export regularly:</strong> Save your logs as a beautifully formatted Excel file. We recommend downloading a backup weekly.<br><br>
    <small>⚠️ Personal tracking only — not medical advice. Always work with your lymphoedema therapist or GP.</small>
</div>
""", unsafe_allow_html=True)

# ─── DATA MANAGEMENT ─────────────────────────────────────────────
st.divider()
with st.expander("🗑️ Delete Your Local Data", expanded=False):
    st.markdown("""
    Your symptom logs are stored **only in this browser** on this device.
    Use this section if you want to permanently erase all logs from this device.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.warning("⚠️ Clearing browser cache will also erase all logs.")
    with col2:
        st.info("📥 Export a backup first from the **Export** page.")
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
                if "log_df" in st.session_state:
                    del st.session_state.log_df
                st.session_state['confirm_delete'] = False
                st.success("All data has been erased.")
                st.rerun()
        with col2:
            if st.button("❌ Cancel"):
                st.session_state['confirm_delete'] = False
                st.rerun()

# ─── GO TO DAILY LOG ──────────────────────────────────────────────
st.divider()
st.markdown("### 📝 Ready to start logging?")
if st.button("Go to Your Daily Log", use_container_width=True):
    st.switch_page("pages/2_Daily_Log.py")

# ─── FAQS ─────────────────────────────────────────────────────────
st.divider()
with st.expander("❓ Frequently Asked Questions", expanded=False):
    st.markdown("**📱 How do I use this on my phone daily?**")
    st.markdown("""
    **iPhone:** Tap the Share button (box with arrow) at the bottom of Safari → tap **Add to Home Screen** → tap **Add**.
    **Android:** Tap the three dots ⋮ in Chrome → tap **Add to Home Screen**.
    """)
    st.markdown("**🔑 How do license keys work?**")
    st.markdown("""
    Your key is emailed after purchase. It works on any device — paste it into
    Settings & License and click Activate. It never expires.
    """)
    st.markdown("**💾 What happens if I clear my browser cache?**")
    st.markdown("""
    Your health logs will be permanently deleted from this device.
    Export an Excel backup regularly from the Export page.
    """)
    st.markdown("**📧 I didn't receive my license key email.**")
    st.markdown("""
    Check your junk/spam folder and search for 'Lymphie Sanctuary'.
    If you still can't find it, email info@thelymphiesanctuary.com.
    """)

st.divider()
st.caption("📧 Need help? Contact: **info@thelymphiesanctuary.com**")

# ─── BRAND FOOTER ────────────────────────────────────────────────
st.divider()
st.markdown("""
<div class="brand-footer">
    Does your workplace support staff with lymphoedema?
    <a href="https://www.lymphatwork.com" target="_blank">Lymphoedema at Work →</a>
</div>
""", unsafe_allow_html=True)