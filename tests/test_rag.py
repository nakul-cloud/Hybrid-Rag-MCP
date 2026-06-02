from pathlib import Path
import sys

from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from mcp_servers.retrieval.rag_engine import (
    RAGEngine
)

rag = RAGEngine()

response = rag.ask_documents(

    query=
    "What is the research gap?",

    top_k=5
)

print("\nANSWER\n")

print(
    response["answer"]
)

print("\nSOURCES\n")

for source in response["sources"]:

    print(source)