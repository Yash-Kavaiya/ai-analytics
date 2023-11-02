import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai import SmartDataframe
from pandasai.llm import GooglePalm

llm = GooglePalm(api_key="AIzaSyAnw_3MPaMeoR6zK3Om9ObtaTXLTfuZ86k")
import matplotlib.pyplot as plt

import seaborn as sns
from PIL import Image
st.set_page_config(
    page_title="PandasAI Insight App",
    layout="wide",
    initial_sidebar_state="expanded"
)
styles = """
<style>
img {
    max-width: 50%;
}
.sidebar .sidebar-content {
    background-color: #f5f5f5;
}
</style>
"""

st.sidebar.title('PandasAI Insights')    
st.sidebar.subheader('AI Insights')
header = st.container()

with header:
    st.title("PandasAI Analysis App")
    st.markdown("Use this Streamlit app to analyze your data in one shot. You can upload your data and ask questions about it. The app will answer your questions and provide you with insights about your data.")
    st.write("")
# Define main content
content = st.container()
with content:
    # Load sales dataset
    sale_file = st.file_uploader('Select Your Local Sales CSV (default provided)')
    if sale_file is not None:
        df = pd.read_csv(sale_file, encoding='latin-1')
        sdf = SmartDataframe(df, config={"llm": llm})
        st.dataframe(df)
        query = st.text_input(label='Enter your query')
        Analyze = st.button(label='Analyze')
        if Analyze:
            result = sdf.chat(query)
            print(result)
            st.write(result)
    else:
        st.warning("Please select a CSV file to continue.")
        st.stop()