import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_similarity_matrix(sim_matrix):

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        sim_matrix,
        cmap="viridis",
        xticklabels=False,
        yticklabels=False
    )

    plt.title("Sentence Similarity Matrix")

    plt.tight_layout()
    plt.show()


def plot_information_gain(info_gain):

    x = np.arange(1, len(info_gain) + 1)

    plt.figure(figsize=(8, 4))

    plt.plot(x, info_gain, marker="o")

    plt.title("Information Gain per Sentence")
    plt.xlabel("Sentence Index")
    plt.ylabel("Information Gain")

    plt.grid(True)

    plt.tight_layout()
    plt.show()