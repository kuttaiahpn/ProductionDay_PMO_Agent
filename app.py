import streamlit as st
import pandas as pd
import os

# 1. Page Config - Must be the first Streamlit command
st.set_page_config(page_title="Agentic PMO Co-Pilot", layout="wide")

# 2. Sidebar - Let's force it to show up first
with st.sidebar:
    st.header("📂 Data Governance")
    st.write("Upload your portfolio data to begin.")
    uploaded_file = st.file_uploader("Upload pmo_dataset.csv", type=["csv"])
    st.markdown("---")
    st.info("Product in a Day: Built by Kuttaiah P N")

# 3. Main Body
st.title("🚀 Production Day: Agentic PMO Command Center")

if uploaded_file is not None:
    try:
        # Import your custom logic inside the 'if' to prevent startup crashes
        from pmo_engine import PMOEngine
        from agent import PMOConsultantAgent
        
        # Save temp file
        with open("temp_pmo_data.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process Data
        engine = PMOEngine("temp_pmo_data.csv")
        df = engine.calculate_metrics()
        
        st.success("Data loaded successfully!")
        st.dataframe(df.head()) # Show a preview immediately
        
    except Exception as e:
        st.error(f"Configuration Error: {e}")
        st.warning("Make sure pmo_engine.py and agent.py are in this folder.")
else:
    st.info("Waiting for data... Please use the sidebar to upload your CSV.")