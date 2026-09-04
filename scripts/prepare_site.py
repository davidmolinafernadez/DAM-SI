"""Prepara la teoría y las actividades del alumnado para MkDocs."""

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

        shutil.copytree(source, destination, dirs_exist_ok=True)
        activities = ROOT / f"UD{number}" / "Activitats"
        if activities.exists():
            shutil.copytree(
                activities,
                destination / "actividades",
                dirs_exist_ok=True,
            )
        readme = destination / "README.md"
        if readme.exists():
            readme.rename(destination / "index.md")

    print(f"Web docente preparada en {DESTINATION}")


if __name__ == "__main__":
    main()
