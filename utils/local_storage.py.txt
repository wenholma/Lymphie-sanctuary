import streamlit as st
import json
from streamlit_javascript import st_javascript

def load_from_localstorage(key, default=None):
    """Retrieve a value from browser localStorage."""
    js_code = f"""
        const value = localStorage.getItem('{key}');
        return value ? JSON.parse(value) : null;
    """
    result = st_javascript(js_code)
    if result is None:
        return default
    return result

def save_to_localstorage(key, value):
    """Save a value to browser localStorage."""
    js_code = f"""
        localStorage.setItem('{key}', JSON.stringify({json.dumps(value)}));
        return true;
    """
    st_javascript(js_code)

def remove_from_localstorage(key):
    """Remove a key from localStorage."""
    js_code = f"""
        localStorage.removeItem('{key}');
        return true;
    """
    st_javascript(js_code)