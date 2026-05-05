import streamlit as st
import json

def load_from_localstorage(key, default=None):
    """
    Read a value from browser localStorage.
    Uses st.query_params to pass data from JavaScript to Python.
    """
    # Check if there's a pending value in query params
    if f"_ls_{key}" in st.query_params:
        try:
            value = json.loads(st.query_params[f"_ls_{key}"])
            # Clear it from URL
            del st.query_params[f"_ls_{key}"]
            return value
        except:
            pass
    
    # If no query param, inject JS to read from localStorage
    # and reload the page with the value
    js_code = f"""
    <script>
        const value = localStorage.getItem('{key}');
        if (value !== null) {{
            const currentUrl = new URL(window.location.href);
            currentUrl.searchParams.set('_ls_{key}', encodeURIComponent(value));
            window.location.href = currentUrl.toString();
        }}
    </script>
    """
    st.components.v1.html(js_code, height=0)
    return default

def save_to_localstorage(key, value):
    """
    Save a value to browser localStorage.
    Injects JavaScript that writes directly to localStorage.
    """
    json_value = json.dumps(value)
    
    js_code = f"""
    <script>
        localStorage.setItem('{key}', JSON.stringify({json_value}));
        document.body.innerHTML += '<div style="display:none;">SAVED:{key}</div>';
    </script>
    """
    st.components.v1.html(js_code, height=0)

def remove_from_localstorage(key):
    """Remove a key from browser localStorage."""
    js_code = f"""
    <script>
        localStorage.removeItem('{key}');
    </script>
    """
    st.components.v1.html(js_code, height=0)
    # Nuclear test - inject JS directly
st.subheader("4. Nuclear Test")
if st.button("NUKE - Force Save", key="nuke_btn"):
    js = """
    <script>
        localStorage.setItem('nuke_test', 'boom');
        document.body.style.backgroundColor = 'red';
    </script>
    """
    st.components.v1.html(js, height=0)
    st.write("JavaScript injected! Check load below.")

if st.button("Check Nuke", key="check_nuke"):
    js = """
    <script>
        const val = localStorage.getItem('nuke_test');
        document.body.innerHTML += '<h1>' + val + '</h1>';
    </script>
    """
    st.components.v1.html(js, height=0)
    st.write("Check the page - do you see 'boom' in big text?")