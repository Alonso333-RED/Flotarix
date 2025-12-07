from pathlib import Path

def find_project_root(marker_files=None):

    if marker_files is None:
        marker_files = ["main.py"]

    current = Path(__file__).resolve().parent
    while current != current.parent:
        for marker in marker_files:
            if (current / marker).exists():
                return current
        current = current.parent

    raise FileNotFoundError("No se encontró la raíz del proyecto.")
