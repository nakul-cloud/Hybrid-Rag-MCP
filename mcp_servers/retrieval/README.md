# Retrieval MCP (V1)

## Overview

Retrieval MCP exposes semantic search over stored document chunks.

Version:

```text
V1
```

Status:

```text
In Progress
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

# Planned Tools

## search_tool

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
