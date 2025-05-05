from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit UI
st.title('CHATBOT With LLAMA2')
input_text = st.text_input("Search the topic u want")

# LLM Setup
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))

# Render-compatible startup block
if __name__ == "__main__":
    import streamlit.web.cli as stcli
    import sys
    port = os.environ.get("PORT", 8501)
    sys.argv = ["streamlit", "run", "localama.py", "--server.port", str(port)]
    sys.exit(stcli.main())
