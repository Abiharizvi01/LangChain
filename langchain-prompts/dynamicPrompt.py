import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

st.header('Research Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.text)

"""
Prompt Template

A PromptTemplate in LangChain is a structured way to create prompts
dynamically by inserting variables into a predefined template.

Instead of hardcoding prompts, PromptTemplate allows you to define
placeholders that can be filled in at runtime with different inputs.

This makes it reusable, flexible, and easy to manage, especially when
working with dynamic user inputs or automated workflows.

Why use PromptTemplate over f-strings?
1. Default validation
2. Reusable
3. LangChain Ecosystem
"""