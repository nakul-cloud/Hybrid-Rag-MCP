from .pdf_utils import (
    parse_pdf_summary,
    get_metadata,
    extract_page_text,
    extract_all_text
)

from .schemas import (
    ParsePDFResponse,
    MetadataResponse,
    PageResponse,
    DocumentTextResponse
)


def parse_pdf(file_path: str):
    result = parse_pdf_summary(file_path)

    return ParsePDFResponse(**result).model_dump()


def get_pdf_metadata(file_path: str):
    result = get_metadata(file_path)

    return MetadataResponse(**result).model_dump()


def extract_page(file_path: str, page_number: int):
    content = extract_page_text(file_path, page_number)

    return PageResponse(
        page_number=page_number,
        content=content
    ).model_dump()


def extract_document_text(file_path: str):
    pages = extract_all_text(file_path)

    return DocumentTextResponse(
        pages=[
            PageResponse(**page)
            for page in pages
        ]
    ).model_dump()