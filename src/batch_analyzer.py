from pathlib import Path
from src.service import analyze_document


def analyze_folder(folder_path):
    """
    Analyze all supported documents inside a folder.
    """

    folder = Path(folder_path)

    results = []

    for file in folder.iterdir():

        if file.suffix.lower() not in [".txt", ".pdf"]:
            continue

        try:
            result = analyze_document(str(file))

            results.append({
                "file": file.name,
                "density": result["information_density"],
                "redundancy": result["redundancy"]
            })

        except Exception as e:

            results.append({
                "file": file.name,
                "error": str(e)
            })

    return results