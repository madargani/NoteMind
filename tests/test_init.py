import pytest
from typer.testing import CliRunner
from pathlib import Path

from madargani_notemind.cli import app

runner = CliRunner()

def test_clean_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ['init'])
    assert result.exit_code == 0

    notemind_dir = tmp_path / '.notemind'

    assert notemind_dir.exists()
    assert (notemind_dir / 'file_status.db').exists()
    assert (notemind_dir / 'vector_db.chroma').exists()
