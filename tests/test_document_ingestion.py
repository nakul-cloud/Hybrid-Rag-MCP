from pathlib import Path
import sys

# Allow running this file directly by adding the repo root to sys.path.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from ingestion.ingestion_service import (
    DocumentIngestionService
)

service = (
    DocumentIngestionService()
)

response = (
    service.ingest_document(
        "data/samples/sample.pdf"
    )
)

print(response)