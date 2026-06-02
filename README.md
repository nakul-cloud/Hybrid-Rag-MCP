# Hybrid PDF + OCR Retrieval Pipeline with MCP

## Overview

Hybrid PDF + OCR Retrieval Pipeline with MCP is an advanced Retrieval-Augmented Generation (RAG) system designed to process, understand, and retrieve information from complex real-world documents.

Traditional RAG systems perform well on clean PDFs containing plain text. However, enterprise documents such as annual reports, financial statements, contracts, research papers, compliance documents, and scanned records often contain multi-column layouts, tables, images, charts, footnotes, and OCR-dependent content that standard retrieval pipelines fail to process effectively.

This project addresses these challenges by combining document parsing, layout analysis, OCR, table extraction, semantic search, and Model Context Protocol (MCP) based orchestration into a modular and scalable architecture.

The system intelligently analyzes uploaded documents, routes them through specialized MCP servers, stores structured document representations in Qdrant, and enables accurate context-aware question answering using Large Language Models.

---

# Project Status

Phase 1  PDF Parser MCP        DONE
Phase 2  Chunking              DONE
Phase 3  Embeddings            DONE
Phase 4  Qdrant                DONE
Phase 5  Ingestion Pipeline    DONE
Phase 6  Retrieval MCP         DONE
Phase 7  Groq RAG              NEXT
Phase 8  OCR MCP               NEXT
Phase 9  Table MCP             NEXT

---

# Problem Statement

Most document chat systems follow a simple pipeline:

Document → Text Extraction → Chunking → Embeddings → Vector Database → Retrieval → LLM

While effective for clean text documents, this approach struggles with:

* Scanned PDFs
* Multi-column layouts
* Financial reports
* Research papers
* Contracts
* Tables and charts
* Images containing text
* Headers and footers
* Mixed document structures

As a result, important information is often lost during ingestion, reducing retrieval accuracy and answer quality.

This project aims to build a robust document intelligence platform capable of handling real-world document complexity.

---

# Objectives

The primary objectives of this project are:

* Build a layout-aware document ingestion pipeline
* Support both digital and scanned PDFs
* Implement OCR-based text extraction
* Extract structured tables from documents
* Preserve document hierarchy and layout information
* Store embeddings in Qdrant Vector Database
* Use MCP for modular tool orchestration
* Enable semantic retrieval over heterogeneous document content
* Improve answer quality for complex document queries
* Build a scalable architecture suitable for enterprise document intelligence systems

---

# Key Features

## PDF Structure Analysis

Analyze uploaded documents and identify:

* Page count
* Metadata
* Layout type
* Multi-column sections
* Tables
* Images
* Scanned content

---

## OCR Processing

Extract text from:

* Scanned PDFs
* Image-based pages
* Embedded document images

---

## Table Extraction

Preserve structured information including:

* Rows
* Columns
* Headers
* Relationships

---

## Layout-Aware Parsing

Detect and separate:

* Headers
* Footers
* Body content
* Captions
* Side notes
* Section boundaries

---

## Intelligent Chunking

Generate semantic chunks based on:

* Headings
* Sections
* Tables
* Layout structure
* Document hierarchy

---

## Semantic Search

Support:

* Dense vector search
* Metadata filtering
* Context retrieval
* Source attribution

---

## Conversational Question Answering

Allow users to ask natural language questions over ingested documents while maintaining source grounding.

---

# System Architecture

```text
User Query
        |
        v
Retrieval MCP
        |
        v
Retrieval Engine
        |
        v
Qdrant

PDF
        |
        v
PDF Parser MCP
        |
        v
Chunking
        |
        v
Embedding
        |
        v
Qdrant
```

---

# MCP Architecture

The project follows a modular MCP-based design where each document processing capability is implemented as an independent MCP server.

## PDF Parser MCP

Responsibilities:

* Open PDF files
* Extract text
* Extract metadata
* Extract page information

---

## OCR MCP

Responsibilities:

* Detect image-based content
* Perform OCR
* Return structured text output

---

## Table Extraction MCP

Responsibilities:

* Detect tables
* Extract tabular content
* Preserve relationships

---

## Layout Analysis MCP

Responsibilities:

* Detect document structure
* Handle multi-column layouts
* Identify headers and footers
* Preserve hierarchy

---

## Vector Store MCP

Responsibilities:

* Store embeddings
* Manage collections
* Perform vector operations

---

## Retrieval MCP

Responsibilities:

* Semantic search
* Context assembly
* Retrieval orchestration

---

# Technology Stack

## Backend

* Python
* FastAPI

## Agent Framework

* LangGraph

## MCP

* Model Context Protocol (MCP)

## Document Processing

* PyMuPDF

## OCR

* DocTR (Planned)
* PaddleOCR (Alternative)

## Table Extraction

* Camelot

## Embeddings

* Sentence Transformers

## Vector Database

* Qdrant (Local Docker Deployment)

## LLM Providers

### Primary

* Gemini

### Alternative

* Ollama (Local Models)

## Frontend

### Phase 1

* Streamlit

### Phase 2

* Next.js
* TypeScript
* Tailwind CSS
* shadcn/ui

## Development Environment

* VS Code
* UV Package Manager
* Docker Desktop

---

# Project Structure

```text
hybrid-rag-mcp/

├── agent/
│   └── graph.py
│
├── app/
│   ├── config.py
│   └── settings.py
│
├── mcp_servers/
│   ├── pdf_parser/
│   ├── ocr/
│   ├── table_extractor/
│   ├── layout_analyzer/
│   ├── vector_store/
│   └── retrieval/
│
├── ingestion/
│   └── pipeline.py
│
├── embeddings/
│   └── embedder.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── samples/
│
├── qdrant_storage/
│
├── docs/
│
├── tests/
│
├── .env
├── pyproject.toml
├── README.md
└── main.py
```

---

# Development Roadmap

## Phase 1 – Foundation

* Project setup
* UV environment setup
* Docker setup
* Local Qdrant deployment
* Sample document collection

---

## Phase 2 – PDF Parser MCP

* PDF extraction
* Metadata extraction
* Page-level processing
* MCP integration

---

## Phase 3 – Ingestion Pipeline

* Chunk generation
* Metadata generation
* Embedding generation
* Qdrant storage

---

## Phase 4 – Retrieval System

* Semantic search
* Context retrieval
* Source attribution

---

## Phase 5 – OCR MCP

* Scanned PDF support
* Image text extraction
* OCR pipeline integration

---

## Phase 6 – Table Extraction MCP

* Structured table extraction
* Table-aware retrieval

---

## Phase 7 – Layout Analysis MCP

* Multi-column support
* Header/footer removal
* Layout-aware chunking

---

## Phase 8 – LangGraph Orchestration

* Tool routing
* Workflow management
* MCP orchestration

---

## Phase 9 – Streamlit Interface

* Document upload
* Chat interface
* Retrieval inspection
* MCP execution monitoring

---

## Phase 10 – Production Frontend

* Next.js frontend
* TypeScript integration
* Dashboard
* Analytics
* Document management

---

# Future Enhancements

* Multi-document reasoning
* Hybrid search (dense + keyword)
* Chart understanding
* Multi-modal retrieval
* Knowledge graph integration
* Multi-agent workflows
* Enterprise document intelligence platform
* User authentication and role-based access
* Document versioning

---
 
