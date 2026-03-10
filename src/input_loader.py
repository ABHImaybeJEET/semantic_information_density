from pathlib import Path
from pypdf import PdfReader


def load_text(input_source):
    """
    Load text from various sources.
    """

    if isinstance(input_source, str):

        path = Path(input_source)

        # If file exists treat as file
        if path.exists():

            if path.suffix == ".txt":
                return load_txt(path)

            if path.suffix == ".pdf":
                return load_pdf(path)

        # Otherwise assume raw text
        return input_source

    raise ValueError("Unsupported input type")


def load_txt(path):

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf(path):

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text