import os
import sqlite3
import secrets
import json
from datetime import datetime
from flask import Flask, request, jsonify
import stripe
import resend

app = Flask(__name__)

# ------------------------------------------------------------------------------
# CONFIGURATION (set these as environment variables on Render)
# ------------------------------------------------------------------------------
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET')
RESEND_API_KEY = os.environ.get('RESEND_API_KEY')
FROM_EMAIL = os.environ.get('FROM_EMAIL', 'The Lymphie Sanctuary <info@thelymphiesanctuary.com>')
DATABASE_PATH = os.environ.get('DATABASE_PATH', 'licenses.db')

stripe.api_key = STRIPE_SECRET_KEY
resend.api_key = RESEND_API_KEY

# ------------------------------------------------------------------------------
# DATABASE SETUP (stores issued license keys)
# ------------------------------------------------------------------------------
def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS licenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            license_key TEXT UNIQUE NOT NULL,
            customer_email TEXT NOT NULL,
            stripe_session_id TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_license_key(license_key, customer_email, stripe_session_id):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO licenses (license_key, customer_email, stripe_session_id) VALUES (?, ?, ?)",
        (license_key, customer_email, stripe_session_id)
    )
    conn.commit()
    conn.close()

def generate_license_key():
    """Generate a unique license key: LKEY-XXXX-YYYY-ZZZZ"""
    part1 = secrets.token_hex(2).upper()
    part2 = secrets.token_hex(2).upper()
    part3 = secrets.token_hex(2).upper()
    return f"LKEY-{part1}-{part2}-{part3}"

# ------------------------------------------------------------------------------
# EMAIL SENDING (using Resend)
# ------------------------------------------------------------------------------
def send_license_email(to_email, license_key):
    html_content = f"""
    <div style="font-family: Arial, sans-serif; max-width: 500px; margin: 0 auto;">
        <h2 style="color: #2E7D5E;">🌿 The Lymphie Sanctuary</h2>
        <p>Thank you so much for supporting The Sanctuary — it means a lot.</p>
        <p>Your lifetime license key is:</p>
        <div style="background: #f0f7f4; padding: 20px; border-radius: 10px;
                    text-align: center; margin: 20px 0;">
            <code style="font-size: 24px; font-weight: bold;
                         letter-spacing: 2px;">{license_key}</code>
        </div>
        <p><strong>How to activate:</strong></p>
        <ol>
            <li>Open <a href="https://thelymphiesanctuary.streamlit.app">
                The Lymphie Sanctuary</a></li>
            <li>Go to <strong>Settings</strong></li>
            <li>Paste this key and click <strong>Activate</strong></li>
        </ol>
        <p>Keep this email safe — this key is yours forever.
           If you ever lose it, just reply and I'll resend it.</p>
        <p>I hope The Sanctuary brings you a little more clarity
           and a little less overwhelm. 🌿</p>
        <p>With gratitude,<br>
           <strong>Marece</strong><br>
           <small>The Lymphie Sanctuary</small></p>
        <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
        <p style="font-size: 12px; color: #888;">
           The Lymphie Sanctuary – A private, local-first symptom journal.<br>
           Questions? Reply to this email or contact
           info@thelymphiesanctuary.com
        </p>
    </div>
    """

    try:
        params = {
            "from": FROM_EMAIL,
            "to": [to_email],
            "subject": "Your Lymphie Sanctuary License Key 🌿",
            "html": html_content
        }
        email = resend.Emails.send(params)
        print(f"Email sent to {to_email}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# ------------------------------------------------------------------------------
# WEBHOOK ENDPOINT
# ------------------------------------------------------------------------------
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError:
        return jsonify({'error': 'Invalid signature'}), 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # ✅ FIXED: Works with both StripeObject (v15) and plain dict (v7)
        customer_email = None
        customer_details = session.get('customer_details')
        if customer_details:
            if hasattr(customer_details, 'get'):
                customer_email = customer_details.get('email')
            else:
                customer_email = getattr(customer_details, 'email', None)
        if not customer_email:
            customer_email = session.get('customer_email')

        if not customer_email:
            print("❌ No customer email found in session")
            return jsonify({'status': 'no email'}), 200

        stripe_session_id = session['id']
        license_key = generate_license_key()

        init_db()
        save_license_key(license_key, customer_email, stripe_session_id)

        email_sent = send_license_email(customer_email, license_key)

        if email_sent:
            print(f"✅ License {license_key} sent to {customer_email}")
        else:
            print(f"❌ Failed to send email to {customer_email}")

    return jsonify({'status': 'success'}), 200

# ------------------------------------------------------------------------------
# VALIDATION ENDPOINT (for Streamlit app to check keys)
# ------------------------------------------------------------------------------
@app.route('/validate', methods=['POST'])
def validate_key():
    data = request.json
    key = data.get('license_key')

    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM licenses WHERE license_key = ?", (key,))
    result = c.fetchone()
    conn.close()

    if result:
        return jsonify({'valid': True}), 200
    else:
        return jsonify({'valid': False}), 200

# ------------------------------------------------------------------------------
# HEALTH CHECK (for Render)
# ------------------------------------------------------------------------------
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))