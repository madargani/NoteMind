import typer
import chromadb
from pprint import pprint
from pathlib import Path

app = typer.Typer()

@app.command()
def chat(query: str):
    base_dir = Path.cwd()

    client = chromadb.PersistentClient(base_dir / '.notemind/vector_db.chroma')
    collection = client.get_collection('notemind')

    results = collection.query(query_texts=query, n_results=3)
    pprint(results['documents'])

