import streamlit as st
from predictpage import show_predict_page
from Stats import show_explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
if page == "Explore":
    show_explore_page()
