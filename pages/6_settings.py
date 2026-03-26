import streamlit as st
import sys
sys.path.append('.')
from utils.local_storage import load_from_localstorage, save_to_localstorage, remove_from_localstorage

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="centered")

st.title("⚙️ Settings & License")

# --- License key section ---
st.subheader("🔑 Lifetime Access")

premium = load_from_localstorage("premium", False)

if premium:
    st.success("✅ You have Lifetime Access! Thank you for supporting The Sanctuary.")
    if st.button("Remove License (for testing)", type="secondary"):
        remove_from_localstorage("premium")
        st.experimental_rerun()
else:
    st.info("✨ Unlock the CSV Export feature with a one‑time payment of $25.")
    st.markdown("""
    **What you get:**
    - Unlimited CSV exports of your logs.
    - Lifetime access – no subscriptions.
    - Support independent development of The Sanctuary.
    """)

    # Replace this with your actual Lemon Squeezy link later
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <a href="https://your-lemon-squeezy-link.com" target="_blank" style="background-color: #4f6b6a; color: white; padding: 0.8rem 2rem; border-radius: 40px; text-decoration: none; font-weight: 600;">
            💳 Get Lifetime Key ($25)
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Already have a key?** Paste it below and click Activate.")

    license_key = st.text_input("License Key", placeholder="e.g., LKEY-XXXX-YYYY-ZZZZ")
    if st.button("Activate Key"):
        # For testing, we use a hardcoded key. Replace with real validation later.
        valid_keys = ["TEST-1234-ABCD"]
        if license_key in valid_keys:
            save_to_localstorage("premium", True)
            st.success("License activated! You can now export your data.")
            st.experimental_rerun()
        else:
            st.error("Invalid key. Please check and try again.")

# --- Data management ---
st.subheader("🗂️ Data Management")
if st.button("⚠️ Delete ALL local data (logs)"):
    remove_from_localstorage("lymphie_logs")
    if "log_df" in st.session_state:
        del st.session_state.log_df
    st.success("All logs have been erased from this browser.")
    st.experimental_rerun()