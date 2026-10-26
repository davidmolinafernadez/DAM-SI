# X2. Ampliación: una web en contenedor dentro de Ubuntu

**Teoría relacionada:** [Contenedores para DAM](../b12-contenedores.md)

Duración adicional: 120 minutos, con motor Docker preparado por el docente. Teoría: B12. Vídeo V7. Producto: contenedor recreado con volumen persistente.

## Preparación docente necesaria

En una VM clonada para esta ampliación se instala Docker Engine con un único procedimiento aprobado. Se registra origen y versión del paquete. Si se utiliza la distribución oficial de Docker, seguir F11 y no mezclarla con docker.io. Debe estar activo el servicio y funcionar sudo docker run --rm hello-world. Este paso requiere conexión y descargas; se prepara con antelación. No se instala Docker Desktop dentro de la VM para este ejercicio.

## Experimento del alumno

1. Registra uname -r dentro de Ubuntu y predice si el contenedor tendrá otro kernel. Comprueba sudo docker version y sudo docker info.
2. Crea el volumen con sudo docker volume create ud3_webdatos.
3. Ejecuta la web:

    ```bash
    sudo docker run -d --name ud3-web \
      -p 127.0.0.1:8081:80 \
      -v ud3_webdatos:/usr/share/nginx/html \
      nginx:stable-alpine
    ```

4. En el navegador de Ubuntu abre <http://127.0.0.1:8081>. La primera ejecución descarga la imagen si no está presente. Guarda la salida de sudo docker image inspect nginx:stable-alpine --format '{{json .RepoDigests}}' para registrar el contenido utilizado; una etiqueta por sí sola puede cambiar.
5. Modifica la página del volumen:

    ```bash
    sudo docker exec ud3-web sh -c \
      'printf "<h1>Datos persistentes UD3</h1>\n" > /usr/share/nginx/html/index.html'
    ```

6. Recarga el navegador y registra el resultado. Consulta sudo docker exec ud3-web uname -r y compáralo con el kernel de Ubuntu. No confundas las herramientas del contenedor con un nuevo kernel arrancado.
7. Detén y elimina únicamente ese contenedor:

    ```bash
    sudo docker stop ud3-web
    sudo docker rm ud3-web
    ```

8. Ejecuta otra vez el comando del paso 3 con el mismo volumen. Comprueba que aparece tu página modificada. Explica por qué eliminar el contenedor no ha eliminado el volumen.
9. Consulta sudo docker ps -a y sudo docker volume ls. Limpia solamente los recursos del ejercicio cuando el docente haya evaluado; no ejecutes limpiezas globales.

Aceptación: respuesta HTTP dentro de Ubuntu, digest registrado, kernel comparado y datos presentes tras recreación. Preguntas: ¿por qué 127.0.0.1:8081 en el navegador del anfitrión físico no apunta al mismo sitio?, ¿un volumen persistente es automáticamente una copia independiente?, ¿qué necesitarías para recrear la práctica sin depender de una etiqueta mutable?
