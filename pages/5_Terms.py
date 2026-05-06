import streamlit as st

st.set_page_config(page_title="Terms of Service | The Lymphie Sanctuary", page_icon="⚖️", layout="centered")

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #2C3E35; font-size: 16px; line-height: 1.7; }
    h1, h2, h3 { font-family: 'Nunito', sans-serif; font-weight: 600; color: #1A3B2E; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("⚖️ Terms of Service")
st.caption("Last updated: May 2026")

st.markdown("""
### Acceptance of Terms
By using The Lymphie Sanctuary, you agree to these terms. If you disagree, please discontinue use.

---

### Not Medical Advice
⚠️ **Important:** This app is a **personal tracking tool only**. It does not provide:
- Medical advice.
- Diagnosis.
- Treatment recommendations.

Always consult a qualified healthcare professional before making decisions about your lymphoedema management.

---

### Lifetime Access Definition
"Lifetime access" means access to the features of The Lymphie Sanctuary for as long as the product is actively maintained and offered by **Marece Wenhold trading as The Lymphie Sanctuary**. The publisher may discontinue the product at its discretion; in such a case, reasonable notice will be provided to all license holders via email.

---

### Refund Policy
Due to the nature of digital license keys, we do not offer refunds once a license key has been issued and delivered, except where required by law.

Under the **Consumer Guarantees Act 1993 (New Zealand)**, if the product fails to function as described — for example, a license key is never delivered or cannot be activated despite correct entry — you may be entitled to a remedy. In such cases, please contact **info@thelymphiesanctuary.com** and we will make it right, either by resending your key or issuing a refund.

---

### Local Storage & Data Loss
You acknowledge and agree that:
- All health logs are stored locally on your device's browser only.
- We are not responsible for data loss if you clear your browser cache, switch devices, or experience browser corruption.
- It is your responsibility to export backups regularly from the **Export** page.

---

### License Key Terms
Lifetime Access keys are:
- **Non‑transferable** — your key is for your personal use only. You may not sell, give away, or share your license key with others.
- **Single‑user** — one key is issued per purchase, for use by one person across their own devices.
- **Subject to revocation** in cases of abuse, fraud, or unauthorised distribution.

---

### Limitation of Liability
To the fullest extent permitted by law:
- The Lymphie Sanctuary and its creator (Marece Wenhold trading as The Lymphie Sanctuary) shall not be liable for any direct, indirect, incidental, or consequential damages arising from your use of the app.
- This includes, without limitation, damages for loss of data, or decisions made based on information logged in the app.

---

### Intellectual Property
The Lymphie Sanctuary name, logo, design, written content, and original source code are protected by copyright under the **Copyright Act 1994 (New Zealand)**. Copyright subsists automatically upon creation and does not require registration.

You may not copy, modify, reverse-engineer, redistribute, or create derivative works from any part of this application without prior written permission from the creator.

Unauthorised reproduction or distribution may give rise to civil and criminal liability under applicable law.

---

### Governing Law and Disputes
These Terms are governed by the laws of **New Zealand**. Any dispute will be resolved in the courts of New Zealand. Parties agree to attempt good‑faith mediation before commencing court proceedings.

---

### Changes to Terms
We may update these terms. Material changes will be posted with a version date. Continued use after notice constitutes acceptance. We recommend checking this page periodically.

---

### Contact
📧 **info@thelymphiesanctuary.com**
""")