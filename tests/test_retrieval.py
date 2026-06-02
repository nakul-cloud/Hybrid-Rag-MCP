from pathlib import Path
import sys


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from mcp_servers.retrieval.retrieval_engine import (
    RetrievalEngine
)

engine = RetrievalEngine()

results = (
    engine.semantic_search(
        "What is this document about?"
    )
)

for item in results:

    print("=" * 60)

    print(
        f"Score: {item['score']}"
    )

    print(
        f"Page: {item['page']}"
    )

    print(
        item["chunk_text"][:500]
    )