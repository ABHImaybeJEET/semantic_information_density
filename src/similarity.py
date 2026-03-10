import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity_matrix(embeddings):
    """
    Compute sentence similarity matrix.
    """

    sim_matrix = cosine_similarity(embeddings)

    return sim_matrix