from uuid import uuid4

from qdrant_client.models import (
    PointStruct
)

from vector_store.qdrant_client import (
    QdrantConnection
)

from embeddings.embedder import (
    HybridEmbedder
)


class QdrantIngestor:

    def __init__(self):

        self.client = (
            QdrantConnection()
            .get_client()
        )

        self.embedder = (
            HybridEmbedder()
        )

    def ingest_chunks(
        self,
        collection_name: str,
        chunks: list[str],
        document_name: str
    ):

        points = []

        vectors = (
            self.embedder.embed_batch(
                chunks
            )
        )

        for chunk, vector in zip(
            chunks,
            vectors
        ):

            point = PointStruct(
                id=str(uuid4()),

                vector=vector,

                payload={
                    "document_name":
                    document_name,

                    "chunk_text":
                    chunk,

                    "chunk_type":
                    "base",

                    "content_type":
                    "text"
                }
            )

            points.append(point)

        self.client.upsert(
            collection_name=collection_name,
            points=points
        )

        print(
            f"{len(points)} chunks stored."
        )