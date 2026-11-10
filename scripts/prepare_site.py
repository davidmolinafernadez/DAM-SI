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
                ignore=shutil.ignore_patterns("Correcciones", "_textos_extraidos", "__pycache__"),
            )
        practices = ROOT / f"UD{number}" / "Practiques"
        if practices.exists():
            shutil.copytree(
                practices,
                destination / "practicas",
                dirs_exist_ok=True,
                ignore=shutil.ignore_patterns("Correcciones", "Docente", "__pycache__"),
            )
        readme = destination / "README.md"
        if readme.exists():
            readme.rename(destination / "index.md")

    simplify_ud3()
    print(f"Web docente preparada en {DESTINATION}")




def simplify_ud3():
    """Publica únicamente las fichas que forman las ocho entregas de UD3."""
    unit = DESTINATION / "ud3"
    allowed = {
        "actividades": {"index.md", "plantillas.md", "A01-decidir-antes-de-instalar.md", "A10-escoger-una-estrategia-de-recuperacion.md"},
        "practicas": {"index.md", "p0-auditoria.md", "p1-crear-vm.md", "p2-ubuntu.md", "p3-windows.md", "p6-actualizaciones.md", "p7-instantaneas.md", "p8-transferencia.md"},
    }
    removed = set()
    for folder, keep in allowed.items():
        for page in (unit / folder).glob("*.md"):
            if page.name not in keep:
                removed.add(page.name)
                page.unlink()
    for page in unit.rglob("*.md"):
        lines = page.read_text(encoding="utf-8-sig").splitlines()
        lines = [line for line in lines if not any(name in line for name in removed)]
        page.write_text("\n".join(lines) + "\n", encoding="utf-8")
    # Evita que los antiguos cuadernos vuelvan a mostrar tareas eliminadas.
    downloads = unit / "actividades" / "descargas"
    if downloads.exists():
        for item in downloads.iterdir():
            if item.is_file() and not item.name.startswith(("Actividad_3_1_", "Actividad_3_10_")):
                item.unlink()


if __name__ == "__main__":
    main()
