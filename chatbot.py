import google.generativeai as genai 
import streamlit as st

GOOGLE_API_KEY="AIzaSyA4ng1ai7JSsfDkEL-geIuOl9vUwWZpvZA"

genai.configure(api_key=GOOGLE_API_KEY)

#Model Initiate
model= genai.GenerativeModel('gemini-1.5-flash')

def get_chatbot_response(user_input):
   response= model.generate_content(user_input)
   return response.text
st.title ("uzair-chatbot")
st.write("Powered by Generative AI")

if "history" not in st.session_state:
   st.session_state["history"] =[]

# user_input=input("enter yout prompt = ")

# output= get_chatbot_response(user_input)

# print(output)

with st.form (key="chat_form" , clear_on_submit=True):
   user_input = st.text_input(label="Enter your message", max_chars=2000)
   submit_button = st.form_submit_button("send")

if submit_button:
   if user_input:
      
      response = get_chatbot_response(user_input)
      st.session_state.history.append((user_input, response))
   else:
      st.warning("please enter a prompt")