from pathlib import Path

from mcp_servers.pdf_parser.pdf_utils import (
    extract_all_text
)

from ingestion.chunker import (
    HybridChunker
)

from vector_store.ingest import (
    QdrantIngestor
)


class IngestionPipeline:

    def __init__(self):

        self.chunker = (
            HybridChunker()
        )

        self.ingestor = (
            QdrantIngestor()
        )

    def process_pdf(
        self,
        pdf_path: str
    ):

        print(
            f"\nProcessing: {pdf_path}"
        )

        pages = extract_all_text(
            pdf_path
        )

        print(
            f"Pages Extracted: {len(pages)}"
        )

        chunk_records = []

        chunk_counter = 1

        for page in pages:

            page_number = (
                page["page_number"]
            )

            page_text = (
                page["content"]
            )

            chunk_result = (
                self.chunker.create_chunks(
                    page_text
                )
            )

            base_chunks = (
                chunk_result[
                    "base_chunks"
                ]
            )

            for chunk in base_chunks:

                chunk_records.append(

                    {
                        "document_name":
                        Path(pdf_path).name,

                        "page":
                        page_number,

                        "chunk_id":
                        f"chunk_{chunk_counter:04d}",

                        "chunk_type":
                        "base",

                        "content_type":
                        "text",

                        "chunk_text":
                        chunk
                    }
                )

                chunk_counter += 1

        print(
            f"Chunks Created: {len(chunk_records)}"
        )

        self.ingestor.ingest_chunks(
            collection_name="documents",

            chunk_records=
            chunk_records
        )

        print(
            "Ingestion Complete"
        )