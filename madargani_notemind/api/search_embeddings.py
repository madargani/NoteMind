from pathlib import Path
import chromadb

def search_embeddings(dir_path: Path, query: str, n_results: int = 10) -> chromadb.QueryResult:
    client = chromadb.PersistentClient(dir_path / '.notemind/vector_db.chroma')
    collection = client.get_collection('notemind')

    results = collection.query(query_texts=query, n_results=n_results)

    return results
