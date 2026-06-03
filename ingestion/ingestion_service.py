from pathlib import Path

from ingestion.pipeline import (
    run_ingestion_pipeline
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

    def ingest_document(
        self,
        file_path: str
    ):

        try:

            path = self.validate_file(
                file_path
            )

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