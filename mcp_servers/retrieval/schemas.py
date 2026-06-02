from pydantic import BaseModel
from typing import List


class RetrievalRequest(BaseModel):
    query: str
    top_k: int = 5


class RetrievalResult(BaseModel):
    document_name: str
    page: int
    chunk_id: str
    chunk_type: str
    content_type: str
    chunk_text: str
    score: float


class RetrievalResponse(BaseModel):
    results: List[RetrievalResult]
