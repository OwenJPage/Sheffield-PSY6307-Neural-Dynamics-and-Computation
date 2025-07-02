import json
import os
from pathlib import Path
import jupytext

data_path = Path("./.nb_sync.json")

try:
    with data_path.open("r") as data_file:
        history: dict[str, float] = json.load(data_file)
except BaseException:
    history = {}

nb_root = Path("./notebooks")
py_root = Path("./scripts")
md_root = Path("./markdown")


def check_overwrite(file_path: Path) -> bool:
    if (
        file_path.exists()
        and str(file_path) in history
        and history[str(file_path)] != file_path.stat().st_mtime
    ):
        print(
            f"E {file_path.exists()}, H {history.get(str(file_path))} S {file_path.stat().st_mtime}"
        )
        while True:
            response = (
                input(
                    f"File {file_path.name} has been modified since last sync. Overwrite? (y/N):"
                )
                .lower()
                .strip()
            )

            match response:
                case "y":
                    return True
                case "n" | "":
                    return False
    else:
        return True


for root, dirs, files in os.walk(nb_root):
    nb_dir = Path(root)
    relative_path = nb_dir.relative_to(nb_root)

    # Skip any hidden folders
    if relative_path.name != "." and relative_path.name.startswith("."):
        print(f"Skipping `{root}`")
        continue

    nb_files = [f for f in files if f.endswith(".ipynb")]

    py_dir = py_root / relative_path
    md_dir = md_root / relative_path

    if len(nb_files) > 0:
        py_dir.mkdir(parents=True, exist_ok=True)
        md_dir.mkdir(parents=True, exist_ok=True)

    for file in nb_files:
        nb_path = nb_dir / file
        py_path = (py_dir / file).with_suffix(".py")
        md_path = (md_dir / file).with_suffix(".md")

        print(f"Processing `{nb_path}`")

        nb_file = jupytext.read(nb_path, fmt="ipynb")

        if check_overwrite(py_path):
            with py_path.open("w") as py_file:
                jupytext.write(nb_file, py_file, fmt="py:percent")

            history[str(py_path)] = py_path.stat().st_mtime
            print(f"--> Written `{py_path}`")

        if check_overwrite(md_path):
            with md_path.open("w") as md_file:
                jupytext.write(nb_file, md_file, fmt="md")

            history[str(md_path)] = md_path.stat().st_mtime
            print(f"--> Written `{md_path}`")


with data_path.open("w") as data_file:
    json.dump(history, data_file)
