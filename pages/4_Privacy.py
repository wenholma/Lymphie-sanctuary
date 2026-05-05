import streamlit as st

st.set_page_config(page_title="Privacy Policy", page_icon="🔒", layout="centered")

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

st.title("🔒 Privacy Policy")
st.caption("Last updated: May 2026")

st.markdown("""
### Your Data — Two Completely Separate Things

**Your health logs (symptoms, triggers, reflections)**  
These are saved exclusively in your browser's local storage and never leave your device. The Lymphie Sanctuary's servers have no ability to receive, read, or store these logs. This is not a policy choice — it is how the app is built.

**Your purchase (email + license key only)**  
When you buy a license, Stripe processes your payment and shares only your email address with us. We store three items on our license server: your email address, the issued license key, and a Stripe transaction reference. We do not store health logs, names, or browsing behaviour. This information is used solely to deliver your license key, validate it during activation, and resend it if you lose it.

**In plain terms:** We know you bought a license. We have no idea what you log in it.

### Data Retention and Legal Obligations
We retain purchase records (the purchaser's email address, the issued license key, and the Stripe transaction reference) for a period of **seven (7) years** from the date of purchase to comply with New Zealand tax and record‑keeping obligations. This retention period is based on New Zealand Inland Revenue guidance requiring businesses to keep financial and tax records for at least seven years.

### Why We Retain This Data
We keep these purchase records only to:
- (a) Deliver and validate lifetime license keys
- (b) Resend keys if lost
- (c) Meet legal, tax, or accounting obligations

We do not store or access your health logs; those remain only in your browser's local storage.

### Security Measures
We protect stored purchase data using industry‑standard safeguards, including:
- Encryption at rest and in transit
- Access controls limiting access to a small number of authorised personnel
- Regular backups
- Periodic security reviews

Access to purchase records is logged and audited.

### Deletion and User Requests
If you request deletion of your purchase record, we will delete your email and license record from our license server **within 30 days**, unless we are required to retain the record to comply with legal or tax obligations (for example, to meet the seven‑year IRD retention requirement). If deletion is delayed for legal reasons, we will notify you and explain the reason.

### Breach Notification
If a security incident affects your purchase data, we will notify you and the relevant authorities in accordance with applicable law and will provide information about the nature of the incident and steps we are taking.

### What Happens If You Clear Your Cache?
If you clear your browser cache or use a different device, your health logs will be lost **unless you have exported them**. We strongly encourage regular Excel exports from the **Export** page to keep a permanent backup.

### Payment Information
When you purchase a Lifetime Access key:
- Payment is processed securely by Stripe (our payment processor).
- We do not receive or store your credit card details.
- Your email address is used only to deliver your license key and is never shared.

### Third‑Party Services
We do **not** use:
- Analytics trackers.
- Advertising cookies.
- Social media pixels.
- Any scripts that collect personal information.

### Your Complete Control
Because we never store your health data on our servers:
- You can delete all logs anytime via **Settings → Delete All Local Data**.
- You can export your data anytime via **Export**.
- You control who sees your information.

### Children
This app is intended for adult use. We take extra care with children's personal information; if you are a parent or guardian and believe your child under 16 has provided personal information, contact us. We do not target or knowingly collect data from children.

### Updates to This Policy
We may update this policy. Material changes will be posted with a version date; continued use after notice constitutes acceptance. We recommend checking this page periodically.

### Contact
📧 **info@thelymphiesanctuary.com**  
Please allow 2–3 days for a reply.
""")