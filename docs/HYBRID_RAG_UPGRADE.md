# Hybrid RAG Upgrade

## Objective

Improve retrieval quality by combining semantic retrieval and keyword retrieval.

---

## Previous Architecture

```text
Query
↓
Dense Retrieval
↓
Gemini
```

Limitations:

- Exact keyword matches could be missed
- Acronyms and entity names were not always ranked correctly
- Retrieval quality depended entirely on embeddings

---

## New Architecture

```text
Query
↓
Dense Retrieval
+
BM25 Retrieval
↓
Reciprocal Rank Fusion (RRF)
↓
Gemini
```

---

## Components Added

### BM25 Retriever

File:

```text
mcp_servers/retrieval/bm25_qdrant_retriever.py
```

Responsibilities:

- Load chunk payloads from Qdrant
- Build BM25 index
- Return keyword-ranked chunks

---

### Hybrid Retriever

File:

```text
mcp_servers/retrieval/hybrid_retriever.py
```

Responsibilities:

- Execute dense retrieval
- Execute BM25 retrieval
- Merge rankings using RRF
- Return fused results

---

### RAG Engine Update

File:

```text
mcp_servers/retrieval/rag_engine.py
```

Changes:

- Replaced `RetrievalEngine` with `HybridRetriever`
- Added section metadata to retrieval context
- Improved retrieval diversity

---

## Validation

Queries tested:

- knowledge gap
- SMART-AI
- customer data

Results:

- BM25 improved exact keyword retrieval
- Dense retrieval improved semantic matching
- Hybrid retrieval combined strengths of both approaches

---

## Current Architecture

```text
PDF Documents
↓
Chunking
↓
Embeddings
↓
Qdrant
↓
Dense Retrieval
+
BM25 Retrieval
↓
RRF Fusion
↓
Gemini
↓
Answer
```
