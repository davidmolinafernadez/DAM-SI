# P4. Particionar y montar un disco de datos

**Teoría relacionada:** [Firmware, arranque y particiones](../b04-firmware-y-particiones.md) · [Sistemas de archivos y montaje](../b05-sistemas-de-archivos.md)

Duración: 150 minutos. Teoría: B4 y B5. Producto: disco de datos con GPT, ext4 y archivo persistente.

## Control del destino

Se usa la VM Ubuntu instalada. Apágala y crea un punto de retorno o un clon antes de empezar. Añade un VDI nuevo de 8 GiB con nombre UD3-DATOS-codigo. No se particiona el disco de 50 GiB del sistema. Predice qué herramientas verán un disco nuevo todavía sin formato.

## Procedimiento gráfico

1. Con Ubuntu apagado, conecta el VDI de 8 GiB al controlador de almacenamiento. Arranca y ejecuta lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS.
2. Identifica el disco por tamaño y ausencia de montajes. El disco que contiene / queda excluido. Anota su nombre real; no supongas /dev/sdb.
3. Abre Discos o GParted, según la imagen del centro. Si falta la herramienta elegida, consulta con el docente; su instalación se hace desde repositorios aprobados.
4. Selecciona el disco de 8 GiB. Antes de crear tabla, contrasta nombre y tamaño con lsblk. Si hay duda, detente en ese punto y solicita verificación del destino.
5. Crea tabla GPT. Después crea una partición de aproximadamente 4 GiB en ext4, con etiqueta UD3_DATOS. Deja el espacio restante sin asignar para distinguir «disco», «partición» y «volumen». No marques opciones de borrado seguro del disco.
6. Monta desde la herramienta gráfica o el explorador. Consulta findmnt y anota el punto de montaje real. Comprueba si tu usuario tiene escritura. Si no la tiene, ajusta únicamente el propietario del directorio raíz de ese volumen montado, verificando antes el punto exacto con findmnt. No cambies permisos de todo /media ni del sistema.
7. Crea un archivo llamado prueba-persistencia.txt con tres líneas. Desmonta mediante la herramienta, vuelve a montar y verifica el contenido. No desconectes el disco mientras esté montado.
8. Compara lsblk, findmnt y df -hT. Explica por qué los 8 GiB del disco no se convierten en 8 GiB de sistema de archivos montado si solamente has particionado la mitad.
9. Apaga, comprueba el VDI conectado y arranca. Si no se monta automáticamente al inicio, móntalo desde la interfaz y comprueba el archivo. Distingue persistencia de datos y montaje automático.

## Ampliación de montaje persistente

Solo después de superar el procedimiento básico: obtén el UUID real con lsblk -f; crea /mnt/ud3-datos; guarda copia de /etc/fstab; añade una entrada del volumen ext4 con UUID real y opciones apropiadas para un disco de laboratorio no esencial, como defaults,nofail. No copies UUID de otro alumno. Desmonta el montaje anterior, valida la sintaxis con findmnt --verify y prueba sudo mount -a antes de reiniciar. Revisa el resultado y los permisos. Una entrada incorrecta se corrige recuperando la copia, sin reiniciar a ciegas.

## Evidencias y preguntas

Aceptación: sistema original intacto, GPT en el disco secundario, partición ext4, espacio no asignado visible y archivo recuperable tras desmontar/montar. Entrega dos mapas antes/después, nombre y tamaño del destino, tabla de sistemas de archivos y una explicación de los comandos. Incidencia de análisis: «Aparece en lsblk pero no en df». Propón dos causas y cómo distinguirlas.

Pregunta final: si falla el SSD del anfitrión, ¿te protege que el archivo esté en otro VDI guardado en ese mismo SSD?
