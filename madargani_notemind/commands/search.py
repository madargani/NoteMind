from typing import Annotated
import typer
import chromadb
from pprint import pprint
from rich import print
from pathlib import Path

app = typer.Typer()

@app.command()
def search(query: str, n_results: Annotated[int, typer.Option()] = 10):
    base_dir = Path.cwd()

    client = chromadb.PersistentClient(base_dir / '.notemind/vector_db.chroma')
    collection = client.get_collection('notemind')

    results = collection.query(query_texts=query, n_results=n_results)

    for i in range(len(results['ids'][0])):
        print(f'[bold green]{results['metadatas'][0][i]['source']}[/bold green]')
        print(f'{results['documents'][0][i]}')
        print()
    # pprint(results['documents'])

