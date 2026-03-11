def label_sentences(info_gain):
    """
    Convert information gain scores into human-readable labels.
    """

    labels = []

    for score in info_gain:

        if score > 0.7:
            labels.append("High novelty")

        elif score > 0.4:
            labels.append("Moderate novelty")

        elif score > 0.2:
            labels.append("Low novelty")

        else:
            labels.append("Likely redundant")

    return labels