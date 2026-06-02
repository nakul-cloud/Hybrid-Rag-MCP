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

chunk_records = []

for idx, chunk in enumerate(
    sample_chunks,
    start=1
):

    chunk_records.append(

        {
            "document_name":
            "sample.pdf",

            "page":
            1,

            "chunk_id":
            f"chunk_{idx:04d}",

            "chunk_type":
            "base",

            "content_type":
            "text",

            "chunk_text":
            chunk
        }
    )

ingestor = (
    QdrantIngestor()
)

ingestor.ingest_chunks(
    collection_name="documents",

    chunk_records=chunk_records
)