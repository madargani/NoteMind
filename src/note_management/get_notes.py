from typing import List
from appdirs import user_data_dir
from pathlib import Path
import chromadb

def get_notes(notemind_name: str) -> List[str]:
    vector_db_path = Path(user_data_dir('notemind')) / 'vector_db'
    client = chromadb.PersistentClient(vector_db_path)
    collection = client.get_collection(notemind_name)

    notes = collection.get(include=["metadatas"])['metadatas']
    notes = {note['source'] for note in notes}

    return notes
