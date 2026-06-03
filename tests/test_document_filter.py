from pathlib import Path
import sys

# Allow running this file directly by adding the repo root to sys.path.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from mcp_servers.retrieval.schemas import (
    RetrievalRequest
)

from mcp_servers.retrieval.retrieval_engine import (
    RetrievalEngine
)

engine = RetrievalEngine()

request = RetrievalRequest(

    query="research gap",

    top_k=5,

    document_name="sample.pdf"
)

response = engine.semantic_search(
    request
)

for result in response.results:

    print(
        result.document_name,
        result.page,
        result.score
    )

for result in response.results:

    print("=" * 80)

    print(
        "Document:",
        result.document_name
    )

    print(
        "Page:",
        result.page
    )

    print(
        "Chunk ID:",
        result.chunk_id
    )

    print(
        "Score:",
        result.score
    )

    print(
        result.chunk_text[:200]
    )