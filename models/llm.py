from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

def load_llm():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(
        model = "gpt-4o-mini",
        timeout = 60,
        max_retries = 2,
        api_key = api_key
    )
    return llm