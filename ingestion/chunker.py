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

    def create_chunks(
        self,
        text: str
    ):
        recursive_chunks = (
            self.recursive_chunks(text)
        )

        window_chunks = (
            self.sliding_window_chunks(
                recursive_chunks
            )
        )

        return {
            "base_chunks": recursive_chunks,
            "context_chunks": window_chunks
        }