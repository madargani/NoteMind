from pathlib import Path
import chromadb

def init_vector_db(path: Path) -> None:
    _ = chromadb.PersistentClient(path)
