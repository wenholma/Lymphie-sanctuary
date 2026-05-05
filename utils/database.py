import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "lymphie_logs.db")

def init_db():
    """Create the logs table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            time TEXT,
            heaviness INTEGER,
            pain INTEGER,
            limb_appearance TEXT,
            measurement_taken TEXT,
            affected_areas TEXT,
            compression_type TEXT,
            compression_hours INTEGER,
            self_care TEXT,
            dietary_triggers TEXT,
            environmental_triggers TEXT,
            health_triggers TEXT,
            stress INTEGER,
            sleep_quality TEXT,
            energy INTEGER,
            mobility INTEGER,
            self_compassion INTEGER,
            biggest_challenge TEXT,
            small_win TEXT,
            temperature REAL,
            humidity INTEGER,
            tags TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_log(entry_dict):
    """Save a single log entry to the database."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    columns = [
        "date", "time", "heaviness", "pain", "limb_appearance", "measurement_taken",
        "affected_areas", "compression_type", "compression_hours", "self_care",
        "dietary_triggers", "environmental_triggers", "health_triggers", "stress",
        "sleep_quality", "energy", "mobility", "self_compassion", "biggest_challenge",
        "small_win", "temperature", "humidity", "tags"
    ]
    
    mapping = {
        "Date": "date",
        "Time": "time",
        "Heaviness": "heaviness",
        "Pain": "pain",
        "Limb Appearance": "limb_appearance",
        "Measurement Taken": "measurement_taken",
        "Affected Areas": "affected_areas",
        "Compression Type": "compression_type",
        "Compression Hours": "compression_hours",
        "Self Care": "self_care",
        "Dietary Triggers": "dietary_triggers",
        "Environmental Triggers": "environmental_triggers",
        "Health Triggers": "health_triggers",
        "Stress": "stress",
        "Sleep Quality": "sleep_quality",
        "Energy": "energy",
        "Mobility": "mobility",
        "Self Compassion": "self_compassion",
        "Biggest Challenge": "biggest_challenge",
        "Small Win": "small_win",
        "Temperature": "temperature",
        "Humidity": "humidity",
        "Tags": "tags"
    }
    
    values = {}
    for form_key, db_col in mapping.items():
        val = entry_dict.get(form_key, "")
        if val == "":
            val = None
        values[db_col] = val
    
    placeholders = ", ".join(["?" for _ in columns])
    sql = f"INSERT INTO logs ({', '.join(columns)}) VALUES ({placeholders})"
    
    c.execute(sql, [values[col] for col in columns])
    conn.commit()
    conn.close()
    return True

def load_all_logs():
    """Load all logs from database into a list of dicts."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM logs ORDER BY date DESC, time DESC", conn)
    conn.close()
    return df.to_dict('records')

def delete_all_logs():
    """Delete all logs (for testing)."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM logs")
    conn.commit()
    conn.close()

def get_premium_status():
    """Check if premium is activated."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS premium (id INTEGER PRIMARY KEY, active BOOLEAN)")
    c.execute("SELECT active FROM premium WHERE id=1")
    row = c.fetchone()
    conn.close()
    return row[0] if row else False

def set_premium_status(active):
    """Set premium status (True/False)."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS premium (id INTEGER PRIMARY KEY, active BOOLEAN)")
    c.execute("DELETE FROM premium WHERE id=1")
    c.execute("INSERT INTO premium (id, active) VALUES (1, ?)", (active,))
    conn.commit()
    conn.close()