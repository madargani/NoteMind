import sqlite3
from pathlib import Path

from madargani_notemind.core.get_files import get_files

def get_status(dir_path: Path):
    # status from db
    con = sqlite3.connect(dir_path / '.notemind/file_status.db')
    cur = con.cursor()
    res = cur.execute('SELECT * FROM FILE_STATUS')
    db_status = res.fetchall()
    db_status = {row[0]: row[1] for row in db_status}
    con.close()

    # Calculate new status
    new_status = []
    for file in get_files(dir_path):
        file_name = str(file.relative_to(dir_path))
        status = 'Up-to-date'
        if file_name not in db_status:
            status = 'New'
        elif file.stat().st_mtime > db_status[file_name]:
            status = 'Modified'
        new_status.append((file_name, file.stat().st_mtime, status))
        if file_name in db_status:
            db_status.pop(file_name)

    # Deleted files
    for name, mtime in db_status.items():
        new_status.append((name, mtime, 'Deleted'))

    return new_status
