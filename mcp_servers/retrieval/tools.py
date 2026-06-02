from mcp_servers.retrieval.retrieval_engine import (
    RetrievalEngine
)

from mcp_servers.retrieval.schemas import (
    RetrievalRequest
)
from mcp_servers.retrieval.rag_engine import (
    RAGEngine
)

_rag_engine = None

_engine = None


def get_engine():

    global _engine

    if _engine is None:
        _engine = RetrievalEngine()

    return _engine


def semantic_search_tool(
    query: str,
    top_k: int = 5
):

    engine = get_engine()

    request = RetrievalRequest(
        query=query,
        top_k=top_k
    )

    response = engine.semantic_search(
        request
    )

    return response.model_dump()


def get_collection_stats_tool():
    engine = get_engine()

    return engine.get_collection_stats()


def list_documents_tool():
    engine = get_engine()

    return {
        "documents":
        engine.list_documents()
    }

def get_rag_engine():

    global _rag_engine

    if _rag_engine is None:

        _rag_engine = (
            RAGEngine()
        )

    return _rag_engine

def ask_documents_tool(
    query: str,
    top_k: int = 5
):

    rag_engine = (
        get_rag_engine()
    )

    return rag_engine.ask_documents(
        query=query,
        top_k=top_k
    )