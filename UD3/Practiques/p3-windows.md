# P3. Windows 11 con instalación y licencia diferenciadas

<div class="lesson-banner" markdown>
<div class="lesson-number">P3</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Instalar y comprobar Windows](../b08-instalar-windows.md)

Duración orientativa: 180 minutos. Necesitas una ISO oficial, una edición y derecho de uso autorizados y el método de cuenta preparado por el docente. No se usan cuentas personales en imágenes compartidas. Si el puesto no cumple los requisitos, se utiliza un equipo compatible; no se eluden con modificaciones del registro.

## 1. Prepara el hardware de la VM

En VirtualBox pulsa **Nueva**. Escribe `UD3-Windows-codigo`, selecciona la ISO y la plantilla Windows 11 de 64 bits. Marca **Omitir instalación desatendida** si aparece. Asigna **2 vCPU**, **4-6 GiB de RAM** según P0 y crea un **VDI dinámico de 80 GiB**. Antes de encender, comprueba que Ubuntu no esté consumiendo recursos que el presupuesto necesite.

Selecciona la VM → **Configuración → Sistema**. Revisa **EFI/UEFI**, **TPM virtual 2.0** y opciones de **Secure Boot/Arranque seguro** disponibles para tu versión. No basta elegir el nombre «Windows 11» si la configuración real no cumple. Si no encuentras esas opciones, anota versión y configuración y consulta la compatibilidad con el docente.

## 2. Abre el instalador y elige el destino

1. Pulsa **Iniciar**. Si aparece «Press any key to boot from CD or DVD», pulsa una tecla dentro de la ventana para arrancar desde la ISO.
2. Selecciona idioma y teclado. Continúa mediante **Siguiente** y la opción de instalar que muestre esa revisión.
3. Identifica edición. Introduce la clave por el método del centro o aplázala si el instalador y el procedimiento acordado lo permiten. «No tengo clave» no concede por sí mismo una licencia de evaluación.
4. Revisa y acepta las condiciones aplicables bajo las indicaciones del centro. Elige la modalidad de instalación nueva o personalizada. Algunas revisiones presentan pantallas distintas a las del material antiguo: identifica la función, no solo el número de pantalla.
5. En la selección del destino comprueba que la capacidad corresponde al disco virtual de 80 GiB vacío. No debe aparecer un disco personal. Selecciona su **espacio sin asignar** y deja al instalador crear las particiones que necesite.
6. Antes de confirmar, anota destino y efecto sobre datos. Espera a la copia y a los reinicios. Cuando el disco ya esté instalado, no vuelvas a pulsar una tecla para iniciar otra instalación desde el CD.

## 3. Completa el primer inicio

Selecciona región, teclado y red. En la cuenta utiliza el procedimiento preparado para la edición del centro. Si aparece una exigencia de organización, Internet o cuenta distinta de la prevista, registra la pantalla y consúltalo: no introduzcas credenciales personales ni utilices instrucciones antiguas para ocultar el requisito.

Tras llegar al escritorio, apaga desde **Inicio → botón de encendido → Apagar**. En VirtualBox retira la ISO desde **Configuración → Almacenamiento** y arranca de nuevo. Crea un archivo de prueba en **Explorador → Documentos**, reinicia desde **Inicio** y comprueba que permanece.

## 4. Abre las herramientas de comprobación

Pulsa **Windows + R** dentro de Windows invitado. Ejecuta por separado:

- `winver`: identifica edición y versión.
- `msinfo32`: en **Resumen del sistema**, consulta modo de firmware y estado observado de arranque seguro.
- `tpm.msc`: identifica si el TPM se muestra disponible y su versión.
- `diskmgmt.msc`: abre **Administración de discos**; observa la zona inferior para interpretar particiones pequeñas, sistema y recuperación.
- `devmgmt.msc`: abre **Administrador de dispositivos** y busca iconos de advertencia.

Estas consultas no requieren inicializar ni eliminar discos. Si Administración de discos ofrece inicializar algún dispositivo inesperado, cancela y consulta cuál es antes de escribir.

## 5. Actualiza y cierra la instalación

Abre **Inicio → Configuración → Windows Update → Buscar actualizaciones**. Anota estado, instala lo acordado y utiliza **Reiniciar ahora** cuando lo solicite. Vuelve a la misma página al iniciar para comprobar el estado posterior. En **Configuración → Sistema → Activación**, registra el estado sin mostrar claves.

Si se requieren Guest Additions, en el menú de la VM abre **Dispositivos → Insertar imagen de CD de Guest Additions**. En el invitado abre **Explorador → Este equipo → unidad de CD** y utiliza el instalador correspondiente bajo el procedimiento del docente. Reinicia y comprueba si la resolución se adapta y si quedan dispositivos con incidencia.

Aceptación: arranque independiente, archivo persistente, requisitos acreditados, particiones explicadas y actualizaciones comprobadas. Una activación pendiente se declara y se resuelve por el centro; no se presenta como evaluación oficial. Entrega una tabla de herramienta, dato real y conclusión. Analiza aparte una ficha ficticia con 2 GiB de RAM, sin TPM virtual y firmware heredado.

## Entrega independiente de la práctica

Guarda `P3_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.

<div class="video-card" markdown>

## Vídeo explicativo · Preparación e instalación de Windows 11

V9: utiliza el fragmento inicial 0:00-5:15. En P3 usamos NAT y la edición/cuenta autorizadas; no copiamos puente ni credenciales del ejemplo.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/uqaj115jamo3y6xb/fs" title="Preparación e instalación de Windows 11" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/uqaj115jamo3y6xb) · [Ficha y preguntas de visionado](../videos.md)

</div>
