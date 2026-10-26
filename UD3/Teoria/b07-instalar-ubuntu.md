# B7. Instalar Ubuntu y comprobar el resultado

> **Del concepto al laboratorio:** [P2 · Instalar Ubuntu](practicas/p2-ubuntu.md) · [P9 · Proyecto integrador](practicas/p9-proyecto.md)

## 7.1. Probar no es instalar

El modo Live permite ejecutar un entorno desde la ISO. Es útil para comprobar dispositivos o inspeccionar un disco que no arranca. Los cambios de una sesión Live ordinaria pueden perderse al reiniciar. Abrir el escritorio Live no demuestra que Ubuntu esté instalado en el disco virtual.

La prueba decisiva será apagar, retirar la ISO y arrancar desde el disco. Si el sistema funciona, comprobarás además que el usuario y un archivo creado antes del reinicio siguen presentes.

## 7.2. Decisiones del instalador

Antes de confirmar, identifica idioma, teclado, zona horaria, red, modalidad de instalación y disco de destino. La práctica P2 utiliza instalación interactiva en un único VDI vacío. La instalación automática o desatendida se reserva para una ampliación, porque el aprendizaje inicial requiere ver las decisiones.

En «Borrar disco», el disco debe ser el VDI de la VM de prácticas. Esta instrucción no se traslada a una instalación física. No habrá discos físicos conectados mediante acceso directo. Para practicar particionado manual utilizaremos otra máquina o un clon, sin mezclarlo con la primera instalación automática. Referencia F6.

## 7.3. Identidad, hora y permisos

El nombre del equipo identifica la máquina; el nombre de usuario identifica una cuenta. Cambiar uno no cambia automáticamente el otro. El primer usuario puede tener permiso para administrar mediante sudo, pero las tareas ordinarias se realizan sin elevación.

Europe/Madrid permite aplicar la zona horaria correspondiente. Una hora incorrecta puede causar fallos de certificados, actualizaciones o registros difíciles de comparar. Si un navegador rechaza un certificado, no desactives la validación antes de revisar hora, red y mensaje exacto.

## 7.4. Comprobar de manera observable

```bash
cat /etc/os-release
uname -r
hostnamectl
timedatectl
free -h
lsblk -f
ip -br address
ip route
```

cat /etc/os-release identifica la distribución y versión. uname -r informa del kernel, no del número de versión de Ubuntu. free muestra memoria y no el tamaño del SSD. ip address muestra interfaces; una dirección 127.0.0.1 identifica la propia máquina, no la conectividad de red.

La aceptación de P2 exige arranque sin ISO, usuario funcional, escritura persistente, disco esperado, memoria coherente, reloj correcto y acceso a los repositorios. Una captura del escritorio por sí sola no permite comprobar esos criterios.

## Actividad A7 · Detectar una falsa instalación

Un compañero trabaja en el escritorio Ubuntu, pero al retirar la ISO aparece «No bootable medium». Escribe dos hipótesis y una comprobación para cada una. ¿Qué evidencia distinguiría un escritorio Live de un sistema instalado? Continúa con P2.
