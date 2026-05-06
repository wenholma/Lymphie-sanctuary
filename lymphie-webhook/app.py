import os
import sqlite3
import secrets
from datetime import datetime
from flask import Flask, request, jsonify
import stripe
import resend

app = Flask(__name__)

STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET')
RESEND_API_KEY = os.environ.get('RESEND_API_KEY')
FROM_EMAIL = os.environ.get('FROM_EMAIL', 'The Lymphie Sanctuary <info@thelymphiesanctuary.com>')
DATABASE_PATH = os.environ.get('DATABASE_PATH', 'licenses.db')

stripe.api_key = STRIPE_SECRET_KEY
resend.api_key = RESEND_API_KEY

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
    part1 = secrets.token_hex(2).upper()
    part2 = secrets.token_hex(2).upper()
    part3 = secrets.token_hex(2).upper()
    return f"LKEY-{part1}-{part2}-{part3}"

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
            <li>Open <a href="https://thelymphiesanctuary.streamlit.app">The Lymphie Sanctuary</a></li>
            <li>Go to <strong>Settings &amp; License</strong></li>
            <li>Copy and paste this key into the box and click <strong>Activate</strong></li>
        </ol>
        <p>Keep this email safe — this key is yours forever.
           If you ever lose it, just reply and I'll resend it.</p>
        <p>📌 <strong>Can't find this email later?</strong> Check your junk/spam folder