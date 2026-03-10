import numpy as np


def compute_information_gain(sim_matrix):
    """
    Calculate semantic novelty for each sentence.
    """

    n = sim_matrix.shape[0]

    gains = []

    for i in range(n):

        if i == 0:
            gains.append(1.0)
            continue

        previous_similarities = sim_matrix[i, :i]

        max_similarity = np.max(previous_similarities)

        novelty = 1 - max_similarity

        gains.append(novelty)

    return gains