import pytest

from src.notemind_management.list_noteminds import list_noteminds
from src.querying.ask import ask

def test_ask():
    print(list_noteminds())
    response = ask('mind_a', 'hello world')
    print(query)
