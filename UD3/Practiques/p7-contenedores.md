# P7 · Contenedores: una web y sus datos persistentes

[Antes de empezar: materiales y preparación](preparacion.md) · [Teoría 3.8 · Contenedores](../b12-contenedores.md)

**Práctica guiada, individual y con entrega. Duración: 120 minutos.** Trabaja en un clon de tu Ubuntu instalado, con Docker Engine preparado y probado por el docente. El anfitrión físico puede ser Windows o Linux: todas las órdenes de esta ficha se ejecutan en la terminal del **Ubuntu invitado**, no en PowerShell del ordenador físico.

**Objetivo:** publicar una web, modificarla y comprobar que sus datos permanecen al eliminar y recrear el contenedor. Distinguirás imagen, contenedor, volumen y máquina virtual.

## 1. Identifica el entorno y comprueba el motor

Abre el clon Ubuntu. El docente debe haber instalado Docker Engine mediante el [procedimiento oficial para Ubuntu](https://docs.docker.com/engine/install/ubuntu/) y preparado la conexión al registro o la imagen necesaria. No necesitas Docker Desktop dentro de la VM. Si falta el motor, utiliza el clon preparado por el docente.

Abre **Terminal** con **Ctrl + Alt + T**. Ejecuta una línea cada vez:

```bash
hostnamectl
uname -r
sudo docker version
sudo docker info
sudo docker ps -a
sudo docker volume ls
```

Anota el nombre de la VM, versión de Ubuntu, kernel y versión del motor. `docker version` debe mostrar cliente y servidor. Si no conecta con el servidor, registra el mensaje y consulta al docente antes de continuar. Las órdenes con `sudo` pueden pedir tu contraseña; no aparecerá al escribirla.

Comprueba que no existen recursos de una sesión anterior con los nombres `ud3-p7-web` y `ud3_p7_webdatos`. Si existen, consúltalo para identificar su contenido antes de reutilizarlos o eliminarlos. Esta ficha parte de esos nombres disponibles.

**Captura P7-01:** identificación del entorno y respuesta del cliente y servidor. Utiliza varias imágenes para mantener legibles los datos.

## 2. Prepara la imagen, el volumen y el servidor

Ejecuta:

```bash
sudo docker pull nginx:stable-alpine
sudo docker image inspect nginx:stable-alpine --format '{{json .RepoDigests}}'
sudo docker volume create ud3_p7_webdatos
sudo docker run -d --name ud3-p7-web -p 127.0.0.1:8081:80 -v ud3_p7_webdatos:/usr/share/nginx/html nginx:stable-alpine
sudo docker ps
sudo docker port ud3-p7-web
sudo docker inspect ud3-p7-web --format '{{.Id}}'
```

Si la imagen ya está disponible y no hay conexión al registro, el docente puede autorizar usar esa copia local sin repetir `pull`; registra su procedencia y digest. Guarda el identificador del contenedor como **ID inicial**.

En `docker run`, `-d` mantiene el servidor en segundo plano, `--name` asigna su nombre, `-p` publica el puerto y `-v` monta el volumen. El volumen nuevo puede recibir los archivos que trae la imagen en ese directorio; por eso podrás ver la página inicial de nginx.

Abre **Firefox dentro de Ubuntu** y visita `http://127.0.0.1:8081`. Debe aparecer la página inicial de nginx. Aquí `127.0.0.1` identifica la VM Ubuntu que ejecuta Docker. En el navegador del ordenador físico identificaría otro sistema.

**Capturas P7-02 y P7-03:** imagen y digest, volumen, contenedor en ejecución, publicación de puertos y página inicial con la dirección visible. Explica qué representa cada recurso.

## 3. Personaliza la página y compara el kernel

Ejecuta en la terminal de Ubuntu:

```bash
sudo docker exec ud3-p7-web sh -c 'printf "<h1>P7 - Mi web de aula</h1>\n<p>Datos persistentes de mi laboratorio</p>\n" > /usr/share/nginx/html/index.html'
sudo docker exec ud3-p7-web cat /usr/share/nginx/html/index.html
sudo docker exec ud3-p7-web uname -r
uname -r
```

Recarga Firefox con **Ctrl + R** y comprueba el texto personalizado. Compara los dos resultados de `uname -r`: en este entorno Linux, el contenedor utiliza el kernel de la VM Ubuntu que ejecuta Docker. No es otro sistema completo arrancado con su propio kernel.

**Captura P7-04:** página personalizada, contenido del archivo y comparación de kernel, con una breve interpretación.

## 4. Elimina el contenedor y predice qué ocurrirá

Antes de ejecutar nada, escribe en tu informe qué esperas que ocurra con la web y con sus datos al eliminar el contenedor, conservando el volumen.

```bash
sudo docker stop ud3-p7-web
sudo docker rm ud3-p7-web
sudo docker ps -a
sudo docker volume inspect ud3_p7_webdatos
```

Comprueba que el contenedor ya no está y que el volumen sigue existiendo. Recarga la dirección en Firefox: la petición debería fallar porque has retirado el servidor. Si aún ves la página anterior, comprueba que no sea una vista en caché; esa pantalla por sí sola no demuestra que el servicio continúe funcionando.

**Captura P7-05:** ausencia del contenedor, presencia del volumen y resultado observado en el navegador. Explica qué ha desaparecido y qué se conserva.

## 5. Crea otro contenedor con el mismo volumen

```bash
sudo docker run -d --name ud3-p7-web -p 127.0.0.1:8081:80 -v ud3_p7_webdatos:/usr/share/nginx/html nginx:stable-alpine
sudo docker inspect ud3-p7-web --format '{{.Id}}'
sudo docker exec ud3-p7-web cat /usr/share/nginx/html/index.html
sudo docker ps
```

Guarda este identificador como **ID nuevo** y compáralo con el inicial. Aunque el nombre sea el mismo, el identificador debe ser distinto: has creado otro contenedor. Recarga Firefox y comprueba que reaparece tu página personalizada gracias al volumen conservado.

**Captura P7-06:** nuevo identificador, archivo y web recuperada. Relaciona el resultado con tu predicción. No basta con reiniciar el mismo contenedor para superar esta comprobación.

## 6. Diagnostica y cierra la sesión

**Incidencia para analizar:** la imagen aparece descargada, pero la web no responde. Propón dos causas distintas y una prueba para cada una. Puedes apoyarte en estas consultas:

```bash
sudo docker ps -a
sudo docker port ud3-p7-web
sudo docker logs ud3-p7-web
```

Comprueba también desde qué sistema abres el navegador y qué dirección y puerto utilizas. Si el error real es «nombre ya utilizado» o «puerto ocupado», registra el mensaje y revisa los recursos existentes con el docente; no elimines otros contenedores para hacer sitio.

Al terminar, detén únicamente el contenedor de esta práctica:

```bash
sudo docker stop ud3-p7-web
sudo docker ps -a
```

Para retomarlo utiliza `sudo docker start ud3-p7-web`. No repitas `docker run` mientras siga existiendo ese nombre. Conserva el volumen hasta que el docente revise la evidencia. No ejecutes limpiezas globales.

**Captura P7-07:** diagnóstico realizado si hubo una incidencia y estado final detenido. Distingue la respuesta al caso propuesto de los problemas que hayas observado realmente.

## Qué debes entregar

Entrega **un único `P7_Apellidos_Nombre.pdf` en la tarea de Aules**, con una sucesión ordenada de capturas propias de los pasos 1–6 y una pequeña explicación de cada paso. Guarda las evidencias fuera del clon para conservarlas.

### Estructura del informe

1. **Portada y preparación:** nombre, grupo, fecha, anfitrión, VM, Ubuntu y versión de Docker.
2. **Proceso:** pasos en orden, comandos utilizados y capturas P7-01 a P7-07. Añade varias imágenes para un código cuando sea necesario.
3. **Explicación por paso:** 2–4 líneas sobre qué has hecho, qué se ve y qué demuestra el resultado.
4. **Comprobación de persistencia:** predicción previa, identificadores inicial y nuevo, y tabla de resultados.
5. **Diagnóstico y conclusión:** respuesta a la incidencia, problemas reales y diferencia entre imagen, contenedor, volumen y VM.

| Evidencia | Qué debe quedar acreditado |
| --- | --- |
| P7-01 | Motor operativo e identificación de la VM. |
| P7-02 | Imagen y digest, volumen, ID inicial y publicación de puertos. |
| P7-03 | Web inicial accesible desde Firefox de Ubuntu. |
| P7-04 | Página modificada y kernel comparado. |
| P7-05 | Contenedor eliminado y volumen conservado. |
| P7-06 | ID nuevo y página personalizada recuperada. |
| P7-07 | Cierre de sesión y diagnóstico, si hubo un problema real. |

### Tabla para copiar y completar

| Momento | ID del contenedor | Estado del contenedor | ¿Existe el volumen? | Resultado de la web |
| --- | --- | --- | --- | --- |
| Creación inicial | [completar] | [completar] | [completar] | [completar] |
| Tras personalizar | [completar] | [completar] | [completar] | [completar] |
| Tras eliminarlo | [no existe] | [completar] | [completar] | [completar] |
| Tras recrearlo | [nuevo ID] | [completar] | [completar] | [completar] |

**Ejemplo de pie de captura:** «P7-06. He creado otro contenedor con el mismo volumen. Su identificador cambia de [ID inicial] a [ID nuevo] y reaparece mi página personalizada. Los datos permanecieron en el volumen cuando eliminé el primer contenedor». Sustituye los campos por resultados reales y utiliza esta conclusión solo si la has comprobado.

**Antes de entregar:** revisa que las capturas sean legibles, que cada una tenga explicación y que aparezcan el digest y los dos identificadores como texto. No incluyas contraseñas. Las imágenes deben ir dentro del PDF; no subas capturas sueltas, VM, imágenes de Docker ni volúmenes.

## Criterios de evaluación · Sobre 10

| Criterio | Puntos |
| --- | ---: |
| Preparación y entorno identificados | 2 |
| Creación del servidor y personalización | 3 |
| Persistencia comprobada con otro contenedor y diagnóstico | 3 |
| Capturas explicadas, comparación de kernel y conclusión | 2 |

Referencias: [ejecución de contenedores](https://docs.docker.com/engine/containers/run/) y [volúmenes de Docker](https://docs.docker.com/engine/storage/volumes/).

[Vídeo explicativo y preguntas de visionado](../videos.md)
