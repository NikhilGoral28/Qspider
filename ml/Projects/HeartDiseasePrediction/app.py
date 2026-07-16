import streamlit as st
import pandas as pd
import joblib




with open('notebook/log_model.joblib','rb') as file:
    model = joblib.load(file)


st.set_page_config(
    page_icon='❤️',
    page_title="Heart Disease Prediction",
    layout='wide'
)

with st.sidebar:
    st.title("House Price Prediction")
    st.image('static/')
