# NoteMind Plan

## Languages and tools
Python:
- good for machine learning (transformers, LLM)
- Streamlit

File Ingestion:
- PyMuPDF, pdfplumber, PyPDF2
- python-docx

Embedding:
- OpenAI(text-embedding-3-small)
- Hugging Face
- InstructorXL

Storing Embeddings:
- JSON or SQLite
- FAISS for fast vector search

Chatbot:
- OpenAI
- Ollama
- LangChain

UI:
- CLI
- Streamlit for Web UI

## Features
- Git like commands

`notemind init`:
- Creates a `.notemind` directory with embedding and metadata data

`notemind status`:
- shows new and edited files without up to date embeddings

`notemind commit`:
- generates and stores embeddings for new/editted files

`notemind chat {prompt}`:
- Answers prompt from user based on embeddings

## Example walk through
1. User installs notemind
2. `cd into note directory`
3. `notemind init`
4. user adds new file to note directory
5. `notemind status` traverse through directory tree and metadata store searching for files that haven't been indexed yet
6. `notemind commit` generates embeddings, stores embeddings and metadata of new file
7. `notemind chat {query}` prompts rag chatbot
