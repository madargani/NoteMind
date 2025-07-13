import sqlite3
from pathlib import Path

def init_file_status_db(path: Path):
    # Check if path is valid
    if not path.is_dir():
        raise ValueError('Path does not exist')

    # connect to db
    con = sqlite3.connect(path / 'file_status.db')
    cur = con.cursor()

    # create file status table
    cur.execute('DROP TABLE IF EXISTS FILE_STATUS;')
    cur.execute('''
        CREATE TABLE FILE_STATUS(
            FILE TEXT PRIMARY KEY, 
            LAST_MODIFIED INT NOT NULL, 
            STATUS TEXT NOT NULL
        );
    ''')

    # close connection to db
    con.close()
