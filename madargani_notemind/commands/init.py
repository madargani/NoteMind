import typer

from pathlib import Path
from typing import Optional
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def init(
    base_dir: Annotated[Path, typer.Argument()] = Path.cwd()
):
    """
    Create hidden notemind directory if it doesn't exist
    """

    print("base dir: ", base_dir.absolute())

    # Check if .notemind exists
    if (base_dir / '.notemind').exists():
        print('notemind directory already exists')

    # Create .notemind directory
