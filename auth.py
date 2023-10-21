import streamlit as st
import requests 

# Streamlit app code (input fields, buttons, etc.)
st.title("Firebase Authentication Example")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Firebase Web API key
api_key = "AIzaSyBiGNTXBSrKniaEE0tkn-ROUo6VA7M2S54"

# Firebase Authentication API endpoints
base_url = "https://identitytoolkit.googleapis.com/v1"
signup_url = f"{base_url}/accounts:signUp?key={api_key}"
signin_url = f"{base_url}/accounts:signInWithPassword?key={api_key}"

# Sign-up function
def signup(email, password):
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(signup_url, json=data)
    result = response.json()
    if "idToken" in result:
        st.success("Sign-up successful!")
    else:
        st.error(result["error"]["message"])

# Sign-in function
def signin(email, password):
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(signin_url, json=data)
    result = response.json()
    if "idToken" in result:
        st.success("Sign-in successful!")
    else:
        st.error(result["error"]["message"])

if st.button("Sign up"):
    signup(email, password)

if st.button("Sign in"):
    signin(email, password)

