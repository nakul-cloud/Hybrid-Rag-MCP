from .retrieval_engine import (
    RetrievalEngine
)

from .schemas import (
    RetrievalResponse,
    RetrievalResult
)

_engine = RetrievalEngine()


def search(
    query: str,
    top_k: int = 5
):
    results = _engine.search(
        query=query,
        top_k=top_k
    )

    return RetrievalResponse(
        results=[
            RetrievalResult(**item)
            for item in results
        ]
    ).model_dump()
