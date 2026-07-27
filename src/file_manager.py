from pathlib import Path


RESULTS_FOLDER = Path("results")


def ensure_results_folder():
    """
    Create the results folder if it does not exist.
    """

    RESULTS_FOLDER.mkdir(exist_ok=True)


def save_text(filename, content):
    """
    Save text to a file inside the results folder.
    """

    ensure_results_folder()

    file_path = RESULTS_FOLDER / filename

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return file_path