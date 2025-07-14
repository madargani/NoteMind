import typer
from pathlib import Path
import sqlite3

from madargani_notemind.core.get_files import get_files

app = typer.Typer()

@app.command()
def commit():
    # Check if .notemind dir exists
    if not (Path.cwd() / '.notemind').exists():
        print('`.notemind` directory could not be found. Use `notemind init` to generate one.')
        raise typer.Exit(code=1)

    # Retrieve file statuses from db
    con = sqlite3.connect(Path.cwd() / '.notemind/file_status.db')
    
    # Retrieve current file states
    files = get_files(Path.cwd())
    for file in files:
        print(file.name, file.stat().st_mtime)

    # Find files that are not up to date
    data = [(file.name, file.stat().st_mtime, 'up-to-date') for file in files]

    # Update database
    cur = con.cursor()
    cur.executemany('''
        INSERT INTO FILE_STATUS VALUES(?, ?, ?)
            ON CONFLICT(FILE) DO UPDATE SET
                LAST_MODIFIED=EXCLUDED.LAST_MODIFIED,
                STATUS='up-to-date';
        ''',
        data
    )
    con.commit()

    # close db connection
    con.close()
