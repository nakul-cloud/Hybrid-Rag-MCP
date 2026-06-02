from pathlib import Path
import sys

from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

load_dotenv()

from llm.gemini_client import (
    GeminiClient
)

client = GeminiClient()

print(
    "\nConnection Test:",
    client.test_connection()
)

print(
    "\nModel:",
    client.get_model_name()
)

response = client.generate(
    "Explain Retrieval Augmented Generation in 3 lines."
)

print("\nResponse:\n")

print(response)