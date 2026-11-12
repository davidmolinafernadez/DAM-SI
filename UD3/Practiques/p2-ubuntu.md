# P2. Ubuntu Desktop: de la ISO al sistema instalado

[Antes de empezar: materiales, descargas y comprobaciones](preparacion.md).

<div class="lesson-banner" markdown>
<div class="lesson-number">P2</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Firmware, arranque y particiones](../b04-firmware-y-particiones.md) · [Instalar y comprobar Ubuntu](../b07-instalar-ubuntu.md)

Duración orientativa: 180 minutos. Estado inicial: máquina de P1, un único VDI vacío de 50 GiB, NAT y Ubuntu Desktop 24.04 LTS. Esta guía describe la secuencia habitual; alguna pantalla puede cambiar de posición según la revisión. Nunca confirmes un borrado sin identificar el destino.

## 1. Arranca el medio y reconoce el modo Live

Selecciona `UD3-Ubuntu-codigo` en el administrador y pulsa **Iniciar**. En el menú de Ubuntu selecciona **Try or Install Ubuntu** con las flechas y pulsa **Intro**. Espera a que cargue. Si llegas al escritorio sin instalador abierto, haz doble clic en **Install Ubuntu / Instalar Ubuntu**.

El escritorio de prueba se ejecuta desde el medio. Abrir Firefox en él no acredita una instalación en disco. La comprobación final consistirá en retirar la ISO y reiniciar conservando un archivo.

## 2. Recorre las decisiones iniciales

1. Selecciona **Español** y pulsa **Siguiente**. En accesibilidad activa las opciones que necesites; en caso contrario continúa.
2. En **Distribución del teclado**, selecciona la del puesto. Utiliza el cuadro de prueba: escribe `ñ`, `@`, `/` y algún signo. Si no coinciden, cambia la distribución antes de crear una contraseña.
3. En conexión de red, utiliza la conexión cableada virtual disponible por NAT. Puede aparecer como cable aunque el anfitrión esté conectado por Wi-Fi.
4. Si se ofrece actualizar el propio instalador, sigue la decisión del docente y espera a que termine. No lo confundas con haber actualizado todo el sistema instalado.
5. Cuando pregunte qué quieres hacer, selecciona **Instalar Ubuntu**. En modalidad, elige **Instalación interactiva**. El archivo de instalación automática no forma parte de esta primera experiencia.
6. En selección de aplicaciones, elige la opción acordada. Anota si instalas una selección predeterminada o ampliada. Decide con el docente las descargas adicionales y el software de terceros; la red del aula puede aconsejar posponerlos.

## 4. Identifica el disco antes de confirmar

En el apartado de configuración del disco selecciona **Borrar disco e instalar Ubuntu** solo después de verificar que es el VDI vacío de 50 GiB de esta VM. Si aparecen discos inesperados o capacidad distinta, vuelve atrás: no se resuelve eligiendo uno al azar.

Abre las opciones avanzadas si necesitas comprobar qué modalidad se aplicará. En la primera instalación usa el reparto automático acordado, sin activar cifrados o LVM que el grupo todavía no haya preparado. El particionado manual se practica después en un disco identificado. Anota qué disco va a cambiar y qué datos contiene actualmente.

## 4. Identidad, ubicación e instalación

Rellena tu nombre de aula, nombre del equipo y usuario. Usa minúsculas y un nombre sencillo para el usuario, por ejemplo `alumno`; el nombre de máquina puede ser `ud3-ubuntu-codigo`. Introduce la contraseña prevista sin incluirla en capturas. Selecciona **Madrid** o la zona **Europe/Madrid** en el mapa o búsqueda de ubicación.

En el resumen final lee el dispositivo afectado y los cambios previstos. Haz una captura recortada a esa información, explica por qué el destino es correcto y pulsa **Instalar**. Durante la copia no cierres la ventana ni fuerces el apagado. El orden exacto de identidad, ubicación y disco puede variar; el requisito es revisar todos los datos antes de la confirmación destructiva.

## 5. Retira la ISO y comprueba un arranque independiente

Cuando el instalador termine pulsa **Reiniciar ahora**. Si solicita retirar el medio, utiliza el menú de la ventana del invitado **Dispositivos → Unidades ópticas → Retirar disco de la unidad virtual** y pulsa **Intro** cuando proceda. Si la unidad no se deja liberar, apaga la VM y realiza la retirada desde **Configuración → Almacenamiento**, seleccionando la ISO y el icono de disco → **Retirar disco**. No elimines el VDI.

Arranca otra vez. Debe aparecer el Ubuntu instalado y la cuenta configurada. Si vuelves a ver el instalador, revisa medio y orden de arranque. No repitas la instalación para resolver un medio aún conectado.

## 6. Abre la terminal y crea una prueba persistente

Dentro de Ubuntu pulsa **Ctrl + Alt + T**. Esta combinación abre una terminal del invitado cuando el foco está dentro de su escritorio. Si el atajo lo captura el anfitrión, abre **Mostrar aplicaciones**, busca **Terminal** y ejecútala.

```bash
printf 'Mi sistema instalado de la UD3\n' > ~/comprobacion-ud3.txt
cat ~/comprobacion-ud3.txt
cat /etc/os-release
hostnamectl
timedatectl
free -h
lsblk -f
ip -br address
ip route
```

Ejecuta una orden cada vez. `printf` crea un archivo en tu carpeta personal; `cat` permite leerlo. Interpreta distribución, nombre, hora, memoria, discos y red. No entregues una captura de diez órdenes sin explicar sus resultados.

Abre el menú de estado de la esquina superior derecha de Ubuntu y selecciona **Apagar/Cerrar sesión → Reiniciar**, según el texto disponible. Tras volver a iniciar sesión, abre la terminal y lee de nuevo el archivo. Debe conservar su contenido.

## 7. Integración y aceptación

La instalación de Guest Additions se realiza solo mediante la ruta aprobada del centro. En la ventana de la VM se encuentra **Dispositivos → Insertar imagen de CD de Guest Additions**. Los complementos se instalan dentro del invitado; el Extension Pack no es su sustituto. Si se necesitan módulos, cabeceras o firma con Secure Boot, registra el resultado y utiliza el procedimiento docente, sin cambiar la seguridad del anfitrión.

Aceptación: arranque sin ISO, usuario correcto, archivo persistente, raíz en el disco, recursos y reloj coherentes. Entrega resumen de destino, tabla de comprobaciones y evidencia tras reinicio. **Incidencia:** explica cómo distinguir sesión Live, ISO aún conectada y disco no instalado utilizando una prueba para cada hipótesis.

## Qué debes entregar

Entrega **un único informe PDF**, llamado `P2_Apellidos_Nombre.pdf`, que documente la práctica de principio a fin con **una sucesión ordenada de capturas de pantalla propias y una pequeña explicación de cada paso**. Toma las capturas mientras trabajas e insértalas junto al paso correspondiente; utiliza la lista de abajo para no olvidar las pruebas necesarias.

### Estructura del informe

1. **Portada:** práctica, nombre y apellidos, grupo, fecha, VM utilizada y sistema anfitrión.
2. **Preparación:** estado inicial, materiales y configuración necesarios.
3. **Proceso paso a paso:** sigue el orden de los apartados de esta guía. En cada paso escribe qué has hecho, añade la captura o capturas y explica el resultado observado en 2–4 líneas. Si una decisión no genera una pantalla propia, escríbela igualmente.
4. **Comprobaciones finales:** presenta las pruebas solicitadas y sus resultados; una barra de progreso o un escritorio por sí solos no acreditan todas las comprobaciones.
5. **Incidencias y conclusión:** responde al caso planteado y registra los problemas reales, las pruebas y su resultado. Si no hubo problemas reales, indícalo. Explica qué has conseguido y qué queda pendiente.

**Modelo para repetir en cada paso:**

- **Paso y título:** [número y acción].
- **Acción realizada:** [qué has hecho y qué opción o comando has utilizado].
- **Captura:** [inserta aquí la imagen propia con su código].
- **Explicación:** [qué se ve, por qué has elegido esa opción y qué demuestra el resultado].

### Capturas y explicaciones que debe contener

| Captura | Momento del proceso | Explicación que debes escribir |
| --- | --- | --- |
| P2-01 | Arranque desde la ISO y sesión Live | Qué medio ha arrancado y por qué aún no acredita una instalación. |
| P2-02 | Idioma, teclado, red y modalidad interactiva | Qué opciones has elegido y cómo has probado el teclado. Añade las imágenes necesarias. |
| P2-03 | Selección de aplicaciones y opciones adicionales | Qué instalarás y qué has decidido posponer. |
| P2-04 | Disco de destino y resumen antes de instalar | Nombre y capacidad del disco virtual, cambios previstos y por qué es el destino correcto. |
| P2-05 | Identidad, zona horaria y progreso o finalización | Usuario y nombre de máquina, zona elegida y resultado de la instalación, sin mostrar contraseñas. |
| P2-06 | Unidad óptica sin ISO y arranque posterior | Cómo has retirado el medio y qué sistema arranca desde el disco. |
| P2-07 | Consultas de sistema, memoria, discos y red | Resultado de cada comando del apartado 6 y qué permite comprobar. Usa varias capturas legibles. |
| P2-08 | Archivo testigo antes y después de reiniciar | Ruta, contenido y por qué su conservación prueba persistencia. |
| P2-09 | Integración y comprobación final | Qué has comprobado de Guest Additions si se realizó, y qué criterios de aceptación se cumplen o quedan pendientes. |

**Incluye además:** tabla de comprobaciones (criterio, prueba, resultado y captura), resumen del disco elegido y respuesta razonada a la incidencia sobre sesión Live, ISO conectada y disco no instalado.

**Ejemplo de pie:** «P2-08. Tras reiniciar sin ISO, leo de nuevo `~/comprobacion-ud3.txt` y conserva el contenido. Junto al arranque sin medio y la raíz en el disco, esta prueba acredita que trabajo sobre la instalación». Utiliza esta conclusión solo si tus pruebas la confirman.

### Antes de entregar

Guarda las capturas en la carpeta de evidencias autorizada, fuera de la VM que puedas restaurar. Numéralas como en la tabla; si necesitas varias para un punto, utiliza `a`, `b`, etc. Deben verse los valores y mensajes necesarios, sin contraseñas ni claves. Si una pantalla cambia según la versión, documenta la equivalente y explícalo; si un paso no puede completarse, registra el error y la comprobación pendiente.

Revisa que el PDF incluya todos los pasos, que sus imágenes se lean y que cada una tenga explicación. **Sube el informe PDF a la tarea de la práctica en Aules; las capturas deben ir dentro del informe.** No subas capturas sueltas, ISO, VDI ni OVA. Las respuestas y tablas de esta práctica van en el mismo PDF y no generan otra entrega.
<div class="video-card" markdown>

## Vídeo explicativo · Instalación Ubuntu 24.04

V3: pausa antes de elegir disco y contrasta el destino con la ficha de P2.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/4dpxwfhdfpr4p799/fs" title="Instalación Ubuntu 24.04" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/4dpxwfhdfpr4p799) · [Ficha y preguntas de visionado](../videos.md)

</div>
