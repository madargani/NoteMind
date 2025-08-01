from pathlib import Path
import sqlite3

def init_state_db(path: Path) -> None:
    con = sqlite3.connect(path)
    con.close()
