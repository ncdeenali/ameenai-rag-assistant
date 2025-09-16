from models.llm import load_llm
from prompt.prompt_config import load_prompt

def load_chain():
    llm = load_llm()
    prompt = load_prompt()

    chain = prompt | llm
    return chain