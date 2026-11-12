# 3.8 · Contenedores y Docker para DAM

<div class="lesson-banner" markdown>
<div class="lesson-number">3.8</div>
<div markdown>
**De la máquina virtual al entorno de una aplicación**

Comprende la arquitectura, gestiona imágenes y contenedores y distingue aplicación, configuración y datos.
</div>
</div>

![Infografía: Imagen, contenedor y datos](imagenes/b12-contenedores.svg)

## 1. Para qué utilizar contenedores

En DAM, una aplicación puede necesitar una versión de Java, bibliotecas y una base de datos. Instalarlas manualmente en cada equipo facilita que aparezcan diferencias entre desarrollo, pruebas y despliegue. Una imagen permite distribuir un entorno de aplicación definido; el contenedor lo ejecuta con aislamiento de procesos, sistema de archivos y red.

La analogía con los contenedores marítimos ayuda a entender el empaquetado y el transporte, pero tiene límites: una imagen necesita una plataforma compatible. Arquitectura de CPU, kernel, dispositivos y configuración influyen en que funcione. Empaquetar una aplicación no garantiza compatibilidad universal ni elimina la necesidad de probarla.

Docker puede utilizarse en un portátil, un servidor local o la nube. La nube no es un requisito. Ejemplos: probar una base de datos sin instalarla directamente en el equipo, preparar un entorno común para un proyecto o repetir pruebas con distintas versiones de una aplicación.

## 2. Máquina virtual y contenedor

| Aspecto | Máquina virtual | Contenedor Linux |
| --- | --- | --- |
| Qué proporciona | Hardware virtual para un sistema invitado | Entorno aislado para procesos y sus dependencias |
| Kernel | El invitado utiliza su propio kernel | Comparte el kernel Linux del sistema que ejecuta el motor |
| Inicio | Arranca el sistema invitado | Inicia el proceso configurado; suele requerir menos preparación |
| Recursos | Incluye un sistema invitado completo | Puede compartir capas de imágenes y evita un kernel por contenedor |
| Uso en esta unidad | Instalar, arrancar y recuperar Ubuntu o Windows | Ejecutar una aplicación y comprobar sus datos |

En nuestro laboratorio conviven ambas tecnologías: **ordenador físico → VirtualBox → VM Ubuntu con su kernel → Docker Engine → contenedores**. Si el ordenador físico usa Windows, el contenedor de P7 comparte el kernel de Ubuntu, no el de Windows. Docker Desktop puede proporcionar otra arquitectura, pero no es la utilizada en esta práctica.

No establezcas una regla de rendimiento sin medir: aplicación, almacenamiento, red y límites de recursos afectan al resultado. Tampoco confundas aislamiento con protección absoluta: el acceso al motor y las imágenes elegidas importan.

## 3. Cliente, motor y registro

Cuando escribes una orden, intervienen tres elementos:

1. **Cliente:** el programa `docker` interpreta la petición y se comunica con el motor.
2. **Motor o servidor:** Docker Engine administra imágenes, contenedores, redes y volúmenes en la VM Ubuntu. Tener el cliente instalado no demuestra que el motor funcione.
3. **Registro:** almacena y distribuye imágenes. Docker Hub es el registro utilizado en nuestros ejemplos; hay otros registros públicos y privados.

Por ejemplo, `sudo docker pull nginx:stable-alpine` solicita descargar una imagen. `sudo docker run ... nginx:stable-alpine` solicita crear un contenedor; si falta la imagen, con la política predeterminada el motor intenta descargarla primero. Son operaciones distintas.

En [Docker Hub](https://hub.docker.com/_/nginx) comprueba quién publica la imagen, sus etiquetas, arquitecturas y documentación. Un resultado de búsqueda no acredita por sí solo que una imagen sea adecuada. Para P7 no necesitas crear una cuenta ni publicar imágenes.

Consulta la [arquitectura oficial de Docker](https://docs.docker.com/get-started/docker-overview/).

## 4. Imagen, etiqueta, digest y contenedor

Una **imagen** es una plantilla de solo lectura con archivos y valores de configuración. Puede incluir capas compartidas con otras imágenes. Al crear un **contenedor**, se añade una capa de escritura y se configura qué proceso se ejecutará. Una misma imagen permite crear varios contenedores independientes.

Una **etiqueta**, como `stable-alpine`, es una referencia que puede cambiar de contenido. `latest` es una etiqueta convencional: no demuestra que se haya descargado la versión más reciente ni fuerza una actualización de una copia local. El **digest** identifica un contenido concreto del registro. Para reconstruir un entorno registra imagen, digest y configuración, además de sus datos.

El nombre de un contenedor se elige para reconocerlo; su identificador permite distinguir instancias. Recrear un contenedor con el mismo nombre genera otro identificador. Detenerlo y volverlo a iniciar conserva su identificador y, normalmente, su capa de escritura.

### Ciclo de vida y órdenes básicas

| Orden de ejemplo | Qué permite comprobar o hacer |
| --- | --- |
| `sudo docker version` | Consultar versiones del cliente y servidor |
| `sudo docker image ls` | Listar imágenes locales |
| `sudo docker ps` | Ver contenedores en ejecución |
| `sudo docker ps -a` | Incluir también los contenedores detenidos |
| `sudo docker run --name prueba hello-world` | Crear un contenedor y ejecutar su proceso |
| `sudo docker start prueba` | Arrancar de nuevo ese contenedor existente |
| `sudo docker stop ud3-p7-web` | Detener el servidor de P7 sin eliminarlo |
| `sudo docker exec ud3-p7-web uname -r` | Ejecutar otra orden en el contenedor que está en marcha |
| `sudo docker logs ud3-p7-web` | Consultar la salida registrada por su proceso |
| `sudo docker rm prueba` | Eliminar ese contenedor una vez detenido |

`hello-world` termina después de mostrar su mensaje: encontrarlo detenido puede ser el resultado correcto. Un contenedor permanece en ejecución mientras lo haga su proceso principal. `run` crea; `start` reutiliza. Repetir `run` con un nombre ya ocupado produce un conflicto.

En una orden de creación, `--name` da un nombre, `-d` ejecuta en segundo plano, `-it` permite una interacción con terminal y `--rm` solicita eliminar automáticamente el contenedor cuando termina. No uses `--rm` si necesitas observar después el contenedor detenido como evidencia.

## 5. Publicación de puertos

En `-p 127.0.0.1:8081:80`, `127.0.0.1` es la dirección de escucha del sistema que ejecuta Docker, `8081` es su puerto publicado y `80` el puerto del contenedor. En P7, abre `http://127.0.0.1:8081` en Firefox **dentro de Ubuntu**. En el navegador del ordenador físico, esa dirección identifica el propio ordenador físico.

Escribir `EXPOSE 80` en un Dockerfile documenta un puerto, pero no sustituye su publicación. Una imagen descargada tampoco acredita que exista un servidor en marcha o que el navegador pueda alcanzarlo. El acceso desde otros equipos se estudia en UD4/P6.

## 6. Qué datos se conservan

| Ubicación | Al detener y arrancar el mismo contenedor | Al eliminar y recrear el contenedor |
| --- | --- | --- |
| Capa de escritura del contenedor | Habitualmente se conserva | Se pierde con el contenedor eliminado |
| Volumen con nombre | Se conserva | Se conserva si no lo eliminas y vuelves a montarlo |
| Carpeta del sistema que ejecuta Docker, montada mediante bind mount | Sus archivos permanecen fuera del contenedor | Permanecen y pueden montarse de nuevo |

Un volumen lo administra Docker; un **bind mount** utiliza una ruta que tú eliges en el sistema que ejecuta el motor. En P7 ese sistema es la VM Ubuntu. Cambiar un archivo en un montaje puede afectar a los datos externos al contenedor. La imagen, por su parte, no se modifica al editar archivos de una instancia.

`docker cp` copia entre el sistema local y un contenedor, incluso detenido; no establece una sincronización permanente ni sustituye una estrategia de persistencia. Ejemplo para extraer la página de P7 desde la terminal de Ubuntu:

```bash
sudo docker cp ud3-p7-web:/usr/share/nginx/html/index.html ./pagina-recuperada.html
```

Conservar un volumen no equivale a disponer de una copia de seguridad independiente. Si se pierde el disco de la VM, también pueden perderse sus volúmenes. Consulta [volúmenes](https://docs.docker.com/engine/storage/volumes/) y [copia de archivos](https://docs.docker.com/reference/cli/docker/container/cp/).

## 7. Introducción a Dockerfile

Un **Dockerfile** describe cómo construir una imagen. Frente a modificar manualmente una instancia, guardar la receta y sus archivos facilita revisar y repetir la construcción. El digest de la base y las versiones de las dependencias también influyen en la reproducibilidad.

```dockerfile
FROM nginx:stable-alpine
COPY index.html /usr/share/nginx/html/index.html
```

Este ejemplo parte de nginx y añade una página del proyecto. `FROM` selecciona la base y `COPY` incorpora un archivo del contexto de construcción. Otras instrucciones son `RUN`, que ejecuta órdenes durante la construcción, y `CMD`, que define el comando predeterminado de ejecución. Aquí heredamos el arranque de nginx de la imagen base.

Desde la carpeta que contiene `Dockerfile` e `index.html`, `sudo docker build -t ud3-p7-web:v1 .` construye la imagen. El punto es el contexto de construcción; `build` no arranca el servidor. Para ejecutarlo hace falta crear un contenedor.

`docker commit` puede capturar cambios de una instancia, pero no sustituye una receta documentada ni incluye los datos de los volúmenes montados. En la ampliación utilizamos Dockerfile. [Guía oficial](https://docs.docker.com/build/concepts/dockerfile/).

## 8. Introducción a Compose y YAML

**Docker Compose** permite describir servicios, redes y volúmenes en un archivo YAML y gestionarlos conjuntamente. También resulta útil con un solo servicio, porque conserva su configuración. YAML expresa la estructura mediante sangrado: utiliza espacios y respeta los niveles.

```yaml
name: ud3-p7-demo
services:
  web:
    image: nginx:stable-alpine
    ports:
      - "127.0.0.1:8083:80"
```

En este ejemplo, `services` contiene el servicio `web`, `image` selecciona su imagen y `ports` configura la publicación. Si necesitas datos persistentes, puedes declarar un volumen y montarlo en el servicio. Para construir una imagen propia utilizarás `build` con su contexto.

| Orden | Resultado |
| --- | --- |
| `sudo docker compose config` | Comprobar y mostrar la configuración interpretada |
| `sudo docker compose up -d` | Crear o actualizar los servicios y arrancarlos en segundo plano |
| `sudo docker compose ps` | Consultar los contenedores del proyecto |
| `sudo docker compose logs` | Consultar sus registros |
| `sudo docker compose stop` | Detener los contenedores conservándolos |
| `sudo docker compose down` | Detener y eliminar los contenedores y redes del proyecto por defecto |

El campo superior `version:` está obsoleto; los ejemplos actuales lo omiten. `down` conserva por defecto los volúmenes con nombre; `down -v` solicita eliminar los declarados por el proyecto y cambia el resultado de persistencia.

Con varios servicios, `depends_on` puede ordenar el arranque, pero no garantiza por sí solo que una base de datos esté lista. Esa condición necesita una comprobación de salud y la dependencia correspondiente. Tampoco basta con pedir varias instancias de una base de datos para obtener replicación o reparto de carga correcto.

Referencias: [Compose](https://docs.docker.com/compose/gettingstarted/), [campo version](https://docs.docker.com/reference/compose-file/version-and-name/), [orden de arranque](https://docs.docker.com/compose/how-tos/startup-order/) y [down](https://docs.docker.com/reference/cli/docker/compose/down/).

## Preparación y permisos en el aula

El docente prepara Docker Engine en un clon Ubuntu siguiendo la [instalación oficial](https://docs.docker.com/engine/install/ubuntu/). Distinguimos el motor Docker Engine de la aplicación Docker Desktop y evitamos mezclar paquetes de procedimientos diferentes.

En P7 utilizamos órdenes con `sudo`. Pertenecer al grupo `docker` concede privilegios equivalentes a root sobre el sistema que ejecuta el motor; no lo presentes como acceso ordinario sin privilegios. [Permisos y postinstalación](https://docs.docker.com/engine/install/linux-postinstall/).

Solo se detienen o eliminan los recursos identificados del ejercicio. Las órdenes de limpieza global no son necesarias para completarlo.

## Práctica y comprobaciones · P7

Realiza [P7 · Contenedores: una web y sus datos persistentes](practicas/p7-contenedores.md). La parte obligatoria dura **dos horas** e incluye comprobación del motor, `hello-world`, ciclo de vida, web, comparación del kernel y persistencia. Entrega un único `P7_Apellidos_Nombre.pdf` con capturas explicadas y resultados reales.

La ficha incluye ampliaciones guiadas de Dockerfile y Compose. Se realizan cuando el docente las propone, con tiempo adicional o sustituyendo trabajo equivalente; no añaden otra entrega ni son necesarias para superar la parte básica. Las preguntas de vídeos se comentan en clase. En UD3 se mantienen nueve entregas: A1, A10 y P1–P7.

**Comprueba que puedes explicar:** por qué `hello-world` termina; qué diferencia `run` de `start`; qué sistema aporta el kernel; dónde se guardan los datos; y por qué una web puede fallar aunque la imagen exista.

## Vídeo explicativo · Docker: explicación inicial

<div class="video-frame">
<iframe src="https://www.youtube-nocookie.com/embed/9eTVZwMZJsA" title="Docker: explicación inicial" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo](https://www.youtube.com/watch?v=9eTVZwMZJsA) · [Ficha y preguntas de visionado](videos.md)

## Material de referencia docente

Contenido ampliado a partir del manual de aula `UD2Docker.pdf` y la presentación `UP2__2_Virtualitzacio-amb-Docker.pdf` del curso 2025–2026. Se aprovechan su secuencia de conceptos, arquitectura, gestión y ejemplos de construcción, adaptados al laboratorio actual y contrastados con las referencias oficiales enlazadas. Los comandos de las fichas web vigentes sustituyen a los ejemplos antiguos cuando difieren.
