# P1. Crear y entender la máquina virtual

<div class="lesson-banner" markdown>
<div class="lesson-number">P1</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Comprender la virtualización](../b02-virtualizacion.md) · [Hardware virtual y recursos](../b06-hardware-virtual.md)

Duración orientativa: 120 minutos. Necesitas VirtualBox 7.x instalado, la ficha de P0 y la ISO verificada. El docente indicará la versión exacta. Los nombres de algunas secciones varían entre el modo básico y el experto; identifica la función del campo antes de modificarlo.

## 1. Reconoce las dos ventanas

Abre **Inicio**, escribe **VirtualBox** y abre el administrador. Esta ventana lista las máquinas y permite configurar su hardware. La ventana que aparecerá al pulsar **Iniciar** será la pantalla del ordenador invitado: sus menús y su sistema son distintos de los del anfitrión.

En el administrador abre **Ayuda → Acerca de VirtualBox** y anota la versión. Abre **Archivo → Preferencias → General** si tu versión muestra esa ruta y consulta la carpeta predeterminada de máquinas. En otras interfaces se encuentra en las preferencias de la aplicación. No cambies la carpeta de otras máquinas ya existentes.

## 2. Abre el asistente de creación

1. Pulsa **Nueva** en la barra principal, o **Máquina → Nueva**. Escribe `UD4-Ubuntu-codigo`, sustituyendo `codigo` por tu identificador de aula.
2. En **Carpeta**, elige la ubicación local aprobada. No uses una carpeta de otra persona ni un dispositivo con espacio insuficiente.
3. Deja inicialmente el campo **Imagen ISO** sin imagen. Si seleccionas una y aparece **Omitir instalación desatendida**, márcalo: necesitamos recorrer el instalador en P2.
4. Selecciona **Linux → Ubuntu de 64 bits** o la identificación equivalente de la plantilla. La plantilla propone hardware; todavía no instala Ubuntu.
5. En **Hardware**, asigna **4096 MB** de memoria y **2 procesadores** si P0 justifica esa cantidad. Registra cualquier ajuste acordado. En el campo de memoria, 4096 MiB corresponden a 4 GiB.
6. En **Disco duro**, elige crear un disco nuevo, formato **VDI** y capacidad **50 GiB** o su equivalente mostrado. Mantén la asignación dinámica: no marques **Reservar tamaño completo** si la interfaz ofrece esa casilla.
7. Revisa el resumen y pulsa **Terminar**. Selecciona la máquina recién creada; comprueba el nombre antes de continuar.

## 4. Revisa la configuración antes de arrancar

Pulsa **Configuración → Sistema → Placa base**. Activa **EFI/UEFI** para el itinerario de referencia si aún no está activado. Revisa el orden de arranque. En **Sistema → Procesador**, comprueba los dos procesadores virtuales. En **Red → Adaptador 1**, marca **Habilitar adaptador de red** y selecciona **NAT** en **Conectado a**. Si aparece **Cable conectado**, debe estar marcado.

Abre **Almacenamiento**. Debes ver un disco virtual de 50 GiB y una unidad óptica vacía. No elimines controladores por confundirlos con medios. La unidad óptica recibirá la ISO; el disco duro recibirá el sistema instalado.

## 4. Compara un arranque sin y con instalador

1. Cierra la configuración con **Aceptar** y pulsa **Iniciar**. Con disco vacío y sin ISO puedes ver el firmware o un aviso de medio no arrancable. Registra lo observado: no hay un mensaje único obligatorio.
2. Cierra la ventana de ejecución. Como no hay un sistema instalado que apagar, utiliza **Apagar la máquina** cuando el diálogo lo ofrezca. Este es un caso de ensayo con disco vacío, no la forma ordinaria de cerrar un sistema en uso.
3. De vuelta en el administrador, abre **Configuración → Almacenamiento**. Selecciona la unidad óptica **Vacío**, pulsa el icono de disco de la derecha y elige **Seleccionar un archivo de disco**. Busca la ISO de P0 y ábrela.
4. Comprueba que su nombre aparece junto a la unidad óptica y pulsa **Aceptar → Iniciar**. Ahora debe aparecer el medio de Ubuntu. Todavía no realices la instalación.

## 5. Ubica los archivos y comprueba el resultado

Con la VM apagada, pulsa su botón derecho en el administrador y utiliza **Mostrar en Explorador**, o abre la carpeta anotada en el asistente. Identifica `.vbox`, `.vdi` y la carpeta de registros. No los borres ni los edites. Compara tamaño actual del VDI con capacidad lógica configurada.

Entrega la ficha técnica, la comparación de los dos arranques y una explicación propia de ISO frente a VDI. **Prueba de aceptación:** otra persona puede reconstruir una configuración equivalente usando tu ficha. **Incidencia:** si no arranca el medio, comprueba primero si la ISO está en la unidad óptica de esta VM y si es arrancable y compatible con su arquitectura.

## Entrega independiente de la práctica

Guarda `P1_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.

<div class="video-card" markdown>

## Vídeo explicativo · Crear una máquina virtual

V2: la interfaz es anterior y su ejemplo usa Windows 10. Identifica la función de cada campo y adapta P1.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/zx533nop3jd9ybjs/fs" title="Crear una máquina virtual" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/zx533nop3jd9ybjs) · [Ficha y preguntas de visionado](../videos.md)

</div>
