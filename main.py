from src.service import analyze_document
from src.visualization import plot_similarity_matrix, plot_information_gain
from src.exporter import export_json, export_csv


def main():

    # Example input. Replace with text, txt path, or pdf path.
    input_source = """
    Artificial intelligence studies intelligent systems.
    Machine learning learns patterns from data.
    Deep learning is a subset of machine learning.
    Neural networks are widely used in AI systems.
    """

    result = analyze_document(input_source)

    print("\nInformation Density:", result["information_density"])
    print("Redundancy:", result["redundancy"])

    if "entropy" in result:
        print("Semantic Entropy:", result["entropy"])

    print("\nInformation Gain:")
    for i, g in enumerate(result["information_gain"]):
        print(f"S{i+1}: {g:.3f}")

    print("\nSentence Insights:")
    for sentence, label in zip(
        result["sentences"],
        result["sentence_labels"]
    ):
        print(f"- {label}: {sentence}")

    # Visualizations
    plot_similarity_matrix(result["similarity_matrix"])
    plot_information_gain(result["information_gain"])

    # Export results
    export_json(result, "analysis_result.json")
    export_csv(result, "sentence_analysis.csv")


if __name__ == "__main__":
    main()