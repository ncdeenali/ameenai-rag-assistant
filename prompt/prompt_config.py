from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path

def load_prompt():
    sysprompt_path = Path(__file__).parent / "sysprompt.txt"
    sysprompt = sysprompt_path.read_text(encoding = "utf-8")

    prompt_template = ChatPromptTemplate([
        ("system", sysprompt + "\n\nCONTEXT\n{context}"),
        ("human", "{input}")
    ])
    return prompt_template