import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# -------------------------------
# ⚙️ Page Config
# -------------------------------
st.set_page_config(page_title="ESG Dashboard", layout="wide")

# -------------------------------
# 🎨 CUSTOM CSS (🔥 GAME CHANGER)
# -------------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: #E6EDF3;
}
.stMetric {
    background-color: #161B22;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 📂 Paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "../data/esg_data.csv")
infosys_logo_path = os.path.join(BASE_DIR, "../assets/infosys.png")
reliance_logo_path = os.path.join(BASE_DIR, "../assets/reliance.png")

# -------------------------------
# 📊 Load Data
# -------------------------------
df = pd.read_csv(data_path)

# -------------------------------
# 🖼️ Load Logos
# -------------------------------
infosys_logo = Image.open(infosys_logo_path)
reliance_logo = Image.open(reliance_logo_path)

# -------------------------------
# 🎯 HEADER (UPGRADED)
# -------------------------------
st.markdown("# 🌍 ESG Analytics Dashboard")
st.markdown("### 🔍 Infosys vs Reliance — Business Insights")

col1, col2 = st.columns([1,1])
with col1:
    st.image(infosys_logo, width=140)
with col2:
    st.image(reliance_logo, width=140)

st.markdown("---")

# -------------------------------
# 📊 KPI CARDS (TOP SECTION 🔥)
# -------------------------------
st.markdown("## 📈 Key Metrics Comparison")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👩 Infosys Female %", f"{df.iloc[0]['Female_Percentage']}%")
    st.metric("👩 Reliance Female %", f"{df.iloc[1]['Female_Percentage']}%")

with col2:
    st.metric("🔁 Infosys Attrition", f"{df.iloc[0]['Attrition_Total']}%")
    st.metric("🔁 Reliance Attrition", f"{df.iloc[1]['Attrition_Total']}%")

with col3:
    st.metric("🏢 Infosys Board %", f"{df.iloc[0]['Board_Female_Percentage']}%")
    st.metric("🏢 Reliance Board %", f"{df.iloc[1]['Board_Female_Percentage']}%")

st.markdown("---")

# -------------------------------
# 📊 CHARTS (CLEAN + COLOR)
# -------------------------------
st.markdown("## 📊 ESG Comparison")

col1, col2, col3 = st.columns(3)

# Gender
with col1:
    st.markdown("### 👩 Gender Diversity")
    fig1, ax1 = plt.subplots()
    ax1.bar(df["Company"], df["Female_Percentage"])
    ax1.set_title("Female %")
    st.pyplot(fig1)

# Attrition
with col2:
    st.markdown("### 🔁 Attrition Rate")
    fig2, ax2 = plt.subplots()
    ax2.bar(df["Company"], df["Attrition_Total"])
    ax2.set_title("Attrition %")
    st.pyplot(fig2)

# Governance
with col3:
    st.markdown("### 🏢 Governance")
    fig3, ax3 = plt.subplots()
    ax3.bar(df["Company"], df["Board_Female_Percentage"])
    ax3.set_title("Board Diversity %")
    st.pyplot(fig3)

st.markdown("---")

# -------------------------------
# 📁 DATA TABLE (CLEAN)
# -------------------------------
with st.expander("📂 View Raw Dataset"):
    st.dataframe(df, use_container_width=True)

# -------------------------------
# 🧠 INSIGHTS (CARD STYLE)
# -------------------------------
st.markdown("## 🧠 Key Insights")

st.success("Infosys has significantly higher gender diversity than Reliance.")
st.info("Infosys has higher attrition, indicating a dynamic workforce.")
st.warning("Reliance shows more workforce stability.")
st.error("Board diversity remains low across both companies.")
st.success("Climate risk is common across industries.")

st.markdown("---")

# -------------------------------
# 🌟 SIDEBAR (CLEAN)
# -------------------------------
st.sidebar.title("📌 About")

st.sidebar.markdown("""
**Project:** ESG Analytics Dashboard  

**Focus:**
- Company comparison  
- ESG metrics  
- Business insights  

**Tech Stack:**
- Python  
- Streamlit  
- Data Analysis  
""")

# -------------------------------
# 🎯 FOOTER
# -------------------------------
st.markdown("""
---
<center>🚀 Built by Divyant Mayank</center>
""", unsafe_allow_html=True)