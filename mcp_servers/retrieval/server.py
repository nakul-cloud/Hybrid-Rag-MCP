from mcp.server.fastmcp import FastMCP

try:
    from .tools import (
        semantic_search_tool,
        get_collection_stats_tool,
        list_documents_tool
    )
except ImportError:
    from pathlib import Path
    import sys

    ROOT_DIR = Path(__file__).resolve().parents[2]
    if str(ROOT_DIR) not in sys.path:
        sys.path.insert(0, str(ROOT_DIR))

    from mcp_servers.retrieval.tools import (
        semantic_search_tool,
        get_collection_stats_tool,
        list_documents_tool
    )

mcp = FastMCP("Retrieval MCP")


@mcp.tool()
def semantic_search(
    query: str,
    top_k: int = 5
):
    """
    Search the vector store for relevant chunks.
    """
    return semantic_search_tool(query, top_k)


@mcp.tool()
def get_collection_stats():
    """
    Return collection statistics for the documents collection.
    """
    return get_collection_stats_tool()


@mcp.tool()
def list_documents():
    """
    List document names currently stored in the collection.
    """
    return list_documents_tool()


if __name__ == "__main__":
    mcp.run()
