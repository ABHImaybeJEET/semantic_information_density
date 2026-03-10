import numpy as np
from scipy.stats import entropy


def compute_semantic_entropy(labels):
    """
    Compute entropy of cluster distribution.
    """

    counts = np.bincount(labels)

    probs = counts / counts.sum()

    return entropy(probs)