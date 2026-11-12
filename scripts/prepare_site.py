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
        "practicas": {"preparacion.md", "index.md", "p1-laboratorio.md", "p2-ubuntu.md", "p3-windows.md", "p4-actualizaciones.md", "p5-instantaneas.md", "p6-transferencia.md"},
    }
    # Las prácticas de continuidad se publican en su unidad correspondiente.
    import re
    for filename, number in (("p4-particionado.md", 5), ("p10-paquetes-linux.md", 6), ("p9-proyecto.md", 7)):
        original = unit / "practicas" / filename
        published_name = "p1-particionado.md" if number == 5 else filename
        target = DESTINATION / f"ud{number}" / "practicas" / published_name
        target.parent.mkdir(parents=True, exist_ok=True)
        content = original.read_text(encoding="utf-8-sig")
        content = re.sub(r"\]\(\.\./", "](../../ud3/", content)
        target.write_text(content, encoding="utf-8")
        index = DESTINATION / f"ud{number}" / "index.md"
        if index.exists():
            content = index.read_text(encoding="utf-8-sig")
            content = content.replace(f"../ud3/practicas/{filename}", f"practicas/{published_name}")
            index.write_text(content, encoding="utf-8")

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
    # Conserva los enlaces de prácticas compartidos antes de la renumeración.
    for old, new in {'p0-p1-laboratorio.md': 'p1-laboratorio.md', 'p6-actualizaciones.md': 'p4-actualizaciones.md', 'p7-instantaneas.md': 'p5-instantaneas.md', 'p8-transferencia.md': 'p6-transferencia.md'}.items():
        (unit / "practicas" / old).write_text(
            f"# Práctica renumerada\n\nEsta ficha ha cambiado de código. [Abrir la práctica vigente]({new}).\n",
            encoding="utf-8",
        )
    (DESTINATION / "ud5/practicas/p4-particionado.md").write_text(
        "# Práctica renumerada\n\n[Abrir UD5/P1 · Particionado](p1-particionado.md).\n", encoding="utf-8"
    )

    # Evita que los antiguos cuadernos vuelvan a mostrar tareas eliminadas.
    downloads = unit / "actividades" / "descargas"
    if downloads.exists():
        for item in downloads.iterdir():
            if item.is_file() and not item.name.startswith(("Actividad_3_1_", "Actividad_3_10_")):
                item.unlink()


if __name__ == "__main__":
    main()
