import re

from langchain_text_splitters import RecursiveCharacterTextSplitter


class HybridChunker:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        window_size: int = 3
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.window_size = window_size

        self.recursive_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                separators=[
                    "\n\n",
                    "\n",
                    ". ",
                    " ",
                    ""
                ]
            )
        )

    def recursive_chunks(
        self,
        text: str
    ):
        return self.recursive_splitter.split_text(text)

    def sliding_window_chunks(
        self,
        chunks: list[str]
    ):
        windows = []

        for i in range(len(chunks)):

            start = max(
                0,
                i - self.window_size // 2
            )

            end = min(
                len(chunks),
                i + self.window_size // 2 + 1
            )

            merged = "\n".join(
                chunks[start:end]
            )

            windows.append(merged)

        return windows

    def detect_sections(
        self,
        text: str
    ):

        pattern = re.compile(

            r"(?:^|\n)"
            r"(\d+(?:\.\d+)?\s+.+)",

            re.MULTILINE
        )

        matches = list(
            pattern.finditer(text)
        )

        sections = []

        if not matches:

            return [

                {
                    "section":
                    "Unknown",

                    "text":
                    text
                }
            ]

        first_start = matches[0].start()

        if first_start > 0:

            sections.append(

                {
                    "section":
                    "Unknown",

                    "text":
                    text[:first_start]
                }
            )

        for i, match in enumerate(matches):

            start = match.start()

            end = (

                matches[i + 1].start()

                if i + 1 < len(matches)

                else len(text)
            )

            section_text = (
                text[start:end].strip()
            )

            if not section_text:
                continue

            sections.append(

                {
                    "section":
                    match.group(1).strip(),

                    "text":
                    section_text
                }
            )

        return sections

    def create_chunks(
        self,
        text: str
    ):
        sections = (
            self.detect_sections(text)
        )

        chunk_counter = 1

        all_chunks = []

        for section in sections:

            base_chunks = (
                self.recursive_chunks(
                    section["text"]
                )
            )

            context_chunks = (
                self.sliding_window_chunks(
                    base_chunks
                )
            )

            for base_chunk, context_chunk in zip(
                base_chunks,
                context_chunks
            ):

                all_chunks.append(

                    {
                        "chunk_id":
                        f"chunk_{chunk_counter:04d}",

                        "section":
                        section["section"],

                        "base_chunk":
                        base_chunk,

                        "context_chunk":
                        context_chunk
                    }
                )

                chunk_counter += 1

        return all_chunks