#save file
#open terminal
#cd desktop
#streamlit run main.py   
import streamlit as st
import requests
import webbrowser
import openai
from streamlit.components.v1 import html
userinfo = """Checking Account Information:
Checking Account 1: 653488429683f20dd518894c
ID: 653488429683f20dd518894c

Type: Checking

Nickname: Check

Rewards: 0

Balance: 15500

Customer ID: 65347c4e9683f20dd5188949

Credit Card Account Information:
Credit Card Account 1: 65347d259683f20dd518894a
ID: 65347d259683f20dd518894a

Type: Credit Card

Nickname: Test

Rewards: 0

Balance: 0

Customer ID: 65347c4e9683f20dd5188949

Credit Card Account 2: 65347fc49683f20dd518894b
ID: 65347fc49683f20dd518894b

Type: Credit Card

Nickname: string

Rewards: 0

Balance: 10000

Customer ID: 65347c4e9683f20dd5188949

There are no bills for your account.

Deposit Information:
Deposit 1: 653489799683f20dd518894d
ID: 653489799683f20dd518894d

Medium: balance

Transaction_date: 2023-10-22

Status: executed

Amount: 500

Description: paycheck

Payee_id: 653488429683f20dd518894c

Type: deposit

Loan Information:
Loan 1: 65348ab29683f20dd518894e
ID: 65348ab29683f20dd518894e

Type: home

Status: pending

Credit_score: 687

Monthly_payment: 750

Amount: 10000

Description: Home loan

Creation_date: 2023-10-22

Account ID: 653488429683f20dd518894c

There are no purchases for your account."""

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

st.title("Talk to the bunny")

openai.api_key = "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"

if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
        st.session_state.messages = [[{"role": "system", "content": "You are a comprehensive financial advisor, well-versed in all aspects of financial planning and literacy. Assist the user in achieving financial well-being by addressing budgeting, savings, investments, debt management, insurance, and retirement planning. Offer tailored advice based on the user's specific needs and financial goals. Also make conversation and keep the conversation flowing, talk with the user. Always end the message in a relevant question to ask the user.Here is the user information such as balance info. You will help them with it if they ask for it: {userinfo}"}]]
        st.session_state.messages.append([{"role": "assistant", "content": "Hi! How can I help you with your financial needs?"}])
for messages in st.session_state.messages:
        for message in messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

if prompt := st.chat_input("Type question"):
        st.session_state.messages.append([{"role": "user", "content": prompt}])
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for messages in st.session_state.messages
                    for m in messages
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages[-1].append({"role": "assistant", "content": full_response})

button_clicked = st.button("Click for a Financial Quiz")

# Check if the button is clicked
if button_clicked:
    nav_page("quiz")
