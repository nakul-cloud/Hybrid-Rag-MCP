from mcp_servers.retrieval.retrieval_engine import (
    RetrievalEngine
)

from mcp_servers.retrieval.schemas import (
    RetrievalRequest
)
from mcp_servers.retrieval.rag_engine import (
    RAGEngine
)
from ingestion.ingestion_service import (
    DocumentIngestionService
)
from mcp_servers.retrieval.bm25_qdrant_retriever import (
    BM25Retriever
)

from mcp_servers.retrieval.hybrid_retriever import (
    HybridRetriever
)

_rag_engine = None

_engine = None

_ingestion_service = None



def get_engine():

    global _engine

    if _engine is None:
        _engine = RetrievalEngine()

    return _engine


def semantic_search_tool(
    query: str,
    top_k: int = 5,
    document_name: str | None = None
):

    engine = get_engine()

    request = RetrievalRequest(
        query=query,
        top_k=top_k,
        document_name=
        document_name
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
    top_k: int = 5,
    document_name: str | None = None
):

    rag_engine = (
        get_rag_engine()
    )

    return rag_engine.ask_documents(
        query=query,
        top_k=top_k,
        document_name=
        document_name
    )
def get_ingestion_service():

    global _ingestion_service

    if _ingestion_service is None:

        _ingestion_service = (
            DocumentIngestionService()
        )

    return _ingestion_service


def ingest_document_tool(
    file_path: str
):
    return (
        get_ingestion_service()
        .ingest_document(file_path)
    )


def bm25_search_tool(
    query: str,
    top_k: int = 5
):
    """
    BM25 keyword search.
    """

    retriever = BM25Retriever()

    return retriever.search(
        query=query,
        top_k=top_k
    )


def hybrid_search_tool(
    query: str,
    top_k: int = 5,
    document_name: str | None = None
):
    """
    Hybrid search (dense + BM25) with RRF fusion.
    """

    retriever = HybridRetriever()

    return retriever.search(
        query=query,
        top_k=top_k,
        document_name=document_name
    )