import streamlit as st
import pandas as pd

st.set_page_config(page_title="Amit", layout="wide")

file = st.file_uploader("Upload CSV", type="csv")

if file:
    df = pd.read_csv(file)
    st.write(df.head())
    st.bar_chart(df.iloc[8])
else:
    st.write("please upload file")