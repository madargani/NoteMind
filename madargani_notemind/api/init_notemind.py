from pathlib import Path
from .core.init_file_status_db import init_file_status_db
from .core.init_vector_db import init_vector_db

def init_notemind(dir_path: Path):
    if not dir_path.is_dir():
        raise Exception(f'Failed to initialize notemind. {dir_path} is not a directory.')

    notemind_dir = dir_path / '.notemind'

    if notemind_dir.exists():
        raise Exception(f'Failed to initialize notemind. {notemind_dir} already exists')

    # Create .notemind directory
    notemind_dir.mkdir()
    init_file_status_db(notemind_dir)
    init_vector_db(notemind_dir)
