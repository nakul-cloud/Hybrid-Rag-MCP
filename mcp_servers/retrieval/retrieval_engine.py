from embeddings.embedder import HybridEmbedder

from vector_store.qdrant_client import (
    QdrantConnection
)

from mcp_servers.retrieval.schemas import (
    RetrievalRequest,
    RetrievalResult,
    RetrievalResponse
)


class RetrievalEngine:

    def __init__(self):

        self.client = (
            QdrantConnection()
            .get_client()
        )

        self.embedder = (
            HybridEmbedder()
        )

        self.collection_name = (
            "documents"
        )

    def semantic_search(
        self,
        request: RetrievalRequest
    ) -> RetrievalResponse:

        query_vector = (
            self.embedder.embed_text(
                request.query
            )
        )

        search_results = (
            self.client.search(
                collection_name=
                self.collection_name,

                query_vector=
                query_vector,

                limit=
                request.top_k
            )
        )

        results = []

        for hit in search_results:

            payload = hit.payload

            result = RetrievalResult(

                document_name=
                payload.get(
                    "document_name",
                    "unknown"
                ),

                page=
                payload.get(
                    "page",
                    0
                ),

                chunk_id=
                payload.get(
                    "chunk_id",
                    "unknown"
                ),

                chunk_type=
                payload.get(
                    "chunk_type",
                    "base"
                ),

                content_type=
                payload.get(
                    "content_type",
                    "text"
                ),

                chunk_text=
                payload.get(
                    "chunk_text",
                    ""
                ),

                score=
                float(
                    hit.score
                )
            )

            results.append(
                result
            )

        return RetrievalResponse(
            results=results
        )

    def get_collection_stats(
        self
    ):

        collection_info = (
            self.client.get_collection(
                self.collection_name
            )
        )

        return {

            "collection_name":
            self.collection_name,

            "points_count":
            collection_info.points_count,

            "vector_dimension":
            collection_info.config.params.vectors.size,

            "distance_metric":
            str(
                collection_info.config
                .params
                .vectors
                .distance
            )
        }

    def list_documents(
        self,
        limit: int = 100
    ):

        points, _ = (
            self.client.scroll(
                collection_name=
                self.collection_name,

                limit=limit,

                with_payload=True,

                with_vectors=False
            )
        )

        documents = set()

        for point in points:

            document_name = (
                point.payload.get(
                    "document_name"
                )
            )

            if document_name:

                documents.add(
                    document_name
                )

        return sorted(
            list(documents)
        )