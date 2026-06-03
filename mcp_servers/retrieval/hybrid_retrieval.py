from rank_bm25 import BM25Okapi

from vector_store.qdrant_client import (
    QdrantConnection
)


class BM25Retriever:

    def __init__(self):

        self.client = (
            QdrantConnection()
            .get_client()
        )

        self.collection_name = (
            "documents"
        )

        self.documents = []

        self.tokenized_docs = []

        self.bm25 = None

        self._build_index()

    def _build_index(self):

        points, _ = self.client.scroll(
            collection_name=
            self.collection_name,

            limit=10000,

            with_payload=True,

            with_vectors=False
        )

        self.documents = []

        self.tokenized_docs = []

        for point in points:

            payload = point.payload

            text = payload.get(
                "chunk_text",
                ""
            )

            self.documents.append(
                payload
            )

            self.tokenized_docs.append(
                text.lower().split()
            )

        self.bm25 = BM25Okapi(
            self.tokenized_docs
        )

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        query_tokens = (
            query.lower()
            .split()
        )

        scores = (
            self.bm25.get_scores(
                query_tokens
            )
        )

        ranked = sorted(
            zip(
                self.documents,
                scores
            ),
            key=lambda x: x[1],
            reverse=True
        )

        results = []

        for doc, score in ranked[:top_k]:

            results.append(

                {
                    "document_name":
                    doc.get(
                        "document_name"
                    ),

                    "page":
                    doc.get(
                        "page"
                    ),

                    "chunk_id":
                    doc.get(
                        "chunk_id"
                    ),

                    "chunk_type":
                    doc.get(
                        "chunk_type"
                    ),

                    "content_type":
                    doc.get(
                        "content_type"
                    ),

                    "chunk_text":
                    doc.get(
                        "chunk_text"
                    ),

                    "score":
                    float(score)
                }
            )

        return results