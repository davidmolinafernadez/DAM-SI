# P0. Auditoría del puesto e ISO verificada

**Teoría relacionada:** [Planificar una instalación](../b01-planificacion.md) · [Medios e integridad](../b03-medios-e-integridad.md)

Duración: 90 minutos. Teoría: B1 y B3. Trabajo individual con contraste por parejas. Producto: ficha de viabilidad y registro de descarga.

## Qué vas a aprender

Comprobar si un equipo puede alojar el laboratorio y demostrar que una imagen coincide con la huella oficial de su revisión. El resultado debe permitir que otra persona entienda por qué has elegido una configuración y de dónde procede el instalador.

## Preparación

Necesitas acceso de lectura a la información del anfitrión y una carpeta de trabajo. No cambies su firmware. Si la virtualización está deshabilitada o se requiere instalar software, comunica la incidencia al docente, que coordinará el puesto del centro. Una descarga puede prepararse antes de clase.

## Procedimiento

1. Registra sistema anfitrión, arquitectura, CPU, núcleos/hilos, RAM total, RAM disponible aproximada y espacio libre en la unidad del laboratorio. En Windows puedes usar Administrador de tareas e Información del sistema. Distingue almacenamiento y memoria.
2. Comprueba si el sistema informa de virtualización habilitada. Anota la herramienta y el dato observado. Si no puedes comprobarlo, marca «pendiente» y explica cómo lo resolverá el docente.
3. Consulta requisitos oficiales de Windows 11 y del Ubuntu elegido. Separa requisitos oficiales de la configuración propuesta para clase.
4. Diseña una tabla con reserva del anfitrión, VM Ubuntu, VM Windows y margen. Indica si se ejecutarán simultáneamente. En 8 GiB, plantea ejecución alterna y un puesto compatible para las tareas que lo necesiten.
5. Accede a la descarga oficial de Ubuntu. Registra edición, versión completa, arquitectura, URL, fecha, tamaño y nombre del archivo. El docente puede proporcionar la ISO desde un repositorio del centro conservando la trazabilidad.
6. Obtén la referencia SHA-256 correspondiente a ese archivo. No uses la huella de otra revisión. Guarda la URL del listado oficial.
7. Calcula la huella con Get-FileHash o sha256sum, como se muestra en B3. Compara todos los caracteres. Adjunta huella calculada y esperada como texto seleccionable.
8. Escribe una conclusión: «Coincide con la referencia ...» o «No coincide; no se autoriza su uso». Explica qué has comprobado y qué requeriría verificar autenticidad mediante firma.

## Comprobación e incidencia

El docente entrega dos cadenas de ejemplo, idénticas salvo un carácter central. Compara las cadenas sin limitarte al principio y al final. Si tu propia descarga no coincide, comprueba primero nombre y revisión; no la uses hasta resolverlo. No es necesario descargar una ISO corrupta para practicar la incidencia.

Aceptación: arquitectura adecuada, presupuesto razonado, ISO identificada sin ambigüedad y huella completa cotejada. Evidencias: tabla del equipo, tabla de presupuesto, salida del hash y referencia. Preguntas: ¿por qué una ISO de 6 GiB no cabe como archivo en FAT32?, ¿por qué un hash obtenido de un foro no demuestra por sí solo autenticidad?

Ampliación: sigue la guía oficial de firma de Ubuntu, identifica la huella de la clave y explica qué significa una firma válida y qué significa una clave aún no confiable localmente.
