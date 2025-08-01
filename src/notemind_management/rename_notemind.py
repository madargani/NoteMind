from appdirs import user_data_dir
from pathlib import Path
import chromadb

def rename_notemind(name: str, new_name: str) -> None:
    vector_db_path = Path(user_data_dir('notemind')) / 'vector_db'
    client = chromadb.PersistentClient(vector_db_path)

    collection = client.get_collection(name)

    collection.modify(new_name)
