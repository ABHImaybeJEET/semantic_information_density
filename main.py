from src.service import analyze_document


def main():

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


if __name__ == "__main__":
    main()