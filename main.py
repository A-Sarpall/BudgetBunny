#save file
#open terminal
#cd desktop
#streamlit run main.py
import streamlit as st
import requests
import webbrowser

url = "https://www.coolmathgames.com/"

st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Centered button
with st.markdown("<div class='centered'>"):
    if st.button("+ Add Bank Account"):
        webbrowser.open(url)