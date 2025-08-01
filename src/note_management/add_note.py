from appdirs import user_data_dir
from pathlib import Path
import chromadb

from src.note_management.extract_text import extract_text
from src.note_management.chunk_text import chunk_text

def add_note(notemind_name: str, note_path: Path):
    vector_db_path = Path(user_data_dir('notemind')) / 'vector_db'
    client = chromadb.PersistentClient(vector_db_path)
    collection = client.get_collection(notemind_name)

    text = extract_text(note_path)
    if text == None:
        return
    chunks = chunk_text(text)

    ids = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(f'{note_path}_chunk{i}')
        documents.append(chunk)
        metadatas.append({
            'source': str(note_path.absolute()),
            'chunk_index': i,
        })

    collection.add(ids=ids, documents=documents, metadatas=metadatas)

