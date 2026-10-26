# 3.3.1 · Instalar Ubuntu y comprobar el resultado

<div class="lesson-banner" markdown>
<div class="lesson-number">3.3.1</div>
<div markdown>
**Instalación de Ubuntu y Windows**

Instalar y comprobar Ubuntu: explicación, ejemplos y comprobaciones.
</div>
</div>

## Probar no es instalar

El modo Live permite ejecutar un entorno desde la ISO. Es útil para comprobar dispositivos o inspeccionar un disco que no arranca. Los cambios de una sesión Live ordinaria pueden perderse al reiniciar. Abrir el escritorio Live no demuestra que Ubuntu esté instalado en el disco virtual.

La prueba decisiva será apagar, retirar la ISO y arrancar desde el disco. Si el sistema funciona, comprobarás además que el usuario y un archivo creado antes del reinicio siguen presentes.

## Decisiones del instalador

Antes de confirmar, identifica idioma, teclado, zona horaria, red, modalidad de instalación y disco de destino. La práctica P2 utiliza instalación interactiva en un único VDI vacío. La instalación automática o desatendida se reserva para una ampliación, porque el aprendizaje inicial requiere ver las decisiones.

En «Borrar disco», el disco debe ser el VDI de la VM de prácticas. Esta instrucción no se traslada a una instalación física. No habrá discos físicos conectados mediante acceso directo. Para practicar particionado manual utilizaremos otra máquina o un clon, sin mezclarlo con la primera instalación automática. Referencia F6.

## Identidad, hora y permisos

El nombre del equipo identifica la máquina; el nombre de usuario identifica una cuenta. Cambiar uno no cambia automáticamente el otro. El primer usuario puede tener permiso para administrar mediante sudo, pero las tareas ordinarias se realizan sin elevación.

Europe/Madrid permite aplicar la zona horaria correspondiente. Una hora incorrecta puede causar fallos de certificados, actualizaciones o registros difíciles de comparar. Si un navegador rechaza un certificado, no desactives la validación antes de revisar hora, red y mensaje exacto.

## Comprobar de manera observable

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

## Qué significan las pantallas de instalación

Idioma determina textos, teclado determina qué carácter produce una tecla y zona horaria interpreta la hora local. Son decisiones distintas: elegir español no garantiza que se haya seleccionado la distribución física del teclado del puesto. Probar símbolos antes de escribir una contraseña evita registrar una clave diferente de la que se cree haber escrito.

La selección de aplicaciones decide qué se instala inicialmente, pero no bloquea para siempre instalar otras después. La pantalla de disco tiene un efecto mucho mayor: puede crear tabla, formatear y cambiar el arranque. Por eso se detiene el procedimiento en el resumen de cambios y se comprueba el destino antes de confirmar.

## La contraseña de sudo y las comprobaciones

En una terminal, sudo puede solicitar la contraseña sin dibujar asteriscos. La ausencia de caracteres visibles es un comportamiento habitual. Después de ejecutar una orden administrativa hay que leer su resultado; que vuelva el prompt no demuestra por sí solo que todo haya terminado correctamente.

La prueba de persistencia debe recorrer un reinicio real desde disco. Suspender o guardar estado puede conservar una sesión Live y ocultar la diferencia. Por eso se retira la ISO, se apaga o reinicia según la práctica y se vuelve a localizar el archivo dentro del sistema instalado.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 3.7 · Detectar una falsa instalación](actividades/A07-detectar-una-falsa-instalacion.md)

## Prácticas relacionadas

- [P2 · Instalar Ubuntu](practicas/p2-ubuntu.md)

<div class="video-card" markdown>

## Vídeo explicativo · Instalación Ubuntu 24.04

V3: pausa antes de elegir disco y contrasta el destino con la ficha de P2.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/4dpxwfhdfpr4p799/fs" title="Instalación Ubuntu 24.04" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/4dpxwfhdfpr4p799) · [Ficha y preguntas de visionado](videos.md)

</div>
