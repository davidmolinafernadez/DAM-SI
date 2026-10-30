# P0. Auditoría del puesto e ISO verificada

<div class="lesson-banner" markdown>
<div class="lesson-number">P0</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Planificar una instalación](../b01-planificacion.md) · [Medios e integridad](../b03-medios-e-integridad.md)

Duración orientativa: 90 minutos. Trabajo individual. Necesitas Windows en el anfitrión, acceso a sus datos de hardware y una carpeta para el laboratorio. No se modifica el firmware del ordenador del aula.

## 1. Abre las herramientas del anfitrión

1. Pulsa **Ctrl + Mayús + Esc** para abrir el **Administrador de tareas**. Si aparece una vista reducida, pulsa **Más detalles**.
2. Abre **Rendimiento → CPU**. Anota modelo, núcleos, procesadores lógicos y estado de **Virtualización**. Un estado habilitado indica lo que informa Windows; no demuestra por sí solo que cualquier combinación de hipervisores vaya a funcionar.
3. Abre **Rendimiento → Memoria**. Distingue memoria total y disponible. La disponible cambia mientras abres programas: anota el momento de la medición.
4. Pulsa **Windows + E → Este equipo**. Localiza la unidad donde se guardarán las VM. Pulsa su botón derecho → **Propiedades** y anota espacio libre. Esa cifra no es RAM.
5. Pulsa **Windows + R**, escribe `msinfo32` y pulsa **Aceptar**. En **Resumen del sistema**, consulta tipo de sistema y modo de BIOS. El modo del anfitrión no obliga a utilizar el mismo firmware en todos sus invitados.

## 2. Decide si el laboratorio cabe

Abre tu documento de entrega y crea una tabla con las filas: anfitrión, Ubuntu, Windows y margen. Separa RAM, CPU y almacenamiento. Explica si ejecutarás los invitados simultáneamente o de forma alterna. Utiliza las cifras propuestas por el docente como punto de partida, no como permiso para asignar toda la memoria disponible.

Para un anfitrión de 16 GiB puedes estudiar una reserva de 6 GiB para Windows y aplicaciones, 4 para Ubuntu, 4 para el invitado Windows y 2 de margen. Después tendrás que medir. Para un equipo de 8 GiB plantea un solo invitado activo y consulta dónde realizar la práctica de Windows si no cumple requisitos.

## 4. Descarga e identifica el medio

1. Abre el navegador y entra en la página oficial indicada en la teoría. Selecciona **Ubuntu Desktop**, la versión acordada y arquitectura **amd64** para el laboratorio x86-64. No confundas amd64 con un requisito de procesador de marca AMD.
2. Guarda la ISO en una carpeta identificable, por ejemplo `ISO_UD3`. Desde el Explorador abre **Ver → Mostrar → Extensiones de nombre de archivo**, si está disponible, para comprobar la extensión real.
3. Anota el nombre completo del archivo, tamaño, versión, arquitectura, fecha y URL. No renombres el archivo antes de cotejar su referencia.
4. Abre el listado oficial de hashes de esa misma revisión. Localiza la fila del nombre exacto de tu ISO. Si el centro proporciona el archivo, también debe proporcionar su procedencia y referencia.

## 4. Calcula la huella en PowerShell

Entra en la carpeta `ISO_UD3`. Pulsa la barra de direcciones del Explorador, escribe `powershell` y pulsa **Intro**. Se abre una consola situada en esa carpeta. Ejecuta `Get-ChildItem` para comprobar qué archivos contiene.

Escribe el comando siguiente sustituyendo el nombre por el de tu ISO. Puedes escribir el comienzo del nombre y pulsar **Tab** para completarlo:

```powershell
Get-FileHash -LiteralPath '.\NOMBRE_REAL_DE_LA_IMAGEN.iso' -Algorithm SHA256
```

El texto `NOMBRE_REAL_DE_LA_IMAGEN.iso` es un marcador, no un archivo que exista. Compara los 64 caracteres del resultado con la referencia. Que coincidan el principio y el final no basta. Copia ambas cadenas como texto en el informe y explica qué confianza aporta su procedencia.

## 5. Comprueba y entrega

Debes entregar ficha del puesto, presupuesto razonado, identificación de ISO y comparación completa. Si la huella no coincide, no uses la imagen: comprueba revisión, nombre y descarga. La ampliación de firma digital se realiza con la guía oficial, verificando la identidad de la clave.

**Incidencia para analizar:** el archivo se llama igual que el de la referencia, pero tiene otra huella. Propón dos explicaciones y una prueba para distinguirlas. No respondas solamente «está mal».

## Entrega independiente de la práctica

Guarda `P0_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.
