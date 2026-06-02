from mcp.server.fastmcp import FastMCP

try:
    from .tools import (
        parse_pdf,
        get_pdf_metadata,
        extract_page,
        extract_document_text
    )
except ImportError:
    from pathlib import Path
    import sys

    ROOT_DIR = Path(__file__).resolve().parents[2]
    if str(ROOT_DIR) not in sys.path:
        sys.path.insert(0, str(ROOT_DIR))

    from mcp_servers.pdf_parser.tools import (
        parse_pdf,
        get_pdf_metadata,
        extract_page,
        extract_document_text
    )

mcp = FastMCP("PDF Parser MCP")


@mcp.tool()
def parse_pdf_tool(file_path: str):
    """
    Parse a PDF and return summary information.
    """
    return parse_pdf(file_path)


@mcp.tool()
def get_pdf_metadata_tool(file_path: str):
    """
    Extract PDF metadata.
    """
    return get_pdf_metadata(file_path)


@mcp.tool()
def extract_page_tool(
    file_path: str,
    page_number: int
):
    """
    Extract text from a specific page.
    """
    return extract_page(file_path, page_number)


@mcp.tool()
def extract_document_text_tool(file_path: str):
    """
    Extract text from all pages.
    """
    return extract_document_text(file_path)


if __name__ == "__main__":
    mcp.run()