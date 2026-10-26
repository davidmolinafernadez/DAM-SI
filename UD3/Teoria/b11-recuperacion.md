# 3.7 · Recuperación, clonación y arranque dual

<div class="lesson-banner" markdown>
<div class="lesson-number">3.7</div>
<div markdown>
**Recuperación y transferencia**

Recuperación y transferencia: explicación, ejemplos y comprobaciones.
</div>
</div>

## Cuatro operaciones diferentes

Una instantánea conserva un punto de retorno dentro de la estructura de la VM. Un clon completo crea otra máquina con discos independientes de los del origen. Un clon enlazado necesita su base. Una exportación produce un paquete transportable con limitaciones de compatibilidad y de elementos conservados. Un respaldo independiente protege frente a la pérdida de la ubicación de trabajo si se almacena y se prueba adecuadamente.

Piensa en qué fallos cubre cada operación. Una instantánea ayuda ante un cambio defectuoso dentro del invitado; no salva los discos si falla el SSD que contiene toda la cadena. Un clon completo en ese mismo SSD es independiente del origen, pero comparte el mismo riesgo físico. Referencia F9.

## Restaurar también pierde cambios

Al volver a una instantánea se pierde o se aparta el estado posterior según la operación elegida. Antes de restaurar, extrae las evidencias que necesites conservar o guarda un estado adicional. Borrar una instantánea no equivale a restaurarla: el hipervisor reorganiza los datos asociados. Nunca elimines manualmente archivos diferenciales.

Una restauración no revierte efectos externos: un archivo modificado en una carpeta compartida del anfitrión, una cuenta en un servicio web o un mensaje enviado seguirán existiendo. La práctica P7 utiliza archivos internos para que el alcance sea observable.

## Clonar y transferir

Para un clon que convivirá en red con el origen, genera nuevas MAC y revisa nombre del equipo, direcciones estáticas e identidades específicas del sistema. Una MAC nueva no cambia automáticamente todas las identidades internas. Un Windows destinado a despliegues generales requiere herramientas y procedimientos de preparación adicionales; clonar una VM de aula no constituye por sí solo un despliegue corporativo correcto.

Una exportación se considera útil cuando se importa y supera las pruebas. Conserva un inventario externo con versión de hipervisor, firmware, CPU, RAM, discos y red. No supongas que un OVA mantiene toda la historia de instantáneas, la configuración TPM, los secretos o todas las funciones específicas entre plataformas.

## Arranque dual como ampliación

La ampliación usa una VM nueva de 120 GiB, Windows y Ubuntu en el mismo disco virtual. Primero Windows; después Linux en espacio sin asignar. Es una secuencia didáctica para observar cargadores y particiones. Comprueba el espacio libre antes de confirmar y conserva la ESP existente sin formatearla.

En un equipo físico habría que resolver además copia independiente, cifrado, claves de recuperación, controladores y política del centro. Esta unidad no pide modificar el arranque del ordenador personal. Si no aparece un menú conjunto, comprueba las entradas UEFI: la ausencia de GRUB visible no demuestra que Windows haya desaparecido.

## Protección del sistema de Windows

Restaurar sistema trabaja sobre estado de sistema, configuración, registro y programas dentro de su alcance. No es una máquina del tiempo para cualquier documento. Se abre desde **Inicio → Crear un punto de restauración**, o mediante `SystemPropertiesProtection`. En el asistente se elige unidad, protección y nombre del punto antes de introducir un cambio.

Para aplicar un punto se puede abrir `rstrui.exe` desde **Windows + R**. La opción **Detectar programas afectados** ayuda a anticipar el efecto. Un punto puede no estar disponible si la protección no estaba activada o no se conservó. No se da por hecho que se crea automáticamente cada semana en cualquier Windows.

La práctica P11 se ejecuta en un clon con un punto de retorno adicional del hipervisor. Permite comparar mecanismos: una instantánea de VirtualBox devuelve el estado de la VM según lo que incluya; el punto de Windows tiene otro alcance. Las evidencias y las copias se guardan donde no se perderán con la operación que se quiere ensayar.

## Timeshift y archivos personales en Linux

Timeshift se orienta a instantáneas de sistema y admite modalidades según configuración y sistema de archivos. Su elección requiere revisar qué se incluye, qué se excluye y dónde se almacena. No debe equipararse sin matices a una copia de todos los documentos de cada usuario. Un modo basado en Btrfs necesita una disposición compatible; no se activa solo porque sea una opción visible.

Si el centro lo utiliza, antes de crear una instantánea se identifican modo, destino, filtros y recuperación desde un medio alternativo. Si las copias residen en el mismo disco que se avería, no cubren la pérdida física de ese disco. Para el laboratorio básico utilizamos las instantáneas del hipervisor; una ampliación con Timeshift se prepara en otra VM y con un objetivo de recuperación definido.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 3.10 · Escoger una estrategia de recuperación](actividades/A10-escoger-una-estrategia-de-recuperacion.md)
- [Actividad 3.13 · Presupuesto profesional de laboratorio](actividades/A13-presupuesto-profesional-de-laboratorio.md)
- [Actividad 3.18 · Punto de restauración o instantánea de VM](actividades/A18-punto-de-restauracion-o-instantanea-de-vm.md)

## Prácticas relacionadas

- [P7 · Recuperar con instantáneas](practicas/p7-instantaneas.md)
- [P8 · Clonar, exportar e importar](practicas/p8-transferencia.md)
- [P11 · Restaurar sistema Windows](practicas/p11-restauracion-windows.md)
- [X1 · Arranque dual](practicas/x1-arranque-dual.md)

<div class="video-card" markdown>

## Vídeo explicativo · Instantáneas de VirtualBox

V4: compara retorno de estado y copia independiente. En P7 tomamos la instantánea apagada.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/zgauof85771q51t9/fs" title="Instantáneas de VirtualBox" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/zgauof85771q51t9) · [Ficha y preguntas de visionado](videos.md)

</div>
