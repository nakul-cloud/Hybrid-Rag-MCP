from pathlib import Path

from ingestion.pipeline import (
    run_ingestion_pipeline
)

from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)

from vector_store.qdrant_client import (
    QdrantConnection
)


class DocumentIngestionService:
    """
    Handles document ingestion requests.

    Responsibilities:
    - Validate file existence
    - Trigger ingestion pipeline
    - Return structured response
    """

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".txt",
        ".md"
    }

    def validate_file(
        self,
        file_path: str
    ):

        path = Path(file_path)

        if not path.exists():

            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        if path.suffix.lower() not in (
            self.SUPPORTED_EXTENSIONS
        ):

            raise ValueError(
                f"Unsupported file type: {path.suffix}"
            )

        return path

    def __init__(self):

        self.client = (
            QdrantConnection()
            .get_client()
        )

    def document_exists(
        self,
        document_name: str
    ):

        points, _ = self.client.scroll(

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

        return len(points) > 0

    def ingest_document(
        self,
        file_path: str
    ):

        try:

            path = self.validate_file(
                file_path
            )

            if self.document_exists(
                path.name
            ):

                return {

                    "status":
                    "skipped",

                    "document_name":
                    path.name,

                    "message":
                    "Document already exists"
                }

            pipeline_result = (
                run_ingestion_pipeline(
                    str(path)
                )
            )

            return {

                "status":
                "success",

                "document_name":
                path.name,

                "file_type":
                path.suffix,

                "details":
                pipeline_result
            }

        except Exception as e:

            return {

                "status":
                "error",

                "message":
                str(e)
            }