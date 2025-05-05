# LANGCHAIN_API _KEY ="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 "
# OPENAI_API _KEY ="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"
# LANGCHAIN_PROJECT ="CHATBOT"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template #creating chatbot

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))