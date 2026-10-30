# 4.3.2 · Windows 11: instalación y aceptación

<div class="lesson-banner" markdown>
<div class="lesson-number">4.3.2</div>
<div markdown>
**Instalación de Ubuntu y Windows**

Instalar y comprobar Windows: explicación, ejemplos y comprobaciones.
</div>
</div>

## Preparar el invitado

La máquina de Windows tendrá su propio disco. La propuesta de laboratorio es 2 vCPU, entre 4 y 6 GiB de RAM según el anfitrión y un VDI dinámico de 80 GiB. Verifica los requisitos vigentes de la edición descargada y la compatibilidad del hipervisor. No se utilizarán modificaciones del registro para omitirlos.

Registra UEFI, TPM virtual y la configuración de Secure Boot aplicable. Si la edición no puede instalarse con el hardware disponible, se documenta la limitación y se utiliza un puesto compatible del aula. El aprendizaje incluye detectar que un encargo no es viable con unos recursos determinados.

## Particiones y configuración inicial

En una instalación limpia sobre disco vacío, permite al instalador crear su distribución de particiones y después interprétala. No esperes que todas tengan letra. La configuración inicial de red y cuentas depende de edición, versión y políticas del centro: prepara la identidad de aula antes de empezar y no utilices credenciales personales en una imagen que se exportará.

La activación y la instalación son procesos relacionados, pero distintos. Un sistema que ha llegado al escritorio puede seguir pendiente de activación. El informe registra el estado sin fotografiar ni publicar claves.

## Comprobaciones

En Windows abre Información del sistema, Administrador de dispositivos, Administración de discos y Windows Update. Comprueba versión mediante winver, firmware y arranque seguro en msinfo32 y TPM mediante tpm.msc cuando esté disponible. Distingue «compatible», «habilitado» y «no disponible» según lo que realmente indiquen las herramientas.

En PowerShell:

```powershell
Get-Disk
Get-Partition
Get-Volume
Get-NetIPConfiguration
```

No ejecutes comandos de eliminación ni inicialización para consultar el estado. Una comprobación de lectura permite describir el equipo sin alterar particiones. Registra dispositivos desconocidos y revisa controladores de integración si aparecen. Completa actualizaciones y reinicios antes de crear el estado base de la VM.

## Instalar aplicaciones en Windows: MSI y EXE

MSI es un formato de paquete gestionado mediante Windows Installer. Un EXE es un ejecutable que puede contener un instalador propio, un lanzador u otro programa. La extensión no certifica la procedencia ni garantiza seguridad. Antes de ejecutar, se revisan origen, editor, arquitectura y propósito.

Una instalación puede necesitar permisos, cerrar programas o reiniciar. Leer el asistente implica identificar carpeta, componentes y opciones adicionales, no aceptar todo por velocidad. Después se comprueba la aplicación y se registra cómo desinstalarla desde **Configuración → Aplicaciones → Aplicaciones instaladas** o mediante el procedimiento indicado.

No se presupone que un MSI vaya a crear siempre un punto de restauración ni que todos los EXE permitan instalaciones simultáneas. El comportamiento depende de protección del sistema, paquete y políticas. La prueba de aceptación se basa en el resultado real del puesto.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 4.8 · Aceptar una instalación de Windows](actividades/A08-aceptar-una-instalacion-de-windows.md)
- [Actividad 4.19 · Leer un instalador MSI o EXE](actividades/A19-leer-un-instalador-msi-o-exe.md)

## Prácticas relacionadas

- [P3 · Instalar Windows 11](practicas/p3-windows.md)
- [P11 · Restaurar sistema Windows](practicas/p11-restauracion-windows.md)

<div class="video-card" markdown>

## Vídeo explicativo · Preparación e instalación de Windows 11

V9: utiliza el fragmento inicial 0:00-5:15. En P3 usamos NAT y la edición/cuenta autorizadas; no copiamos puente ni credenciales del ejemplo.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/uqaj115jamo3y6xb/fs" title="Preparación e instalación de Windows 11" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/uqaj115jamo3y6xb) · [Ficha y preguntas de visionado](videos.md)

</div>
