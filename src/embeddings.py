from sentence_transformers import SentenceTransformer


class SentenceEmbedder:
    """
    Wrapper around sentence-transformers model.
    Responsible for generating sentence embeddings.
    """

    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def encode(self, sentences):
        """
        Convert sentences into vector embeddings.
        """
        embeddings = self.model.encode(
            sentences,
            normalize_embeddings=True
        )

        return embeddings