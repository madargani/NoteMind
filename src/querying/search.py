from appdirs import user_data_dir
from pathlib import Path
import chromadb

def search(notemind_name: str, query: str, n_results: int = 10) -> chromadb.QueryResult:
    vector_db_path = Path(user_data_dir('notemind')) / 'vector_db'
    client = chromadb.PersistentClient(vector_db_path)
    collection = client.get_collection(notemind_name)

    results = collection.query(query_texts=query, n_results=n_results)

    return results
