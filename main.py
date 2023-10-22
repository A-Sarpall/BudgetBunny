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

#logo
# Create a Streamlit layout with two columns
col1, col2, col3 = st.columns([0.5, 2, 4], gap = "small")

# Add an image to the left column
with col1:
    st.image("budgetbunny.png")

# Add content to the right column
with col2:
    st.title("BudgetBunny")

with col3:
    tab1, tab2 = st.tabs(["Budgeting", "Trading"])

    with tab2:
        st.write("feature is under construction")

# Centered button
with st.markdown("<div class='centered'>"):
    if st.button("+ Add Bank Account"):
        webbrowser.open(url)