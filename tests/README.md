# Tests Overview

This README consolidates the per-test notes for quick reference.

---

## test_chunking.py

Purpose:

Validate the hybrid chunker output (base chunks and context chunks) on a fixed sample string.

Command:

```bash
uv run python tests/test_chunking.py
```

Expected Output:

```text
CHUNKING RESULTS
Base Chunks: <count>
Context Chunks: <count>

FIRST BASE CHUNK
<first 500 chars>

FIRST CONTEXT CHUNK
<first 500 chars>
```

Prerequisites:

* Repo root as the working directory.
* Dependencies installed in the active environment.

Troubleshooting:

* If imports fail, ensure you run from the repo root and that `.venv` is active.

---

## test_collection_info.py

Purpose:

Print the Qdrant collection info for the `documents` collection.

Command:

```bash
uv run python tests/test_collection_info.py
```

Expected Output:

```text
CollectionInfo(...)
```

Prerequisites:

* Qdrant is running.
* `documents` collection exists.

Troubleshooting:

* If you see connection errors, confirm the Qdrant host/port in `vector_store/qdrant_client.py`.
* If the collection is missing, run `tests/test_create_collection.py` first.

---

## test_create_collection.py

Purpose:

Create the `documents` collection using the embedding dimension from the model.

Command:

```bash
uv run python tests/test_create_collection.py
```

Expected Output:

```text
Embedding Dimension: 768
```

Prerequisites:

* Qdrant is running.
* The embedding model can be loaded (first run may download weights).

Troubleshooting:

* If the collection already exists, Qdrant may return an error. Delete it or skip creation.
* If the model fails to load, check internet access and HF cache.

---

## test_document_ingestion.py

Purpose:

Ingest a sample document using the document ingestion service.

Command:

```bash
uv run python tests/test_document_ingestion.py
```

Expected Output:

```text
{'status': 'success', 'document_name': 'sample.pdf', 'file_type': '.pdf', 'details': {...}}
```

Prerequisites:

* Qdrant is running.
* `data/samples/sample.pdf` exists.

Troubleshooting:

* If ingestion fails, confirm the PDF path and that the PDF parser is installed.
* If you see a "skipped" status, the document already exists and duplicate protection is active.

---

## test_document_counts.py

Purpose:

Count stored points grouped by document name.

Command:

```bash
uv run python tests/test_document_counts.py
```

Expected Output:

```text
{'sample.pdf': 40}
```

Prerequisites:

* Qdrant is running.

Troubleshooting:

* If counts grow unexpectedly after reingestion, check duplicate protection and point ID strategy.

---

## test_document_filter.py

Purpose:

Run a semantic search filtered to a single document using `document_name`.

Command:

```bash
uv run python tests/test_document_filter.py
```

Expected Output:

```text
sample.pdf 1 0.86
```

Prerequisites:

* Qdrant is running.
* `sample.pdf` is ingested.

Troubleshooting:

* If results are empty, confirm the document name matches the stored payload.

---

## test_documents.py

Purpose:

Print the total points stored in the `documents` collection.

Command:

```bash
uv run python tests/test_documents.py
```

Expected Output:

```text
Total Points: <count>
```

Prerequisites:

* Qdrant is running.

Troubleshooting:

* If the total is zero, run the ingestion pipeline first.

---

## test_embeddings.py

Purpose:

Load the embedding model and generate a single vector from sample text.

Command:

```bash
uv run python tests/test_embeddings.py
```

Expected Output:

```text
LOADING MODEL
Embedding Dimension: 768
VECTOR GENERATED
Vector Length: 768
First 10 Values:
[...]
```

Prerequisites:

* Internet access on first run to download model weights.

Troubleshooting:

* If the model download is slow, set `HF_TOKEN` for higher rate limits.

---

## test_gemini.py

Purpose:

Verify Gemini connectivity and basic generation.

Command:

```bash
uv run python tests/test_gemini.py
```

Expected Output:

```text
Connection Test: True
Model: <model name>
Response:
<text>
```

Prerequisites:

* `GEMINI_API_KEY` available via environment or `.env`.

Troubleshooting:

* If auth fails, verify the API key and that `.env` is loaded.

---

## test_ingest.py

Purpose:

Insert a few sample chunks into the `documents` collection.

Command:

```bash
uv run python tests/test_ingest.py
```

Expected Output:

```text
<message indicating chunks stored>
```

Prerequisites:

* Qdrant is running.
* `documents` collection exists.

Troubleshooting:

* If ingestion fails, confirm Qdrant is running and the collection exists.

---

## test_bm25.py

Purpose:

Run a BM25 search over indexed chunks (for hybrid retrieval work).

Command:

```bash
uv run python tests/test_bm25.py
```

Expected Output:

```text
Document: <name>
Page: <number>
Score: <float>
<chunk excerpt>
```

Prerequisites:

* BM25 retriever implementation is available.

Troubleshooting:

* If the module import fails, the hybrid retrieval implementation is not wired yet.

---

## test_list_collections.py

Purpose:

List all Qdrant collections.

Command:

```bash
uv run python tests/test_list_collections.py
```

Expected Output:

```text
CollectionsResponse(...)
```

Prerequisites:

* Qdrant is running.

Troubleshooting:

* If you see connection errors, confirm the Qdrant host/port in `vector_store/qdrant_client.py`.

---

## test_retrieval.py

Purpose:

Run a semantic search query using the retrieval engine and print top results.

Command:

```bash
uv run python tests/test_retrieval.py
```

Expected Output:

```text
Document: <name>
Page: <number>
Score: <float>
<chunk excerpt>
```

Prerequisites:

* Qdrant is running.
* `documents` collection exists and has points.

Troubleshooting:

* If results are empty, run the ingestion pipeline first.

---

## test_rag.py

Purpose:

Run Gemini-powered RAG over ingested chunks.

Command:

```bash
uv run python tests/test_rag.py
```

Expected Output:

```text
ANSWER
<text>

SOURCES
{...}
```

Prerequisites:

* Qdrant is running and has ingested data.
* `GEMINI_API_KEY` available via environment or `.env`.

Troubleshooting:

* If sources are empty, run the ingestion pipeline first.
* If Gemini fails, verify API credentials.

---

## test_pipeline.py

Purpose:

Run the end-to-end ingestion pipeline on a sample PDF and store vectors in Qdrant.

Command:

```bash
uv run python tests/test_pipeline.py
```

Expected Output:

```text
Processing: data/samples/sample.pdf
Pages Extracted: <count>
Chunks Created: <count>
Ingestion Complete
```

Notes:

* Duplicate protection may return a skipped response if the document already exists.

Prerequisites:

* Qdrant is running.
* `data/samples/sample.pdf` exists.
* PyMuPDF is installed and working.

Troubleshooting:

* If you see `fitz` import errors, ensure PyMuPDF is installed and the `fitz` shadow package is removed.
* If the PDF path is wrong, update the script with the correct file location.

---

## test_qdrant_connection.py

Purpose:

Verify that the Qdrant client can connect and list collections.

Command:

```bash
uv run python tests/test_qdrant_connection.py
```

Expected Output:

```text
CollectionsResponse(...)
```

Prerequisites:

* Qdrant is running.

Troubleshooting:

* If you see connection errors, confirm the Qdrant host/port in `vector_store/qdrant_client.py`.

---

## test_delete_collections.py

Purpose:

Delete the `documents` collection (destructive).

Command:

```bash
uv run python tests/test_delete_collections.py
```

Expected Output:

```text
Collection Deleted
```

Prerequisites:

* Qdrant is running.

Troubleshooting:

* Recreate the collection before ingestion if you delete it.

---

## test_scroll_points.py

Purpose:

Scroll a few points from the `documents` collection and print payloads.

Command:

```bash
uv run python tests/test_scroll_points.py
```

Expected Output:

```text
============================================================
{...payload...}
```

Prerequisites:

* Qdrant is running.
* `documents` collection exists and has points.

Troubleshooting:

* If no points are returned, run the ingestion pipeline first.
