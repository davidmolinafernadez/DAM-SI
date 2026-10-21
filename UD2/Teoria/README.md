# UD2 · Fundamentos de sistemas operativos

Manual de consulta y secuencia de explicación para comprender por qué existe un
sistema operativo, cómo administra recursos, cómo se observa en un equipo real y
cómo elegir una plataforma con criterios técnicos, legales y de soporte.

## Índice jerárquico

- **UD2 · Fundamentos de sistemas operativos**
  - [Teoría general](01-arquitectura-y-funciones.md)
  - **Tareas del tema general**
    - [Tarea 2.1 · Mapa de capas del sistema operativo](actividades/A1-mapa-capas-so.md)
    - [Tarea 2.2 · Comparativa de gestión de procesos](actividades/A2-observatorio-procesos.md)
    - [Tarea 2.3 · Elección justificada de sistema operativo](actividades/A3-eleccion-so.md)
  - **Subunidad 2.1 · Procesos, memoria y entrada/salida**
    - [Teoría 2.1](02-procesos-memoria-e-io.md)
    - [Tarea 2.1.1 · Diagnóstico de rendimiento](actividades/A21-diagnostico-rendimiento.md)
  - **Subunidad 2.2 · Familias, licencias y soporte**
    - [Teoría 2.2](03-familias-licencias-y-eleccion.md)
  - **Subunidad 2.3 · Virtualización y arranque**
    - [Teoría 2.3](04-virtualizacion-y-arranque.md)
    - [Tarea 2.3.1 · Ficha de una máquina virtual reproducible](actividades/A23-maquina-virtual.md)
  - [Síntesis](apuntes.md)

## Propuesta de aula

| Bloque | Sesiones | Tiempo real |
| --- | ---: | --- |
| UD2 · Arquitectura y funciones | 4 | 3 h 40 min |
| 2.1 · Procesos, memoria y E/S | 4 | 3 h 40 min |
| 2.2 · Familias, licencias y soporte | 3 | 2 h 45 min |
| 2.3 · Virtualización y arranque | 3 | 2 h 45 min |
| **Total** | **14** | **12 h 50 min** |

## Qué debes poder explicar al terminar

- Seguir una lectura o escritura desde la aplicación hasta el dispositivo.
- Distinguir modo usuario, modo kernel y permisos de administración.
- Explicar estados, planificación, hilos y sincronización mediante ejemplos.
- Diferenciar memoria virtual, RAM, caché e intercambio al interpretar medidas.
- Elegir una versión de SO con requisitos obligatorios y matriz ponderada.
- Justificar recursos, red y recuperación de una VM reproducible.

Las tareas conservan su numeración de Aules. El orden recomendado de trabajo es:
**2.1 → 2.2 → 2.1.1 → 2.3 → 2.3.1**, siguiendo los capítulos de teoría.

## Pregunta conductora

> ¿Qué tendría que hacer una aplicación si no existiera el sistema operativo?
