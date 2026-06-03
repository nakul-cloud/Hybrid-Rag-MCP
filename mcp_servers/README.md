# MCP Servers Overview

This folder contains the MCP servers that make up the document intelligence pipeline.

## Servers

* pdf_parser
  * Status: Completed (V2)
  * Responsibilities: PDF parsing, metadata extraction, page text extraction

* retrieval
  * Status: Completed (V3)
  * Responsibilities: Semantic search, collection stats, document listing, Gemini RAG, document ingestion, document-level filtering
  * Tools: semantic_search, get_collection_stats, list_documents, ask_documents, ingest_document

* ocr
  * Status: Planned (V1)
  * Responsibilities: OCR for scanned pages

* table_extractor
  * Status: Planned (V1)
  * Responsibilities: Table detection and extraction

* layout_analyzer
  * Status: Planned (V1)
  * Responsibilities: Layout parsing and section detection

* vector_store
  * Status: Planned (V1)
  * Responsibilities: MCP access to vector store operations

## Running Locally

Use the MCP server list in VS Code or run modules directly:

```bash
uv run python -m mcp_servers.pdf_parser.server
uv run python -m mcp_servers.retrieval.server
```
