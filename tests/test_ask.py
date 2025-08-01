import pytest

from src.querying.ask import ask

def test_ask():
    response = ask('mind_a', 'hello world')
    print(response)
