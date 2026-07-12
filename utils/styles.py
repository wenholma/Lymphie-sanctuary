import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
        :root {
            --teal: #0F766E;
            --ink: #0F1F1B;
            --tint: #EAF6F1;
            --body-text: #22302B;
            --muted-text: #647A73;
            --mint: #4FE3BC;
        }
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: var(--body-text);
            font-size: 16px;
            background-color: #FAFCFA;
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Nunito', sans-serif;
            font-weight: 600;
            color: var(--ink);
        }
        .stCaption, .stMarkdown p, li, div {
            color: var(--body-text);
        }
        .stCaption { color: var(--muted-text); }
        .green-box {
            background: var(--tint);
            border-left: 6px solid var(--mint);
            padding: 1.4rem 1.8rem;
            border-radius: 20px;
            margin: 1.5rem 0;
        }
        .stButton button, .stDownloadButton button, .stForm button[type="submit"] {
            background-color: var(--teal) !important;
            color: white !important;
            font-weight: 700 !important;
            font-family: 'Nunito', sans-serif !important;
            border: none !important;
            border-radius: 60px !important;
            padding: 0.9rem 2.2rem !important;
            font-size: 1.1rem !important;
            min-height: 48px !important;
            box-shadow: 0 2px 8px rgba(15, 118, 110, 0.25) !important;
            transition: all 0.2s ease !important;
            letter-spacing: 0.3px !important;
            cursor: pointer !important;
        }
        .stButton button:hover, .stDownloadButton button:hover, .stForm button[type="submit"]:hover {
            background-color: #0D5F58 !important;
            box-shadow: 0 4px 16px rgba(15, 118, 110, 0.35) !important;
            transform: translateY(-2px);
        }
        .stButton button:active, .stDownloadButton button:active {
            transform: scale(0.97);
            box-shadow: 0 1px 4px rgba(15, 118, 110, 0.2) !important;
        }
        .stButton button[kind="secondary"], .stButton button[data-kind="secondary"] {
            background-color: transparent !important;
            color: var(--teal) !important;
            box-shadow: inset 0 0 0 2px var(--teal) !important;
            background: white !important;
        }
        .stButton button[kind="secondary"]:hover, .stButton button[data-kind="secondary"]:hover {
            background-color: var(--tint) !important;
            color: #0D5F58 !important;
            box-shadow: inset 0 0 0 2px #0D5F58 !important;
            transform: translateY(-2px);
        }
        .stDownloadButton button {
            background-color: #1E5F45 !important;
            box-shadow: 0 2px 8px rgba(30, 95, 69, 0.25) !important;
        }
        .stDownloadButton button:hover {
            background-color: #164D36 !important;
        }
        a { color: var(--teal); text-decoration: none; font-weight: 500; }
        a:hover { color: #0D5F58; text-decoration: underline; }
        .brand-footer {
            text-align: center;
            padding: 1.5rem 0 0.5rem 0;
            font-size: 0.85rem;
            color: var(--muted-text);
            border-top: 1px solid #e0e8e0;
            margin-top: 2rem;
        }
        .brand-footer a { color: var(--teal); font-weight: 500; }
        #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
        @media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }
    </style>
    """, unsafe_allow_html=True)