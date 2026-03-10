from src.text_processing import split_sentences
from src.embeddings import SentenceEmbedder
from src.similarity import compute_similarity_matrix
from src.information_gain import compute_information_gain


def main():

    text = """
    Artificial intelligence studies intelligent systems.
    Machine learning allows computers to learn from data.
    Deep learning is a subset of machine learning.
    Machine learning algorithms are widely used in AI.
    """

    sentences = split_sentences(text)

    print("\nSentences:")
    for s in sentences:
        print("-", s)

    embedder = SentenceEmbedder()

    embeddings = embedder.encode(sentences)

    sim_matrix = compute_similarity_matrix(embeddings)

    gains = compute_information_gain(sim_matrix)

    print("\nInformation Gain per sentence:")
    for i, g in enumerate(gains):
        print(f"S{i+1}: {g:.3f}")


if __name__ == "__main__":
    main()