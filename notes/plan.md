# NoteMind Plan

## Languages and tools
Python:
- good for machine learning (transformers, LLM)
- Streamlit

File Ingestion:
- PyMuPDF
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
- CLI: Typer
- Web UI: Streamlit

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

## Structure

### API folder
API folder will contain commands for all the core functionalities. This will make it easier to transition to a gui app or to any other application. Devs can interact with a simple api instead of copying code. One file per function.

functions:
- init_notemind(dir_path: Path) -> int
- get_status(dir_path: Path) -> List\[Path, str\]
- commit(dir_path: Path) -> int
- search(dir_path: Path, query: str) -> List\[QueryResult\]
- chat(dir_path: Path, query: str, stream: bool = True) -> Iterator\[ChatResponse\]

## Example walk through
1. User installs notemind
2. `cd into note directory`
3. `notemind init`
4. user adds new file to note directory
5. `notemind status` traverse through directory tree and metadata store searching for files that haven't been indexed yet
6. `notemind commit` generates embeddings, stores embeddings and metadata of new file
7. `notemind chat {query}` prompts rag chatbot
