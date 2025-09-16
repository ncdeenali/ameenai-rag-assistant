# AmeenAI RAG Assistant 💳🤖

AmeenAI is a Retrieval-Augmented Generation (RAG) assistant prototype built with **LangChain** and **LCEL**, designed to answer questions about Arab Bank consumer cards.  
It demonstrates how to structure external data into a knowledge base, embed it into a vector database, and query it using modern LLMs.

---

## ✨ Features
* **Custom Knowledge Base**: Consumer card info structured into `cards.json`  
* **Semantic Chunking**: Splits text into meaningful chunks before indexing  
* **Vector Store**: Uses **ChromaDB** for storage and retrieval  
* **Embeddings**: `nomic-embed-text` (via Ollama)  
* **LLM**: `gpt-4o-mini` from OpenAI for responses  
* **Prompt Engineering**: Variable injection of retrieved docs into the response template  
* **Chains**: Built with **LangChain Expression Language (LCEL)**  

---

## 📂 Project Structure
* `chains/` – LCEL chain definitions  
* `chromadb/` – Vector database files  
* `data/` – Raw and structured JSON data (`cards.json`)  
* `models/` – Placeholder for future models  
* `prompt/` – Prompt templates  
* `rag/` – Ingestion and RAG pipeline scripts  
* `main.py` – Entry point to run the assistant  
* `req.txt` – Python dependencies  
* `README.md` – Project documentation  

---

## ⚙️ Setup

1. Create a virtual environment  
   * Windows: `python -m venv venv && venv\Scripts\activate`  
   * Mac/Linux: `python -m venv venv && source venv/bin/activate`  

2. Install dependencies  
   * `pip install -r req.txt`  

3. Add your API key in a `.env` file  
   * `OPENAI_API_KEY=your_key_here`  

---

## 🚀 How to Run

* Ingest data into the vector DB  
  * `$env:PYTHONPATH = "."; python rag/ingest.py`  

* Run the assistant  
  * `$env:PYTHONPATH = "."; python main.py`  

---

## 💡 Example Query
* **User**: What is the cashback rate for the Visa Platinum card?  
* **Assistant**: …  

---

## 🔮 Future Work
* Add more financial product categories (loans, accounts, etc.)  
* Expand to multilingual support  
* Deploy as a web app with FastAPI + Streamlit  
