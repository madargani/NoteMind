from pathlib import Path
from typing import Iterator
from .search_embeddings import search_embeddings
import ollama

def get_rag_response(dir_path: Path, query: str, n_results: int = 10) -> Iterator[ollama.ChatResponse]:
    context_chunks = search_embeddings(Path.cwd(), query, n_results)['documents'][0]

    context = "\n---\n".join(context_chunks)
    prompt = f'''Use the following note excerpts to answer the question: 

    {context}

    Question:

    {query}
    '''

    messages = [{'role': 'user', 'content': prompt}]

    return ollama.chat('gemma3n', messages=messages, stream=True)
