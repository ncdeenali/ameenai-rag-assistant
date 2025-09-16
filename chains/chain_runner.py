from rag.vector_store import load_vectors
from chains.chain_config import load_chain

def run_chain(user_query: str, k: int = 3):
    vs = load_vectors()
    docs = vs.similarity_search(user_query)

    if docs:
        context = "\n\n".join(
            (
                f"{d.page_content}\n\n"
                f"URL: {d.metadata.get('url', '')}\n"
                f"Application Methods: {', '.join(d.metadata.get('application_methods', []))}"
            )
            for d in docs
        )
    else:
        context = ""
    
    chain = load_chain()
    response = chain.invoke({
        "context": context,
        "input": user_query
    })
    return response.content