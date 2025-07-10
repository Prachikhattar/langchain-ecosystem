from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os

# dotenv is a Python library used to load environment variables from a .env file.
from dotenv import load_dotenv

# To load the variables from .env file
load_dotenv()

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
  [
    ("system","You are helpful assistant. Please respond to the user query"),
    ("user", "Question:{question}")
  ]
)

## streamlit framework
st.title("Langchain Demo with Ollama")
input_text = st.text_input("Search the topic you want")

# Ollama LLM
llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
  ## chain.run is used for running simple chains with single input and output.
  ## chain.invoke accepts a dictionary of input and returns structured output.
  st.write(chain.invoke({'question':input_text}))


