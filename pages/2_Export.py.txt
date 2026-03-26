import streamlit as st
import pandas as pd
import sys
sys.path.append('.')
from utils.local_storage import load_from_localstorage, save_to_localstorage

st.set_page_config(page_title="Export & History", page_icon="📊")

st.title("📊 Export & History")
st.markdown("View your past entries and download your data.")

# Load data
if "log_df" not in st.session_state:
    data = load_from_localstorage("lymphie_logs", [])
    if data:
        st.session_state.log_df = pd.DataFrame(data)
    else:
        st.session_state.log_df = pd.DataFrame()

df = st.session_state.log_df.copy()

if df.empty:
    st.info("No logs yet. Start tracking on the Daily Log page.")
    st.stop()

# Show a table of recent entries
st.subheader("Recent Entries")
st.dataframe(df.tail(10), use_container_width=True)

# Export section
st.subheader("📥 Export Your Data")

premium = load_from_localstorage("premium", False)

if premium:
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV (Lifetime Access)",
        data=csv,
        file_name="lymphie_logs_export.csv",
        mime="text/csv",
        use_container_width=True
    )
    st.info("💡 Save this file to your computer. You can open it in Excel or Numbers, or email it directly to your care team.")
else:
    st.info("✨ **Unlock CSV Export with Lifetime Access** – one‑time payment of $25. [Go to Settings →](#settings) to purchase or enter your key.")
    st.button("🔑 Get Lifetime Access", on_click=lambda: st.switch_page("pages/6_Settings.py"), use_container_width=True)