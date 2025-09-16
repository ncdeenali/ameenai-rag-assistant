from langchain_ollama import OllamaEmbeddings

def load_embedder():
    embedder = OllamaEmbeddings(model = "nomic-embed-text")
    return embedder