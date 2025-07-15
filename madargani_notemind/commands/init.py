from click import echo
import typer

from pathlib import Path
from typing_extensions import Annotated

from madargani_notemind.core.init_file_status_db import init_file_status_db
from madargani_notemind.core.init_vector_db import init_vector_db

app = typer.Typer()

@app.command()
def init(
    base_dir: Annotated[Path, typer.Argument()] = None
):
    """
    Create hidden notemind directory if it doesn't exist
    """
    if base_dir is None:
        base_dir = Path.cwd()

    # Check if base directory exists
    if not base_dir.is_dir():
        print(f'{base_dir} is not a directory.')
        raise typer.Exit(code=1)

    notemind_dir = base_dir / '.notemind'

    # Check if .notemind exists
    if notemind_dir.exists():
        print(f'{notemind_dir} already exists')
        raise typer.Exit()

    # Create .notemind directory
    notemind_dir.mkdir()

    init_file_status_db(notemind_dir)
    init_vector_db(notemind_dir)
