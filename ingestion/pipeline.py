from pathlib import Path

from mcp_servers.pdf_parser.pdf_utils import (
    extract_all_text
)

from ingestion.chunker import (
    HybridChunker
)

from ingestion.filters import (
    ChunkFilter
)

from vector_store.ingest import (
    QdrantIngestor
)

from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
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
        pdf_path: str,
        skip_if_exists: bool = True
    ):

        print(
            f"\nProcessing: {pdf_path}"
        )

        document_name = (
            Path(pdf_path).name
        )

        if skip_if_exists:

            points, _ = (
                self.ingestor.client.scroll(

                    collection_name="documents",

                    limit=1,

                    with_payload=True,

                    with_vectors=False,

                    scroll_filter=Filter(
                        must=[
                            FieldCondition(
                                key="document_name",
                                match=MatchValue(
                                    value=document_name
                                )
                            )
                        ]
                    )
                )
            )

            if points:

                print(
                    "Document already exists. Skipping ingestion."
                )

                return {

                    "status":
                    "skipped",

                    "document_name":
                    document_name,

                    "pages":
                    0,

                    "chunks":
                    0,

                    "vectors":
                    0
                }

        pages = extract_all_text(
            pdf_path
        )

        total_base_chunks = 0

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

            total_base_chunks += (
                len(base_chunks)
            )

            for chunk in base_chunks:

                if ChunkFilter.is_noise_chunk(
                    chunk
                ):
                    continue

                chunk_records.append(

                    {
                        "document_name":
                        document_name,

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

        return {

            "pages":
            len(pages),

            "chunks":
            len(chunk_records),

            "vectors":
            len(chunk_records)
        }


def run_ingestion_pipeline(
    pdf_path: str
):

    pipeline = (
        IngestionPipeline()
    )

    return pipeline.process_pdf(
        pdf_path
    )