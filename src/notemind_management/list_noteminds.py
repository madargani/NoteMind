from typing import Sequence
from appdirs import user_data_dir
from pathlib import Path
import chromadb

def list_noteminds() -> Sequence[chromadb.Collection]:
    vector_db_path = Path(user_data_dir('notemind')) / 'vector_db'
    client = chromadb.PersistentClient(vector_db_path)

    return client.list_collections()
