import chromadb

def init_vector_db(dir_path):
    client = chromadb.PersistentClient(dir_path / 'vector_db.chroma')
    client.create_collection(
        name="notemind",
        embedding_function=None
    )
