import json
from langchain_experimental.text_splitter import SemanticChunker
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from models.embedder import load_embedder
from rag.vector_store import store_vectors

embedder = load_embedder()

def load_chunker(embedder):
    chunker = SemanticChunker(
        embeddings = embedder,
        breakpoint_threshold_type = "percentile",
        breakpoint_threshold_amount = 92,
        buffer_size = 1
    )
    capper = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 120,
        separators = ["\n\n", "\n", ". ", " "]
    )
    return chunker, capper

def json_chunker(path: str):
    with open(path, "r", encoding = "utf-8") as f:
        data = json.load(f)

    semantic, capper = load_chunker(embedder)
    all_chunks = []

    for p in data["products"]:
        text = (
            f"Name: {p.get('name')}\n"
            f"Description: {p.get('description')}\n"
            f"Features: {', '.join(p.get('features', []))}\n"
            f"Notes: {', '.join(p.get('assistant_notes', []))}\n"
        )
    
        semantic_chunks = semantic.create_documents([text])
        final_chunks = sum([capper.split_documents([c]) for c in semantic_chunks], [])

        for chunk in final_chunks:
            doc = Document(
                page_content = chunk.page_content,
                metadata = {
                    "name": p.get("name", ""),
                    "category": data.get("category", "Cards"),
                    "url": p.get("url", ""),
                    "application_methods": p.get("application", {}).get("methods", [])
                }
            )
            all_chunks.append(doc)
    
    store_vectors(all_chunks)