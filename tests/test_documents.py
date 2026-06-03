from pathlib import Path
import sys

# Allow running this file directly by adding the repo root to sys.path.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from qdrant_client import QdrantClient

client = QdrantClient(
    host="localhost",
    port=6333
)

points, _ = client.scroll(
    collection_name="documents",
    limit=10000,
    with_payload=True,
    with_vectors=False
)

print(
    "Total Points:",
    len(points)
)