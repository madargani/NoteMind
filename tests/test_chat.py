import pytest
from typer.testing import CliRunner
from pathlib import Path
import shutil

from madargani_notemind.cli import app

runner = CliRunner()

def test_sample_notes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    shutil.copytree('tests/sample_notes', tmp_path / 'notes')

    monkeypatch.chdir(tmp_path)
    runner.invoke(app, ['init'])
    runner.invoke(app, ['commit'])

    result = runner.invoke(app, ['chat', 'how does rag work?'])

    print(result.stdout)
