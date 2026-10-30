# 1. Usuarios, grupos, permisos y ACL

## 1.1 Identidad y control de acceso

```mermaid
flowchart LR
    ID["Identificación: quién dices ser"] --> AUTHN["Autenticación: demostrarlo"]
    AUTHN --> AUTHZ["Autorización: qué puedes hacer"]
    AUTHZ --> AUDIT["Auditoría: qué hiciste"]
```

Una cuenta personal permite trazabilidad. Las cuentas de servicio no deben usarse para sesiones interactivas. Los grupos representan funciones: alumnado, desarrollo, copias o administración.

## 1.2 Linux

`/etc/passwd` relaciona nombre y UID; `/etc/shadow` almacena información de contraseña con acceso restringido; `/etc/group` define grupos.

```bash
sudo useradd -m -s /bin/bash ana
sudo passwd ana
sudo groupadd desarrollo
sudo usermod -aG desarrollo ana
id ana
getent passwd ana
```

Olvidar `-a` al modificar grupos suplementarios puede reemplazar membresías existentes.

## 1.3 Permisos POSIX

```text
-rwxr-x--- 1 ana desarrollo 1200 informe.sh
```

- `-`: archivo ordinario;
- `rwx`: propietaria puede leer, escribir y ejecutar;
- `r-x`: grupo puede leer y ejecutar;
- `---`: otros no acceden.

En directorios, `r` lista nombres, `w` modifica entradas y `x` permite atravesar. Para leer un archivo se necesitan permisos sobre él y ejecución en todos los directorios de la ruta.

```bash
chmod 750 proyecto
chmod u=rw,g=r,o= informe.txt
chown -R ana:desarrollo proyecto
```

## 1.4 Bits especiales

- setgid en un directorio hace que nuevos elementos hereden el grupo;
- sticky bit limita borrado en directorios compartidos;
- setuid ejecuta un binario con identidad propietaria y exige especial revisión.

```bash
sudo chmod 2770 /srv/proyecto
```

## 1.5 ACL

Las ACL conceden permisos a identidades adicionales:

```bash
setfacl -m u:revisor:r-x /srv/proyecto
setfacl -m d:g:desarrollo:rwx /srv/proyecto
getfacl /srv/proyecto
```

La máscara limita permisos efectivos de entradas nombradas. Una ACL aparentemente `rwx` puede resultar `r-x` por la máscara.

## 1.6 Windows

NTFS usa descriptores y entradas ACE en una DACL. La herencia propaga permisos desde carpetas superiores. Es preferible asignar permisos a grupos y gestionar membresías.

```powershell
New-LocalGroup -Name "Desarrollo"
Add-LocalGroupMember -Group "Desarrollo" -Member "ana"
Get-Acl C:\Proyectos | Format-List
```

Permisos de compartición y NTFS se combinan; el resultado es el más restrictivo aplicable. Las denegaciones explícitas complican el análisis y se reservan para casos justificados.

## 1.7 Diseño por roles

Caso: `/srv/web` debe permitir que desarrollo modifique, revisión lea y el servicio web solo lea.

1. Crear grupos funcionales.
2. Asignar propiedad y setgid.
3. Conceder `rwx` a desarrollo.
4. ACL `r-x` a revisión y cuenta del servicio.
5. Retirar acceso a otros.
6. Probar con cada identidad.
7. Documentar permisos efectivos.

## Principio de mínimo privilegio

Una persona administra con cuenta ordinaria y eleva solo la operación necesaria. Dar administración permanente “por comodidad” aumenta superficie de error y ataque.

## Ejemplo resuelto: leer, modificar y borrar son permisos diferentes

Supongamos `/srv/proyecto` con permisos `2770`, propiedad de `ana:desarrollo`,
y un archivo `informe.txt` con permisos `640` y la misma propiedad. No hay
ACL adicionales. Bruno pertenece a `desarrollo` y Clara no pertenece al grupo.
Ambos pueden atravesar `/srv`; no hay otros controles que restrinjan el acceso.

| Operación | Ana | Bruno | Clara |
|---|---|---|---|
| Listar `/srv/proyecto` | Sí | Sí | No |
| Leer `informe.txt` | Sí | Sí | No |
| Modificar el contenido existente | Sí | No | No |
| Crear otro archivo en la carpeta | Sí | Sí | No |
| Borrar la entrada `informe.txt` | Sí | Sí | No |

Bruno puede borrar el archivo porque dispone de escritura y ejecución sobre
el **directorio**, aunque no pueda modificar el contenido del archivo. Si se
añade sticky bit, el borrado se restringe a la persona propietaria del archivo,
la propietaria del directorio o una identidad privilegiada.

El bit setgid conserva el grupo del directorio en nuevos elementos, pero no
garantiza escritura para el grupo: también intervienen el modo solicitado al
crear, la `umask` y las ACL por defecto. Una `umask 0027` transforma los modos
habituales `666` y `777` en `640` para archivos y `750` para directorios.

Comprueba estos casos con cuentas de prueba en una VM. Registra `id`, `ls -ld`
y `getfacl` antes de concluir. Tras añadir una cuenta a un grupo, abre una nueva
sesión para que los procesos reciban la membresía actualizada.
