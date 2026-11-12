# Antes de empezar: materiales y preparación de UD3

Esta guía acompaña las siete prácticas. Léela antes de P1. No genera otra entrega. Conserva tus máquinas para las unidades posteriores.

Para preparar la entrega, utiliza la [plantilla del informe P1](p1-laboratorio.md#plantilla-del-informe-copia-y-completa), con un [ejemplo de redacción](p1-laboratorio.md#ejemplo-breve-de-redaccion-datos-ficticios) y la [lista de capturas de pantalla del proceso](p1-laboratorio.md#capturas-de-pantalla-del-proceso). Inserta las capturas en el informe y explica qué demuestra cada una.

## 1. Qué recibirás del docente

Antes de descargar, comprueba en el anuncio de Aules estos datos:

| Dato | Qué necesitas conocer |
| --- | --- |
| VirtualBox | Versión exacta instalada en el aula |
| Ubuntu | Versión y revisión de Ubuntu Desktop, arquitectura amd64, nombre exacto de la ISO y enlace oficial |
| Windows | Versión, idioma, arquitectura x64 y edición autorizada; ubicación de la ISO |
| Integridad | Referencia oficial SHA-256 correspondiente al archivo exacto |
| Ubicación | Carpeta del puesto donde guardar VM y exportaciones; si se conserva al cerrar sesión |
| Cuenta de Windows | Procedimiento de acceso autorizado para la edición del centro |
| Recursos | Puesto alternativo si tu equipo no puede realizar alguna práctica |

Si falta uno de estos datos, consúltalo antes del paso que dependa de él. No elijas otra edición ni utilices una cuenta personal por tu cuenta. La versión de la web de descarga puede cambiar durante el curso: utiliza la acordada en clase.

VirtualBox y la conectividad NAT inicial los proporciona el docente. Si trabajas en un equipo propio, utiliza el instalador de [VirtualBox](https://www.virtualbox.org/wiki/Downloads) correspondiente a tu sistema y la versión acordada. Instala con la configuración indicada y reinicia si lo solicita. No necesitas Extension Pack para estas prácticas. En el aula no cambies instalaciones ni firmware sin indicación.

## Descargas oficiales

| Material | Enlace y elección |
| --- | --- |
| VirtualBox | [Descargas oficiales](https://www.virtualbox.org/wiki/Downloads). Para un anfitrión Windows, elige **Windows hosts**; para Linux, **Linux distributions** y el paquete de tu distribución. Usa la versión acordada con el docente; en el aula ya estará instalado. |
| ISO de Ubuntu Desktop | [Descargar Ubuntu Desktop](https://ubuntu.com/download/desktop). Elige la versión acordada y arquitectura **amd64 / Intel o AMD de 64 bits** para los puestos x86-64. |
| Otras revisiones y huellas de Ubuntu | [Directorio oficial de imágenes](https://releases.ubuntu.com/). Entra en la carpeta de la versión y busca la ISO y su `SHA256SUMS`; la referencia debe corresponder al nombre exacto descargado. [Guía oficial de verificación](https://ubuntu.com/tutorials/how-to-verify-ubuntu). |
| ISO de Windows 11 (para la práctica de Windows) | [Descargar Windows 11](https://www.microsoft.com/es-es/software-download/windows11). Utiliza **Descargar imagen de disco (ISO) para dispositivos x64**, con idioma y edición autorizados, o la copia del centro. Consulta **Verificar la descarga** para su SHA-256 cuando se ofrezca. |

Elige el instalador de VirtualBox según el **anfitrión** y la ISO según el **invitado**: puedes descargar Ubuntu y Windows desde cualquiera de los dos anfitriones. No necesitas crear un USB para estas prácticas. La versión más reciente de una web puede diferir de la acordada en clase; utiliza la indicada por el docente.

## 2. Carpetas y espacio

En la ubicación autorizada crea `UD3_Apellidos_Nombre` y, dentro, `ISO`, `Maquinas`, `Exportaciones` y `Evidencias`. No guardes las VM en una carpeta temporal ni en una ubicación que se borre al cerrar sesión. Guarda las evidencias también en tu espacio autorizado fuera de las VM.

En VirtualBox, al crear cada VM, selecciona `Maquinas` como carpeta de destino. Utiliza los nombres de las fichas. No muevas después los VDI manualmente desde el Explorador: puedes romper la referencia al disco.

Los 50 GiB del disco Ubuntu y los 80 GiB del disco Windows son capacidades virtuales. Al ser dinámicos, los archivos crecen conforme se utilizan. No confundas capacidad máxima con espacio físico reservado o disponible. Para P6 necesitas guardar además el clon, el OVA y la importación. Antes de copiar, mide el tamaño real del origen y el espacio libre; si no cabe, solicita el equipo alternativo. No borres el original para dejar sitio a su única copia.

## 3. Descargar y verificar Ubuntu

1. Entra en [Ubuntu Desktop](https://ubuntu.com/download/desktop). Selecciona la versión acordada; si no aparece, utiliza las descargas alternativas oficiales. Para los puestos x86-64 del aula elige **amd64 / Intel o AMD de 64 bits**, no ARM64, Server ni WSL.
2. Descarga la ISO en `ISO`. Si el docente facilita una copia, cópiala a esa carpeta y anota igualmente su procedencia oficial. No necesitas grabarla en un USB para VirtualBox.
3. En Windows, activa **Explorador → Ver → Mostrar → Extensiones de nombre de archivo**. En Linux, comprueba el nombre completo en **Propiedades** del gestor de archivos o con `ls -lh`. Espera a que finalice la descarga; un archivo parcial no sirve.
4. En el directorio oficial de esa misma revisión localiza `SHA256SUMS`. Busca la línea cuyo nombre coincida exactamente con tu ISO. La [guía oficial de verificación](https://ubuntu.com/tutorials/how-to-verify-ubuntu) explica también la comprobación de autenticidad mediante firma.
5. **En Windows**, abre la carpeta `ISO`, escribe `powershell` en la barra de direcciones y pulsa Intro. Ejecuta lo siguiente sustituyendo el nombre de ejemplo por el nombre real:

```powershell
Get-ChildItem
Get-FileHash -Algorithm SHA256 -LiteralPath '.\nombre-exacto-de-la-imagen.iso'
```

**En Linux**, abre la carpeta `ISO` en el gestor de archivos y selecciona **Abrir en una terminal**, o usa `cd` con su ruta real entre comillas. Ejecuta lo siguiente con el nombre exacto de tu imagen:

```bash
pwd
ls -lh
sha256sum -- './nombre-exacto-de-la-imagen.iso'
```

La huella aparece antes del nombre del archivo. Consulta también la auditoría completa para Windows y Linux en la [primera parte de P1](p1-laboratorio.md#primera-parte-auditoria-e-iso).

Compara los 64 caracteres del resultado con la referencia oficial; las mayúsculas no cambian el valor. Guarda nombre, versión, URL de origen, referencia y resultado de la comparación. Un hash calculado por ti sin referencia no verifica la descarga. Si no coincide, revisa el nombre y la revisión y vuelve a copiar o descargar; no arranques esa imagen.

## 4. Obtener Windows 11

Utiliza preferentemente la ISO autorizada proporcionada por el centro. Si el docente pide descargarla, entra en [Descargar Windows 11](https://www.microsoft.com/software-download/windows11), busca **Descargar imagen de disco (ISO) para dispositivos x64**, selecciona las opciones acordadas, confirma el idioma y guarda el archivo en `ISO`. No ejecutes el Asistente de instalación sobre el ordenador anfitrión.

Comprueba el SHA-256 con el mismo procedimiento anterior y la referencia oficial correspondiente a ese idioma y revisión, cuando se ofrezca. Si no la encuentras, solicita la referencia al docente. No compares ISO de idiomas o revisiones diferentes.

La ISO no proporciona por sí sola una licencia. La edición y el acceso los determina el centro. No publiques claves, contraseñas ni datos de recuperación en capturas. Si el asistente exige una cuenta o una conexión que no coincide con el procedimiento del centro, detente en esa pantalla y consulta. No se utilizan trucos para omitir requisitos.

## 5. Comprobar el puesto y la red

Realiza la auditoría de P1 antes de asignar recursos. La configuración de referencia de P1 es Ubuntu con el disco indicado en la ficha; la memoria debe ajustarse a los requisitos de la versión elegida y a lo disponible en el puesto. No asignes toda la RAM o todos los procesadores al invitado. Si no caben dos VM, ejecútalas por turnos. Si una sola no cumple los requisitos, utiliza el puesto alternativo.

Con la VM apagada abre **Configuración → Red → Adaptador 1**: habilitado, conectado a **NAT** y con cable conectado. No necesitas reenvío de puertos para instalar y actualizar. Arranca el invitado, abre su navegador y visita una página oficial. Si falla, comprueba también Internet en el anfitrión y la fecha y hora del invitado. Registra el mensaje; no cambies a adaptador puente al azar. La configuración de redes se desarrolla en UD4.

## 6. Qué debes tener antes de cada práctica

| Práctica | Estado inicial | Comprobación de salida |
| --- | --- | --- |
| P1 | Puesto auditado, VirtualBox disponible e ISO Ubuntu verificada | VM creada; distingues disco vacío y arranque desde ISO |
| P2 | VM de P1, ISO conectada y destino identificado | Ubuntu arranca sin ISO y conserva un archivo tras reiniciar |
| P3 | ISO Windows autorizada, método de cuenta y recursos suficientes | Windows arranca sin ISO; registras requisitos, edición y estado real |
| P4 | Sistemas instalados y conexión NAT comprobada | Registras propuesta, resultado y reinicio si procede; un error no cuenta como éxito |
| P5 | VM funcional y archivo testigo; evidencias fuera del invitado | Restauras el estado previsto y explicas qué cambios desaparecen |
| P6 | Ubuntu apagado y espacio para copias e importación | Clon e importación arrancan y conservan el archivo testigo |
| P7 | Clon Ubuntu con Docker Engine operativo e imagen disponible | Web personalizada recuperada en otro contenedor con el mismo volumen |

Sigue después los pasos completos de cada ficha. Antes de restaurar una instantánea, saca fuera del invitado los documentos que necesites conservar. Al terminar una sesión apaga desde el sistema invitado y espera al estado **Apagada** antes de cerrar VirtualBox o copiar material. La instantánea depende de la VM y sus discos; no sustituye una copia independiente.

## 7. Contenedores: qué haces tú

En [P7 · Contenedores](p7-contenedores.md) realizarás una práctica guiada de dos horas y entregarás `P7_Apellidos_Nombre.pdf` con capturas explicadas. Trabajarás en un clon Ubuntu con Docker Engine ya instalado y probado por el docente. El motor se prepara mediante el [procedimiento oficial de Docker para Ubuntu](https://docs.docker.com/engine/install/ubuntu/). No necesitas instalar Docker en el ordenador físico ni Docker Desktop dentro de la VM.

El docente debe comprobar acceso al registro o proporcionar la imagen `nginx:stable-alpine` ya descargada, y verificar que no estén ocupados los nombres y el puerto de la práctica. Guardarás las evidencias fuera del clon. P7 se realiza después de la teoría 3.8 y forma parte de las nueve entregas de UD3: dos actividades y siete prácticas.

## 8. Evidencias y problemas

Guarda las capturas en `Evidencias` con el código de práctica y una descripción. Deben mostrar el dato necesario y llevar una explicación de qué demuestra. Nunca subas ISO, VDI u OVA a la tarea de Aules: entrega el informe solicitado. La auditoría y la creación de la VM se recogen en un único `P1_Apellidos_Nombre.pdf`.

Si algo falla, anota práctica, paso, mensaje exacto, versión y qué has comprobado. Si aparece medio no arrancable, comprueba la ISO conectada a esa VM. Si vuelve al instalador después de instalar, revisa si sigue conectada la ISO. Si no aparece el archivo testigo, comprueba qué VM y qué estado has arrancado. No reinstales ni borres discos antes de identificar la causa.
