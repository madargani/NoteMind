import pytest
from pathlib import Path

from src.note_management.add_note import add_note

def test_add_note():
     add_note('mind_a', Path('/home/madargani/Mei/1_Projects/notemind/plan_v1.md'))
