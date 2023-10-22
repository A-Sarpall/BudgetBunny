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
col1, col2 = st.sidebar.columns([1, 3], gap = "small")

st.sidebar.markdown(" ")

# Add an image to the left column
with col1:
    st.image("budgetbunny.png")

# Add content to the right column
with col2:
    st.title("BudgetBunny")

# Define a dictionary to store the pages
pages = {
    "Chat": "This is where you chat wth Bunny",
    "Banking Information": "This is where you can see your banking information",
}

# Create a sidebar for navigation
selected_page = st.sidebar.radio("Select a page", list(pages.keys()))

st.empty()

# Display the selected page content
if selected_page in pages:
    if selected_page is "Chat":
        exec(open("budgetbunny.py").read())

    if selected_page is "Banking Information":
        exec(open("info.py").read())
