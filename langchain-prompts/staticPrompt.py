import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

st.header('Research Tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summerize'):
    if user_input:
        result = model.invoke(user_input)
        st.write(result.content)  # Changed .text to .content
    else:
        st.warning("Please enter a prompt first!")

#**Static Prompt:**  
#A fixed prompt whose instructions and content remain the same for every
#  user/input.

#**Problem with Static Prompts:**  
#They **cannot adapt to changing context or user needs**, so they may produce
#less relevant or personalized responses and require manual changes when 
# requirements change.

#When i am asking a prompt complete prompt from a user then it can sometimes
#hallucinate and even dont produce good answers