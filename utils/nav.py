import streamlit as st

def mobile_nav():
    """Show navigation buttons at the top of every page for mobile users."""
    st.markdown("""
    <style>
        .mobile-nav {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            justify-content: center;
            margin-bottom: 1rem;
            padding: 0.5rem;
            background: #F4F9F6;
            border-radius: 16px;
        }
        .mobile-nav a {
            background: white;
            color: #2E7D5E;
            padding: 0.5rem 0.8rem;
            border-radius: 20px;
            text-decoration: none;
            font-size: 0.8rem;
            font-weight: 600;
            border: 1px solid #C2D9CD;
            white-space: nowrap;
        }
        .mobile-nav a:hover {
            background: #2E7D5E;
            color: white;
        }
    </style>
    <div class="mobile-nav">
        <a href="/" target="_self">🏠 Home</a>
        <a href="/Settings" target="_self">⚙️ Settings & License</a>
        <a href="/Daily_Log" target="_self">📝 Daily Log</a>
        <a href="/Export" target="_self">📊 Export</a>
        <a href="/Privacy" target="_self">🔒 Privacy</a>
        <a href="/Terms" target="_self">⚖️ Terms of Service</a>
        <a href="/About" target="_self">👋 About</a>
    </div>
    """, unsafe_allow_html=True)