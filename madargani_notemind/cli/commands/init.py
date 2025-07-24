from types import NoneType
import typer
from pathlib import Path
from typing_extensions import Annotated
from madargani_notemind.api.init_notemind import init_notemind

app = typer.Typer()

@app.command()
def init(
    dir_path: Annotated[Path | NoneType, typer.Argument()] = None
):
    """
    Create hidden notemind directory if it doesn't exist
    """
    if dir_path is None:
        dir_path = Path.cwd()

    # Check if base directory exists
    if not dir_path.is_dir():
        print(f'{dir_path} is not a directory.')
        raise typer.Exit(code=1)

    notemind_dir = dir_path / '.notemind'

    # Check if .notemind exists
    if notemind_dir.exists():
        print(f'{notemind_dir} already exists')
        raise typer.Exit()

    init_notemind(dir_path)

    print(f'Initialized notemind directory at `{dir_path / '.notemind'}`')
