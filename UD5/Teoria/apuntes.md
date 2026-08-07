# UD5. Administración de sistemas operativos

## 1. Resultados de aprendizaje

El alumnado gestionará usuarios, grupos, permisos, procesos, servicios, software, tareas y monitorización mediante herramientas gráficas y línea de comandos, aplicando privilegio mínimo.

## 2. Cuentas, grupos y privilegios

Una cuenta identifica a una persona o servicio. Los grupos simplifican la asignación de permisos. Deben evitarse cuentas compartidas porque impiden atribuir acciones.

En Linux, `/etc/passwd` contiene información de cuentas y `/etc/shadow` protege los verificadores de contraseña. `sudo` permite ejecutar acciones concretas con privilegios. En Windows, las cuentas y grupos locales pueden administrarse mediante herramientas gráficas o PowerShell.

```bash
sudo useradd -m alumne
sudo passwd alumne
sudo usermod -aG developers alumne
id alumne
```

```powershell
New-LocalUser -Name "alumne" -Password (Read-Host -AsSecureString)
Add-LocalGroupMember -Group "Users" -Member "alumne"
Get-LocalGroupMember -Group "Users"
```

Las contraseñas deben combinar longitud, bloqueo de credenciales filtradas y segundo factor cuando esté disponible. El cambio periódico sin evidencia de compromiso no sustituye una política adecuada.

## 3. Permisos y ACL

Linux aplica permisos de lectura, escritura y ejecución a propietario, grupo y otros. Para un directorio, ejecución significa poder atravesarlo.

```bash
chmod 750 proyecto
chown -R alumne:developers proyecto
getfacl proyecto
setfacl -m u:revisor:r-x proyecto
```

Windows utiliza ACL con entradas de permitir o denegar y herencia desde carpetas superiores. Las denegaciones explícitas requieren especial cuidado. La práctica recomendada es asignar permisos a grupos y añadir usuarios a esos grupos.

## 4. Procesos

Un proceso posee identificador, estado, prioridad, memoria y propietario. La terminación forzada es el último recurso porque puede dejar datos inconsistentes.

```bash
ps aux
top
pgrep nginx
nice -n 10 comando
kill -TERM 1234
```

En PowerShell:

```powershell
Get-Process
Get-Process -Name code | Select-Object Id,CPU,WorkingSet
Stop-Process -Id 1234
```

Primero se solicita una finalización ordenada; solo después se usa una señal o acción forzada.

## 5. Servicios

Un servicio ejecuta funciones en segundo plano y puede iniciarse durante el arranque.

```bash
systemctl status ssh
sudo systemctl enable --now ssh
journalctl -u ssh --since today
```

```powershell
Get-Service
Get-Service -Name sshd
Start-Service sshd
Set-Service sshd -StartupType Automatic
```

Antes de habilitar un servicio se revisan su necesidad, puerto, cuenta de ejecución, configuración y exposición de red.

## 6. Software y actualizaciones

Los gestores de paquetes resuelven dependencias y registran instalaciones. En Debian/Ubuntu se usa APT; Windows dispone de Microsoft Store, instaladores y `winget`.

```bash
sudo apt update
apt list --upgradable
sudo apt install paquete
```

```powershell
winget search Git
winget install --id Git.Git --exact
winget upgrade --all
```

En producción se prueban actualizaciones, se dispone de copia y se documenta una reversión.

## 7. Registros y monitorización

La monitorización observa CPU, memoria, disco, red, procesos y disponibilidad de servicios. Un valor aislado tiene poco contexto; interesa la tendencia y su relación con la carga.

En Linux se consultan `journalctl`, `/var/log`, `free`, `vmstat`, `iostat`, `ss` y `df`. En Windows se usan Visor de eventos, Administrador de tareas, Monitor de recursos, Monitor de rendimiento y cmdlets de PowerShell.

Una investigación básica:

1. Definir el síntoma y periodo afectado.
2. Revisar eventos y cambios recientes.
3. Medir recursos y localizar cuellos de botella.
4. Formular una hipótesis.
5. Aplicar un cambio controlado.
6. Verificar y documentar.

## 8. Tareas programadas y scripts

Las tareas repetitivas deben automatizarse de manera idempotente cuando sea posible. Un script debe validar entradas, manejar errores, devolver códigos de salida y escribir registros.

`cron` y los temporizadores de `systemd` automatizan Linux; el Programador de tareas lo hace en Windows. La cuenta ejecutora solo debe tener los permisos imprescindibles.

## 9. Mantenimiento y optimización

- Revisar capacidad y salud del almacenamiento.
- Aplicar actualizaciones planificadas.
- Retirar cuentas, servicios y programas innecesarios.
- Verificar copias y restauraciones.
- Comprobar registros, alertas y sincronización horaria.
- Mantener inventario y documentación de cambios.

No deben emplearse limpiadores o ajustes sin comprender su efecto. Optimizar significa medir, identificar la limitación y comprobar la mejora.

## 10. Resumen

La administración combina control de acceso, operación diaria, observabilidad y documentación. El principio de privilegio mínimo y la trazabilidad reducen errores y facilitan el diagnóstico.

## Fuentes internas utilizadas

- `SI_Celia/Unit_3_Administracio_de_SO_Linux/UP3-Configuracio-i-Gestio-de-Sistemes-Operatius.pdf`.
- `SI_Celia/Unit_3_Administracio_de_SO_Linux/Scripts/manual_scripts_bash.pdf`.
- `Programacion_Didactica_SI_David_Moli.docx`.
