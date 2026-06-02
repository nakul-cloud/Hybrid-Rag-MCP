# Hybrid PDF + OCR Retrieval Pipeline with MCP

## Overview

Hybrid PDF + OCR Retrieval Pipeline with MCP is a modular Retrieval-Augmented Generation (RAG) system designed for complex enterprise documents.

It combines PDF parsing, hybrid chunking, embeddings, vector storage, and MCP-based orchestration to deliver grounded answers with sources.

---

## What Is Done

* PDF Parser MCP
* Hybrid Chunking
* Hybrid Embeddings
* Qdrant Vector Store
* Ingestion Pipeline
* Retrieval Engine
* Retrieval MCP
* Gemini-Powered RAG

---

## Architecture

### Ingestion Flow

```mermaid
flowchart TB
    A[PDF] --> B[PDF Parser MCP]
    B --> C[Hybrid Chunking]
    C --> D[Hybrid Embeddings]
    D --> E[Qdrant]
```

### Query Flow

```mermaid
flowchart TB
    Q[User Query] --> R[Retrieval MCP]
    R --> S[Semantic Search]
    S --> G[Gemini]
    G --> A[Grounded Answer]
```

---

## Roadmap

```text
Phase 1  - PDF Parser MCP         DONE
Phase 2  - Hybrid Chunking        DONE
Phase 3  - Hybrid Embeddings      DONE
Phase 4  - Qdrant Integration     DONE
Phase 5  - Ingestion Pipeline     DONE
Phase 6  - Retrieval MCP          DONE
Phase 7  - Gemini RAG             DONE
Phase 8  - Document Ingestion MCP NEXT
Phase 9  - OCR MCP                NEXT
Phase 10 - Table Extraction MCP   NEXT
Phase 11 - Layout Analysis MCP    NEXT
Phase 12 - Hybrid Retrieval       NEXT
Phase 13 - Reranking              NEXT
```

---

## Core Modules

### PDF Parser MCP

* Extracts metadata, page text, and document text.

### Ingestion Pipeline

* Hybrid chunking
* Metadata filtering
* Embedding generation
* Qdrant upsert

### Retrieval MCP

* `semantic_search`
* `get_collection_stats`
* `list_documents`
* `ask_documents`

---

## Key Capabilities

* Hybrid chunking with context windows
* Embeddings with sentence-transformers
* Qdrant vector search
* Gemini-powered grounded answers
* MCP orchestration for tool separation

---

## Project Structure

```text
hybrid-rag-mcp/

├── agent/
├── app/
├── embeddings/
├── ingestion/
├── llm/
├── mcp_servers/
│   ├── pdf_parser/
│   ├── retrieval/
│   ├── ocr/
│   ├── table_extractor/
│   ├── layout_analyzer/
│   └── vector_store/
├── vector_store/
├── data/
├── tests/
└── main.py
```

---

## Future Enhancements

Not yet implemented:

* Document Ingestion MCP
* OCR MCP
* Table Extraction MCP
* Layout Analysis MCP
* Hybrid Retrieval
* Reranking

---

## Technology Stack

* Python
* MCP (FastMCP)
* Qdrant
* PyMuPDF
* Sentence Transformers
* Gemini SDK
