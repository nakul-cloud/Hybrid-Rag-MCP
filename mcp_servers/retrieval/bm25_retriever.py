from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self):

        self.bm25 = None

        self.documents = []

    def build_index(
        self,
        chunk_records: list
    ):

        self.documents = chunk_records

        corpus = [

            record["chunk_text"]
            .lower()
            .split()

            for record in chunk_records
        ]

        self.bm25 = (
            BM25Okapi(corpus)
        )

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        if self.bm25 is None:

            return []

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

        return ranked[:top_k]