# B3. Medios de instalación e integridad

> **Del concepto al laboratorio:** [P0 · Auditoría e ISO](practicas/p0-auditoria.md) · [P9 · Proyecto integrador](practicas/p9-proyecto.md)

## 3.1. ISO, disco virtual e imagen de despliegue

Una ISO representa el contenido de un medio óptico y suele incluir el instalador arrancable. Se conecta a la unidad óptica virtual. Un VDI almacena los sectores de un disco virtual donde se instalará el sistema. Un OVA es un paquete de intercambio que agrupa una descripción de máquina y sus discos. Cambiar la extensión de una ISO a VDI no transforma un instalador en un disco instalado.

Un USB arrancable requiere escribir una estructura de arranque adecuada. Copiar una ISO como archivo a un pendrive ordinario no garantiza que arranque. En el laboratorio principal no hace falta preparar un USB: la ISO se conecta directamente a la VM.

## 3.2. Elegir una descarga

Selecciona producto, edición, versión, arquitectura e idioma. Guarda la URL oficial, el nombre completo, la fecha de descarga y el tamaño. Conserva el comprobante de licencia o la autorización del centro cuando corresponda. Las ISO de Windows y los derechos de uso son asuntos distintos: disponer del instalador no concede una licencia.

No se usarán ISO modificadas para saltar requisitos. En Windows se utilizará el medio y la edición autorizados por el centro, o una evaluación oficial si sus condiciones cubren el laboratorio. La opción «No tengo clave» no convierte automáticamente Windows Pro en una edición de evaluación.

## 3.3. Qué demuestra SHA-256

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

## 3.4. Integridad y autenticidad

Si alguien sustituyera tanto una imagen como un fichero de hashes, podrían coincidir entre sí. Una firma digital permite comprobar quién firmó el fichero de hashes, siempre que se verifique también la identidad de la clave. Ubuntu publica SHA256SUMS y una firma asociada. La ampliación de P0 propone seguir el procedimiento oficial de verificación de firma, sin importar claves de procedencia desconocida. Referencia F1.

## Actividad A3 · Una coincidencia insuficiente

Dos estudiantes descargan una ISO y el hash desde un foro; coinciden. Otro descarga la ISO desde un espejo y verifica la firma oficial del listado de hashes con una clave autenticada. Explica qué ha demostrado cada uno y qué confianza falta en el primer caso. Continúa con P0.
