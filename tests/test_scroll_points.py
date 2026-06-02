from pathlib import Path
import sys

# Allow running this file directly by adding the repo root to sys.path.
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

points, _ = client.scroll(
    collection_name="documents",
    limit=3
)

for point in points:

    print("=" * 60)

    print(
        point.payload
    )