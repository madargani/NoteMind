import typer
from pathlib import Path
import sqlite3
import chromadb

from madargani_notemind.core.get_status import get_status
from madargani_notemind.core.chunk_text import chunk_text
from madargani_notemind.core.update_embeddings import update_embeddings

app = typer.Typer()

@app.command()
def commit():
    # Check if .notemind dir exists
    base_path = Path.cwd()
    if not (base_path / '.notemind').exists():
        print('`.notemind` directory could not be found. Use `notemind init` to generate one.')
        raise typer.Exit(code=1)

    # Get files that need to be updated
    files_to_update = [x for x in get_status(base_path) if x[2] != 'Up-to-date']

    # Update embeddings
    update_embeddings(base_path, files_to_update)

    # Update sqlite db
    con = sqlite3.connect(base_path / '.notemind/file_status.db')
    cur = con.cursor()
    cur.executemany(
        '''
        INSERT INTO FILE_STATUS VALUES(?, ?)
            ON CONFLICT(FILE) DO UPDATE SET
                LAST_MODIFIED=EXCLUDED.LAST_MODIFIED;
        ''',
        [(x[0], x[1]) for x in files_to_update]
    )
    con.commit()
    con.close()
