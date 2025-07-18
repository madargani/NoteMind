import typer
from typing_extensions import Annotated
from pathlib import Path
from rich.table import Table
from rich.console import Console

from madargani_notemind.core.get_status import get_status

app = typer.Typer()

@app.command()
def status(
    all: Annotated[bool, typer.Option()] = False,
):
    # Check if .notemind dir exists
    if not (Path.cwd() / '.notemind').exists():
        print('`.notemind` directory could not be found. Use `notemind init` to generate one.')
        raise typer.Exit(code=1)
    
    # Get filter and sort statuses
    statuses = get_status(Path.cwd())
    if not all:
        statuses = [x for x in statuses if x[2] != 'Up-to-date'] 
    statuses.sort(key=lambda x:x[2])

    # Print table
    table = Table('file', 'status')
    for file, last_modifed, status in statuses:
        table.add_row(file, status)
    Console().print(table)
