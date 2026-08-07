"""Prepara exclusivamente la teoría para publicarla con MkDocs."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / ".site-src"


def main() -> None:
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)

    shutil.copytree(ROOT / "web", DESTINATION)

    for number in range(1, 8):
        source = ROOT / f"UD{number}" / "Teoria"
        destination = DESTINATION / f"ud{number}"
        destination.mkdir(parents=True)

        for document in source.glob("*.md"):
            filename = "index.md" if document.name == "README.md" else document.name
            shutil.copy2(document, destination / filename)

    print(f"Web preparada en {DESTINATION}")


if __name__ == "__main__":
    main()
