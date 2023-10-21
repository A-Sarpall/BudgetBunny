import streamlit as st
import pyrebase

# Firebase Configuration
config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_AUTH_DOMAIN",
    "projectId": "YOUR_PROJECT_ID",
    "storageBucket": "YOUR_STORAGE_BUCKET",
    "messagingSenderId": "YOUR_MESSAGING_SENDER_ID",
    "appId": "YOUR_APP_ID"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Streamlit App
def main():
    st.title("Firebase Login")
    
    # Login Form
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Login successful!")
        except:
            st.error("Login failed. Check your credentials.")

if __name__ == "__main__":
    main()
