import json
from pathlib import Path

def request_path(output_filename="paths.json"):
    rutas_directorios = {}

    for directory in Path.home().glob("*"):
        if directory.is_dir() and directory.name.startswith("."):
            continue
        elif directory.is_dir():
            rutas_directorios[directory.name] =  str(directory)

    with open("paths.json", "w", encoding="utf-8") as file:
        json.dump(rutas_directorios, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    request_path()