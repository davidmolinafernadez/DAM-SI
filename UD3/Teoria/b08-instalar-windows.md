# B8. Windows 11: instalación y aceptación

> **Del concepto al laboratorio:** [P3 · Instalar Windows 11](practicas/p3-windows.md) · [P9 · Proyecto integrador](practicas/p9-proyecto.md)

## 8.1. Preparar el invitado

La máquina de Windows tendrá su propio disco. La propuesta de laboratorio es 2 vCPU, entre 4 y 6 GiB de RAM según el anfitrión y un VDI dinámico de 80 GiB. Verifica los requisitos vigentes de la edición descargada y la compatibilidad del hipervisor. No se utilizarán modificaciones del registro para omitirlos.

Registra UEFI, TPM virtual y la configuración de Secure Boot aplicable. Si la edición no puede instalarse con el hardware disponible, se documenta la limitación y se utiliza un puesto compatible del aula. El aprendizaje incluye detectar que un encargo no es viable con unos recursos determinados.

## 8.2. Particiones y configuración inicial

En una instalación limpia sobre disco vacío, permite al instalador crear su distribución de particiones y después interprétala. No esperes que todas tengan letra. La configuración inicial de red y cuentas depende de edición, versión y políticas del centro: prepara la identidad de aula antes de empezar y no utilices credenciales personales en una imagen que se exportará.

La activación y la instalación son procesos relacionados, pero distintos. Un sistema que ha llegado al escritorio puede seguir pendiente de activación. El informe registra el estado sin fotografiar ni publicar claves.

## 8.3. Comprobaciones

En Windows abre Información del sistema, Administrador de dispositivos, Administración de discos y Windows Update. Comprueba versión mediante winver, firmware y arranque seguro en msinfo32 y TPM mediante tpm.msc cuando esté disponible. Distingue «compatible», «habilitado» y «no disponible» según lo que realmente indiquen las herramientas.

En PowerShell:

```powershell
Get-Disk
Get-Partition
Get-Volume
Get-NetIPConfiguration
```

No ejecutes comandos de eliminación ni inicialización para consultar el estado. Una comprobación de lectura permite describir el equipo sin alterar particiones. Registra dispositivos desconocidos y revisa controladores de integración si aparecen. Completa actualizaciones y reinicios antes de crear el estado base de la VM.

## Actividad A8 · Instalar no es aceptar

Windows arranca, pero hay un dispositivo desconocido y Windows Update solicita reiniciar. Redacta una incidencia con estado actual, riesgo, siguiente acción y criterio de cierre. Explica si entregarías el equipo como terminado. Continúa con P3.
