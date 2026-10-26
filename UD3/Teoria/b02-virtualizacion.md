# B2. Virtualización: qué se crea realmente

> **Del concepto al laboratorio:** [P1 · Crear la máquina virtual](practicas/p1-crear-vm.md) · [P9 · Proyecto integrador](practicas/p9-proyecto.md)

## 2.1. Anfitrión, invitado e hipervisor

El anfitrión es el equipo que aporta los recursos. El invitado es el sistema que se ejecuta dentro de la máquina virtual. El hipervisor organiza la ejecución y presenta dispositivos virtuales. Una VM tiene configuración de CPU, memoria, firmware, almacenamiento y red; un disco virtual es solamente una parte de ella.

Esquema del laboratorio: hardware físico → sistema anfitrión → VirtualBox → hardware virtual → sistema invitado → aplicaciones. El invitado ve, por ejemplo, una tarjeta de red virtual, aunque el ordenador físico se conecte mediante Wi-Fi. Por eso el instalador puede mostrar una conexión «por cable» dentro de la VM.

En un hipervisor de tipo 1, la capa de virtualización actúa directamente sobre el hardware; en uno de tipo 2, la aplicación funciona sobre un sistema anfitrión. Esta clasificación es introductoria: tecnologías como Hyper-V tienen una arquitectura más compleja que la apariencia de su consola. VirtualBox es la herramienta de escritorio utilizada en esta unidad.

## 2.2. Virtualizar, emular y contenerizar

Virtualizar permite ejecutar invitados aprovechando la arquitectura y las capacidades de la CPU. Emular reproduce el comportamiento de otra máquina y puede permitir una arquitectura distinta, con un coste de traducción. Descargar una ISO ARM64 para una VM x86-64 no se soluciona aumentando la RAM.

Un contenedor Linux comparte el kernel del sistema Linux que lo ejecuta y aísla procesos, archivos y recursos. Puede contener herramientas de Ubuntu sin arrancar su propio kernel como haría una VM Ubuntu. En Windows, una herramienta de contenedores Linux suele apoyarse en una capa Linux, como WSL 2 o una VM. Por eso «los contenedores nunca utilizan máquinas virtuales» es una conclusión incorrecta.

## 2.3. CPU y memoria virtuales

Una vCPU es una unidad de ejecución presentada al invitado. Asignar cuatro no reserva necesariamente cuatro núcleos físicos exclusivos. Si varios invitados compiten, el hipervisor reparte tiempo. Empezaremos con dos vCPU para los escritorios del laboratorio y mediremos antes de aumentar.

La memoria asignada necesita respaldo en el anfitrión. No se debe confundir la RAM con el almacenamiento del archivo VDI. Un invitado puede tener 4 GiB de RAM y un disco virtual de 50 GiB. El primero condiciona la ejecución; el segundo, los datos que puede almacenar.

VT-x y AMD-V son extensiones de virtualización de CPU. El firmware puede permitir activarlas o desactivarlas. La disponibilidad también depende de la configuración del anfitrión. Si aparece un error de acceso a virtualización, registra el texto exacto y comprueba el estado: no desactives características de seguridad del equipo por ensayo y error.

## 2.4. Aislamiento y límites

Una VM ayuda a contener cambios, pero puede acceder a recursos reales a través de red, carpetas compartidas, USB o portapapeles. Una carpeta compartida con escritura permite modificar archivos del anfitrión. Para esta unidad se comparten solamente carpetas específicas, con archivos de prueba y permisos mínimos.

Un sistema invitado desactualizado no se convierte en seguro por estar dentro de una ventana. Tampoco deben probarse programas maliciosos para demostrar aislamiento. Las averías de esta unidad son reversibles y se provocan con archivos y configuraciones del laboratorio.

## Actividad A2 · Seguir un recurso

Dibuja el recorrido desde un archivo index.html del invitado hasta los sectores físicos del SSD del anfitrión. Incluye sistema de archivos del invitado, partición, disco virtual, archivo del anfitrión y sistema de archivos del anfitrión. Después explica qué ocurre si el SSD físico se queda sin espacio aunque Ubuntu muestre espacio libre. Continúa con P1.
