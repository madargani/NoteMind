import typer
import chromadb
from pprint import pprint
from pathlib import Path
import ollama

app = typer.Typer()

@app.command()
def chat(query: str):
    response = ollama.chat(
        model='gemma3n',
        messages=[{
            'role': 'user',
            'content': query
        }]
    )
    print(response)
