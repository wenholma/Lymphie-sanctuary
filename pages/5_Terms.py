import streamlit as st

st.set_page_config(page_title="Terms of Service", page_icon="⚖️", layout="centered")

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

st.title("⚖️ Terms of Service")
st.caption("Last updated: May 2026")

st.markdown("""
### Acceptance of Terms
By using The Lymphie Sanctuary, you agree to these terms. If you disagree, please discontinue use.

### Not Medical Advice
⚠️ **Important:** This app is a **personal tracking tool only**. It does **not** provide:
- Medical advice.
- Diagnosis.
- Treatment recommendations.

Always consult a qualified healthcare professional before making decisions about your lymphoedema management.

### Lifetime Access Definition
"Lifetime access" means access to the features of The Lymphie Sanctuary for as long as the product is actively maintained and offered by the publisher. The publisher may discontinue the product at its discretion; in such a case, we will provide reasonable notice to license holders.

### Refund Policy
Due to the nature of digital license keys, we do not offer refunds once a license key has been issued, except where required by law (for example, where a consumer guarantee applies under the Consumer Guarantees Act 1993).

### Local Storage & Data Loss
You acknowledge and agree that:
- All health logs are stored locally on your device's browser.
- We are not responsible for data loss if you clear your browser cache, switch devices, or experience browser corruption.
- It is your responsibility to export backups regularly.

### License Key Terms
Lifetime Access keys are:
- Non‑transferable — for personal use only.
- Single‑user — one key per person.
- Subject to revocation in cases of abuse, fraud, or unauthorized distribution.
- **License keys are non-refundable once issued, as they are delivered instantly.**

### Limitation of Liability
To the fullest extent permitted by law:
- The Lymphie Sanctuary and its creator shall not be liable for any direct, indirect, incidental, or consequential damages arising from your use of the app.
- This includes, without limitation, damages for loss of data, personal injury, or emotional distress.

### Intellectual Property
The Lymphie Sanctuary name, logo, design, content and original code are protected by copyright and other IP laws. You may not copy, modify, or redistribute the app without prior written permission.

### Governing Law and Disputes
These Terms are governed by the laws of New Zealand. Any dispute will be resolved in the courts of New Zealand; parties agree to attempt good‑faith mediation before commencing court proceedings.

### Changes to Terms
We may update these terms. Material changes will be posted with a version date; continued use after notice constitutes acceptance. We recommend checking this page periodically.

### Contact
📧 **info@thelymphiesanctuary.com**
""")