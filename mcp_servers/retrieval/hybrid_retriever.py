from mcp_servers.retrieval.bm25_qdrant_retriever import (
    BM25Retriever
)

from mcp_servers.retrieval.retrieval_engine import (
    RetrievalEngine
)

from mcp_servers.retrieval.schemas import (
    RetrievalRequest
)


class HybridRetriever:

    def __init__(self):

        self.dense_retriever = (
            RetrievalEngine()
        )

        self.bm25_retriever = (
            BM25Retriever()
        )

    def _build_key(
        self,
        document_name: str,
        page: int,
        chunk_id: str
    ):

        return (
            f"{document_name}::{page}::{chunk_id}"
        )

    def rrf_fusion(
        self,
        dense_results,
        bm25_results,
        k: int = 60
    ):

        scores = {}

        for rank, result in enumerate(
            dense_results
        ):

            key = self._build_key(
                result.document_name,
                result.page,
                result.chunk_id
            )

            scores[key] = (
                scores.get(key, 0)
                + 1 / (k + rank + 1)
            )

        for rank, result in enumerate(
            bm25_results
        ):

            key = self._build_key(
                result.get("document_name"),
                result.get("page"),
                result.get("chunk_id")
            )

            scores[key] = (
                scores.get(key, 0)
                + 1 / (k + rank + 1)
            )

        return scores

    def search(
        self,
        query: str,
        top_k: int = 5,
        document_name: str | None = None
    ):

        retrieval_k = max(
            top_k * 3,
            20
        )

        dense_response = (
            self.dense_retriever
            .semantic_search(

                RetrievalRequest(
                    query=query,
                    top_k=retrieval_k,
                    document_name=document_name
                )
            )
        )

        dense_results = (
            dense_response.results
        )

        bm25_results = (
            self.bm25_retriever.search(
                query=query,
                top_k=retrieval_k
            )
        )

        if document_name:

            bm25_results = [
                result
                for result in bm25_results
                if result.get("document_name") == document_name
            ]

        fused_scores = (
            self.rrf_fusion(
                dense_results,
                bm25_results
            )
        )

        chunk_lookup = {}

        for result in dense_results:

            key = self._build_key(
                result.document_name,
                result.page,
                result.chunk_id
            )

            chunk_lookup[key] = (
                result.model_dump()
            )

        for result in bm25_results:

            key = self._build_key(
                result.get("document_name"),
                result.get("page"),
                result.get("chunk_id")
            )

            if key in chunk_lookup:
                continue

            chunk_lookup[key] = {

                "document_name":
                result.get("document_name"),

                "page":
                result.get("page"),

                "section":
                result.get("section", "Unknown"),

                "chunk_id":
                result.get("chunk_id"),

                "chunk_type":
                result.get("chunk_type", "base"),

                "content_type":
                result.get("content_type", "text"),

                "chunk_text":
                result.get("chunk_text", ""),

                "score":
                float(result.get("score", 0.0))
            }

        sorted_scores = sorted(
            fused_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        results = []

        for key, score in sorted_scores[:top_k]:

            result = chunk_lookup.get(key)

            if not result:
                continue

            result["score"] = float(score)

            results.append(result)

        return results
