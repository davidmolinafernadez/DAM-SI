# 3.2.1 · Virtualización: qué se crea realmente

<div class="lesson-banner" markdown>
<div class="lesson-number">3.2.1</div>
<div markdown>
**Virtualización y hardware virtual**

Comprender la virtualización: explicación, ejemplos y comprobaciones.
</div>
</div>

## Anfitrión, invitado e hipervisor

El anfitrión es el equipo que aporta los recursos. El invitado es el sistema que se ejecuta dentro de la máquina virtual. El hipervisor organiza la ejecución y presenta dispositivos virtuales. Una VM tiene configuración de CPU, memoria, firmware, almacenamiento y red; un disco virtual es solamente una parte de ella.

Esquema del laboratorio: hardware físico → sistema anfitrión → VirtualBox → hardware virtual → sistema invitado → aplicaciones. El invitado ve, por ejemplo, una tarjeta de red virtual, aunque el ordenador físico se conecte mediante Wi-Fi. Por eso el instalador puede mostrar una conexión «por cable» dentro de la VM.

En un hipervisor de tipo 1, la capa de virtualización actúa directamente sobre el hardware; en uno de tipo 2, la aplicación funciona sobre un sistema anfitrión. Esta clasificación es introductoria: tecnologías como Hyper-V tienen una arquitectura más compleja que la apariencia de su consola. VirtualBox es la herramienta de escritorio utilizada en esta unidad.

## Virtualizar, emular y contenerizar

Virtualizar permite ejecutar invitados aprovechando la arquitectura y las capacidades de la CPU. Emular reproduce el comportamiento de otra máquina y puede permitir una arquitectura distinta, con un coste de traducción. Descargar una ISO ARM64 para una VM x86-64 no se soluciona aumentando la RAM.

Un contenedor Linux comparte el kernel del sistema Linux que lo ejecuta y aísla procesos, archivos y recursos. Puede contener herramientas de Ubuntu sin arrancar su propio kernel como haría una VM Ubuntu. En Windows, una herramienta de contenedores Linux suele apoyarse en una capa Linux, como WSL 2 o una VM. Por eso «los contenedores nunca utilizan máquinas virtuales» es una conclusión incorrecta.

## CPU y memoria virtuales

Una vCPU es una unidad de ejecución presentada al invitado. Asignar cuatro no reserva necesariamente cuatro núcleos físicos exclusivos. Si varios invitados compiten, el hipervisor reparte tiempo. Empezaremos con dos vCPU para los escritorios del laboratorio y mediremos antes de aumentar.

La memoria asignada necesita respaldo en el anfitrión. No se debe confundir la RAM con el almacenamiento del archivo VDI. Un invitado puede tener 4 GiB de RAM y un disco virtual de 50 GiB. El primero condiciona la ejecución; el segundo, los datos que puede almacenar.

VT-x y AMD-V son extensiones de virtualización de CPU. El firmware puede permitir activarlas o desactivarlas. La disponibilidad también depende de la configuración del anfitrión. Si aparece un error de acceso a virtualización, registra el texto exacto y comprueba el estado: no desactives características de seguridad del equipo por ensayo y error.

## Aislamiento y límites

Una VM ayuda a contener cambios, pero puede acceder a recursos reales a través de red, carpetas compartidas, USB o portapapeles. Una carpeta compartida con escritura permite modificar archivos del anfitrión. Para esta unidad se comparten solamente carpetas específicas, con archivos de prueba y permisos mínimos.

Un sistema invitado desactualizado no se convierte en seguro por estar dentro de una ventana. Tampoco deben probarse programas maliciosos para demostrar aislamiento. Las averías de esta unidad son reversibles y se provocan con archivos y configuraciones del laboratorio.

## Qué está mirando realmente cada sistema

Imagina un equipo físico con 8 procesadores lógicos. El administrador del anfitrión muestra esos recursos. Si la VM tiene 2 vCPU, sus herramientas normalmente mostrarán las dos unidades que el hipervisor le presenta, no un inventario completo de la placa física. Ambas observaciones pueden ser correctas: describen niveles distintos.

Lo mismo ocurre con los dispositivos. La VM puede ver una controladora SATA virtual sobre un archivo alojado en un SSD NVMe del anfitrión. El nombre del controlador invitado no cambia el hardware físico donde finalmente se guardan los datos. Confundir ambos niveles lleva a diagnósticos erróneos, como buscar en Ubuntu el modelo exacto de la tarjeta Wi-Fi real.

## Por qué la asignación debe medirse

Asignar más RAM puede ayudar si faltaba memoria al invitado, pero perjudicar si el anfitrión empieza a intercambiar páginas continuamente. Asignar más vCPU puede aumentar competencia por ejecución. El procedimiento razonable es medir una carga definida, cambiar un parámetro, repetir y comparar. Si se cambian cuatro recursos a la vez, cuesta explicar qué causó la mejora.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 3.2 · El recorrido de un archivo en una VM](actividades/A02-el-recorrido-de-un-archivo-en-una-vm.md)

## Prácticas relacionadas

- [P1 · Crear la máquina virtual](practicas/p1-crear-vm.md)

<div class="video-card" markdown>

## Vídeo explicativo · Máquinas virtuales con VirtualBox

V1: identifica anfitrión, hipervisor e invitado. Contrasta las simplificaciones con la explicación escrita.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/bh97chmwc7d66tfd/fs" title="Máquinas virtuales con VirtualBox" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/bh97chmwc7d66tfd) · [Ficha y preguntas de visionado](videos.md)

</div>
