import pytest
from typer.testing import CliRunner
from pathlib import Path
import shutil
import chromadb

from madargani_notemind.cli import app

runner = CliRunner()

def test_sample_notes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    shutil.copytree('tests/sample_notes', tmp_path / 'notes')

    monkeypatch.chdir(tmp_path)
    runner.invoke(app, ['init'])

    result = runner.invoke(app, ['commit'])
    assert result.exit_code == 0

    print(result.stdout)

    client = chromadb.PersistentClient('.notemind/chroma')
    collection = client.get_collection('notemind')

    assert collection.count() > 0
