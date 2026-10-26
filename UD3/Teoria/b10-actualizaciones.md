# 3.6 · Actualizar, instalar aplicaciones y validar

<div class="lesson-banner" markdown>
<div class="lesson-number">3.6</div>
<div markdown>
**Aplicaciones y actualizaciones**

Actualizaciones y aceptación: explicación, ejemplos y comprobaciones.
</div>
</div>

## Repositorios y dependencias

Un repositorio ofrece paquetes y metadatos. El gestor consulta esa información y resuelve dependencias. Una aplicación puede necesitar bibliotecas y servicios adicionales: instalar un único archivo no siempre basta. Añadir un repositorio amplía las fuentes de software en las que confías; no es una solución automática a cualquier error.

No todo archivo tar.gz es un instalador ni todo paquete utiliza versionado semántico. Un número como 2.4.1 puede seguir una convención del proyecto; hay que consultar su política. Las actualizaciones de seguridad pueden mantener gran parte del número de versión y aun así corregir vulnerabilidades.

## APT con comprensión

```bash
sudo apt update
apt list --upgradable
sudo apt upgrade
apt show tree
sudo apt install tree
tree --version
```

update refresca información; no actualiza por sí solo los programas instalados. upgrade instala actualizaciones y puede añadir dependencias, pero no elimina paquetes existentes. full-upgrade puede eliminar paquetes para resolver cambios. No se utilizará sin revisar su propuesta. remove y purge también se distinguen por el tratamiento de configuración de paquetes, y no garantizan borrar datos del directorio personal. Referencia F8.

Lee lo que el gestor propone antes de aceptar. Si hay un bloqueo porque otra actualización sigue trabajando, espera y consulta el proceso. Borrar archivos de bloqueo a ciegas puede dejar una operación inconsistente. Si falla la descarga, comprueba red, DNS, reloj, espacio y repositorios antes de intentar reinstalar todo.

## Windows Update y reinicios

En Windows registra estado inicial, actualizaciones propuestas y estado posterior al reinicio. Si una actualización requiere reiniciar, el trabajo no ha terminado hasta comprobar que el sistema vuelve a arrancar y funciona. En un aula, centraliza descargas o programa tandas para no saturar la red.

## Criterios de aceptación

Una aceptación profesional contiene pruebas y resultados. «Funciona» no basta. Ejemplo: «Tras reiniciar sin ISO, inicio sesión como alumno; index.html permanece; la herramienta tree devuelve versión; se accede al repositorio; no quedan reinicios pendientes observados; el sistema muestra la fecha correcta».

Compara con una línea base: antes/después, versiones y cambios. Una captura debe tener pie que explique lo que demuestra. No se valorará acumular imágenes sin interpretación. Continúa con P6.

## Formatos de paquete: qué identifica cada uno

Un DEB es un paquete usado en sistemas como Debian y Ubuntu; RPM pertenece a otra familia de gestores. No se instala un RPM con APT por cambiarle la extensión. Un archivo tar.gz es un archivo comprimido: puede contener código, binarios, datos o documentación; hay que inspeccionar qué ofrece el proyecto. Un ebuild es una descripción de construcción propia de Gentoo, no un paquete intercambiable con DEB.

En `programa_version_arquitectura.deb`, nombre del archivo y nombre del paquete están relacionados, pero no son la misma cadena. Se instala un archivo local por su ruta; se consulta o elimina el paquete por su identificador. Así se evita copiar el error de pasar siempre el nombre completo del archivo a una orden de desinstalación.

## APT, apt-get y dpkg

APT proporciona una interfaz apropiada para trabajo interactivo; apt-get ofrece opciones estables utilizadas en automatización. dpkg gestiona paquetes DEB a un nivel inferior y no descarga por sí solo toda la resolución de dependencias desde repositorios. Para un archivo local se puede utilizar `sudo apt install ./archivo.deb`, una vez verificada su procedencia.

`dpkg-deb --info archivo.deb` inspecciona el archivo. `dpkg-query -W nombre-paquete` consulta un paquete instalado. `remove` y `purge` expresan distintas decisiones sobre configuración de paquete, sin sustituir una política de borrado de datos personales. Las operaciones que propongan retirar dependencias se leen antes de aceptar.

## Repositorios tradicionales y formato deb822

APT puede leer definiciones `.list` y `.sources` dentro de `/etc/apt/sources.list.d/`. Las primeras suelen usar líneas que comienzan por `deb`; las segundas organizan campos como `Types`, `URIs`, `Suites`, `Components` y `Signed-By`. La ruta y formato reales se consultan en el equipo: no se presupone que toda instalación use el mismo archivo histórico.

La URI identifica el origen; la suite lo relaciona con una versión o canal; los componentes organizan conjuntos de paquetes. `Signed-By` limita qué clave se acepta para ese origen cuando está configurado. Un archivo de clave no se transforma en otro formato simplemente renombrándolo. Añadir repositorios externos requiere seguir las instrucciones actuales del editor para esa distribución y revisar su confianza.

En P10 se inspeccionan los orígenes ya aprobados. No se añade WineHQ, un PPA o un origen de Chrome solo para copiar un ejemplo antiguo. Se comprueba antes necesidad, versión admitida, formato de clave y procedimiento de retirada. Cambiar la firma o ignorar errores para que la descarga continúe oculta el problema.

## Snap y gestión gráfica de aplicaciones

Snap utiliza snapd y un modelo de distribución con canales y confinamiento según el paquete. Puede incluir dependencias y utilizar bases o componentes compartidos; no significa que cada programa lleve absolutamente todo ni que cualquier permiso esté garantizado. `snap list` consulta instalaciones; `snap info` ayuda a revisar un programa. Las aplicaciones de una tienda gráfica pueden proceder de formatos distintos: conviene identificar el origen mostrado.

Una retirada de Snap puede conservar una instantánea de datos según el comportamiento configurado. Por eso «quitar un programa» no equivale a certificar que nunca queda configuración ni datos. La copia y la política de conservación se estudian por separado.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 3.16 · Leer una actualización antes de aceptarla](actividades/A16-leer-una-actualizacion-antes-de-aceptarla.md)
- [Actividad 3.17 · Identificar paquetes y repositorios](actividades/A17-identificar-paquetes-y-repositorios.md)

## Prácticas relacionadas

- [P6 · Actualizar y verificar](practicas/p6-actualizaciones.md)
- [P10 · Aplicaciones Linux](practicas/p10-paquetes-linux.md)

## Lectura técnica para las herramientas

[Orígenes APT y formato deb822](https://manpages.ubuntu.com/manpages/noble/man5/sources.list.5.html) · [Manual de APT](https://manpages.ubuntu.com/manpages/noble/man8/apt.8.html) · [Documentación de Snap](https://snapcraft.io/docs)
