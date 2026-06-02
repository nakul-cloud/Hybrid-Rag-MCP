from mcp.server.fastmcp import FastMCP

from .tools import (
    search
)

mcp = FastMCP("Retrieval MCP")


@mcp.tool()
def search_tool(
    query: str,
    top_k: int = 5
):
    """
    Search the vector store for relevant chunks.
    """
    return search(query, top_k)


if __name__ == "__main__":
    mcp.run()
