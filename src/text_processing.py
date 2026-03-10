import spacy

nlp = spacy.load("en_core_web_sm")


def split_sentences(text: str):
    """
    Split text into sentences using spaCy.
    """

    doc = nlp(text)

    sentences = [sent.text.strip() for sent in doc.sents]

    return sentences