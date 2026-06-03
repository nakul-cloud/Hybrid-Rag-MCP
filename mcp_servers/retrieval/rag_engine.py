from llm.gemini_client import (
    GeminiClient
)

from mcp_servers.retrieval.hybrid_retriever import (
    HybridRetriever
)


class RAGEngine:

    def __init__(self):

        self.retriever = (
            HybridRetriever()
        )

        self.llm = (
            GeminiClient()
        )

    def ask_documents(
        self,
        query: str,
        top_k: int = 8,
        document_name: str | None = None
    ):

        retrieval_results = (
            self.retriever.search(
                query=query,
                top_k=top_k,
                document_name=document_name
            )
        )

        contexts = []

        sources = []

        for result in retrieval_results:

            contexts.append(
                f"""
Document: {result["document_name"]}
Page: {result["page"]}
Section: {result["section"]}

{result["chunk_text"]}
"""
            )

            sources.append(
                {
                    "document_name":
                    result["document_name"],

                    "page":
                    result["page"],

                    "section":
                    result["section"],

                    "score":
                    result["score"],

                    "snippet":
                    result["chunk_text"][:300]
                }
            )

        context_text = "\n\n".join(
            contexts
        )

        system_prompt = """
You are a document intelligence assistant.

Rules:

1. Answer ONLY from the supplied context.

2. Do not invent information.

3. If the answer is not found,
   say:

   "I could not find the answer in the provided documents."

4. Provide a concise but complete answer.

5. Mention document evidence when possible.
"""

        user_prompt = f"""
Context:

{context_text}

Question:

{query}
"""

        answer = (
            self.llm.generate_with_system_prompt(
                system_prompt=
                system_prompt,

                user_prompt=
                user_prompt,

                temperature=0.2
            )
        )

        return {

            "answer":
            answer,

            "sources":
            sources
        }