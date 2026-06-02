import pymupdf as fitz


def open_pdf(file_path: str):
    return fitz.open(file_path)


def get_metadata(file_path: str):
    doc = open_pdf(file_path)

    metadata = doc.metadata

    return {
        "title": metadata.get("title"),
        "author": metadata.get("author"),
        "subject": metadata.get("subject"),
        "creator": metadata.get("creator"),
        "producer": metadata.get("producer"),
        "pages": len(doc),
    }


def extract_page_text(file_path: str, page_number: int):
    doc = open_pdf(file_path)

    if page_number < 1 or page_number > len(doc):
        raise ValueError("Invalid page number")

    page = doc[page_number - 1]

    return page.get_text()


def extract_all_text(file_path: str):
    doc = open_pdf(file_path)

    pages = []

    for idx, page in enumerate(doc):
        pages.append(
            {
                "page_number": idx + 1,
                "content": page.get_text()
            }
        )

    return pages


def parse_pdf_summary(file_path: str):
    doc = open_pdf(file_path)

    total_characters = 0

    for page in doc:
        total_characters += len(page.get_text())

    return {
        "document_name": file_path.split("\\")[-1],
        "page_count": len(doc),
        "total_characters": total_characters
    }