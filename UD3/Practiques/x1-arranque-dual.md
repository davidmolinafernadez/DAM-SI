# X1. Ampliación: Windows y Ubuntu en arranque dual virtual

<div class="lesson-banner" markdown>
<div class="lesson-number">X1</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Firmware, arranque y particiones](../b04-firmware-y-particiones.md) · [Recuperación y transferencia](../b11-recuperacion.md)

Duración adicional: 180 minutos. Se usa una VM nueva de 120 GiB compatible con Windows 11. Nunca se modifica el arranque del ordenador personal.

## 1. Instala Windows dejando un destino para Linux

Crea la VM desde **Nueva**, con los requisitos y configuración de P3. En la pantalla del instalador que permite elegir el destino, selecciona el espacio del VDI de 120 GiB y utiliza **Nuevo / Crear partición**, si esa revisión lo ofrece, para reservar unos 70 GiB para Windows y sus particiones auxiliares. Deja al menos 45 GiB sin asignar. Revisa los tamaños que realmente muestra el instalador antes de aceptar; la suma debe dejar espacio para ESP, MSR y recuperación.

Termina Windows y comprueba arranque y archivo testigo. Si se ha activado cifrado de dispositivo, confirma el procedimiento y la clave de recuperación de aula antes de continuar. Apaga y crea un clon completo o copia recuperable mediante el procedimiento de P8.

## 2. Instala Ubuntu en el espacio sin asignar

En **Configuración → Almacenamiento**, conecta la ISO Ubuntu a la unidad óptica. Arranca en el mismo modo UEFI. Sigue idioma, teclado y modalidad interactiva de P2. En configuración de disco selecciona **Instalación manual**; no uses **Borrar disco**.

En la tabla localiza el espacio libre reservado. Selecciónalo y usa **+ / Añadir** para crear la raíz Linux en ext4, con punto de montaje `/`. Identifica la ESP existente por su función y formato FAT32. Reutilízala como `/boot/efi` sin marcar formateo. No uses para Linux la partición NTFS de Windows.

## 3. Revisa el resumen y prueba los dos sistemas

Antes de instalar, escribe qué partición se formateará y cuáles se conservarán. Si el resumen incluye borrar o formatear Windows o ESP, cancela y corrige. Termina, retira ISO y prueba ambos sistemas.

Si no aparece un menú combinado, abre las entradas de arranque del firmware virtual: en muchas VM UEFI se accede con **Esc** al comienzo, pero depende de versión y tiempo de arranque. Sigue la ayuda de esa VM y localiza sus entradas de Windows y Ubuntu. La ausencia de un menú GRUB visible no prueba que Windows se haya borrado.

Entrega mapa final, testigo conservado en Windows y evidencia de arranque de cada sistema. Explica por qué solo uno se ejecuta cada vez, a diferencia de dos invitados separados.

## Entrega independiente de la práctica

Guarda `X1_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.

<div class="video-card" markdown>

## Vídeo explicativo · Particionar con GParted

V10: observa tabla y partición. Su ejemplo usa MBR; nuestra práctica usa GPT en otro disco.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/417dd5j5i92wjmop/fs" title="Particionar con GParted" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/417dd5j5i92wjmop) · [Ficha y preguntas de visionado](../videos.md)

</div>
