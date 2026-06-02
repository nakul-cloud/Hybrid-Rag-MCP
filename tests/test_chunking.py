from pathlib import Path
import sys

# Allow running this file directly by adding the repo root to sys.path.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
	sys.path.insert(0, str(ROOT_DIR))

from ingestion.chunker import HybridChunker

sample_text = """
Revenue Growth

Revenue increased by 24 percent.

Revenue by Region

North America grew significantly.

Risk Factors

Economic slowdown remains a concern.
""" * 100

chunker = HybridChunker()

result = chunker.create_chunks(sample_text)

print("=" * 50)
print("CHUNKING RESULTS")
print("=" * 50)

print(f"Base Chunks: {len(result['base_chunks'])}")
print(f"Context Chunks: {len(result['context_chunks'])}")

print("\nFIRST BASE CHUNK")
print("-" * 50)
print(result["base_chunks"][0][:500])

print("\nFIRST CONTEXT CHUNK")
print("-" * 50)
print(result["context_chunks"][0][:500])