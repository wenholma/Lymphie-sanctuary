import streamlit as st
import pandas as pd
import sys
import io
from datetime import datetime
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.path.append('.')
from utils.database import load_all_logs, get_premium_status

st.set_page_config(page_title="Export & History", page_icon="📊", layout="wide")

from utils.nav import mobile_nav
mobile_nav()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #2C3E35; font-size: 16px; }
    h1, h2, h3, h4 { font-family: 'Nunito', sans-serif; font-weight: 600; color: #1A3B2E; }
    .stButton > button { font-family: 'Nunito', sans-serif !important; background-color: #2E7D5E !important; color: white !important; border-radius: 60px !important; padding: 0.9rem 2.2rem !important; border: none !important; font-weight: 700 !important; font-size: 1.1rem !important; min-height: 48px; }
    .stDownloadButton > button { font-family: 'Nunito', sans-serif !important; background-color: #1E5F45 !important; color: white !important; border-radius: 60px !important; padding: 1rem 2.4rem !important; border: none !important; font-weight: 700 !important; font-size: 1.1rem !important; min-height: 48px; }
    @media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("📊 Export & History")
st.caption("View your past entries and download your data.")

premium = get_premium_status()
logs = load_all_logs()

if not logs:
    st.info("📝 No entries yet. Your daily logs will appear here once you start tracking.")
    if st.button("📝 Go to Daily Log", use_container_width=True):
        st.switch_page("pages/2_Daily_Log.py")
    st.stop()

df = pd.DataFrame(logs)

st.subheader("📋 Your Entries")
st.dataframe(df, use_container_width=True, hide_index=True)
st.caption(f"📊 **{len(logs)}** total entries logged")

st.markdown("---")
st.subheader("💾 Backup Reminder")
st.markdown("""
<div style="background: linear-gradient(135deg, #F4F9F6 0%, #EAF3EE 100%); padding: 1.2rem; border-radius: 12px; border-left: 4px solid #2E7D5E;">
    <strong>📥 Your data is stored locally in a database file.</strong><br>
    Download an Excel backup regularly and keep it somewhere safe.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.subheader("📥 Export Your Data")

if premium:
    df_export = df.copy()
    cols_to_drop = ['id', 'created_at']
    df_export = df_export.drop(columns=[col for col in cols_to_drop if col in df_export.columns])

    column_rename = {
        'date': 'Date',
        'time': 'Time',
        'heaviness': 'Heaviness (0-10)',
        'pain': 'Pain (0-10)',
        'limb_appearance': 'Limb Appearance',
        'measurement_taken': 'Measurement Taken',
        'affected_areas': 'Affected Areas',
        'compression_type': 'Compression Worn',
        'compression_hours': 'Compression Hours',
        'self_care': 'Home Self-Care',
        'professional_treatment': 'Professional Treatment',
        'movement_exercise': 'Movement & Exercise',
        'dietary_triggers': 'Dietary Triggers',
        'environmental_triggers': 'Environmental Triggers',
        'health_triggers': 'Health Triggers',
        'stress': 'Stress (0-10)',
        'sleep_quality': 'Sleep Quality',
        'energy': 'Energy (0-10)',
        'mobility': 'Mobility (0-10)',
        'self_compassion': 'Self-Compassion (0-10)',
        'biggest_challenge': 'Biggest Challenge',
        'small_win': 'Small Win',
        'temperature': 'Temperature (°C)',
        'humidity': 'Humidity (%)',
        'tags': 'Tags'
    }
    df_export = df_export.rename(
        columns={k: v for k, v in column_rename.items() if k in df_export.columns}
    )
    df_export = df_export.fillna('')

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_export.to_excel(writer, index=False, sheet_name='Lymphie Sanctuary Logs')
        workbook = writer.book
        worksheet = writer.sheets['Lymphie Sanctuary Logs']

        header_font = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
        header_fill = PatternFill(start_color='2E7D5E', end_color='2E7D5E', fill_type='solid')
        header_alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell_alignment = Alignment(vertical='top', wrap_text=True)
        thin_border = Border(
            left=Side(style='thin', color='DDE9E2'),
            right=Side(style='thin', color='DDE9E2'),
            top=Side(style='thin', color='DDE9E2'),
            bottom=Side(style='thin', color='DDE9E2')
        )

        for col_idx in range(1, len(df_export.columns) + 1):
            cell = worksheet.cell(row=1, column=col_idx)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_alignment
            cell.border = thin_border

        for row_idx in range(2, len(df_export) + 2):
            for col_idx in range(1, len(df_export.columns) + 1):
                cell = worksheet.cell(row=row_idx, column=col_idx)
                cell.alignment = cell_alignment
                cell.border = thin_border
                cell.font = Font(name='Calibri', size=10)

        for col_idx, col_name in enumerate(df_export.columns, 1):
            max_length = len(str(col_name)) + 2
            for row in range(2, len(df_export) + 2):
                cell_value = str(worksheet.cell(row=row, column=col_idx).value or '')
                max_length = max(max_length, len(cell_value))
            worksheet.column_dimensions[get_column_letter(col_idx)].width = min(max_length + 2, 40)

        worksheet.freeze_panes = 'A2'
        worksheet.auto_filter.ref = f"A1:{get_column_letter(len(df_export.columns))}{len(df_export) + 1}"
        worksheet.row_dimensions[1].height = 25

    output.seek(0)
    excel_data = output.read()

    st.download_button(
        label="📥 Download Beautiful Excel Backup (.xlsx)",
        data=excel_data,
        file_name=f"Lymphie_Sanctuary_Export_{datetime.now().strftime('%Y%m%d')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

    st.success("✅ Lifetime Access active — export anytime.")

else:
    st.warning("✨ Full Export requires Lifetime Access")
    st.markdown("""
    <div style="background: #EAF3EE; padding: 1.5rem; border-radius: 16px; margin: 1rem 0; text-align: center;">
        <h3 style="color: #1A3B2E; margin-bottom: 0.5rem; font-family: 'Nunito', sans-serif;">NZ$19.99 — One‑time payment</h3>
        <p>Lifetime access to formatted Excel exports, trend visualizations, and all future updates.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🌿 Go to Settings to Unlock", use_container_width=True):
        st.switch_page("pages/1_Settings.py")