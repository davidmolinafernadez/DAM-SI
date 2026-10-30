# 4.4 · Sistemas de archivos y montaje

<div class="lesson-banner" markdown>
<div class="lesson-number">4.4</div>
<div markdown>
**Particiones y sistemas de archivos**

Sistemas de archivos y montaje: explicación, ejemplos y comprobaciones.
</div>
</div>

## Qué organiza un sistema de archivos

Además de los datos de los archivos, hay metadatos: nombres, tamaños, permisos, propietarios, fechas y referencias a bloques. Una carpeta ayuda a localizar entradas; no es una caja física de sectores contiguos. Borrar un nombre no equivale siempre a sobrescribir inmediatamente todos los datos asociados.

El journaling registra operaciones para mejorar la recuperación de coherencia tras interrupciones. No recupera automáticamente un documento borrado ni convierte la unidad en una copia de seguridad. El cifrado protege datos frente a determinados accesos sin la clave; también exige planificar cómo recuperar la clave.

## Elegir según el uso

NTFS es habitual para el sistema Windows y permite permisos y archivos grandes. ext4 es una elección habitual para Linux. FAT32 tiene amplia compatibilidad y limita el tamaño de un archivo a 4 GiB menos 1 byte. exFAT suele servir para intercambio de archivos grandes entre sistemas, pero no ofrece el mismo modelo de permisos que NTFS o ext4. FAT32 conserva un papel importante en la partición EFI.

No existe un «mejor sistema de archivos» para todos los destinos. Para una ISO de 6 GiB en una memoria de intercambio, FAT32 sería una elección problemática. Para la raíz del Ubuntu de esta unidad elegiremos ext4. Para el sistema Windows dejaremos que el instalador utilice el esquema correspondiente. La actividad se centra en justificar decisiones, no en memorizar máximos teóricos dependientes de implementación.

## Letras y puntos de montaje

Windows suele mostrar volúmenes mediante letras como C: o D:. Linux integra los sistemas de archivos en un árbol mediante puntos de montaje. /home es un directorio que puede pertenecer a la raíz o ser el punto donde se monta otro volumen.

No confíes en que /dev/sdb será siempre el disco secundario: el orden puede cambiar y puede haber nombres NVMe o distintos controladores. Compara tamaño, tipo, identificadores y montajes. Para referencias persistentes se pueden usar UUID. Dos discos clonados pueden compartir UUID, una razón adicional para planificar cómo se conectan.

Comprobaciones de lectura en Ubuntu:

```bash
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
findmnt /
df -hT
```

lsblk describe dispositivos y su jerarquía; findmnt muestra qué se ha montado; df informa del uso de sistemas montados. Un disco sin montar puede aparecer en lsblk y no en df. No es una contradicción.

## Capacidad aparente y capacidad física

GB decimal y GiB binario no son iguales. Un fabricante y una herramienta pueden representar la misma capacidad con cifras diferentes. Además, un disco virtual dinámico presenta al invitado su capacidad máxima, mientras el archivo del anfitrión crece según se escriben datos y metadatos. Borrar archivos dentro del invitado no garantiza que el archivo VDI se reduzca inmediatamente.

## Leer una jerarquía de dispositivos

En una salida de lsblk, el nivel superior puede representar un disco y los inferiores sus particiones. El tipo `disk` no significa que ya haya un sistema de archivos montado. Si aparece `part`, se trata de una partición; su columna de formato puede seguir vacía antes de crear un sistema de archivos. La columna de montajes indica dónde se integra lo que está disponible para acceder a archivos.

Un directorio y un volumen no son equivalentes. Si creas `/mnt/datos` y no montas nada ahí, escribir dentro puede estar utilizando el sistema de archivos raíz. Por eso, antes de celebrar que el disco de datos funciona, hay que consultar findmnt y comprobar que la ruta corresponde al volumen previsto.

## Desmontar también es una operación técnica

El sistema puede mantener escrituras pendientes. Desmontar de forma ordenada permite cerrar el acceso y completar operaciones antes de retirar el dispositivo. Si una herramienta indica que el volumen está ocupado, comprueba archivos y terminales que lo estén usando. No fuerces la retirada como respuesta inicial: el mensaje describe una condición que debe investigarse.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 4.5 · Elegir un sistema de archivos](actividades/A05-elegir-un-sistema-de-archivos.md)

## Prácticas relacionadas

- [P4 · Particionar y montar](practicas/p4-particionado.md)

<div class="video-card" markdown>

## Vídeo explicativo · Particionar con GParted

V10: distingue dispositivo, partición y formato. No reproduzcas su mapa sobre el disco del sistema.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/417dd5j5i92wjmop/fs" title="Particionar con GParted" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/417dd5j5i92wjmop) · [Ficha y preguntas de visionado](videos.md)

</div>
