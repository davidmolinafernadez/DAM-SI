# P0–P1 · Preparar el laboratorio

[Antes de empezar: materiales, descargas y comprobaciones](preparacion.md).

**Una práctica guiada en clase y una única entrega.** Duración orientativa: 3,5 horas. Primero se audita el puesto y se verifica la ISO; después se crea y se comprueba la VM. No entregues informes separados de P0 y P1.

## Primera parte · Auditoría e ISO

**Teoría relacionada:** [Planificar una instalación](../b01-planificacion.md) · [Medios e integridad](../b03-medios-e-integridad.md)

Duración orientativa: 90 minutos. Trabajo individual. Necesitas un anfitrión Windows o Linux, acceso a sus datos de hardware y una carpeta para el laboratorio. No se modifica el firmware del ordenador del aula.

### 1. Abre las herramientas del anfitrión

Elige la ruta de tu sistema anfitrión. Haz las comprobaciones en el ordenador donde ejecutarás VirtualBox, fuera de los invitados.

#### En Windows

1. Pulsa **Ctrl + Mayús + Esc** para abrir el **Administrador de tareas**. Si aparece una vista reducida, pulsa **Más detalles**.
2. Abre **Rendimiento → CPU**. Anota modelo, núcleos, procesadores lógicos y estado de **Virtualización**. Un estado habilitado indica lo que informa Windows; no demuestra por sí solo que cualquier combinación de hipervisores vaya a funcionar.
3. Abre **Rendimiento → Memoria**. Distingue memoria total y disponible. La disponible cambia mientras abres programas: anota el momento de la medición.
4. Pulsa **Windows + E → Este equipo**. Localiza la unidad donde se guardarán las VM. Pulsa su botón derecho → **Propiedades** y anota espacio libre. Esa cifra no es RAM.
5. Pulsa **Windows + R**, escribe `msinfo32` y pulsa **Aceptar**. En **Resumen del sistema**, consulta tipo de sistema y modo de BIOS. El modo del anfitrión no obliga a utilizar el mismo firmware en todos sus invitados.

#### En Linux (Ubuntu o similar)

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

5. Consulta el modo de arranque del anfitrión:

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

### 2. Decide si el laboratorio cabe

Abre tu documento de entrega y crea una tabla con las filas: anfitrión, Ubuntu, Windows y margen. Separa RAM, CPU y almacenamiento. Explica si ejecutarás los invitados simultáneamente o de forma alterna. Utiliza las cifras propuestas por el docente como punto de partida, no como permiso para asignar toda la memoria disponible.

Para un anfitrión de 16 GiB puedes estudiar una reserva de 6 GiB para el sistema anfitrión y sus aplicaciones, 4 para Ubuntu, 4 para el invitado Windows y 2 de margen. Después tendrás que medir. Para un equipo de 8 GiB plantea un solo invitado activo y consulta dónde realizar la práctica de Windows si no cumple requisitos.

### 3. Descarga e identifica el medio

#### Descargas oficiales

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

### 4. Calcula la huella SHA-256

#### En Windows: PowerShell

Entra en la carpeta `ISO_UD4`. Pulsa la barra de direcciones del Explorador, escribe `powershell` y pulsa **Intro**. Se abre una consola situada en esa carpeta. Ejecuta `Get-ChildItem` para comprobar qué archivos contiene.

Escribe el comando siguiente sustituyendo el nombre por el de tu ISO. Puedes escribir el comienzo del nombre y pulsar **Tab** para completarlo:

```powershell
Get-FileHash -LiteralPath '.\NOMBRE_REAL_DE_LA_IMAGEN.iso' -Algorithm SHA256
```

#### En Linux: Terminal

Abre la carpeta `ISO_UD4` en el gestor de archivos y selecciona **Abrir en una terminal**, o usa `cd` con su ruta real entre comillas. Comprueba dónde estás y sustituye el nombre del ejemplo por el de tu ISO. Puedes usar **Tab** para completarlo:

```bash
pwd
ls -lh
sha256sum -- './NOMBRE_REAL_DE_LA_IMAGEN.iso'
```

La salida muestra la huella seguida del nombre del archivo. Copia los 64 caracteres de la huella, sin el nombre. Si aparece «No existe el archivo o el directorio», revisa carpeta y nombre, incluidas mayúsculas y minúsculas; ese error no significa que la huella sea incorrecta.

#### Compara el resultado (ambos sistemas)

El texto `NOMBRE_REAL_DE_LA_IMAGEN.iso` es un marcador, no un archivo que exista. Compara los 64 caracteres del resultado con la referencia. Que coincidan el principio y el final no basta. Copia ambas cadenas como texto en el informe y explica qué confianza aporta su procedencia.

### 5. Comprueba y entrega

Debes entregar ficha del puesto, presupuesto razonado, identificación de ISO y comparación completa. Si la huella no coincide, no uses la imagen: comprueba revisión, nombre y descarga. La ampliación de firma digital se realiza con la guía oficial, verificando la identidad de la clave.

**Incidencia para analizar:** el archivo se llama igual que el de la referencia, pero tiene otra huella. Propón dos explicaciones y una prueba para distinguirlas. No respondas solamente «está mal».

## Segunda parte · Crear y comprobar la máquina virtual

**Teoría relacionada:** [Comprender la virtualización](../b02-virtualizacion.md) · [Hardware virtual y recursos](../b06-hardware-virtual.md)

Duración orientativa: 120 minutos. Necesitas VirtualBox 7.x instalado, la ficha de P0 y la ISO verificada. El docente indicará la versión exacta. Los nombres de algunas secciones varían entre el modo básico y el experto; identifica la función del campo antes de modificarlo.

### 1. Reconoce las dos ventanas

Abre **Inicio**, escribe **VirtualBox** y abre el administrador. Esta ventana lista las máquinas y permite configurar su hardware. La ventana que aparecerá al pulsar **Iniciar** será la pantalla del ordenador invitado: sus menús y su sistema son distintos de los del anfitrión.

En el administrador abre **Ayuda → Acerca de VirtualBox** y anota la versión. Abre **Archivo → Preferencias → General** si tu versión muestra esa ruta y consulta la carpeta predeterminada de máquinas. En otras interfaces se encuentra en las preferencias de la aplicación. No cambies la carpeta de otras máquinas ya existentes.

### 2. Abre el asistente de creación

1. Pulsa **Nueva** en la barra principal, o **Máquina → Nueva**. Escribe `UD3-Ubuntu-codigo`, sustituyendo `codigo` por tu identificador de aula.
2. En **Carpeta**, elige la ubicación local aprobada. No uses una carpeta de otra persona ni un dispositivo con espacio insuficiente.
3. Deja inicialmente el campo **Imagen ISO** sin imagen. Si seleccionas una y aparece **Omitir instalación desatendida**, márcalo: necesitamos recorrer el instalador en P2.
4. Selecciona **Linux → Ubuntu de 64 bits** o la identificación equivalente de la plantilla. La plantilla propone hardware; todavía no instala Ubuntu.
5. En **Hardware**, asigna **4096 MB** de memoria y **2 procesadores** si P0 justifica esa cantidad. Registra cualquier ajuste acordado. En el campo de memoria, 4096 MiB corresponden a 4 GiB.
6. En **Disco duro**, elige crear un disco nuevo, formato **VDI** y capacidad **50 GiB** o su equivalente mostrado. Mantén la asignación dinámica: no marques **Reservar tamaño completo** si la interfaz ofrece esa casilla.
7. Revisa el resumen y pulsa **Terminar**. Selecciona la máquina recién creada; comprueba el nombre antes de continuar.

### 4. Revisa la configuración antes de arrancar

Pulsa **Configuración → Sistema → Placa base**. Activa **EFI/UEFI** para el itinerario de referencia si aún no está activado. Revisa el orden de arranque. En **Sistema → Procesador**, comprueba los dos procesadores virtuales. En **Red → Adaptador 1**, marca **Habilitar adaptador de red** y selecciona **NAT** en **Conectado a**. Si aparece **Cable conectado**, debe estar marcado.

Abre **Almacenamiento**. Debes ver un disco virtual de 50 GiB y una unidad óptica vacía. No elimines controladores por confundirlos con medios. La unidad óptica recibirá la ISO; el disco duro recibirá el sistema instalado.

### 4. Compara un arranque sin y con instalador

1. Cierra la configuración con **Aceptar** y pulsa **Iniciar**. Con disco vacío y sin ISO puedes ver el firmware o un aviso de medio no arrancable. Registra lo observado: no hay un mensaje único obligatorio.
2. Cierra la ventana de ejecución. Como no hay un sistema instalado que apagar, utiliza **Apagar la máquina** cuando el diálogo lo ofrezca. Este es un caso de ensayo con disco vacío, no la forma ordinaria de cerrar un sistema en uso.
3. De vuelta en el administrador, abre **Configuración → Almacenamiento**. Selecciona la unidad óptica **Vacío**, pulsa el icono de disco de la derecha y elige **Seleccionar un archivo de disco**. Busca la ISO de P0 y ábrela.
4. Comprueba que su nombre aparece junto a la unidad óptica y pulsa **Aceptar → Iniciar**. Ahora debe aparecer el medio de Ubuntu. Todavía no realices la instalación.

### 5. Ubica los archivos y comprueba el resultado

Con la VM apagada, pulsa su botón derecho en el administrador y utiliza **Mostrar en Explorador**, o abre la carpeta anotada en el asistente. Identifica `.vbox`, `.vdi` y la carpeta de registros. No los borres ni los edites. Compara tamaño actual del VDI con capacidad lógica configurada.

Entrega la ficha técnica, la comparación de los dos arranques y una explicación propia de ISO frente a VDI. **Prueba de aceptación:** otra persona puede reconstruir una configuración equivalente usando tu ficha. **Incidencia:** si no arranca el medio, comprueba primero si la ISO está en la unidad óptica de esta VM y si es arrancable y compatible con su arquitectura.

<div class="video-card" markdown>

### Vídeo explicativo · Crear una máquina virtual

V2: la interfaz es anterior y su ejemplo usa Windows 10. Identifica la función de cada campo y adapta P1.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/zx533nop3jd9ybjs/fs" title="Crear una máquina virtual" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/zx533nop3jd9ybjs) · [Ficha y preguntas de visionado](../videos.md)

</div>

## Única entrega · P0–P1

Guarda un solo archivo llamado `P0_P1_Apellidos_Nombre.pdf`. Incluye inventario del puesto, presupuesto de recursos, fuente y verificación de la ISO, configuración de la VM y prueba de arranque. Explica el resultado sin confundir crear la máquina con instalar el sistema. Añade las incidencias y sus comprobaciones al mismo informe. No subas ISO ni discos virtuales.

## Plantilla del informe · Copia y completa

Copia esta plantilla en Writer, Word o tu editor de documentos. Sustituye los campos entre corchetes, inserta tus capturas y exporta el resultado como `P0_P1_Apellidos_Nombre.pdf`. Sirve para anfitriones Windows y Linux. Completa solo la ruta que hayas realizado y utiliza tus mediciones reales.

### Portada y preparación

- **Nombre y apellidos:** [completar].
- **Grupo, fecha y puesto:** [completar].
- **Sistema anfitrión y versión:** [completar].
- **Versión de VirtualBox:** [completar].
- **Carpetas de ISO, máquinas y evidencias:** [rutas reales].

### 1. Auditoría del anfitrión

| Dato | Mi resultado | Herramienta utilizada | Captura |
| --- | --- | --- | --- |
| Sistema, versión y arquitectura | [completar] | [Información del sistema o `/etc/os-release` y `lscpu`] | [E01/E02] |
| Modelo de CPU | [completar] | [Administrador de tareas o `lscpu`] | [E01] |
| Núcleos físicos y procesadores lógicos | [completar por separado] | [Administrador de tareas o `lscpu`] | [E01] |
| Virtualización observada | [estado o capacidad visible y sus límites] | [Administrador de tareas o `lscpu`] | [E01] |
| RAM total y disponible | [valores, unidades y hora] | [Administrador de tareas o `free -h`] | [E02] |
| Carpeta para las VM y espacio libre de su unidad | [ruta y espacio] | [Propiedades o `pwd` y `df -h .`] | [E03] |
| Modo de arranque del anfitrión | [UEFI, BIOS o dato pendiente de confirmar] | [`msinfo32` o comprobación de `/sys/firmware/efi`] | [E04] |

**Interpretación:** [explica qué recursos puedes utilizar y qué limitaciones has detectado].

### 2. Presupuesto de recursos

| Uso | RAM prevista | CPU previstas | Almacenamiento y ubicación |
| --- | --- | --- | --- |
| Anfitrión y aplicaciones | [reserva] | [margen de CPU que conservarás] | [uso del anfitrión] |
| Invitado Ubuntu | [GiB] | [vCPU] | [capacidad virtual y carpeta] |
| Invitado Windows | [GiB] | [vCPU] | [capacidad virtual y carpeta] |
| Margen | [GiB sin comprometer] | [justificación] | [espacio para crecimiento y evidencias] |

**Decisión:** [invitados simultáneos o alternos y por qué].

**Comprobación:** [relaciona las asignaciones con la RAM disponible medida y los requisitos de las versiones acordadas; distingue capacidad virtual y espacio físico]. La CPU se comparte: indica qué VM estarán encendidas, sin tratar las vCPU como núcleos físicos reservados.

### 3. Descarga y verificación de la ISO

| Campo | Mi registro |
| --- | --- |
| Nombre exacto de la ISO | [completar] |
| Sistema, versión, revisión y arquitectura | [completar] |
| Tamaño y fecha de descarga | [completar con unidades] |
| URL oficial de origen o procedencia de la copia del centro | [enlace] |
| URL de la referencia SHA-256 | [enlace de esa misma revisión] |
| Comando ejecutado | [comando real de PowerShell o Linux] |
| SHA-256 de referencia | [pega los 64 caracteres como texto] |
| SHA-256 calculado | [pega los 64 caracteres como texto] |
| Resultado | [coinciden o no coinciden, y decisión] |

**Capturas E05–E07:** [página oficial y versión elegida, referencia del archivo exacto y cálculo local].

**Interpretación:** [qué demuestra la coincidencia y qué confianza aporta la procedencia de la referencia].

### 4. Creación y comprobación de la VM

| Parámetro | Configuración real |
| --- | --- |
| Nombre y carpeta de la VM | [completar] |
| Tipo y versión del invitado | [completar] |
| RAM y número de vCPU | [completar] |
| Firmware | [completar] |
| Disco virtual | [formato, capacidad lógica y asignación dinámica o fija] |
| Red | [adaptador habilitado, modo y cable conectado] |
| Medio óptico | [nombre de la ISO conectada] |
| Archivos localizados | [rutas de `.vbox`, `.vdi` y registros] |
| Tamaño actual del VDI | [valor y unidad; comparación con capacidad lógica] |

**Arranque sin ISO (E09):** [qué apareció y por qué].

**Arranque con ISO (E11):** [qué apareció y qué demuestra; indica si el sistema está instalado o solo ha arrancado el medio].

**Diferencia entre ISO y VDI:** [explicación propia].

### 5. Incidencias y conclusión

- **Incidencia propuesta: mismo nombre de ISO y distinta huella.** Hipótesis 1: [completar]. Hipótesis 2: [completar]. Prueba para distinguirlas: [completar].
- **Incidencia real, si la hubo:** [paso, mensaje exacto, hipótesis, prueba, resultado y solución o duda pendiente]. Si no la hubo, indícalo.
- **Conclusión:** [qué has preparado, qué has comprobado y qué queda pendiente para instalar Ubuntu en P2].

## Capturas de pantalla del proceso

**Añade capturas propias al informe, junto al apartado que documentan.** Tómalas mientras realizas la práctica. En Windows puedes utilizar **Windows + Mayús + S**; en Linux, la aplicación **Captura de pantalla** del menú. Guarda las imágenes en `Evidencias` e insértalas en el documento antes de exportarlo a PDF.

| Código | Qué debe verse | Qué debes explicar debajo |
| --- | --- | --- |
| E01 | CPU y virtualización: Administrador de tareas o salida de `lscpu` | Modelo, núcleos, hilos y alcance del dato de virtualización. |
| E02 | RAM y datos del sistema; utiliza varias imágenes si hace falta | Total, disponible, hora, sistema y versión. |
| E03 | Carpeta de VM y espacio libre de su unidad | Por qué ese espacio corresponde al destino elegido. |
| E04 | Modo de arranque en `msinfo32` o resultado de la comprobación en Linux | Qué has podido confirmar del anfitrión. |
| E05 | Página oficial de descarga con la versión y arquitectura elegidas | Qué archivo has elegido y de dónde procede. Si usas una copia del centro, documenta esa procedencia. |
| E06 | Referencia SHA-256 con el nombre exacto de la ISO | Por qué corresponde a tu archivo y revisión. |
| E07 | Comando y huella calculada completos | Si coinciden los 64 caracteres con la referencia. Pega también ambas cadenas como texto. |
| E08 | Resumen del asistente o configuración de la VM | RAM, CPU, firmware, disco y red; añade las imágenes necesarias para que se lean los datos. |
| E09 | Resultado del arranque con disco vacío y sin ISO | Qué ocurre al no existir todavía un sistema instalado. |
| E10 | Configuración de almacenamiento con la ISO conectada | Diferencia entre la unidad óptica y el disco virtual. |
| E11 | Pantalla de arranque del medio de Ubuntu | Que la ISO arranca; esto todavía no acredita una instalación. |
| E12 | Archivos de la VM y tamaño actual del VDI | Diferencia entre tamaño físico actual y capacidad lógica. |

Puedes usar varias imágenes para un código (por ejemplo, `E08a` y `E08b`) o una misma imagen para varios datos si se leen con claridad. Recorta lo irrelevante conservando el contexto necesario; no incluyas contraseñas ni claves. Comprueba que todas las capturas se leen en el PDF final. Una captura sin explicación no sustituye el razonamiento.

**Modelo de pie de captura:** «E03. Carpeta de destino: [ruta]. La unidad tiene [valor y unidad] disponibles en el momento de la medición. Este espacio se utilizará para [destino previsto]».

## Ejemplo breve de redacción · Datos ficticios

Este ejemplo muestra cómo justificar una comprobación. No es una medición del aula ni una configuración que debas copiar.

> **Auditoría en Linux:** he ejecutado `lscpu` en el anfitrión físico. La salida muestra 1 socket, 4 núcleos por socket y 2 hilos por núcleo: son 4 núcleos y 8 procesadores lógicos (E01). Aparece VT-x; lo registro como capacidad visible, pendiente de comprobar el arranque con VirtualBox.
>
> **Memoria y decisión:** a las 10:15, `free -h` muestra 16 GiB totales y 10 GiB disponibles (E02). Para este supuesto, el docente ha autorizado una imagen de Ubuntu que admite 4 GiB de RAM. Asignaré 4 GiB y 2 vCPU a Ubuntu y ejecutaré los invitados por turnos. Después mediré de nuevo la memoria y el rendimiento con la VM encendida.
>
> **Almacenamiento:** he abierto una terminal en la carpeta autorizada para las VM; `pwd` confirma la ruta y `df -h .` muestra 180 GiB disponibles en ese sistema de archivos (E03). El VDI de Ubuntu tendrá una capacidad lógica de 50 GiB y será dinámico. Su tamaño inicial será menor y crecerá con el uso; tendré que vigilar el espacio físico disponible.
>
> **Verificación de ISO:** he consultado la línea del nombre exacto en el `SHA256SUMS` de su revisión (E06) y he calculado la huella local con `sha256sum` (E07). En mi informe pego ambas cadenas completas. Si coinciden, registro la coincidencia y la procedencia de la referencia; si difieren, no utilizo la imagen hasta aclarar la causa.
>
> **Prueba de arranque:** sin ISO, la VM no encuentra un sistema arrancable (E09). Tras conectar la ISO aparece el medio de Ubuntu (E11). He creado la VM y comprobado el medio; todavía no he instalado Ubuntu en el VDI.

[Ejercicios de aula resueltos · Sin entrega](../soluciones-clase.md){ target="_blank" }
