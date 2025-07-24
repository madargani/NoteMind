from pathlib import Path
from .get_status import get_status
from .core.update_status import update_status
from .core.update_embeddings import update_embeddings

def commit_files(dir_path: Path):
    files = [x for x in get_status(dir_path) if x[1] != 'Up-to-date' and x[0][-4:] != '.pdf']
    update_embeddings(dir_path, files)
    update_status(dir_path, files)
