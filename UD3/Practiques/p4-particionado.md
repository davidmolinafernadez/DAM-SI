# P4. Particionar y montar un disco de datos

<div class="lesson-banner" markdown>
<div class="lesson-number">P4</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Firmware, arranque y particiones](../b04-firmware-y-particiones.md) · [Sistemas de archivos y montaje](../b05-sistemas-de-archivos.md)

Duración orientativa: 150 minutos. Se trabaja con un **VDI nuevo de 8 GiB** añadido a Ubuntu. El disco de sistema de 50 GiB queda excluido de cualquier formato. Antes de escribir, compara nombre, tamaño y montajes.

## 1. Añade el disco desde VirtualBox

Apaga Ubuntu desde su menú. En el administrador comprueba el estado **Apagada**. Abre **Configuración → Almacenamiento** y selecciona el controlador al que se conectan los discos duros, normalmente SATA. Pulsa el icono de **Añadir disco duro**; si ofrece un selector de medios, pulsa **Crear**. Crea `UD3-DATOS-codigo.vdi`, formato VDI, asignación dinámica y capacidad de **8 GiB**. Selecciona ese archivo y confirma que quedan conectados el disco de sistema y el nuevo.

Arranca Ubuntu y pulsa **Ctrl + Alt + T**. Ejecuta:

```bash
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
```

Identifica el disco de 8 GiB sin sistemas montados. El disco que contiene `/` no se toca. El nombre puede ser `sdb`, pero no debes darlo por supuesto: depende del controlador y del orden de detección.

## 2. Abre Discos e identifica el destino otra vez

Pulsa **Mostrar aplicaciones**, busca **Discos** y abre la herramienta. Si no está instalada, el docente indicará la herramienta alternativa antes de continuar. Selecciona en la columna izquierda el dispositivo de **8 GiB**. Contrasta su capacidad con `lsblk` y haz una captura del destino antes del formato.

En **Discos**, utiliza el menú de opciones del dispositivo —normalmente tres puntos en la parte superior— → **Formatear disco**. Esta opción crea o reemplaza la tabla del disco entero; no es lo mismo que formatear una sola partición. Elige **GPT** como esquema y confirma únicamente sobre el dispositivo vacío de 8 GiB. No selecciones borrado seguro completo.

## 3. Crea una partición ext4 de aproximadamente 4 GiB

Selecciona el espacio libre de ese dispositivo y pulsa **+**. Escribe una capacidad cercana a **4 GiB**, comprobando si el cuadro usa GiB, GB o MB. Continúa y elige formato **ext4**, con etiqueta `UD3_DATOS`. Si la interfaz no lo muestra inicialmente, utiliza **Otro** para localizarlo. Confirma y espera a que finalice.

Observa que queda una partición con sistema de archivos y otra zona sin asignar. No es un error: queremos distinguir capacidad del disco y capacidad del volumen. Si utilizas GParted, selecciona el disco en el desplegable superior, después **Dispositivo → Crear tabla de particiones → gpt**, y crea la partición mediante **Partición → Nueva**. En GParted revisa las operaciones pendientes y aplica con el botón de confirmación; no mezcles operaciones de ambas herramientas a la vez.

## 4. Monta, escribe y desmonta

Con la partición seleccionada en **Discos**, pulsa el botón triangular de montar. Anota la ruta que aparece como **Montado en**. También puedes abrir **Archivos → Otras ubicaciones** y seleccionar el volumen de datos. Ejecuta `findmnt` y `df -hT` para observar qué volumen está realmente montado.

Intenta crear `prueba-persistencia.txt` dentro de ese volumen. Si el directorio pertenece a root y tu usuario no puede escribir, no cambies permisos de todo `/media`. Primero comprueba el punto exacto con `findmnt`; después ajusta el propietario de la raíz de ese volumen mediante el procedimiento supervisado. Escribir en tu carpeta personal no demuestra que hayas escrito en el disco secundario.

Vuelve a Discos y pulsa el botón cuadrado de **Desmontar**. Monta otra vez y abre el archivo. Apaga y reinicia; si el volumen no se monta automáticamente, vuelve a montarlo desde la interfaz y comprueba el mismo contenido. Los datos persistentes y el montaje automático son propiedades distintas.

## 5. Aceptación y ampliación

Entrega mapas antes/después, identificación del destino, partición ext4, espacio libre sin asignar y archivo tras remontar. Explica por qué el dispositivo puede aparecer en `lsblk` y no en `df`.

La ampliación de montaje al inicio usa el UUID real, copia de `/etc/fstab`, punto `/mnt/ud3-datos` y validación con `findmnt --verify` y `sudo mount -a` antes de reiniciar. El docente revisará la entrada; no se copia el UUID de otra persona. No hace falta modificar fstab para superar el procedimiento básico.

## Entrega independiente de la práctica

Guarda `P4_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.

<div class="video-card" markdown>

## Vídeo explicativo · Particionar con GParted

V10: distingue dispositivo, partición y formato. No reproduzcas su mapa sobre el disco del sistema.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/417dd5j5i92wjmop/fs" title="Particionar con GParted" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/417dd5j5i92wjmop) · [Ficha y preguntas de visionado](../videos.md)

</div>
