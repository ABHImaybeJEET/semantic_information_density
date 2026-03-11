import numpy as np

from src.config import DEFAULT_EMBEDDING_MODEL

from src.text_processing import split_sentences
from src.insights import label_sentences
from src.embeddings import SentenceEmbedder
from src.similarity import compute_similarity_matrix
from src.information_gain import compute_information_gain
from src.clustering import cluster_embeddings
from src.entropy import compute_semantic_entropy


class InformationDensityAnalyzer:

    def __init__(self, model_name=None, use_clustering=True):

        # use default model from config if none provided
        if model_name is None:
            model_name = DEFAULT_EMBEDDING_MODEL

        self.embedder = SentenceEmbedder(model_name)
        self.use_clustering = use_clustering

    def analyze(self, text):

        if not text or not text.strip():
            raise ValueError("Input text is empty.")

        sentences = split_sentences(text)

        if len(sentences) == 0:
            raise ValueError("No valid sentences found in input.")

        # generate embeddings
        embeddings = self.embedder.encode(sentences)

        # similarity matrix
        sim_matrix = compute_similarity_matrix(embeddings)

        # novelty / information gain
        info_gain = compute_information_gain(sim_matrix)

        sentence_labels = label_sentences(info_gain)

        # redundancy calculation
        if len(sentences) > 1:
            redundancy = np.mean(
                sim_matrix[np.triu_indices(len(sim_matrix), 1)]
            )
        else:
            redundancy = 0.0

        result = {
            "sentences": sentences,
            "information_gain": info_gain,
            "sentence_labels": sentence_labels,
            "redundancy": float(redundancy),
            "similarity_matrix": sim_matrix
        }

        # optional semantic clustering
        if self.use_clustering and len(sentences) > 1:

            labels = cluster_embeddings(embeddings)

            entropy_score = compute_semantic_entropy(labels)

            result["entropy"] = float(entropy_score)

        # final density score
        density = np.mean(info_gain) * (1 - redundancy)

        result["information_density"] = float(density)

        return result