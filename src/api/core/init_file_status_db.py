import sqlite3
from pathlib import Path

def init_file_status_db(dir_path: Path):
    # connect to db
    con = sqlite3.connect(dir_path / 'file_status.db')
    cur = con.cursor()

    # create file status table
    cur.execute('DROP TABLE IF EXISTS FILE_STATUS;')
    cur.execute('''
        CREATE TABLE FILE_STATUS(
            PATH TEXT PRIMARY KEY, 
            LAST_MODIFIED REAL NOT NULL
        );
    ''')

    # close connection to db
    con.close()
