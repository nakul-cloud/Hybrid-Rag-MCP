from pathlib import Path
import sys


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from vector_store.ingest import (
    QdrantIngestor
)

sample_chunks = [

    "Revenue increased by 24 percent.",

    "North America grew significantly.",

    "Risk factors remain a concern."
]

ingestor = (
    QdrantIngestor()
)

ingestor.ingest_chunks(
    collection_name="documents",

    chunks=sample_chunks,

    document_name="sample.pdf"
)