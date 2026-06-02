from qdrant_client.models import (
    Distance,
    VectorParams
)

from vector_store.qdrant_client import (
    QdrantConnection
)


class CollectionManager:

    def __init__(self):
        self.client = (
            QdrantConnection()
            .get_client()
        )

    def create_documents_collection(
        self,
        vector_size: int
    ):
        self.client.recreate_collection(
            collection_name="documents",

            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

        print(
            "Collection 'documents' created successfully."
        )