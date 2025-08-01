from appdirs import user_data_dir
from pathlib import Path
import chromadb

def create_notemind(name: str):
    vector_db_path = Path(user_data_dir('notemind')) / 'vector_db'
    client = chromadb.PersistentClient(vector_db_path)
    
    _ = client.create_collection(name)
