# X2. Ampliación: una web en contenedor dentro de Ubuntu

<div class="lesson-banner" markdown>
<div class="lesson-number">X2</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Contenedores para DAM](../b12-contenedores.md)

Duración adicional: 120 minutos, con Docker Engine preparado y probado por el docente. Se trabaja en un clon Ubuntu. No se instala Docker Desktop dentro de la VM para este ejercicio ni se mezclan paquetes de diferentes procedimientos.

## 1. Abre la terminal del sistema que ejecuta el motor

Arranca Ubuntu y pulsa **Ctrl + Alt + T**. Comprueba `uname -r`, `sudo docker version` y `sudo docker info`. Si no responde el motor, registra el error y resuelve el servicio con el docente. No continúes suponiendo que cualquier error se arregla añadiendo usuarios al grupo docker.

## 2. Crea el volumen y el servidor

Ejecuta una orden cada vez. Las barras invertidas permiten continuar la misma orden en la línea siguiente; no añadas texto después de ellas.

    ```bash
    sudo docker volume create ud3_webdatos
    sudo docker run -d --name ud3-web \
      -p 127.0.0.1:8081:80 \
      -v ud3_webdatos:/usr/share/nginx/html \
      nginx:stable-alpine
    sudo docker ps
    ```

`--name` identifica el contenedor, `-d` lo deja en segundo plano y `-p` publica el puerto. El volumen se monta en el directorio de páginas de nginx. La imagen se descarga si no estaba disponible; eso requiere conexión al registro.

Abre **Firefox dentro de Ubuntu**, escribe `http://127.0.0.1:8081` en su barra y pulsa **Intro**. El bucle local pertenece aquí a la VM Ubuntu. Si usas el navegador del anfitrión físico, esa misma dirección designará otro sistema.

## 3. Cambia la página y observa persistencia

    ```bash
    sudo docker exec ud3-web sh -c \
      'printf "<h1>Datos persistentes UD3</h1>\n" > /usr/share/nginx/html/index.html'
    sudo docker exec ud3-web uname -r
    sudo docker image inspect nginx:stable-alpine --format '{{json .RepoDigests}}'
    ```

Vuelve a Firefox y pulsa **Ctrl + R**. Comprueba tu página. Compara el kernel con el del primer paso y registra el digest de imagen: una etiqueta como `stable-alpine` puede apuntar a otro contenido en el futuro.

## 4. Recrea el contenedor sin borrar el volumen

    ```bash
    sudo docker stop ud3-web
    sudo docker rm ud3-web
    ```

Repite la orden `docker run` del apartado 2 con el mismo nombre de volumen. Recarga el navegador y comprueba que sigue tu página. Consulta `sudo docker volume ls` y `sudo docker ps -a` para distinguir los recursos. El volumen conserva datos entre instancias, pero no es automáticamente una copia independiente.

Entrega salida del motor, kernel comparado, digest y página tras recreación. Cuando termine la evaluación, limpia únicamente los recursos de este ejercicio siguiendo la indicación del docente; no ejecutes una limpieza global del motor.

## Entrega y comprobación común

Cada práctica se entrega con su código, versiones, estado inicial, decisiones, resultados e incidencias. Las capturas llevan pie explicativo. No se mezclan en la misma entrega las respuestas de otra actividad salvo indicación docente.

## Rúbrica común de prácticas

| Criterio | Puntos |
| --- | ---: |
| Preparación y destino identificados | 2 |
| Procedimiento y resultado funcional | 3 |
| Comprobaciones y diagnóstico | 3 |
| Evidencias explicadas y entrega | 2 |

## Entrega independiente de la práctica

Guarda `X2_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.

<div class="video-card" markdown>

## Vídeo explicativo · Docker: explicación inicial

V7: observa la comparación de capas; la instalación del motor sigue el procedimiento de aula.

<div class="video-frame">
<iframe src="https://www.youtube-nocookie.com/embed/9eTVZwMZJsA" title="Docker: explicación inicial" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://www.youtube.com/watch?v=9eTVZwMZJsA) · [Ficha y preguntas de visionado](../videos.md)

</div>
