import typer
from pathlib import Path

from madargani_notemind.core.get_status import get_status

app = typer.Typer()

@app.command()
def status():
    # Check if .notemind dir exists
    if not (Path.cwd() / '.notemind').exists():
        print('`.notemind` directory could not be found. Use `notemind init` to generate one.')
        raise typer.Exit(code=1)

    print(*get_status(Path.cwd()), sep='\n')
