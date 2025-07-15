import typer
from pathlib import Path
import sqlite3

from madargani_notemind.core.get_status import get_status

app = typer.Typer()

@app.command()
def commit():
    # Check if .notemind dir exists
    if not (Path.cwd() / '.notemind').exists():
        print('`.notemind` directory could not be found. Use `notemind init` to generate one.')
        raise typer.Exit(code=1)

    # Get files that need to be indexed
    files_to_update = [(x[0], x[1]) for x in get_status(Path.cwd()) if x[2] != 'Up-to-date']

    # chunk

    # generate embeddings

    # update sqlite db
    con = sqlite3.connect(Path.cwd() / '.notemind/file_status.db')
    cur = con.cursor()
    cur.executemany(
        '''
        INSERT INTO FILE_STATUS VALUES(?, ?)
            ON CONFLICT(FILE) DO UPDATE SET
                LAST_MODIFIED=EXCLUDED.LAST_MODIFIED;
        ''',
        files_to_update
    )
    con.commit()
    con.close()
