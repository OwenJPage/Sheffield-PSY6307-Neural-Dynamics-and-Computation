import jupytext
import os
from pathlib import Path
import json

data_file = Path("./.nb_sync.json")

if data_file.exists() and data_file.is_file():
    history: dict[str, float] = json.load(data_file)
else:
    history = {}

nb_root = Path("./notebooks")
py_root = Path("./scripts")
md_root = Path("./markdown")


def check_overwrite(file_path: Path) -> bool:
    if file_path.exists() and history[file_path] != file_path.stat().st_mtime:
        while True:
            match (
                input(
                    f"File {py_path.name} has been modified since last sync. Overwrite? (y/N):"
                )
                .lower()
                .strip()
            ):
                case "y":
                    return True
                case "n" | "":
                    return False
    else:
        return True


for root, dirs, files in os.walk(nb_root):
    root_path = Path(root)
    relative_path = root_path.relative_to(nb_root)

    print(f"root: {relative_path}")

    # Skip any hidden folders
    if relative_path.name != "." and relative_path.name.startswith("."):
        print(f"Skipping `{root}`")
        continue

    for file in [f for f in files if f.endswith(".ipynb")]:
        print(f"file: {file}")

        file_path = relative_path / file

        nb_path = nb_root / file_path
        py_path = (py_root / file_path).with_suffix(".py")
        md_path = (md_root / file_path).with_suffix(".md")

        nb_file = jupytext.read(nb_path, fmt="ipynb")

        if check_overwrite(py_path):
            jupytext.write(nb_file, py_path, fmt="py:percent")

            history[py_path] = py_path.stat().st_mtime

        if check_overwrite(md_path):
            jupytext.write(nb_file, md_path, fmt="md")

            history[md_path] = md_path.stat().st_mtime


json.dump(history, data_file)
