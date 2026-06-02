from qdrant_client import QdrantClient


class QdrantConnection:

    def __init__(
        self,
        host="localhost",
        port=6333
    ):
        self.client = QdrantClient(
            host=host,
            port=port
        )

    def get_client(self):
        return self.client