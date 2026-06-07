import streamlit as st

def mobile_nav():
    """Show navigation buttons at the top of every page for mobile users."""
    st.markdown("""
    <style>
        #MainMenu {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        header {visibility: hidden !important;}
        [data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
        [data-testid="stDecoration"] {visibility: hidden !important; display: none !important;}
        [data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
        [data-testid="collapsedControl"] {display: none !important;}
        [data-testid="stAppViewBlockContainer"] ~ div {display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
        .viewerBadge_container__1QSob {display: none !important;}
        .styles_viewerBadge__1yB5_ {display: none !important;}
        .viewerBadge_link__1S137 {display: none !important;}
        .viewerBadge_text__1JaDK {display: none !important;}
        ._profileContainer_pgbpb_53 {display: none !important;}
        ._profile_pgbpb_61 {display: none !important;}
        ._profilePreview_pgbpb_74 {display: none !important;}
        a[href*="share.streamlit.io"] {display: none !important;}
        a[href*="streamlit.io"] img {display: none !important;}
        div[class*="profileContainer"] {display: none !important;}
        div[class*="viewerBadge"] {display: none !important;}
        div[class*="_profileContainer"] {display: none !important;}
        div[class*="_profile"] {display: none !important;}
        div[class*="stAppDeployButton"] {display: none !important;}
        .stDeployButton {display: none !important;}
        [data-testid="stDeployButton"] {display: none !important;}

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
            cursor: pointer;
        }
        .mobile-nav a:hover {
            background: #2E7D5E;
            color: white;
        }
        .mobile-nav a:active {
            background: #1A3B2E;
            color: white;
        }
        /* Highlight the Coming Soon button slightly */
        .mobile-nav a.whats-coming {
            border-color: #E6C940;
            color: #1A3B2E;
            background: #FFF9E6;
        }
        .mobile-nav a.whats-coming:hover {
            background: #E6C940;
            color: #1A3B2E;
        }
    </style>
    <div class="mobile-nav">
        <a href="/" target="_self" onclick="window.location.href='/'">🏠 Home</a>
        <a href="/Settings" target="_self" onclick="window.location.href='/Settings'">⚙️ Settings & License</a>
        <a href="/Daily_Log" target="_self" onclick="window.location.href='/Daily_Log'">📝 Daily Log</a>
        <a href="/Export" target="_self" onclick="window.location.href='/Export'">📊 Export</a>
        <a href="/Whats_Coming" target="_self" class="whats-coming" onclick="window.location.href='/Whats_Coming'">🚀 What's Coming</a>
        <a href="/Privacy" target="_self" onclick="window.location.href='/Privacy'">🔒 Privacy Policy</a>
        <a href="/Terms" target="_self" onclick="window.location.href='/Terms'">⚖️ Terms of Service</a>
        <a href="/About" target="_self" onclick="window.location.href='/About'">👋 About</a>
    </div>
    """, unsafe_allow_html=True)