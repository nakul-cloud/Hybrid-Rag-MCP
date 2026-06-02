from pathlib import Path
import sys


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from mcp_servers.retrieval.retrieval_engine import (
    RetrievalEngine
)

from mcp_servers.retrieval.schemas import (
    RetrievalRequest
)

engine = RetrievalEngine()

request = RetrievalRequest(
    query="What is this document about?",
    top_k=5
)

response = engine.semantic_search(
    request
)

for result in response.results:

    print("=" * 80)

    print(
        f"Document: {result.document_name}"
    )

    print(
        f"Page: {result.page}"
    )

    print(
        f"Score: {result.score:.4f}"
    )

    print(
        result.chunk_text[:500]
    )