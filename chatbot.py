import google.generativeai as genai
import streamlit as st

GOOGLE_API_KEY = "AIzaSyA4ng1ai7JSsfDkEL-geIuOl9vUwWZpvZA"
genai.configure(api_key=GOOGLE_API_KEY)

# Model Initiate
model = genai.GenerativeModel('gemini-1.5-flash')

def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        color: #2c3e50;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #2c3e50;
        border-radius: 5px;
        border: 1px solid #bdc3c7;
        padding: 10px;
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #2980b9;
    }
    .chat-message {
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .user-message {
        background-color: #3498db;
        color: white;
    }
    .bot-message {
        background-color: #ecf0f1;
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

st.title("uzair-chatbot")
st.write("Powered by Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(label="Enter your message", max_chars=2000)
    submit_button = st.form_submit_button("Send")

if submit_button:
    if user_input:
        response = get_chatbot_response(user_input)
        st.session_state.history.append((user_input, response))
    else:
        st.warning("Please enter a prompt")

# Display chat history
for user_msg, bot_msg in st.session_state.history:
    st.markdown(f'<div class="chat-message user-message">You: {user_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-message bot-message">Bot: {bot_msg}</div>', unsafe_allow_html=True)
