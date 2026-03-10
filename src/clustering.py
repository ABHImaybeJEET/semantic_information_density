import numpy as np
from sklearn.cluster import KMeans


def cluster_embeddings(embeddings):
    """
    Cluster sentence embeddings into semantic groups.
    """

    n = len(embeddings)

    # Not enough data to cluster
    if n < 2:
        return np.zeros(n, dtype=int)

    k = min(max(2, int(np.sqrt(n))), n)

    model = KMeans(n_clusters=k, random_state=42)

    labels = model.fit_predict(embeddings)

    return labels