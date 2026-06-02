

from pathlib import Path
import sys

# Allow running this file directly by adding the repo root to sys.path.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from embeddings.embedder import (
    HybridEmbedder
)

from vector_store.collections import (
    CollectionManager
)

embedder = HybridEmbedder()

dimension = (
    embedder.get_dimension()
)

print(
    f"Embedding Dimension: {dimension}"
)

manager = CollectionManager()

manager.create_documents_collection(
    vector_size=dimension
)