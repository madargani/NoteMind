from pathlib import Path
from typing_extensions import List, Tuple
import sqlite3
from .core.get_files import get_files

def get_status(dir_path: Path) -> List[Tuple[str, str]]:
    if not (dir_path / '.notemind').exists():
        raise Exception(f'Failed to get status of notemind. {dir_path / '.notemind'} does not exist')

    tracked_files = {}
    cur_files = {}

    # Tracked files
    con = sqlite3.connect(dir_path / '.notemind/file_status.db')
    cur = con.cursor()
    cur.execute('SELECT PATH, LAST_MODIFIED FROM FILE_STATUS')
    for path, last_modified in cur.fetchall():
        tracked_files[path] = last_modified
    con.close()

    # Current files
    for file in get_files(dir_path):
        cur_files[str(file.relative_to(dir_path))] = file.stat().st_mtime

    # Compare file timestamps
    statuses = []

    for path, last_modified in cur_files.items():
        if path not in tracked_files:
            statuses.append((path, 'New'))
        elif tracked_files[path] != last_modified:
            statuses.append((path, 'Modified'))
        else:
            statuses.append((path, 'Up-to-date'))

    for path, last_modified in tracked_files.items():
        if path not in cur_files:
            statuses.append((path, 'Deleted'))
        
    return statuses
