# Retrieval MCP (V2)

## Overview

Retrieval MCP exposes semantic search over stored document chunks.

Version:

```text
V2
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
Question
  |
  v
Qdrant Retrieval
  |
  v
Top K Chunks
  |
  v
Gemini
  |
  v
Answer
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

## ask_documents

Runs Gemini-powered RAG over the top K chunks.

Input:

```json
{
  "query": "What is the research gap?",
  "top_k": 8
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
      "score": 0.48,
      "snippet": "..."
    }
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

# Verification

✅ MCP Inspector
✅ Semantic Search
✅ Gemini Integration
✅ Source Attribution

---

# Future Roadmap

## V3

* Multimodal retrieval
* Reranking
* Hybrid search (dense + sparse)
