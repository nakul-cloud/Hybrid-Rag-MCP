# PDF Parser MCP (V1)

## Overview

PDF Parser MCP is the first Model Context Protocol (MCP) server developed as part of the Hybrid PDF + OCR Retrieval Pipeline.

The purpose of this server is to provide foundational PDF document processing capabilities by exposing document extraction functionality through MCP tools.

This server acts as the entry point of the document ingestion pipeline and is responsible for reading PDF files, extracting metadata, retrieving page-level content, and returning full document text.

Version:

```text
V1
```

Status:

```text
Completed
```

---

# Responsibilities

The PDF Parser MCP server is responsible for:

* Opening PDF documents
* Extracting document metadata
* Extracting page-level text
* Extracting full document text
* Returning structured responses through MCP tools

The server does not perform:

* OCR
* Table extraction
* Embedding generation
* Vector storage
* Semantic retrieval
* LLM inference

These capabilities will be implemented in separate MCP servers.

---

# Architecture

```text
PDF File
    │
    ▼
PDF Parser MCP
    │
 ┌──┼───────────────────┐
 │  │                   │
 ▼  ▼                   ▼

Metadata
Extraction

Page
Extraction

Document
Extraction
```

---

# Technology Stack

Framework:

```text
MCP Python SDK
FastMCP
```

PDF Processing:

```text
PyMuPDF
```

Validation:

```text
Pydantic
```

Development Environment:

```text
VS Code
UV
Docker Desktop
```

---

# Implemented Tools

## parse_pdf_tool

### Purpose

Returns a high-level summary of a PDF document.

### Input

```json
{
  "file_path": "data/samples/sample.pdf"
}
```

### Output

```json
{
  "document_name": "sample.pdf",
  "page_count": 10,
  "total_characters": 25430
}
```

---

## get_pdf_metadata_tool

### Purpose

Extract PDF metadata.

### Input

```json
{
  "file_path": "data/samples/sample.pdf"
}
```

### Output

```json
{
  "title": "Document Title",
  "author": "Author Name",
  "pages": 10
}
```

---

## extract_page_tool

### Purpose

Extract text from a specific page.

### Input

```json
{
  "file_path": "data/samples/sample.pdf",
  "page_number": 1
}
```

### Output

```json
{
  "page_number": 1,
  "content": "Extracted page text..."
}
```

---

## extract_document_text_tool

### Purpose

Extract text from all pages.

### Input

```json
{
  "file_path": "data/samples/sample.pdf"
}
```

### Output

```json
{
  "pages": [
    {
      "page_number": 1,
      "content": "..."
    }
  ]
}
```

---

# Project Structure

```text
pdf_parser/

├── __init__.py
├── server.py
├── tools.py
├── schemas.py
├── pdf_utils.py
└── README.md
```

---

# Verification

## MCP Inspector

Connection Method:

```text
STDIO
```

Command:

```bash
uv
```

Arguments:

```bash
run python -m mcp_servers.pdf_parser.server
```

---

## Tool Discovery

Status:

```text
PASSED
```

Detected Tools:

```text
parse_pdf_tool
get_pdf_metadata_tool
extract_page_tool
extract_document_text_tool
```

---

## PDF Summary Extraction

Status:

```text
PASSED
```

Result:

```text
Document information successfully extracted.
```

---

## Metadata Extraction

Status:

```text
PASSED
```

Result:

```text
Metadata successfully extracted.
```

---

## Page Extraction

Status:

```text
PASSED
```

Result:

```text
Page-level extraction successfully completed.
```

---

## Full Document Extraction

Status:

```text
PASSED
```

Result:

```text
Full document text successfully extracted.
```

---

# Challenges Encountered

## Tool Input Formatting

Issue:

```text
MCP Inspector initially passed JSON input incorrectly.
```

Resolution:

```text
Tool input structure was corrected and validated.
```

---

# Deliverables

Completed:

* MCP Server Setup
* Tool Registration
* PDF Metadata Extraction
* Page Extraction
* Full Document Extraction
* MCP Inspector Validation

---

# Current Limitations

Current version does not support:

* OCR
* Scanned PDFs
* Table extraction
* Layout analysis
* Chunk generation
* Vector storage

---

# Next Version (V2)

Planned enhancements:

* Integration with document ingestion pipeline
* Chunk generation
* Metadata enrichment
* Embedding preparation
* Qdrant integration support

---

# Status

```text
Version: V1
Status: Stable
Verification: Passed
```
