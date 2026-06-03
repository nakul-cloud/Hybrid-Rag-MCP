from pathlib import Path
import sys

# Allow running this file directly by adding the repo root to sys.path.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
	sys.path.insert(0, str(ROOT_DIR))

from mcp_servers.retrieval.bm25_qdrant_retriever import (
    BM25Retriever
)

retriever = (
    BM25Retriever()
)

results = retriever.search(
    query="research gap",
    top_k=5
)

for result in results:

    print("=" * 80)

    print(
        "Document:",
        result["document_name"]
    )

    print(
        "Page:",
        result["page"]
    )

    print(
        "Score:",
        result["score"]
    )

    print(
        result["chunk_text"][:400]
    )