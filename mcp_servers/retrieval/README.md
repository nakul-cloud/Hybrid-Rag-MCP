# Retrieval MCP (V1)

## Overview

Retrieval MCP exposes semantic search over stored document chunks.

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

* Accept a user query
* Search the vector store
* Return ranked chunks with metadata
* Support downstream MCP servers

---

# Architecture

```text
Query
  |
  v
Retrieval MCP
  |
  v
Qdrant
```

---

# Components

## retrieval_engine.py

Responsibilities:

* Execute vector search
* Return scored results

---

## tools.py

Responsibilities:

* Provide MCP tool wrappers
* Validate and format responses

---

## schemas.py

Responsibilities:

* Define request and response models
* Standardize payloads

---

# Tools

## semantic_search

Input:

```json
{
  "query": "revenue growth",
  "top_k": 5
}
```

Output:

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

# Schemas

## RetrievalRequest

```json
{
  "query": "...",
  "top_k": 5
}
```

## RetrievalResult

```json
{
  "document_name": "sample.pdf",
  "page": 1,
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

# Verification Results

## Retrieval Engine Test

Command:

```bash
uv run python tests/test_retrieval.py
```

Status:

```text
PASSED
```

---

# Future Roadmap

## V2

* Groq RAG integration
* Ask-documents MCP tool
* Answer grounding with citations
