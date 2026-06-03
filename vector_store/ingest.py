import hashlib

from qdrant_client.models import PointStruct

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
        chunk_records: list
    ):

        points = []

        texts = [
            record["chunk_text"]
            for record in chunk_records
        ]

        vectors = (
            self.embedder.embed_batch(
                texts
            )
        )

        for record, vector in zip(
            chunk_records,
            vectors
        ):

            point = PointStruct(

                id=hashlib.md5(

                    (
                        record["document_name"]
                        + str(record["page"])
                        + record["chunk_text"]
                    ).encode("utf-8")

                ).hexdigest(),

                vector=vector,

                payload={

                    "document_name":
                    record["document_name"],

                    "page":
                    record["page"],

                    "chunk_id":
                    record["chunk_id"],

                    "chunk_type":
                    record["chunk_type"],

                    "content_type":
                    record["content_type"],

                    "chunk_text":
                    record["chunk_text"]
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