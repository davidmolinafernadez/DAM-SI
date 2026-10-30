# 4.2.2 · Crear una máquina que se pueda mantener

<div class="lesson-banner" markdown>
<div class="lesson-number">4.2.2</div>
<div markdown>
**Virtualización y hardware virtual**

Hardware virtual y recursos: explicación, ejemplos y comprobaciones.
</div>
</div>

## Archivos y ubicación

La carpeta de una VM puede incluir configuración .vbox, discos, registros y datos de instantáneas. Copiar solamente el primer VDI puede dejar fuera cambios recientes almacenados en discos diferenciales. Utiliza las operaciones del hipervisor para clonar, mover o exportar.

Guarda el laboratorio en almacenamiento local aprobado, con suficiente espacio. Evita ejecutar una VM mientras su carpeta se sincroniza activamente o se copia parcialmente. El medio de respaldo debe ser independiente del disco de trabajo cuando se pretenda proteger frente a su avería.

## Disco fijo o dinámico

Un disco fijo reserva aproximadamente su capacidad desde el principio. Uno dinámico empieza ocupando menos y crece hasta el límite configurado, con variaciones de formato y metadatos. En ambos casos, el invitado ve una capacidad lógica. Si se agota el espacio físico del anfitrión, la VM puede sufrir errores aunque su partición tenga espacio libre.

El disco dinámico facilita el aula, pero requiere vigilancia. Para dos máquinas de escritorio, clones, exportaciones y varias instantáneas, no basta con sumar el espacio actualmente usado por Windows y Ubuntu. La guía docente incluye un cálculo de presupuesto y margen.

## Estados de una VM

Apagada significa que el sistema ha finalizado su sesión y ya no se ejecuta. Pausada detiene temporalmente la ejecución. Guardar estado conserva la memoria y la ejecución para reanudar. No equivale a completar un apagado ordenado. Forzar apagado se parece a cortar la corriente y puede perder escrituras pendientes.

Para las prácticas de almacenamiento, clonación y cambios de firmware, apagaremos el invitado desde su propio sistema y comprobaremos el estado apagado en VirtualBox. Así se reducen ambigüedades y se facilita repetir los pasos.

## Guest Additions y Extension Pack

Las Guest Additions se instalan dentro del invitado e incorporan controladores y servicios de integración, como ajuste de pantalla y determinadas funciones de intercambio. El Extension Pack se añade al hipervisor del anfitrión y habilita funciones adicionales según la versión. Son productos diferentes. Las prácticas básicas no requieren instalar el Extension Pack. Referencias F4 y F5.

Si una función de integración no funciona, comprueba versión, servicio, permisos y reinicio. No reinstales el sistema completo por un fallo de portapapeles. En Ubuntu la construcción de módulos puede requerir herramientas, cabeceras del kernel y, con Secure Boot, gestión de firma de módulos. La práctica ofrece una ruta alternativa si el centro distribuye los complementos como paquetes.

## Menú de VirtualBox y menú del invitado

En el administrador, **Configuración → Red** cambia el dispositivo virtual y su conexión. Dentro de Ubuntu, **Configuración → Red** modifica el perfil IP que utiliza el sistema invitado. Los dos controles influyen en la comunicación, pero en niveles diferentes. Añadir una tarjeta virtual no configura automáticamente una dirección estática en Ubuntu.

La unidad óptica también tiene dos vistas. Desde el administrador conectas un archivo ISO al dispositivo; dentro del invitado aparece como un CD que se puede montar y leer. No se debe buscar el archivo `.vdi` dentro del CD ni ejecutar el instalador de VirtualBox para instalar Guest Additions: el primero pertenece al anfitrión y los complementos al invitado.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 4.6 · Prever el crecimiento de discos virtuales](actividades/A06-prever-el-crecimiento-de-discos-virtuales.md)
- [Actividad 4.13 · Presupuesto profesional de laboratorio](actividades/A13-presupuesto-profesional-de-laboratorio.md)

## Prácticas relacionadas

- [P1 · Crear la máquina virtual](practicas/p1-crear-vm.md)
- [P8 · Clonar, exportar e importar](practicas/p8-transferencia.md)

<div class="video-card" markdown>

## Vídeo explicativo · Crear una máquina virtual

V2: la interfaz es anterior y su ejemplo usa Windows 10. Identifica la función de cada campo y adapta P1.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/zx533nop3jd9ybjs/fs" title="Crear una máquina virtual" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/zx533nop3jd9ybjs) · [Ficha y preguntas de visionado](videos.md)

</div>
