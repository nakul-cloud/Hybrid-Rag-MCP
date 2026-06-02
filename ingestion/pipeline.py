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

        all_chunks = []

        for page in pages:

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

            all_chunks.extend(
                base_chunks
            )

        print(
            f"Chunks Created: {len(all_chunks)}"
        )

        self.ingestor.ingest_chunks(
            collection_name="documents",

            chunks=all_chunks,

            document_name=Path(
                pdf_path
            ).name
        )

        print(
            "Ingestion Complete"
        )