import openai
import streamlit as st

st.title("Talk to the bunny")

openai.api_key = "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"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = [[{"role": "system", "content": "You are a comprehensive financial advisor, well-versed in all aspects of financial planning and literacy. Assist the user in achieving financial well-being by addressing budgeting, savings, investments, debt management, insurance, and retirement planning. Offer tailored advice based on the user's specific needs and financial goals. Also make conversation and keep the conversation flowing, talk with the user. Always end the message in a relevant question to ask the user."}]]
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
