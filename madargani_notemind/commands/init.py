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
    notemind_dir = base_dir / '.notemind'

    # Check if .notemind exists
    if notemind_dir.exists():
        print(f'Reinitializing NoteMind in {notemind_dir.absolute()}')
    else:
        print(f'Initializing NoteMind in {notemind_dir.absolute()}')

    # Create .notemind directory
