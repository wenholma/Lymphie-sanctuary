import streamlit as st

def mobile_nav():
    """Show polished navigation buttons at the top of every page."""
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

        .sanctuary-nav {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 0.6rem;
            margin: 0 auto 1.2rem auto;
            padding: 0.8rem 1rem;
            background: linear-gradient(135deg, #F4F9F6 0%, #EAF3EE 100%);
            border-radius: 24px;
            box-shadow: 0 4px 12px rgba(46, 125, 94, 0.06);
        }

        .sanctuary-nav a {
            background: white;
            color: #1A3B2E;
            padding: 0.7rem 1.2rem;
            border-radius: 40px;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 600;
            font-family: 'Nunito', sans-serif;
            letter-spacing: -0.01em;
            border: 1px solid #D4E8DC;
            transition: all 0.2s ease;
            box-shadow: 0 2px 6px rgba(0,0,0,0.02);
            white-space: nowrap;
        }

        .sanctuary-nav a:hover {
            background: #2E7D5E;
            color: white;
            border-color: #2E7D5E;
            box-shadow: 0 6px 14px rgba(46, 125, 94, 0.15);
            transform: translateY(-1px);
        }

        .sanctuary-nav a:active {
            background: #1A3B2E;
            color: white;
            transform: translateY(0);
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }

        /* Slightly smaller text for very small screens */
        @media (max-width: 400px) {
            .sanctuary-nav a {
                font-size: 0.8rem;
                padding: 0.6rem 0.9rem;
            }
        }
    </style>
    <div class="sanctuary-nav">
        <a href="/" target="_self">🏠 Home</a>
        <a href="/Settings" target="_self">⚙️ Settings</a>
        <a href="/Daily_Log" target="_self">📝 Daily Log</a>
        <a href="/Export" target="_self">📊 Export</a>
        <a href="/Media" target="_self">🎙️ Media</a>
        <a href="/Privacy" target="_self">🔒 Privacy</a>
        <a href="/Terms" target="_self">⚖️ Terms</a>
        <a href="/About" target="_self">👋 About</a>
    </div>
    """, unsafe_allow_html=True)