from langchain_chroma import Chroma
from models.embedder import load_embedder

embedder = load_embedder()
PERSIST_DIR = "./chromadb"

def chromadb(name: str) -> Chroma:
    return Chroma(
        collection_name = name,
        embedding_function = embedder,
        persist_directory = PERSIST_DIR
    )

def store_vectors(texts: list[str]):
    vector = chromadb("ameenai")
    vector.delete_collection()
    vector = chromadb("ameenai")
    vector.add_texts(texts)
    print(f"Stored {len(texts)} texts into ChromaDB at {PERSIST_DIR}.")

def load_vectors() -> Chroma:
    vector = chromadb("ameenai")
    return vector
