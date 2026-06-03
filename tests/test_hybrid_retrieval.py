from retrieval.retrieval_engine import (
    RetrievalEngine
)

from retrieval.bm25_qdrant_retriever import (
    BM25Retriever
)

from retrieval.hybrid_retriever import (
    HybridRetriever
)

from mcp_servers.retrieval.schemas import (
    RetrievalRequest
)


query = "research gap"

print("\nDENSE RESULTS\n")

dense = (
    RetrievalEngine()
)

dense_results = (
    dense.semantic_search(
        RetrievalRequest(
            query=query,
            top_k=5
        )
    )
)

for result in dense_results.results:

    print(
        result.document_name,
        result.page,
        result.score
    )

print("\nBM25 RESULTS\n")

bm25 = (
    BM25Retriever()
)

for result in bm25.search(
    query,
    top_k=5
):

    print(
        result["document_name"],
        result["page"],
        result["score"]
    )

print("\nHYBRID RESULTS\n")

hybrid = (
    HybridRetriever()
)

for result in hybrid.search(
    query,
    top_k=5
):

    print(
        result["document_name"],
        result["page"],
        result["score"]
    )