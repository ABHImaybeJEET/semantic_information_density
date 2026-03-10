from src.analyzer import InformationDensityAnalyzer
from src.input_loader import load_text


def analyze_document(input_source):
    """
    High-level function for analyzing any supported input.
    Accepts raw text, txt files, or pdf files.
    """

    text = load_text(input_source)

    analyzer = InformationDensityAnalyzer()

    result = analyzer.analyze(text)

    return result