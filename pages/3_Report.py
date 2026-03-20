import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from fpdf import FPDF
import tempfile
import os
from collections import Counter
import unicodedata

st.set_page_config(page_title="GP Report", page_icon="📄", layout="centered")

st.title("📄 GP-Ready Summary Report")
st.markdown("Generate a structured report to share with your healthcare team.")

# Check if we have data
if "log_df" not in st.session_state or st.session_state.log_df.empty:
    st.warning("No data yet. Complete a few daily logs to generate a report!")
    st.stop()

df = st.session_state.log_df.copy()

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Date range selector
st.subheader("Select Report Period")
col1, col2 = st.columns(2)
with col1:
    min_date = df['Date'].min().date()
    start_date = st.date_input("Start Date", value=min_date)
with col2:
    max_date = df['Date'].max().date()
    end_date = st.date_input("End Date", value=max_date)

# Filter data
filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

if filtered_df.empty:
    st.warning("No data in selected date range.")
    st.stop()

total_days = len(filtered_df)
st.success(f"Generating report for {total_days} days from {start_date} to {end_date}")

# ---------- CALCULATE METRICS ----------
# Helper function to clean text
def clean_text(text):
    if pd.isna(text):
        return ""
    # Convert to string and normalize unicode characters
    text = str(text)
    # Replace common problematic characters
    text = text.replace('•', '-').replace('—', '-').replace('"', '"').replace('"', '"')
    text = text.replace(''', "'").replace(''', "'")
    # Remove any remaining non-ASCII characters
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    return text

# Compression adherence (hours > 0)
if 'Compression Hours' in filtered_df.columns:
    filtered_df['Compression Hours'] = pd.to_numeric(filtered_df['Compression Hours'], errors='coerce').fillna(0)
    compression_days = filtered_df[filtered_df['Compression Hours'] > 0].shape[0]
    compression_pct = (compression_days / total_days) * 100
else:
    compression_days = 0
    compression_pct = 0

# MLD adherence
if 'Self Care' in filtered_df.columns:
    mld_days = filtered_df[filtered_df['Self Care'].str.contains('MLD', na=False)].shape[0]
    mld_pct = (mld_days / total_days) * 100
else:
    mld_days = 0
    mld_pct = 0

# Symptom averages
avg_heaviness = filtered_df['Heaviness'].mean() if 'Heaviness' in filtered_df.columns else 0
avg_pain = filtered_df['Pain'].mean() if 'Pain' in filtered_df.columns else 0
avg_stress = filtered_df['Stress'].mean() if 'Stress' in filtered_df.columns else 0
avg_energy = filtered_df['Energy'].mean() if 'Energy' in filtered_df.columns else 0

# Limb appearance distribution
if 'Limb Appearance' in filtered_df.columns:
    appearance_counts = filtered_df['Limb Appearance'].value_counts()
else:
    appearance_counts = {}

# Trigger analysis - find most common triggers on high-pain days
high_pain_days = filtered_df[filtered_df['Pain'] >= 7] if 'Pain' in filtered_df.columns else pd.DataFrame()
all_triggers = []

if not high_pain_days.empty:
    for idx, row in high_pain_days.iterrows():
        for trigger_type in ['Dietary Triggers', 'Environmental Triggers', 'Health Triggers']:
            if trigger_type in row and pd.notna(row[trigger_type]) and row[trigger_type]:
                triggers = [t.strip() for t in str(row[trigger_type]).split(',')]
                all_triggers.extend(triggers)
    
    trigger_counts = Counter(all_triggers)
    top_triggers = trigger_counts.most_common(3)
else:
    top_triggers = []

# ---------- CREATE PDF ----------
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'The Lymphie Sanctuary', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'GP-Ready Summary Report', 0, 1, 'C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(230, 240, 240)
        self.cell(0, 10, clean_text(title), 0, 1, 'L', 1)
        self.ln(5)
    
    def section_body(self, text):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, clean_text(text))
        self.ln(5)
    
    def metric_row(self, label, value):
        self.set_font('Arial', 'B', 11)
        self.cell(60, 8, clean_text(label), 0, 0)
        self.set_font('Arial', '', 11)
        self.cell(0, 8, clean_text(str(value)), 0, 1)

# Create PDF
pdf = PDF()
pdf.add_page()

# Section 1: Patient Info & Date Range
pdf.section_title("1. Patient Information & Report Period")
pdf.metric_row("Report generated:", datetime.now().strftime("%Y-%m-%d %H:%M"))
pdf.metric_row("Date range:", f"{start_date} to {end_date}")
pdf.metric_row("Days logged:", str(total_days))
pdf.ln(5)

# Section 2: Therapy Adherence
pdf.section_title("2. Therapy Adherence Summary")
pdf.metric_row("Compression adherence:", f"{compression_pct:.1f}% ({compression_days}/{total_days} days)")
pdf.metric_row("Self-MLD adherence:", f"{mld_pct:.1f}% ({mld_days}/{total_days} days)")
pdf.ln(5)

# Section 3: Symptom Averages
pdf.section_title("3. Symptom Averages (0-10 scale)")
pdf.metric_row("Average heaviness:", f"{avg_heaviness:.1f}")
pdf.metric_row("Average pain:", f"{avg_pain:.1f}")
pdf.metric_row("Average stress:", f"{avg_stress:.1f}")
pdf.metric_row("Average energy:", f"{avg_energy:.1f}")
pdf.ln(5)

# Section 4: Limb Appearance Trends
pdf.section_title("4. Limb Appearance Distribution")
if appearance_counts:
    for appearance, count in appearance_counts.items():
        pct = (count / total_days) * 100
        pdf.metric_row(f"  - {clean_text(appearance)}:", f"{pct:.1f}% ({count} days)")
else:
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 8, "No appearance data recorded.", 0, 1)
pdf.ln(5)

# Section 5: Trigger Correlation
pdf.section_title("5. Top Triggers on High-Pain Days (Pain ≥ 7/10)")
if top_triggers:
    for trigger, count in top_triggers:
        pdf.metric_row(f"  - {clean_text(trigger)}:", f"present in {count} high-pain days")
else:
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 8, "No high-pain days recorded in this period.", 0, 1)
pdf.ln(5)

# Add note
pdf.set_font('Arial', 'I', 9)
pdf.multi_cell(0, 5, "This report is generated from self-reported data. Always consult with your healthcare provider for medical advice.")

# ---------- DOWNLOAD BUTTON ----------
# Save PDF to temp file
with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
    pdf.output(tmp_file.name)
    tmp_path = tmp_file.name

with open(tmp_path, 'rb') as f:
    pdf_bytes = f.read()

os.unlink(tmp_path)  # Delete temp file

# Download button
st.subheader("Download Report")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.download_button(
        label="📥 Download PDF Report",
        data=pdf_bytes,
        file_name=f"lymphie_report_{start_date}_to_{end_date}.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# Preview section
with st.expander("Preview Report Summary"):
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Compression Adherence", f"{compression_pct:.0f}%")
        st.metric("Average Pain", f"{avg_pain:.1f}/10")
    with col2:
        st.metric("MLD Adherence", f"{mld_pct:.0f}%")
        st.metric("Days Logged", total_days)
    
    if top_triggers:
        st.write("**Top Triggers:**")
        for trigger, count in top_triggers:
            st.write(f"- {trigger}: {count} high-pain days")