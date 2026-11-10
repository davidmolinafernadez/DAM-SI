# P0–P1 · Preparar el laboratorio

**Una práctica guiada en clase y una única entrega.** Duración orientativa: 3,5 horas. Primero se audita el puesto y se verifica la ISO; después se crea y se comprueba la VM. No entregues informes separados de P0 y P1.

## Primera parte · Auditoría e ISO

**Teoría relacionada:** [Planificar una instalación](../b01-planificacion.md) · [Medios e integridad](../b03-medios-e-integridad.md)

Duración orientativa: 90 minutos. Trabajo individual. Necesitas Windows en el anfitrión, acceso a sus datos de hardware y una carpeta para el laboratorio. No se modifica el firmware del ordenador del aula.

### 1. Abre las herramientas del anfitrión

1. Pulsa **Ctrl + Mayús + Esc** para abrir el **Administrador de tareas**. Si aparece una vista reducida, pulsa **Más detalles**.
2. Abre **Rendimiento → CPU**. Anota modelo, núcleos, procesadores lógicos y estado de **Virtualización**. Un estado habilitado indica lo que informa Windows; no demuestra por sí solo que cualquier combinación de hipervisores vaya a funcionar.
3. Abre **Rendimiento → Memoria**. Distingue memoria total y disponible. La disponible cambia mientras abres programas: anota el momento de la medición.
4. Pulsa **Windows + E → Este equipo**. Localiza la unidad donde se guardarán las VM. Pulsa su botón derecho → **Propiedades** y anota espacio libre. Esa cifra no es RAM.
5. Pulsa **Windows + R**, escribe `msinfo32` y pulsa **Aceptar**. En **Resumen del sistema**, consulta tipo de sistema y modo de BIOS. El modo del anfitrión no obliga a utilizar el mismo firmware en todos sus invitados.

### 2. Decide si el laboratorio cabe

Abre tu documento de entrega y crea una tabla con las filas: anfitrión, Ubuntu, Windows y margen. Separa RAM, CPU y almacenamiento. Explica si ejecutarás los invitados simultáneamente o de forma alterna. Utiliza las cifras propuestas por el docente como punto de partida, no como permiso para asignar toda la memoria disponible.

Para un anfitrión de 16 GiB puedes estudiar una reserva de 6 GiB para Windows y aplicaciones, 4 para Ubuntu, 4 para el invitado Windows y 2 de margen. Después tendrás que medir. Para un equipo de 8 GiB plantea un solo invitado activo y consulta dónde realizar la práctica de Windows si no cumple requisitos.

### 4. Descarga e identifica el medio

1. Abre el navegador y entra en la página oficial indicada en la teoría. Selecciona **Ubuntu Desktop**, la versión acordada y arquitectura **amd64** para el laboratorio x86-64. No confundas amd64 con un requisito de procesador de marca AMD.
2. Guarda la ISO en una carpeta identificable, por ejemplo `ISO_UD4`. Desde el Explorador abre **Ver → Mostrar → Extensiones de nombre de archivo**, si está disponible, para comprobar la extensión real.
3. Anota el nombre completo del archivo, tamaño, versión, arquitectura, fecha y URL. No renombres el archivo antes de cotejar su referencia.
4. Abre el listado oficial de hashes de esa misma revisión. Localiza la fila del nombre exacto de tu ISO. Si el centro proporciona el archivo, también debe proporcionar su procedencia y referencia.

### 4. Calcula la huella en PowerShell

Entra en la carpeta `ISO_UD4`. Pulsa la barra de direcciones del Explorador, escribe `powershell` y pulsa **Intro**. Se abre una consola situada en esa carpeta. Ejecuta `Get-ChildItem` para comprobar qué archivos contiene.

Escribe el comando siguiente sustituyendo el nombre por el de tu ISO. Puedes escribir el comienzo del nombre y pulsar **Tab** para completarlo:

```powershell
Get-FileHash -LiteralPath '.\NOMBRE_REAL_DE_LA_IMAGEN.iso' -Algorithm SHA256
```

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

[Ejercicios de aula resueltos · Sin entrega](../soluciones-clase.md){ target="_blank" }
