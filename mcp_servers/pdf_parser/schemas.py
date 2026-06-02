from pydantic import BaseModel
from typing import List, Optional


class ParsePDFResponse(BaseModel):
    document_name: str
    page_count: int
    total_characters: int


class MetadataResponse(BaseModel):
    title: Optional[str]
    author: Optional[str]
    subject: Optional[str]
    creator: Optional[str]
    producer: Optional[str]
    pages: int


class PageResponse(BaseModel):
    page_number: int
    content: str


class DocumentTextResponse(BaseModel):
    pages: List[PageResponse]