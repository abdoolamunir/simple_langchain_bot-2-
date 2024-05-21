from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

# initialize
load_dotenv()

# Getting environment keys from .env file

langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# Set environment variables for LangChain and OpenAI
os.environ["LANGCHAIN_TRACING_V2"] = "true"
if langchain_api_key is not None:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please answer user queries"),
        ("user", "Question: {question}")
    ]
)

# Streamlit framework setup
st.title("LangChain Chatbot with OLLAMA")
input_text = st.text_input("Search the topic you'd like to know about!")

# Ollama Gemma as LLM
llm = Ollama(model = "gemma")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)


