from appdirs import user_data_dir
from pathlib import Path

from src.app_init.init_state_db import init_state_db
from src.app_init.init_vector_db import init_vector_db

def init_app_data() -> None:
    data_dir = Path(user_data_dir('notemind'))
    state_db_path = data_dir / 'state.db'
    vector_db_path = data_dir / 'vector_db'

    # delete existing files in data dir
    for root, dirs, files in data_dir.walk(top_down=False):
        for name in files:
            (root / name).unlink()
        for name in dirs:
            (root / name).rmdir()

    data_dir.mkdir(exist_ok=True)
    init_state_db(state_db_path)
    init_vector_db(vector_db_path)


init_app_data()
