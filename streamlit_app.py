import streamlit as st
from groq import Groq

st.title("💬 Groq Chatbot")
st.write("Chat with AI powered by Groq 🚀")

groq_api_key = st.text_input("Groq API Key", type="password")

if not groq_api_key:
    st.info("Please enter your Groq API Key 🔑")
else:
    client = Groq(api_key=groq_api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What do you want to ask?"):

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        # Groq AI response
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=st.session_state.messages
            )

            answer = response.choices[0].message.content
            st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })
