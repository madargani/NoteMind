from langchain.chat_models import init_chat_model
from langchain import hub
from dotenv import load_dotenv

from src.querying.search import search

def ask(notemind_name: str, query: str, n_results: int = 10):
    context = search(notemind_name, query, n_results)['documents']
    if context is not None:
        context = context[0]

    prompt = hub.pull('rlm/rag-prompt')
    messages = prompt.invoke({'question': query, 'context': context})

    load_dotenv()
    llm = init_chat_model('gemini-2.5-flash-lite', model_provider='google_genai')
    response = llm.invoke(messages)

    return response.content
