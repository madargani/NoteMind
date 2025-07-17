import chromadb
from pathlib import Path

from madargani_notemind.core.chunk_text import chunk_text

def update_embeddings(base_path: Path, files_to_update: list[tuple[str, float, str]]):
    client = chromadb.PersistentClient(base_path / '.notemind/vector_db.chroma')
    collection = client.get_collection('notemind')
    for file_path, last_modified, status in files_to_update:
        if status == 'New':
            ids = []
            documents = []
            metadatas = []
            for i, chunk in enumerate(chunk_text((base_path / file_path).read_text())):
                ids.append(f'{file_path}_chunk{i}')
                documents.append(chunk)
                metadatas.append({
                    'source': file_path,
                    'chunk_index': i,
                    'last_modified': last_modified
                })
            collection.add(ids=ids, documents=documents, metadatas=metadatas)
