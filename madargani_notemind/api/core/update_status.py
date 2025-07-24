from pathlib import Path
from typing_extensions import List, Tuple
import sqlite3

def update_status(dir_path: Path, files: List[Tuple[str, str]]):
    con = sqlite3.connect(dir_path / '.notemind/file_status.db')
    cur = con.cursor()
    cur.executemany(
        'DELETE FROM FILE_STATUS WHERE PATH=?;',
        [(x[0],) for x in files if x[1] == 'Deleted']
    )
    cur.executemany(
        '''
        INSERT INTO FILE_STATUS VALUES(?, ?)
            ON CONFLICT(PATH) DO UPDATE SET
                LAST_MODIFIED=EXCLUDED.LAST_MODIFIED;
        ''',
        [(x[0], (dir_path / x[0]).stat().st_mtime) for x in files if x[1] != 'Deleted']
    )
    con.commit()
    con.close()
