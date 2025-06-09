import streamlit as st
import pandas as pd

st.set_page_config(page_title="Amit", layout="wide")

file=pd.read_csv("data/amazon.csv")

st.write("Hello World!")
st.write(file)