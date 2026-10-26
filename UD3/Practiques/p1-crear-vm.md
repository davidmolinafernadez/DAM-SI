# P1. Crear y entender la máquina virtual

**Teoría relacionada:** [Comprender la virtualización](../b02-virtualizacion.md) · [Hardware virtual y recursos](../b06-hardware-virtual.md)

Duración: 120 minutos. Teoría: B2 y B6. Vídeo: V1; V2 como apoyo. Producto: VM Ubuntu vacía y ficha técnica.

## Preparación y predicción

VirtualBox debe estar instalado o lo instalará el docente desde la fuente oficial con la versión estable acordada. Las prácticas básicas no necesitan Extension Pack. Predice qué ocurrirá al iniciar una máquina con disco vacío y sin ISO.

## Procedimiento

1. Anota la versión de VirtualBox. Localiza la carpeta por defecto de máquinas y escoge una ubicación local del aula con espacio suficiente.
2. Crea UD3-Ubuntu-codigo. Selecciona el tipo Linux y la versión Ubuntu de 64 bits compatible. No conectes todavía la ISO. Evita la instalación desatendida para esta primera práctica.
3. Asigna inicialmente 2 vCPU y 4 GiB de RAM si el presupuesto de P0 lo permite. Justifica cualquier ajuste. Mantén recursos libres para el anfitrión.
4. Crea un disco VDI dinámico de 50 GiB. Explica qué capacidad verá el invitado y cuánto puede ocupar inicialmente el archivo real.
5. Selecciona firmware UEFI para mantener el itinerario de referencia. Registra controlador de almacenamiento, adaptador de pantalla y modo de red NAT. Si tu versión presenta otros nombres, identifica su función.
6. Inicia sin ISO. Registra el mensaje o la pantalla de firmware. Apaga mediante el control de la VM; todavía no hay sistema instalado que cerrar.
7. Con la VM apagada, conecta la ISO verificada a la unidad óptica virtual. Comprueba que se ve el archivo correcto y no un disco de otra máquina.
8. Arranca hasta el menú o entorno inicial de Ubuntu. No instales todavía. Identifica la diferencia entre el archivo ISO y el archivo VDI.
9. Apaga y consulta la carpeta de la VM desde el anfitrión. Identifica configuración, disco y registros. No edites ni elimines sus archivos.

## Pruebas y razonamiento

Aceptación: la VM aparece en el gestor, posee el hardware acordado, no arranca un sistema de disco vacío y sí puede iniciar el medio verificado. Entrega ficha de CPU, RAM, firmware, VDI, red, ruta de la carpeta y versión del hipervisor; añade dos capturas de configuración y la comparación de arranques.

Incidencia controlada: con la VM apagada, desconecta la ISO y repite el arranque. Diagnostica utilizando «medio disponible» y «disco instalado». Después restituye la ISO. Preguntas: ¿crear un VDI instala Ubuntu?, ¿por qué la tarjeta de red del invitado puede aparecer como cableada si el anfitrión usa Wi-Fi?, ¿qué problema puede causar asignar toda la RAM del anfitrión?
