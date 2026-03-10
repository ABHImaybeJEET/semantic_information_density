# src/config.py

"""
Central configuration file for the project.
Keeps model names and key parameters in one place.
"""

# Default embedding model
DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Future models you may test
AVAILABLE_MODELS = [
    "sentence-transformers/all-MiniLM-L6-v2",
    "BAAI/bge-base-en-v1.5",
    "intfloat/e5-base-v2"
]

# Similarity threshold (can be used later if needed)
SIMILARITY_THRESHOLD = 0.75