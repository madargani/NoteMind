import chromadb
from pathlib import Path

from .chunk_text import chunk_text
from .extract_text import extract_text

def update_embeddings(dir_path: Path, files: list[tuple[str, str]]):
    # Connect to vector db
    client = chromadb.PersistentClient(dir_path / '.notemind/chroma')
    collection = client.get_collection('notemind')

    for file_path, status in files:
        # If not new delete old embeddings before adding new ones
        if status != 'New':
            collection.delete(where={'source': file_path})
        if status == 'Deleted':
            continue
        ids = []
        documents = []
        metadatas = []

        text = extract_text(dir_path / file_path)
        if text == None:
            continue

        for i, chunk in enumerate(chunk_text(text)):
            ids.append(f'{file_path}_chunk{i}')
            documents.append(chunk)
            metadatas.append({
                'source': file_path,
                'chunk_index': i,
            })
        if len(documents) == 0:
            continue
        collection.add(ids=ids, documents=documents, metadatas=metadatas)
