# P0. Auditoría del puesto e ISO verificada

<div class="lesson-banner" markdown>
<div class="lesson-number">P0</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Planificar una instalación](../b01-planificacion.md) · [Medios e integridad](../b03-medios-e-integridad.md)

Duración orientativa: 90 minutos. Trabajo individual. Necesitas un anfitrión Windows o Linux, acceso a sus datos de hardware y una carpeta para el laboratorio. No se modifica el firmware del ordenador del aula.

## 1. Abre las herramientas del anfitrión

Elige la ruta de tu sistema anfitrión. Haz las comprobaciones en el ordenador donde ejecutarás VirtualBox, fuera de los invitados.

### En Windows

1. Pulsa **Ctrl + Mayús + Esc** para abrir el **Administrador de tareas**. Si aparece una vista reducida, pulsa **Más detalles**.
2. Abre **Rendimiento → CPU**. Anota modelo, núcleos, procesadores lógicos y estado de **Virtualización**. Un estado habilitado indica lo que informa Windows; no demuestra por sí solo que cualquier combinación de hipervisores vaya a funcionar.
3. Abre **Rendimiento → Memoria**. Distingue memoria total y disponible. La disponible cambia mientras abres programas: anota el momento de la medición.
4. Pulsa **Windows + E → Este equipo**. Localiza la unidad donde se guardarán las VM. Pulsa su botón derecho → **Propiedades** y anota espacio libre. Esa cifra no es RAM.
5. Pulsa **Windows + R**, escribe `msinfo32` y pulsa **Aceptar**. En **Resumen del sistema**, consulta tipo de sistema y modo de BIOS. El modo del anfitrión no obliga a utilizar el mismo firmware en todos sus invitados.

### En Linux (Ubuntu o similar)

Abre **Terminal** desde el menú de aplicaciones; en Ubuntu también puedes usar **Ctrl + Alt + T**. Ejecuta estos comandos de uno en uno, sin `sudo`:

```bash
cat /etc/os-release
lscpu
free -h
```

1. Anota distribución y versión de `/etc/os-release`. En `lscpu`, registra arquitectura, modelo, sockets, núcleos por socket, hilos por núcleo y CPU lógicas. En un equipo físico, los núcleos totales se obtienen multiplicando sockets por núcleos por socket; no confundas núcleos e hilos.
2. Busca la información de virtualización **VT-x** (Intel) o **AMD-V** (AMD). Indica la capacidad que Linux ve, pero no garantiza que VirtualBox pueda arrancar una VM. Si no aparece, registra el resultado y consulta al docente; no cambies el firmware.
3. En `free -h`, usa la fila **Mem:** y distingue **total** de **available** (disponible). La columna **free** no incluye toda la memoria recuperable. La swap no sustituye la RAM. Anota la hora de la medición.
4. Abre la carpeta autorizada para las VM en el gestor de archivos y selecciona **Abrir en una terminal**, si está disponible. También puedes usar `cd` con su ruta real entre comillas. Ejecuta:

```bash
pwd
df -h .
```

Anota la ruta y el espacio disponible (**Avail** o **Disp.**) del sistema de archivos que contiene esa carpeta. El punto significa «carpeta actual»: el espacio de otra unidad podría no servir para guardar tus VM.

**Modo de arranque del anfitrión:** consulta el resultado con este comando:

```bash
if [ -d /sys/firmware/efi ]; then
    echo "Arranque UEFI"
else
    echo "Arranque BIOS heredado o interfaz EFI no accesible"
fi
```

En una sesión normal sobre el equipo físico, ese directorio indica arranque UEFI. Si no está accesible o trabajas dentro de una VM o contenedor, registra la limitación y contrasta el dato con el docente. El firmware del anfitrión no obliga a usar el mismo en los invitados.

**Evidencia común a ambos sistemas:** registra sistema y versión, CPU y arquitectura, núcleos e hilos, virtualización observada, RAM total y disponible, carpeta de VM, espacio libre y modo de arranque. Explica qué demuestra cada captura o salida.

Consulta: manuales de [`lscpu`](https://man7.org/linux/man-pages/man1/lscpu.1.html), [`free`](https://man7.org/linux/man-pages/man1/free.1.html) y [`df`](https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html).

## 2. Decide si el laboratorio cabe

Abre tu documento de entrega y crea una tabla con las filas: anfitrión, Ubuntu, Windows y margen. Separa RAM, CPU y almacenamiento. Explica si ejecutarás los invitados simultáneamente o de forma alterna. Utiliza las cifras propuestas por el docente como punto de partida, no como permiso para asignar toda la memoria disponible.

Para un anfitrión de 16 GiB puedes estudiar una reserva de 6 GiB para el sistema anfitrión y sus aplicaciones, 4 para Ubuntu, 4 para el invitado Windows y 2 de margen. Después tendrás que medir. Para un equipo de 8 GiB plantea un solo invitado activo y consulta dónde realizar la práctica de Windows si no cumple requisitos.

## 3. Descarga e identifica el medio

### Descargas oficiales

| Material | Enlace y elección |
| --- | --- |
| VirtualBox | [Descargas oficiales](https://www.virtualbox.org/wiki/Downloads). Para un anfitrión Windows, elige **Windows hosts**; para Linux, **Linux distributions** y el paquete de tu distribución. Usa la versión acordada con el docente; en el aula ya estará instalado. |
| ISO de Ubuntu Desktop | [Descargar Ubuntu Desktop](https://ubuntu.com/download/desktop). Elige la versión acordada y arquitectura **amd64 / Intel o AMD de 64 bits** para los puestos x86-64. |
| Otras revisiones y huellas de Ubuntu | [Directorio oficial de imágenes](https://releases.ubuntu.com/). Entra en la carpeta de la versión y busca la ISO y su `SHA256SUMS`; la referencia debe corresponder al nombre exacto descargado. [Guía oficial de verificación](https://ubuntu.com/tutorials/how-to-verify-ubuntu). |
| ISO de Windows 11 (para la práctica de Windows) | [Descargar Windows 11](https://www.microsoft.com/es-es/software-download/windows11). Utiliza **Descargar imagen de disco (ISO) para dispositivos x64**, con idioma y edición autorizados, o la copia del centro. Consulta **Verificar la descarga** para su SHA-256 cuando se ofrezca. |

Elige el instalador de VirtualBox según el **anfitrión** y la ISO según el **invitado**: puedes descargar Ubuntu y Windows desde cualquiera de los dos anfitriones. No necesitas crear un USB para estas prácticas. La versión más reciente de una web puede diferir de la acordada en clase; utiliza la indicada por el docente.

1. Abre el navegador y entra en la página oficial indicada en la teoría. Selecciona **Ubuntu Desktop**, la versión acordada y arquitectura **amd64** para el laboratorio x86-64. No confundas amd64 con un requisito de procesador de marca AMD.
2. Guarda la ISO en una carpeta identificable, por ejemplo `ISO_UD4`. En Windows, desde el Explorador abre **Ver → Mostrar → Extensiones de nombre de archivo**, si está disponible. En Linux, comprueba el nombre completo en **Propiedades** del gestor de archivos o con `ls -lh`. Espera a que termine la descarga y comprueba la extensión real.
3. Anota el nombre completo del archivo, tamaño, versión, arquitectura, fecha y URL. No renombres el archivo antes de cotejar su referencia.
4. Abre el listado oficial de hashes de esa misma revisión. Localiza la fila del nombre exacto de tu ISO. Si el centro proporciona el archivo, también debe proporcionar su procedencia y referencia.

## 4. Calcula la huella SHA-256

### En Windows: PowerShell

Entra en la carpeta `ISO_UD4`. Pulsa la barra de direcciones del Explorador, escribe `powershell` y pulsa **Intro**. Se abre una consola situada en esa carpeta. Ejecuta `Get-ChildItem` para comprobar qué archivos contiene.

Escribe el comando siguiente sustituyendo el nombre por el de tu ISO. Puedes escribir el comienzo del nombre y pulsar **Tab** para completarlo:

```powershell
Get-FileHash -LiteralPath '.\NOMBRE_REAL_DE_LA_IMAGEN.iso' -Algorithm SHA256
```

### En Linux: Terminal

Abre la carpeta `ISO_UD4` en el gestor de archivos y selecciona **Abrir en una terminal**, o usa `cd` con su ruta real entre comillas. Comprueba dónde estás y sustituye el nombre del ejemplo por el de tu ISO. Puedes usar **Tab** para completarlo:

```bash
pwd
ls -lh
sha256sum -- './NOMBRE_REAL_DE_LA_IMAGEN.iso'
```

La salida muestra la huella seguida del nombre del archivo. Copia los 64 caracteres de la huella, sin el nombre. Si aparece «No existe el archivo o el directorio», revisa carpeta y nombre, incluidas mayúsculas y minúsculas; ese error no significa que la huella sea incorrecta.

### Compara el resultado (ambos sistemas)

El texto `NOMBRE_REAL_DE_LA_IMAGEN.iso` es un marcador, no un archivo que exista. Compara los 64 caracteres del resultado con la referencia. Que coincidan el principio y el final no basta. Copia ambas cadenas como texto en el informe y explica qué confianza aporta su procedencia.

## 5. Comprueba y entrega

Debes entregar ficha del puesto, presupuesto razonado, identificación de ISO y comparación completa. Si la huella no coincide, no uses la imagen: comprueba revisión, nombre y descarga. La ampliación de firma digital se realiza con la guía oficial, verificando la identidad de la clave.

**Incidencia para analizar:** el archivo se llama igual que el de la referencia, pero tiene otra huella. Propón dos explicaciones y una prueba para distinguirlas. No respondas solamente «está mal».

## Modelo de informe y capturas

Utiliza la [plantilla del informe P0–P1](p0-p1-laboratorio.md#plantilla-del-informe-copia-y-completa) y consulta el [ejemplo de redacción](p0-p1-laboratorio.md#ejemplo-breve-de-redaccion-datos-ficticios). Añade tus capturas del proceso con un pie explicativo: para esta primera parte corresponden E01–E07 de la [lista de evidencias](p0-p1-laboratorio.md#capturas-de-pantalla-del-proceso). Después completa la creación de la VM en el mismo documento.

## Entrega conjunta P0–P1

Guarda un único `P0_P1_Apellidos_Nombre.pdf` con la auditoría, la ISO y la creación de la VM. P0 y P1 forman una sola entrega. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Solo A1 y A10 tienen archivo propio. El resto de preguntas se trabaja en clase o dentro de la práctica, sin otra entrega.
