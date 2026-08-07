# UD4. Sistemas de archivos, particionado y copias

## 1. Resultados de aprendizaje

Esta unidad aborda la organización de la información, los sistemas de archivos, particiones y volúmenes, localización de datos, copias de seguridad, automatización e integridad.

## 2. Archivos, directorios y rutas

Un archivo contiene datos y metadatos como nombre, tamaño, fechas, propietario y permisos. Los directorios organizan entradas de forma jerárquica.

Una ruta absoluta comienza en la raíz del sistema; una ruta relativa parte del directorio de trabajo. En Linux la raíz es `/`; en Windows cada volumen suele usar una letra, como `C:\`.

Linux distingue mayúsculas y minúsculas y usa `/` como separador. Windows normalmente no distingue mayúsculas en NTFS y usa `\`, aunque muchas herramientas aceptan `/`.

## 3. Estructura de directorios

En Linux son importantes:

- `/etc`: configuración del sistema;
- `/home`: datos de usuarios;
- `/var`: datos variables y registros;
- `/usr`: aplicaciones y recursos compartidos;
- `/tmp`: archivos temporales;
- `/dev`: representación de dispositivos;
- `/proc` y `/sys`: información del kernel y hardware.

En Windows destacan `C:\Windows`, `C:\Program Files`, `C:\Users` y `C:\ProgramData`. Las variables de entorno ayudan a localizar rutas sin depender de nombres concretos.

## 4. Sistemas de archivos

Un sistema de archivos define cómo se nombran, almacenan y recuperan datos.

| Sistema | Uso frecuente | Características |
| --- | --- | --- |
| NTFS | Windows | ACL, registro, compresión y archivos grandes |
| FAT32 | Compatibilidad | Muy extendido, pero limita archivos a 4 GiB |
| exFAT | Unidades extraíbles | Archivos grandes y buena interoperabilidad |
| ext4 | GNU/Linux | Registro, estabilidad y amplio soporte |
| XFS | Linux y servidores | Escalabilidad y buen rendimiento |

El journaling registra operaciones pendientes para mejorar la recuperación tras una interrupción. No evita la necesidad de copias.

## 5. Particiones y volúmenes

Una partición divide lógicamente un dispositivo. MBR admite un esquema heredado con limitaciones; GPT incluye identificadores, redundancia y soporte para discos grandes.

Un volumen es una unidad lógica formateada. LVM añade una capa flexible: los volúmenes físicos forman grupos y estos proporcionan volúmenes lógicos ampliables.

Operaciones de consulta en Linux:

```bash
lsblk -f
df -h
du -sh /ruta
findmnt
```

Antes de crear o modificar particiones debe verificarse el nombre del dispositivo y desmontar el sistema de archivos cuando la herramienta lo requiera.

## 6. Operaciones y búsqueda

```bash
pwd
ls -lah
mkdir proyecto
cp -a origen destino
mv origen destino
find /var/log -type f -name "*.log"
grep -R "error" /var/log
```

`rm` elimina sin papelera en la mayoría de shells. Debe comprobarse la ruta y evitar privilegios elevados innecesarios. Las tuberías conectan la salida de una orden con la entrada de otra; las redirecciones guardan o alimentan datos.

## 7. Integridad

Una suma criptográfica detecta cambios accidentales o maliciosos:

```bash
sha256sum imagen.iso
```

En PowerShell puede usarse:

```powershell
Get-FileHash .\imagen.iso -Algorithm SHA256
```

Una coincidencia confirma integridad respecto al valor de referencia, pero no demuestra por sí sola que la fuente sea legítima.

## 8. Copias de seguridad

- **Completa:** incluye todos los datos seleccionados.
- **Incremental:** guarda cambios desde la última copia de cualquier tipo.
- **Diferencial:** guarda cambios desde la última completa.
- **Espejo:** replica el estado; puede propagar borrados y no equivale a un histórico.

La regla 3-2-1 recomienda tres copias, dos soportes distintos y una copia fuera de la ubicación principal. Una estrategia moderna debe añadir versiones inmutables o desconectadas frente a ransomware.

RPO expresa cuánto dato se puede perder; RTO, cuánto tiempo puede tardar la recuperación.

## 9. Restauración y automatización

Una copia solo es válida si puede restaurarse. Se debe comprobar registro, integridad, permisos, propietarios y funcionamiento de los datos recuperados.

La automatización puede realizarse con el Programador de tareas o `cron`/temporizadores de `systemd`. Los scripts deben registrar fecha, origen, destino, resultado y código de salida.

Ejemplo con `robocopy`:

```powershell
robocopy C:\Datos D:\Copias\Datos /MIR /R:2 /W:5 /LOG:D:\Copias\copia.log
```

`/MIR` replica también eliminaciones; debe probarse primero con datos no críticos.

## 10. Resumen

Gestionar información exige comprender la jerarquía, el sistema de archivos y la capa de almacenamiento. Las copias deben estar planificadas, automatizadas, protegidas y, sobre todo, verificadas mediante restauraciones periódicas.

## Fuentes internas utilizadas

- `Jose_SO/UD4.pdf`.
- `Jose_SO/UD4B.pdf`.
- `Programacion_Didactica_SI_David_Moli.docx`.
