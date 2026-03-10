from sentence_transformers import SentenceTransformer


class SentenceEmbedder:
    """
    Generates embeddings for sentences using transformer models.
    """

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def encode(self, sentences):

        embeddings = self.model.encode(sentences)

        return embeddings