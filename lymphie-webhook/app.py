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
FROM_EMAIL = os.environ.get('FROM_EMAIL', 'Marece <info@thelymphiesanctuary.com>')
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
    part1 = secrets.token_hex(2).upper()  # 4 chars
    part2 = secrets.token_hex(2).upper()  # 4 chars
    part3 = secrets.token_hex(2).upper()  # 4 chars
    return f"LKEY-{part1}-{part2}-{part3}"

# ------------------------------------------------------------------------------
# EMAIL SENDING (using Resend)
# ------------------------------------------------------------------------------
def send_license_email(to_email, license_key):
    html_content = f"""
    <div style="font-family: Arial, sans-serif; max-width: 500px; margin: 0 auto;">
        <h2 style="color: #2E7D5E;">🌿 The Lymphie Sanctuary</h2>
        <p>Thank you for supporting The Sanctuary!</p>
        <p>Your lifetime license key is:</p>
        <div style="background: #f0f7f4; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
            <code style="font-size: 24px; font-weight: bold; letter-spacing: 2px;">{license_key}</code>
        </div>
        <p><strong>How to activate:</strong></p>
        <ol>
            <li>Open The Lymphie Sanctuary app</li>
            <li>Go to <strong>Settings</strong></li>
            <li>Paste this key and click <strong>Activate</strong></li>
        </ol>
        <p>This key is yours forever. Keep it safe! If you ever lose it, just reply to this email.</p>
        <p>With gratitude,<br>Marece</p>
        <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
        <p style="font-size: 12px; color: #888;">The Lymphie Sanctuary – A private, local-first symptom journal.</p>
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
    
    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        # Get customer email
        customer_email = session.get('customer_details', {}).get('email')
        if not customer_email:
            customer_email = session.get('customer_email')
        
        stripe_session_id = session['id']
        
        # Generate a unique license key
        license_key = generate_license_key()
        
        # Save to database
        init_db()
        save_license_key(license_key, customer_email, stripe_session_id)
        
        # Send email
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