from typing import Annotated
import typer
from rich import print
from pathlib import Path
from madargani_notemind.api import search_embeddings
from madargani_notemind.api.search_embeddings import search_embeddings

app = typer.Typer()

@app.command()
def search(query: str, n_results: Annotated[int, typer.Option()] = 10):
    results = search_embeddings(Path.cwd(), query, n_results)

    for i in range(len(results['ids'][0])):
        print(f'[bold green]{results['metadatas'][0][i]['source']}[/bold green]')
        print(f'{results['documents'][0][i]}')
        print()

