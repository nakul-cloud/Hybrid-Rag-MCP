from pathlib import Path
import sys


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from vector_store.qdrant_client import (
    QdrantConnection
)

client = (
    QdrantConnection()
    .get_client()
)

collections = (
    client.get_collections()
)

print(collections)