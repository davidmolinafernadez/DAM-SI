# B11. Recuperación, clonación y arranque dual

> **Del concepto al laboratorio:** [P7 · Recuperar con instantáneas](practicas/p7-instantaneas.md) · [P8 · Clonar, exportar e importar](practicas/p8-transferencia.md) · [P9 · Proyecto integrador](practicas/p9-proyecto.md) · [X1 · Arranque dual](practicas/x1-arranque-dual.md)

## 11.1. Cuatro operaciones diferentes

Una instantánea conserva un punto de retorno dentro de la estructura de la VM. Un clon completo crea otra máquina con discos independientes de los del origen. Un clon enlazado necesita su base. Una exportación produce un paquete transportable con limitaciones de compatibilidad y de elementos conservados. Un respaldo independiente protege frente a la pérdida de la ubicación de trabajo si se almacena y se prueba adecuadamente.

Piensa en qué fallos cubre cada operación. Una instantánea ayuda ante un cambio defectuoso dentro del invitado; no salva los discos si falla el SSD que contiene toda la cadena. Un clon completo en ese mismo SSD es independiente del origen, pero comparte el mismo riesgo físico. Referencia F9.

## 11.2. Restaurar también pierde cambios

Al volver a una instantánea se pierde o se aparta el estado posterior según la operación elegida. Antes de restaurar, extrae las evidencias que necesites conservar o guarda un estado adicional. Borrar una instantánea no equivale a restaurarla: el hipervisor reorganiza los datos asociados. Nunca elimines manualmente archivos diferenciales.

Una restauración no revierte efectos externos: un archivo modificado en una carpeta compartida del anfitrión, una cuenta en un servicio web o un mensaje enviado seguirán existiendo. La práctica P7 utiliza archivos internos para que el alcance sea observable.

## 11.3. Clonar y transferir

Para un clon que convivirá en red con el origen, genera nuevas MAC y revisa nombre del equipo, direcciones estáticas e identidades específicas del sistema. Una MAC nueva no cambia automáticamente todas las identidades internas. Un Windows destinado a despliegues generales requiere herramientas y procedimientos de preparación adicionales; clonar una VM de aula no constituye por sí solo un despliegue corporativo correcto.

Una exportación se considera útil cuando se importa y supera las pruebas. Conserva un inventario externo con versión de hipervisor, firmware, CPU, RAM, discos y red. No supongas que un OVA mantiene toda la historia de instantáneas, la configuración TPM, los secretos o todas las funciones específicas entre plataformas.

## 11.4. Arranque dual como ampliación

La ampliación usa una VM nueva de 120 GiB, Windows y Ubuntu en el mismo disco virtual. Primero Windows; después Linux en espacio sin asignar. Es una secuencia didáctica para observar cargadores y particiones. Comprueba el espacio libre antes de confirmar y conserva la ESP existente sin formatearla.

En un equipo físico habría que resolver además copia independiente, cifrado, claves de recuperación, controladores y política del centro. Esta unidad no pide modificar el arranque del ordenador personal. Si no aparece un menú conjunto, comprueba las entradas UEFI: la ausencia de GRUB visible no demuestra que Windows haya desaparecido.

## Actividad A10 · Elegir recuperación

Propón una solución para: deshacer una instalación experimental; transportar una VM a otro equipo; soportar la avería del SSD; distribuir una base de prácticas ahorrando espacio. Indica una dependencia o limitación de cada solución. Continúa con P7, P8 y ampliación X1.
