from pydantic_core.core_schema import filter_seq_schema
import typer
from pathlib import Path
from madargani_notemind.api.commit_files import commit_files

app = typer.Typer()

@app.command()
def commit():
    # Check if .notemind dir exists
    dir_path = Path.cwd()
    if not (dir_path / '.notemind').exists():
        print('`.notemind` directory could not be found. Use `notemind init` to generate one.')
        raise typer.Exit(code=1)

    commit_files(dir_path)
