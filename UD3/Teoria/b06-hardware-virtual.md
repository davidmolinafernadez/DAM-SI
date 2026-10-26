# B6. Crear una máquina que se pueda mantener

> **Del concepto al laboratorio:** [P1 · Crear la máquina virtual](practicas/p1-crear-vm.md) · [P8 · Clonar, exportar e importar](practicas/p8-transferencia.md) · [P9 · Proyecto integrador](practicas/p9-proyecto.md)

## 6.1. Archivos y ubicación

La carpeta de una VM puede incluir configuración .vbox, discos, registros y datos de instantáneas. Copiar solamente el primer VDI puede dejar fuera cambios recientes almacenados en discos diferenciales. Utiliza las operaciones del hipervisor para clonar, mover o exportar.

Guarda el laboratorio en almacenamiento local aprobado, con suficiente espacio. Evita ejecutar una VM mientras su carpeta se sincroniza activamente o se copia parcialmente. El medio de respaldo debe ser independiente del disco de trabajo cuando se pretenda proteger frente a su avería.

## 6.2. Disco fijo o dinámico

Un disco fijo reserva aproximadamente su capacidad desde el principio. Uno dinámico empieza ocupando menos y crece hasta el límite configurado, con variaciones de formato y metadatos. En ambos casos, el invitado ve una capacidad lógica. Si se agota el espacio físico del anfitrión, la VM puede sufrir errores aunque su partición tenga espacio libre.

El disco dinámico facilita el aula, pero requiere vigilancia. Para dos máquinas de escritorio, clones, exportaciones y varias instantáneas, no basta con sumar el espacio actualmente usado por Windows y Ubuntu. La guía docente incluye un cálculo de presupuesto y margen.

## 6.3. Estados de una VM

Apagada significa que el sistema ha finalizado su sesión y ya no se ejecuta. Pausada detiene temporalmente la ejecución. Guardar estado conserva la memoria y la ejecución para reanudar. No equivale a completar un apagado ordenado. Forzar apagado se parece a cortar la corriente y puede perder escrituras pendientes.

Para las prácticas de almacenamiento, clonación y cambios de firmware, apagaremos el invitado desde su propio sistema y comprobaremos el estado apagado en VirtualBox. Así se reducen ambigüedades y se facilita repetir los pasos.

## 6.4. Guest Additions y Extension Pack

Las Guest Additions se instalan dentro del invitado e incorporan controladores y servicios de integración, como ajuste de pantalla y determinadas funciones de intercambio. El Extension Pack se añade al hipervisor del anfitrión y habilita funciones adicionales según la versión. Son productos diferentes. Las prácticas básicas no requieren instalar el Extension Pack. Referencias F4 y F5.

Si una función de integración no funciona, comprueba versión, servicio, permisos y reinicio. No reinstales el sistema completo por un fallo de portapapeles. En Ubuntu la construcción de módulos puede requerir herramientas, cabeceras del kernel y, con Secure Boot, gestión de firma de módulos. La práctica ofrece una ruta alternativa si el centro distribuye los complementos como paquetes.

## Actividad A6 · Prever crecimiento

Un anfitrión tiene 100 GiB libres. Dos VDI dinámicos de 80 GiB ocupan hoy 20 GiB cada uno. ¿Puedes asegurar que nunca se agotará el almacenamiento? Propón una política de vigilancia y explica cómo cambian tus cálculos al exportar ambas máquinas. Continúa con P1 y P7.
