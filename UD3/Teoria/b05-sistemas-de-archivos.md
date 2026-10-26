# B5. Sistemas de archivos y montaje

> **Del concepto al laboratorio:** [P4 · Particionar y montar](practicas/p4-particionado.md) · [P9 · Proyecto integrador](practicas/p9-proyecto.md)

## 5.1. Qué organiza un sistema de archivos

Además de los datos de los archivos, hay metadatos: nombres, tamaños, permisos, propietarios, fechas y referencias a bloques. Una carpeta ayuda a localizar entradas; no es una caja física de sectores contiguos. Borrar un nombre no equivale siempre a sobrescribir inmediatamente todos los datos asociados.

El journaling registra operaciones para mejorar la recuperación de coherencia tras interrupciones. No recupera automáticamente un documento borrado ni convierte la unidad en una copia de seguridad. El cifrado protege datos frente a determinados accesos sin la clave; también exige planificar cómo recuperar la clave.

## 5.2. Elegir según el uso

NTFS es habitual para el sistema Windows y permite permisos y archivos grandes. ext4 es una elección habitual para Linux. FAT32 tiene amplia compatibilidad y limita el tamaño de un archivo a 4 GiB menos 1 byte. exFAT suele servir para intercambio de archivos grandes entre sistemas, pero no ofrece el mismo modelo de permisos que NTFS o ext4. FAT32 conserva un papel importante en la partición EFI.

No existe un «mejor sistema de archivos» para todos los destinos. Para una ISO de 6 GiB en una memoria de intercambio, FAT32 sería una elección problemática. Para la raíz del Ubuntu de esta unidad elegiremos ext4. Para el sistema Windows dejaremos que el instalador utilice el esquema correspondiente. La actividad se centra en justificar decisiones, no en memorizar máximos teóricos dependientes de implementación.

## 5.3. Letras y puntos de montaje

Windows suele mostrar volúmenes mediante letras como C: o D:. Linux integra los sistemas de archivos en un árbol mediante puntos de montaje. /home es un directorio que puede pertenecer a la raíz o ser el punto donde se monta otro volumen.

No confíes en que /dev/sdb será siempre el disco secundario: el orden puede cambiar y puede haber nombres NVMe o distintos controladores. Compara tamaño, tipo, identificadores y montajes. Para referencias persistentes se pueden usar UUID. Dos discos clonados pueden compartir UUID, una razón adicional para planificar cómo se conectan.

Comprobaciones de lectura en Ubuntu:

```bash
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
findmnt /
df -hT
```

lsblk describe dispositivos y su jerarquía; findmnt muestra qué se ha montado; df informa del uso de sistemas montados. Un disco sin montar puede aparecer en lsblk y no en df. No es una contradicción.

## 5.4. Capacidad aparente y capacidad física

GB decimal y GiB binario no son iguales. Un fabricante y una herramienta pueden representar la misma capacidad con cifras diferentes. Además, un disco virtual dinámico presenta al invitado su capacidad máxima, mientras el archivo del anfitrión crece según se escriben datos y metadatos. Borrar archivos dentro del invitado no garantiza que el archivo VDI se reduzca inmediatamente.

## Actividad A5 · Justificar el formato

Selecciona formato para: raíz Linux, partición de Windows, ESP y memoria de intercambio con vídeos de 8 GiB. Explica una limitación de cada elección. En Ubuntu, compara lo que muestran lsblk y df sobre la partición EFI. Continúa con P4.
