# Document Ingestion Pipeline

## V1 (Archived)

### Overview

The Hybrid Chunking Pipeline is responsible for transforming raw document text into retrieval-ready chunks that can later be embedded and stored in a vector database.

Chunking is one of the most critical stages in a Retrieval-Augmented Generation (RAG) system because retrieval quality depends heavily on how information is segmented before embedding generation.

Traditional RAG systems often rely on a single chunking strategy such as fixed-size or recursive chunking. While simple to implement, these approaches may lose contextual relationships between sections, resulting in lower retrieval accuracy.

To address this limitation, this project implements a Hybrid Chunking Strategy that combines recursive splitting, overlapping chunks, and sliding window context generation.

Version:

```text
V1
```

Status:

```text
Completed
```

---

### Objectives

The objectives of the Hybrid Chunking Pipeline are:

* Split large documents into manageable chunks
* Preserve semantic continuity between chunks
* Reduce context fragmentation
* Improve retrieval quality
* Prepare documents for embedding generation
* Support future layout-aware and OCR-aware chunking

---

### Architecture

```text
Raw Document Text
    |
    v
Recursive Chunking
    |
    v
Overlapping Chunks
    |
    v
Sliding Window Context
    |
    v
Final Retrieval Chunks
```

---

### Implemented Chunking Strategies

#### 1. Recursive Chunking

Recursive chunking is used as the primary segmentation strategy.

The splitter attempts to break text using progressively smaller separators:

```text
Paragraphs
    |
    v
Lines
    |
    v
Sentences
    |
    v
Words
```

This helps preserve document structure while maintaining chunk size constraints.

##### Configuration

```python
chunk_size = 1000
chunk_overlap = 200
```

---

#### 2. Overlapping Chunks

To prevent information loss at chunk boundaries, overlapping content is included between consecutive chunks.

Example:

```text
Chunk A
--------------------
Revenue increased...
Market growth...

Chunk B
--------------------
Market growth...
Risk factors...
```

Benefits:

* Preserves context
* Reduces retrieval fragmentation
* Improves answer grounding

---

#### 3. Sliding Window Context

Sliding window chunking creates contextual chunks by combining neighboring chunks.

Example:

```text
Chunk A
Chunk B
Chunk C
```

Generated Context Window:

```text
A + B + C
```

Benefits:

* Provides broader context
* Improves retrieval for multi-section questions
* Preserves cross-section relationships

---

### Current Configuration

#### Chunk Size

```python
1000
```

Represents the maximum number of characters per chunk.

---

#### Chunk Overlap

```python
200
```

Represents the amount of overlapping content shared between chunks.

---

#### Window Size

```python
3
```

Represents the number of neighboring chunks included in the contextual window.

---

### Output Structure

The chunking pipeline produces two outputs:

#### Base Chunks

Used for:

* Precise retrieval
* Embedding generation
* Vector storage

Example:

```python
{
        "base_chunks": [...]
}
```

---

#### Context Chunks

Used for:

* Context enrichment
* Broader retrieval context
* Future hybrid retrieval workflows

Example:

```python
{
        "context_chunks": [...]
}
```

---

### Project Structure

```text
ingestion/

├── chunker.py
├── pipeline.py
└── README.md
```

---

### Verification

#### Test Script

File:

```text
tests/test_chunking.py
```

Command:

```bash
uv run python tests/test_chunking.py
```

---

### Verification Results

#### Recursive Chunk Generation

Status:

```text
PASSED
```

Result:

```text
20 base chunks generated successfully.
```

---

#### Sliding Window Context Generation

Status:

```text
PASSED
```

Result:

```text
20 contextual chunks generated successfully.
```

---

#### Overlap Verification

Status:

```text
PASSED
```

Result:

```text
Chunk overlap preserved contextual continuity between neighboring chunks.
```

---

### Sample Output

```text
Base Chunks: 20
Context Chunks: 20
```

Example output successfully demonstrated:

* Recursive splitting
* Overlapping chunks
* Sliding window context generation

---

### Current Limitations

The current implementation does not yet support:

* Semantic chunking
* Layout-aware chunking
* OCR-aware chunking
* Table-aware chunking
* Section-aware chunking
* Metadata enrichment

These capabilities will be added in future versions.

---

### Future Versions

#### V2

Planned enhancements:

* Semantic chunking
* Document section detection
* Metadata generation

---

#### V3

Planned enhancements:

* Layout-aware chunking
* OCR-aware chunking
* Table-aware chunking
* Multi-modal document chunking

---

### Deliverables Completed

Completed:

* Hybrid chunker implementation
* Recursive chunking
* Overlapping chunking
* Sliding window context generation
* Verification testing
* Documentation

---

### Status

```text
Version: V1
Status: Stable
Verification: Passed
```

---

### Next Component

Embedding Generation Pipeline

Objectives:

* Convert chunks into dense vector representations
* Generate embeddings using local embedding models
* Prepare vectors for Qdrant storage
* Enable semantic retrieval

---

## V1.5 (Current)

### Overview

V1.5 adds page-level metadata, stable chunk identifiers, and standardized payloads for downstream MCP services while keeping the hybrid chunking strategy intact.

Version:

```text
V1.5
```

Status:

```text
Completed
```

---

### Workflow

```text
PDF
    |
    v
PDF Parser MCP
    |
    v
Hybrid Chunker
    |
    v
Hybrid Embedder
    |
    v
Qdrant
```

---

### Verification

```text
PDF Processed: sample.pdf

Pages Extracted: 19

Chunks Created: 40

Vectors Stored: 40
```

---

### Metadata

```json
{
        "document_name": "sample.pdf",
        "page": 1,
        "chunk_id": "chunk_0001",
        "chunk_type": "base",
        "content_type": "text"
}
```
