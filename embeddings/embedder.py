from sentence_transformers import SentenceTransformer


class HybridEmbedder:

    def __init__(
        self,
        model_name: str = "BAAI/bge-base-en-v1.5"
    ):
        self.model = SentenceTransformer(
            model_name
        )

    def embed_text(
        self,
        text: str
    ):
        return self.model.encode(
            text,
            normalize_embeddings=True
        ).tolist()

    def embed_batch(
        self,
        texts: list[str]
    ):
        vectors = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return vectors.tolist()

    def get_dimension(self):
        return self.model.get_sentence_embedding_dimension()