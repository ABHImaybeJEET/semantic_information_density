import json
import csv
import numpy as np
from pathlib import Path


def convert_numpy(obj):
    """
    Convert numpy types into Python native types.
    """

    if isinstance(obj, np.integer):
        return int(obj)

    if isinstance(obj, np.floating):
        return float(obj)

    if isinstance(obj, np.ndarray):
        return obj.tolist()

    return obj


def export_json(result, output_path):
    """
    Save the full analysis result to a JSON file.
    """

    path = Path(output_path)

    cleaned = {}

    for k, v in result.items():

        if isinstance(v, list):
            cleaned[k] = [convert_numpy(x) for x in v]

        else:
            cleaned[k] = convert_numpy(v)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2)


def export_csv(result, output_path):
    """
    Save sentence-level insights to CSV.
    """

    path = Path(output_path)

    sentences = result["sentences"]
    info_gain = result["information_gain"]
    labels = result["sentence_labels"]

    with open(path, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["sentence", "information_gain", "label"])

        for s, g, l in zip(sentences, info_gain, labels):
            writer.writerow([s, float(g), l])