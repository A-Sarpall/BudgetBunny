import streamlit as st
import openai
import requests
from streamlit.components.v1 import html

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)
    

# Define app states
states = {"Login": 0, "Home": 1}

# Initialize the state
state = states["Login"]

# Streamlit app code (input fields, buttons, etc.)
st.set_page_config(initial_sidebar_state= "collapsed")
st.title("BudgetBunny Login")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Firebase Web API key
api_key = "AIzaSyBiGNTXBSrKniaEE0tkn-ROUo6VA7M2S54"  # Replace with your Firebase API key

# Firebase Authentication API endpoints
base_url = "https://identitytoolkit.googleapis.com/v1"
signup_url = f"{base_url}/accounts:signUp?key={api_key}"
signin_url = f"{base_url}/accounts:signInWithPassword?key={api_key}"

# Create a container for content
content_container = st.container()

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
        nav_page("AI")
        return states["Home"]
    else:
        st.error(result["error"]["message"])
        return states["Login"]

if state == states["Login"]:
    if st.button("Sign up"):
        signup(email, password)
        # Clear the content container to remove previous content
    if st.button("Sign in"):
        state = signin(email, password)
        # Clear the content container to remove previous content
        content_container.empty()
