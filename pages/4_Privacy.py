import streamlit as st

st.set_page_config(page_title="Privacy Policy | The Lymphie Sanctuary", page_icon="🔒", layout="centered")

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

st.title("🔒 Privacy Policy")
st.caption("Last updated: May 2026")

st.markdown("""
### Your Data — Two Completely Separate Things

**Your health logs (symptoms, triggers, reflections)**
These are saved exclusively in your browser's local storage and never leave your device. The Lymphie Sanctuary's servers have no ability to receive, read, or store these logs. This is not a policy choice — it is how the app is built.

**Your purchase (email + license key only)**
When you buy a license, Stripe processes your payment and shares only your email address with us. We store three items on our license server: your email address, the issued license key, and a Stripe transaction reference. We do not store health logs, names, or browsing behaviour. This information is used solely to deliver your license key, validate it during activation, and resend it if you lose it.

**In plain terms:** We know you bought a license. We have no idea what information you capture.

---

### Data Retention and Legal Obligations
We retain purchase records (your email address, license key, and Stripe transaction reference) for **seven (7) years** from the date of purchase, as required by New Zealand Inland Revenue for financial and tax records.

---

### Why We Retain This Data
We keep purchase records only to:
- Deliver and validate lifetime license keys.
- Resend keys if lost.
- Meet legal, tax, or accounting obligations under NZ law.

We do not store or access your health logs — those remain only in your browser.

---

### Security Measures
We protect stored purchase data as follows:

- **Encryption in transit:** All data is transmitted over HTTPS — encrypted between your device and our server.
- **Encryption at rest:** Our hosting provider (Render) encrypts data stored on disk as part of our paid hosting plan.
- **Access controls:** Only the app owner has access to the license server and its database.
- **Backups:** Automated backups of the license database are performed by our hosting provider (Render) as part of our hosting plan.
- **Security reviews:** We review our server configuration periodically.

We do not store health logs on any server — those remain only in your browser.

---

### Deletion and User Requests
If you would like your purchase record deleted, email **info@thelymphiesanctuary.com** with the subject line **"Data Deletion Request"** and include the email address you used to purchase.

We will:
1. Delete your email address and license key from our license server within 30 days.
2. Send you a confirmation email once deletion is complete.

Please note: if there is an unresolved dispute, a fraud investigation, or a legal obligation under NZ tax law (IRD requires financial records for 7 years), we may need to retain your record longer. If this applies, we will tell you why and for how long.

---

### Breach Notification
A security incident in the context of this app would most likely mean unauthorised access to our license server — for example, someone gaining access to the database containing email addresses and license keys.

**Important:** Health logs are never stored on our server, so a server breach would never expose your health data.

If a breach occurs affecting your purchase data, we will:
- Notify you by email (using the address stored for your purchase) as soon as practicable.
- Report the breach to the **Office of the Privacy Commissioner (New Zealand)** as required under the **Privacy Act 2020**, which requires notification of breaches likely to cause serious harm.

Using your stored email to notify you of a breach is not a contradiction — it is the appropriate and lawful use of that data to protect your interests.

---

### What Happens If You Clear Your Cache?
If you clear your browser cache or use a different device, your health logs will be lost unless you have exported them. We strongly encourage regular Excel exports from the **Export** page.

---

### Payment Information
When you purchase a Lifetime Access key:
- Payment is processed securely by **Stripe** (our payment processor).
- We do not receive or store your credit card details.
- Your email address is stored solely to deliver and validate your license key. It is never sold or shared with third parties.

---

### Third‑Party Services
We do not use:
- Analytics trackers.
- Advertising cookies.
- Social media pixels.
- Any scripts that collect personal information.

---

### Your Complete Control
Because we never store your health data on our servers:
- You can delete all logs anytime via **Settings & License → Data Management → Delete All Local Data**.
- You can export your data anytime via the **Export** page.
- You control who sees your information.

---

### Children and Minors
The Lymphie Sanctuary is intended for adult use only. Purchasing a license requires a credit or debit card, which acts as a practical barrier to use by minors.

We do not knowingly accept purchases from anyone under 18. If you are a parent or guardian and believe your child has made a purchase, please contact us at **info@thelymphiesanctuary.com** and we will review the situation.

We do not collect health data from anyone — adults or minors — as all health logs remain on the user's own device and are never transmitted to us.

---

### Updates to This Policy
We may update this policy. Material changes will be posted with a version date. Continued use after notice constitutes acceptance. We recommend checking this page periodically.

---

### Contact
📧 **info@thelymphiesanctuary.com**
Please allow 2–3 days for a reply.
""")