# Retrieval MCP (V3)

## Overview

Retrieval MCP exposes semantic search and Gemini-powered RAG over stored document chunks, plus document ingestion via MCP tooling.

Version:

```text
V3
```

Status:

```text
Completed
```

---

# Responsibilities

* Accept a user query
* Search the vector store
* Return ranked chunks with metadata
* Run Gemini-powered question answering
* Ingest new documents into Qdrant
* Support document-level filtering

---

# Architecture

## Query Flow

```mermaid
flowchart TB
    Q[Question] --> R[Qdrant]
    R --> T[Top Chunks]
    T --> G[Gemini]
    G --> A[Answer]
```

## Ingestion Flow

```mermaid
flowchart TB
    D[New PDF] --> I[ingest_document]
    I --> Q[Qdrant]
```

---

# Components

## retrieval_engine.py

Responsibilities:

* Execute vector search
* Return scored results

---

## rag_engine.py

Responsibilities:

* Build context from top K chunks
* Generate grounded answers via Gemini
* Return citations with source metadata

---

## tools.py

Responsibilities:

* Provide MCP tool wrappers
* Validate and format responses
* Connect to ingestion service

---

## schemas.py

Responsibilities:

* Define request and response models
* Standardize payloads

---

# Tools

## Tool Summary

| Tool | Purpose |
|------|---------|
| semantic_search | Search relevant chunks (optionally filtered by document) |
| ask_documents | Gemini-powered RAG answers |
| bm25_search | Keyword search using BM25 |
| ingest_document | Ingest new PDFs into Qdrant |
| list_documents | List indexed documents |
| get_collection_stats | Collection statistics |

## semantic_search

Input:

```json
{
  "query": "revenue growth",
  "top_k": 5,
  "document_name": "sample.pdf"
}
```

Output:

```json
{
  "results": [
    {
      "document_name": "sample.pdf",
      "page": 1,
      "section": "1 Introduction",
      "chunk_id": "chunk_0001",
      "chunk_type": "base",
      "content_type": "text",
      "chunk_text": "...",
      "score": 0.86
    }
  ]
}
```

---

## get_collection_stats

Returns collection stats for the documents collection.

Output:

```json
{
  "collection_name": "documents",
  "points_count": 40,
  "vector_dimension": 768,
  "distance_metric": "COSINE"
}
```

---

## list_documents

Lists unique document names currently stored.

Output:

```json
{
  "documents": [
    "sample.pdf"
  ]
}
```

---

## ask_documents

Runs Gemini-powered RAG over the top K chunks.

Input:

```json
{
  "query": "What is the research gap?",
  "top_k": 8,
  "document_name": "sample.pdf"
}
```

Output:

```json
{
  "answer": "...",
  "sources": [
    {
      "document_name": "sample.pdf",
      "page": 9,
      "section": "5 Research Gap",
      "score": 0.48,
      "snippet": "..."
    }
  ]
}
```

---

## ingest_document

Ingests a new document into Qdrant via the ingestion pipeline.

Input:

```json
{
  "file_path": "data/samples/sample.pdf"
}
```

Output:

```json
{
  "status": "success",
  "document_name": "sample.pdf",
  "file_type": ".pdf",
  "details": {
    "pages": 19,
    "chunks": 40,
    "vectors": 40
  }
}
```

If the document already exists, the tool returns:

```json
{
  "status": "skipped",
  "document_name": "sample.pdf",
  "message": "Document already exists"
}
```

---

## bm25_search

Runs BM25 keyword search over stored chunks.

Input:

```json
{
  "query": "research gap",
  "top_k": 5
}
```

Output:

```json
[
  {
    "document_name": "sample.pdf",
    "page": 9,
    "section": "5 Research Gap",
    "chunk_id": "chunk_0017",
    "chunk_type": "base",
    "content_type": "text",
    "chunk_text": "...",
    "score": 4.21
  }
]
```

---

# Schemas

## RetrievalRequest

```json
{
  "query": "...",
  "top_k": 5,
  "document_name": "sample.pdf"
}
```

## RetrievalResult

```json
{
  "document_name": "sample.pdf",
  "page": 1,
  "section": "1 Introduction",
  "chunk_id": "chunk_0001",
  "chunk_type": "base",
  "content_type": "text",
  "chunk_text": "...",
  "score": 0.86
}
```

## RetrievalResponse

```json
{
  "results": [
    {
      "document_name": "sample.pdf",
      "page": 1,
      "chunk_id": "chunk_0001",
      "chunk_type": "base",
      "content_type": "text",
      "chunk_text": "...",
      "score": 0.86
    }
  ]
}
```

---

# Verification

* MCP Inspector
* Semantic Search
* Gemini Integration
* Source Attribution
* Document Ingestion

---

# Future Roadmap

* Hybrid retrieval (dense + sparse)
* Reranking
* Multimodal retrieval