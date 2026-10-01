# Tarea 2.1 · Mapa de capas del sistema operativo

<div class="lesson-banner" markdown>
<div class="lesson-number">2.1</div>
<div markdown>
**Reto de arquitectura**

Explica qué ocurre entre una aplicación y el hardware cuando se abre, guarda y
protege un archivo.
</div>
</div>

<div class="activity-meta" markdown>
<span>55 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

## Producto final

PDF de 3-4 páginas llamado `Tarea_2_1_Apellidos_Nombre.pdf`, con un diagrama
propio, una explicación técnica y una fuente oficial consultada.

## Fase 1 · Dibuja las capas

Crea un esquema con estas capas mínimas: usuario, aplicación, biblioteca/API,
llamada al sistema, kernel, controlador, sistema de archivos y hardware. Puedes
usar draw.io, LibreOffice Draw, Mermaid o una herramienta similar.

Incluye al menos dos flechas de ida y vuelta: una operación de lectura y una de
escritura.

## Fase 2 · Sigue una operación real

Elige una acción cotidiana:

- guardar un documento;
- descargar un archivo desde el navegador;
- instalar una aplicación;
- imprimir un PDF;
- conectar un pendrive y copiar datos.

Describe, en 10-15 líneas, qué responsabilidad tiene cada capa. No basta con
nombrarlas: debes explicar qué problema resuelve cada una.

## Fase 3 · Modo usuario y modo kernel

Responde:

1. ¿Por qué una aplicación no debería escribir directamente en un SSD?
2. ¿Qué daño podría causar un controlador defectuoso?
3. ¿Qué diferencia hay entre una API de biblioteca y una llamada al sistema?
4. ¿Por qué el shell no es lo mismo que el kernel?

## Fase 4 · Evidencia

Busca una fuente técnica fiable sobre requisitos, arquitectura o seguridad de un
sistema operativo. Añade URL, fecha de consulta y dos ideas que hayas verificado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Diagrama correcto y legible | 2 |
| Explicación por capas | 3 |
| Modo usuario/kernel y llamadas al sistema | 2 |
| Evidencia citada y bien usada | 1 |
| Claridad, vocabulario y presentación | 2 |

!!! warning "Entrega"
    Sube el PDF a Aules. El diagrama debe ser propio; si usas una imagen externa,
    cita su fuente.
