import json
from pathlib import Path

rutas_directorios = {}

for directory in Path.home().glob("*"):
    if directory.name != "VirtualBox VMs" and not directory.name.startswith("."):
        rutas_directorios[f'{directory.name}'] =  f'{directory}'


with open("paths.json", "w", encoding="utf-8") as file:
    json.dump(rutas_directorios, file, indent=4, ensure_ascii=False)