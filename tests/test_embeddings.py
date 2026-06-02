from pathlib import Path
import sys

# Allow running this file directly by adding the repo root to sys.path.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from embeddings.embedder import HybridEmbedder

print("=" * 50)
print("LOADING MODEL")
print("=" * 50)

embedder = HybridEmbedder()

print(
    "Embedding Dimension:",
    embedder.get_dimension()
)

sample_text = """
Revenue increased by 24 percent.
"""

vector = embedder.embed_text(
    sample_text
)

print("\nVECTOR GENERATED")

print(
    "Vector Length:",
    len(vector)
)

print(
    "First 10 Values:"
)

print(vector[:10])