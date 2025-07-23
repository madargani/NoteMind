import typer
import chromadb
from pprint import pprint
from pathlib import Path
from typing import Annotated
import ollama

app = typer.Typer()

@app.command()
def chat(query: str, n_results: Annotated[int, typer.Option()] = 10):
    base_dir = Path.cwd()
    client = chromadb.PersistentClient(base_dir / '.notemind/vector_db.chroma')
    collection = client.get_collection('notemind')

    results = collection.query(query_texts=query, n_results=n_results)

    context_chunks = results['documents'][0]

    context = "\n---\n".join(context_chunks)
    prompt = f'''Use the following note excerpts to answer the question: 

    {context}

    Question:

    {query}
    '''

    messages = [
        {
            'role': 'user',
            'content': prompt
        }
    ]
    for part in ollama.chat('gemma3n', messages=messages, stream=True):
        print(part['message']['content'], end='', flush=True)
    print()
