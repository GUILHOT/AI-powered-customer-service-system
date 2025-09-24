#!/usr/bin/env python3
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from openai import OpenAI

# Load environment variables
load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Chat with the Chatbot!", page_icon="🤖")

st.title("Chat with the Chatbot! 🤖")
st.markdown("*(System message includes detailed instructions about OrderBot)*")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Service Assistant"}
    ]

# User input
user_input = st.text_input("You:", key="user_input", placeholder="Enter text here...")

# Dummy implementation of process_user_message
def process_user_message(user_input, messages, debug=False):
    # Step 1: Append the user's message
    messages.append({"role": "user", "content": user_input})

    # Step 2: Call OpenAI to get the assistant's reply
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7
    )

    # Step 3: Extract the assistant's reply
    bot_reply = response.choices[0].message.content

    # Step 4: Append the assistant's reply to the message history
    messages.append({"role": "assistant", "content": bot_reply})


    # Step 5: Return the reply and updated message history
    return bot_reply, messages


# On send button click
if st.button("Send", key="send_button") and user_input:
        # Do NOT append user message here
    response, updated_messages = process_user_message(user_input, st.session_state.messages[1:], debug=False)
    st.session_state.messages = [{"role": "system", "content": "You are Service Assistant"}] + updated_messages
    st.rerun()


    # Clear input
    st.rerun()

# Display chat history
for msg in st.session_state.messages[1:]:  # skip system message
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Service Assistant:** {msg['content']}")

