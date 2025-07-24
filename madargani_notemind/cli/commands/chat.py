import typer
import chromadb
from pprint import pprint
from pathlib import Path
from typing import Annotated
import ollama
from madargani_notemind.api.get_rag_response import get_rag_response

app = typer.Typer()

@app.command()
def chat(query: str, n_results: Annotated[int, typer.Option()] = 10):
    # Stream ollama output
    for part in get_rag_response(Path.cwd(), query, n_results):
        print(part['message']['content'], end='', flush=True)
    print()
