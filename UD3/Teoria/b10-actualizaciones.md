# B10. Actualizar, instalar aplicaciones y validar

> **Del concepto al laboratorio:** [P6 · Actualizar y verificar](practicas/p6-actualizaciones.md) · [P9 · Proyecto integrador](practicas/p9-proyecto.md)

## 10.1. Repositorios y dependencias

Un repositorio ofrece paquetes y metadatos. El gestor consulta esa información y resuelve dependencias. Una aplicación puede necesitar bibliotecas y servicios adicionales: instalar un único archivo no siempre basta. Añadir un repositorio amplía las fuentes de software en las que confías; no es una solución automática a cualquier error.

No todo archivo tar.gz es un instalador ni todo paquete utiliza versionado semántico. Un número como 2.4.1 puede seguir una convención del proyecto; hay que consultar su política. Las actualizaciones de seguridad pueden mantener gran parte del número de versión y aun así corregir vulnerabilidades.

## 10.2. APT con comprensión

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

## 10.3. Windows Update y reinicios

En Windows registra estado inicial, actualizaciones propuestas y estado posterior al reinicio. Si una actualización requiere reiniciar, el trabajo no ha terminado hasta comprobar que el sistema vuelve a arrancar y funciona. En un aula, centraliza descargas o programa tandas para no saturar la red.

## 10.4. Criterios de aceptación

Una aceptación profesional contiene pruebas y resultados. «Funciona» no basta. Ejemplo: «Tras reiniciar sin ISO, inicio sesión como alumno; index.html permanece; la herramienta tree devuelve versión; se accede al repositorio; no quedan reinicios pendientes observados; el sistema muestra la fecha correcta».

Compara con una línea base: antes/después, versiones y cambios. Una captura debe tener pie que explique lo que demuestra. No se valorará acumular imágenes sin interpretación. Continúa con P6.
