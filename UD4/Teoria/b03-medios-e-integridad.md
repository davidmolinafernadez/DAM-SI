# 4.1.2 · Medios de instalación e integridad

<div class="lesson-banner" markdown>
<div class="lesson-number">4.1.2</div>
<div markdown>
**Planificación, medios y arranque**

Medios e integridad: explicación, ejemplos y comprobaciones.
</div>
</div>

## ISO, disco virtual e imagen de despliegue

Una ISO representa el contenido de un medio óptico y suele incluir el instalador arrancable. Se conecta a la unidad óptica virtual. Un VDI almacena los sectores de un disco virtual donde se instalará el sistema. Un OVA es un paquete de intercambio que agrupa una descripción de máquina y sus discos. Cambiar la extensión de una ISO a VDI no transforma un instalador en un disco instalado.

Un USB arrancable requiere escribir una estructura de arranque adecuada. Copiar una ISO como archivo a un pendrive ordinario no garantiza que arranque. En el laboratorio principal no hace falta preparar un USB: la ISO se conecta directamente a la VM.

## Elegir una descarga

Selecciona producto, edición, versión, arquitectura e idioma. Guarda la URL oficial, el nombre completo, la fecha de descarga y el tamaño. Conserva el comprobante de licencia o la autorización del centro cuando corresponda. Las ISO de Windows y los derechos de uso son asuntos distintos: disponer del instalador no concede una licencia.

No se usarán ISO modificadas para saltar requisitos. En Windows se utilizará el medio y la edición autorizados por el centro, o una evaluación oficial si sus condiciones cubren el laboratorio. La opción «No tengo clave» no convierte automáticamente Windows Pro en una edición de evaluación.

## Qué demuestra SHA-256

Un hash es una huella calculada a partir de los bytes del archivo. Si cambia el archivo, la huella normalmente cambia. Para comprobar una descarga, calcula SHA-256 y compara los 64 caracteres hexadecimales con los publicados para ese archivo exacto. Una coincidencia permite comprobar integridad frente a esa referencia; la confianza depende también de la procedencia de la referencia.

En PowerShell, desde la carpeta donde está la ISO, sustituye el nombre por el archivo real:

```powershell
Get-FileHash -LiteralPath '.\ubuntu-24.04.x-desktop-amd64.iso' -Algorithm SHA256
```

En Linux:

```bash
sha256sum ubuntu-24.04.x-desktop-amd64.iso
```

No copies literalmente la «x»: representa la revisión descargada. El hash correcto cambia con cada imagen. Comparar solamente el principio o el final no constituye una verificación completa. Si no coincide, no instales: comprueba nombre, revisión y referencia; después vuelve a descargar si procede.

## Integridad y autenticidad

Si alguien sustituyera tanto una imagen como un fichero de hashes, podrían coincidir entre sí. Una firma digital permite comprobar quién firmó el fichero de hashes, siempre que se verifique también la identidad de la clave. Ubuntu publica SHA256SUMS y una firma asociada. La ampliación de P0 propone seguir el procedimiento oficial de verificación de firma, sin importar claves de procedencia desconocida. Referencia F1.

## Una descarga se identifica por algo más que su nombre comercial

«Ubuntu 24.04» identifica una familia de versión, pero pueden existir revisiones, arquitecturas y ediciones distintas. La referencia que acompaña a una ISO se debe contrastar con el nombre exacto. El tamaño orienta sobre una descarga incompleta, pero no sustituye una huella: dos archivos del mismo tamaño pueden tener contenido diferente.

Una firma comprueba la relación entre un documento y una clave; la identidad de esa clave también necesita una fuente fiable. No basta con que el programa muestre «firma correcta» si se importó una clave que nadie ha autenticado. En el aula se separa la práctica básica de integridad de la ampliación de autenticidad para que el alumnado pueda decir con precisión qué ha demostrado.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 4.3 · Integridad y autenticidad de una ISO](actividades/A03-integridad-y-autenticidad-de-una-iso.md)

## Prácticas relacionadas

- [P0 · Auditoría e ISO](practicas/p0-auditoria.md)

<div class="video-card" markdown>

## Vídeo explicativo · Instalación Ubuntu 24.04

V3: observa la selección de la imagen. El vídeo no sustituye la verificación SHA-256 de P0.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/4dpxwfhdfpr4p799/fs" title="Instalación Ubuntu 24.04" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/4dpxwfhdfpr4p799) · [Ficha y preguntas de visionado](videos.md)

</div>
