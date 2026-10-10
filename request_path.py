from pathlib import Path
import platform
import json
import os

sysop = platform.system()

if sysop == "Linux":
    linux_paths = {}
    for dir in Path.home().glob("*"):
        if dir.name.startswith("."):
            continue
        else:
            linux_paths[dir.name] = str(dir)

    with open(f'paths_{sysop}.json', 'w') as file:
         json.dump(linux_paths,file,indent=2)


elif sysop == "Windows":
    general_windows_directories = ['Desktop','Documents','Downloads','Music','Pictures','Videos']
    windows_path = {}
    for dir in Path.home().glob("*"):
        if dir.name in general_windows_directories:
                windows_path[dir.name] = str(dir)

    with open(f'paths_windows.json', 'w') as file:
        json.dump(windows_path,file, indent=2)