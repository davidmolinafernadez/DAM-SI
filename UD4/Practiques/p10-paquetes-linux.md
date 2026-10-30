# P10. Aplicaciones Linux: APT, paquete DEB y Snap

<div class="lesson-banner" markdown>
<div class="lesson-number">P10</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Actualizaciones y aceptación](../b10-actualizaciones.md)

Duración orientativa: 120 minutos. Esta práctica desarrolla los apartados de paquetes del material de referencia. Utiliza Ubuntu instalado, repositorios del centro y una instantánea anterior. No se añaden PPA o claves de terceros para practicar su escritura.

## 1. Consulta los orígenes sin cambiarlos

Abre una terminal del invitado con **Ctrl + Alt + T**. Ejecuta `ls /etc/apt/sources.list.d`. Busca archivos `.sources` y `.list`. Si existe `ubuntu.sources`, consúltalo con `cat /etc/apt/sources.list.d/ubuntu.sources`; si no existe, el docente identificará el archivo utilizado por esa imagen. No crees uno vacío para que coincida con el ejemplo.

Anota una URI, una suite y un componente realmente presentes. Explica `Types`, `URIs`, `Suites`, `Components` y `Signed-By` cuando aparezcan. Leer un archivo de configuración no equivale a habilitar otro origen.

## 2. Descarga un DEB desde el repositorio aprobado

Ejecuta `sudo apt update` y comprueba que no quedan errores sin resolver. Crea una carpeta específica:

```bash
mkdir -p ~/ud4-paquetes
cd ~/ud4-paquetes
apt show hello
apt download hello
ls -lh
```

El paquete `hello` es un programa pequeño de demostración. Si la imagen del aula no lo ofrece, el docente indicará un equivalente. `apt download` descarga el archivo, pero no lo instala. Copia su nombre real, que incluye versión y arquitectura. Si hay varias revisiones en la carpeta, identifica una; no instales un comodín que seleccione archivos diferentes por accidente.

## 4. Inspecciona e instala el archivo local

Consulta los metadatos con `dpkg-deb --info ./NOMBRE_REAL.deb`. Sustituye el marcador por el nombre exacto. Después ejecuta `sudo apt install ./NOMBRE_REAL.deb`. El prefijo `./` identifica un archivo local; no es el nombre de un paquete que se buscará solamente por su identificador.

Lee la propuesta y acepta bajo el procedimiento de aula. Ejecuta `hello` y consulta `dpkg-query -W hello`. En **Mostrar aplicaciones** puede no aparecer un icono: este programa se usa desde la terminal. Que no haya lanzador gráfico no demuestra que la instalación haya fallado.

## 4. Distingue el nombre del paquete y el nombre del archivo

Consulta `dpkg -l hello` y localiza estado, versión y arquitectura. Ejecuta `sudo apt remove hello` y lee qué va a retirar. Comprueba si `hello` sigue disponible. Explica por qué los comandos de eliminación reciben normalmente `hello`, no el nombre completo `hello_version_arquitectura.deb` del archivo descargado.

`purge` trata también la configuración de paquete, pero no garantiza borrar documentos personales. No ejecutes limpiezas generales. El archivo descargado puede seguir en `~/ud4-paquetes` aunque el programa ya no esté instalado: son objetos distintos.

## 5. Observa Snap sin duplicar instalaciones

Ejecuta `snap --version` y `snap list` si Snap está disponible en la imagen. Selecciona un programa que ya esté instalado y consulta `snap info NOMBRE_REAL_DEL_SNAP`, sustituyendo el marcador. Anota canal, editor y versión que puedas identificar. No instales otra copia de la misma aplicación por rutina y no elimines un snap del sistema para demostrar el comando.

Entrega una tabla: origen, herramienta, objeto que gestiona, instalación comprobada y desinstalación. Compara APT/DEB con Snap. Conserva la evidencia de que descargar el DEB y ejecutar la aplicación son dos pasos diferentes. Si Snap no está disponible, documenta esa situación y resuelve la comparación con la información docente.

## Entrega independiente de la práctica

Guarda `P10_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.
