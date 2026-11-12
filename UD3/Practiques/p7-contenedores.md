# P7 · Contenedores: una web y sus datos persistentes

[Antes de empezar: materiales y preparación](preparacion.md) · [Teoría 3.8 · Contenedores](../b12-contenedores.md)

**Práctica guiada, individual y con entrega. Duración obligatoria: 120 minutos.** Trabaja en un clon de tu Ubuntu instalado, con Docker Engine preparado y probado por el docente. El anfitrión físico puede ser Windows o Linux: todas las órdenes de esta ficha se ejecutan en la terminal del **Ubuntu invitado**, no en PowerShell del ordenador físico.

**Objetivo:** comprobar Docker con `hello-world`, gestionar el ciclo de vida de los contenedores, publicar una web y comprobar que sus datos permanecen al eliminar y recrear su contenedor. Distinguirás imagen, contenedor, volumen y máquina virtual.

**Organización orientativa:** entorno y hello-world (20 min), web y ciclo de vida (25 min), personalización y copia (25 min), persistencia (30 min) y diagnóstico/revisión del informe (20 min). Las ampliaciones de Dockerfile y Compose tienen tiempo adicional y no son obligatorias.

## 1. Identifica el entorno y comprueba el motor

Abre el clon Ubuntu. El docente debe haber instalado Docker Engine mediante el [procedimiento oficial para Ubuntu](https://docs.docker.com/engine/install/ubuntu/) y preparado la conexión al registro o la imágenes necesarias (`hello-world` y `nginx:stable-alpine`). No necesitas Docker Desktop dentro de la VM. Si falta el motor, utiliza el clon preparado por el docente.

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

### 1.1. Primera ejecución con hello-world

El docente proporciona también la imagen `hello-world`, o conexión para descargarla. Comprueba que el nombre `ud3-p7-saludo` esté disponible; si existe de una sesión anterior, identifica su estado con el docente antes de continuar.

```bash
sudo docker run --name ud3-p7-saludo hello-world
sudo docker image ls
sudo docker ps
sudo docker ps -a
sudo docker inspect ud3-p7-saludo --format '{{.Id}}'
sudo docker start -a ud3-p7-saludo
sudo docker inspect ud3-p7-saludo --format '{{.Id}}'
```

`run` crea el contenedor, que muestra un mensaje y termina. Por eso puede no aparecer en `ps` y sí en `ps -a` con estado `Exited (0)`. `start -a` ejecuta de nuevo el contenedor existente y muestra su salida: compara los identificadores para comprobar que es el mismo. No confundas un proceso que termina correctamente con un fallo del motor.

**Captura P7-01b:** mensaje, imagen local, estado detenido e identificador conservado tras `start`. Explica la diferencia entre descargar una imagen, crear un contenedor y volver a iniciarlo. Cuando hayas guardado la evidencia, elimina solo el contenedor de saludo, ya detenido:

```bash
sudo docker rm ud3-p7-saludo
```

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

### 2.1. Detener y arrancar no equivale a recrear

Guarda primero el ID inicial indicado arriba. Después ejecuta:

```bash
sudo docker stop ud3-p7-web
sudo docker ps -a
sudo docker start ud3-p7-web
sudo docker inspect ud3-p7-web --format '{{.Id}}'
```

Recarga Firefox. El ID debe coincidir con el inicial: has recuperado el mismo contenedor. Contrastarás este resultado con el paso 5, donde sí lo recrearás. Añade las capturas de esta comprobación como **P7-03b**.

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

También puedes extraer una copia de la página al sistema que ejecuta Docker. Desde tu carpeta de evidencias autorizada en Ubuntu, ejecuta lo siguiente y comprueba el archivo creado:

```bash
sudo docker cp ud3-p7-web:/usr/share/nginx/html/index.html ./p7-pagina-extraida.html
cat ./p7-pagina-extraida.html
```

Esta copia queda fuera del contenedor, pero todavía dentro de Ubuntu. Guárdala junto a las evidencias fuera del clon si necesitas conservarla al restaurar o eliminar la VM. `docker cp` es una copia puntual: modificar uno de los archivos no sincroniza automáticamente el otro. Añade la comprobación a **P7-04b**.

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
| P7-01 y P7-01b | Motor operativo, VM identificada y hello-world: imagen, terminación correcta y mismo ID tras start. |
| P7-02 | Imagen y digest, volumen, ID inicial y publicación de puertos. |
| P7-03 y P7-03b | Web inicial accesible y mismo ID al detener y arrancar el servidor. |
| P7-04 y P7-04b | Página modificada, kernel comparado y copia del archivo a Ubuntu. |
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

## Ampliación A · Construye tu propia imagen con Dockerfile

**Opcional y guiada, unos 35 minutos adicionales.** Hazla tras completar la parte básica, cuando lo indique el docente. Se documenta como anexo del mismo PDF; no constituye otra entrega ni es un requisito para aprobar P7. El docente adapta el tiempo de ampliación sin aumentar las dos horas obligatorias.

### A.1. Prepara los archivos

En la terminal de Ubuntu, crea una carpeta de proyecto vacía. Si ya contiene un ejercicio anterior, consulta antes de sobrescribirlo. Ejecuta cada bloque completo:

```bash
mkdir -p ~/ud3-p7-imagen
cd ~/ud3-p7-imagen
cat > index.html <<'EOF'
<h1>Mi imagen propia de P7</h1>
<p>Esta pagina se incorpora durante la construccion.</p>
EOF
cat > Dockerfile <<'EOF'
FROM nginx:stable-alpine
COPY index.html /usr/share/nginx/html/index.html
EOF
```

Comprueba los dos archivos con el editor de texto. `Dockerfile` lleva esa mayúscula y no tiene extensión. Aquí `COPY` incorpora la página a la imagen, mientras que en la parte básica modificabas los datos del volumen con `exec`.

### A.2. Construye y prueba

```bash
sudo docker build -t ud3-p7-web:v1 .
sudo docker image ls ud3-p7-web
sudo docker history ud3-p7-web:v1
sudo docker run -d --name ud3-p7-imagen -p 127.0.0.1:8082:80 ud3-p7-web:v1
```

Abre `http://127.0.0.1:8082` en Firefox de Ubuntu. Comprueba que muestra la página del proyecto. No montamos el volumen de la parte básica en este contenedor, para que sus archivos no oculten la página incorporada a la imagen. Si el nombre o puerto están ocupados, identifica el recurso con el docente antes de continuar.

**Capturas P7-A1 y P7-A2:** archivos fuente, construcción, imagen local y página. Explica `FROM`, `COPY`, la etiqueta `v1` y el punto como contexto de construcción. Cambiar después el archivo local no cambia por sí solo la imagen ya construida: habría que reconstruirla y recrear el contenedor para distribuir ese cambio.

Tras guardar las evidencias, cierra solo esta prueba:

```bash
sudo docker stop ud3-p7-imagen
sudo docker rm ud3-p7-imagen
```

## Ampliación B · Describe la web con Compose

**Opcional y guiada, unos 25 minutos adicionales.** Requiere haber completado la parte básica, conservar el volumen `ud3_p7_webdatos` y disponer del plugin Compose preparado por el docente. Puede hacerse sin realizar la ampliación A. No requiere cuenta en Docker Hub ni publicar imágenes.

### B.1. Crea y valida la configuración

Comprueba el plugin con `sudo docker compose version`. Si falta, utiliza el procedimiento preparado por el docente; no instales herramientas distintas al azar. En una carpeta vacía, crea el archivo:

```bash
mkdir -p ~/ud3-p7-compose
cd ~/ud3-p7-compose
cat > compose.yaml <<'EOF'
name: ud3-p7-ampliacion
services:
  web:
    image: nginx:stable-alpine
    ports:
      - "127.0.0.1:8083:80"
    volumes:
      - datos:/usr/share/nginx/html
volumes:
  datos:
    external: true
    name: ud3_p7_webdatos
EOF
sudo docker volume inspect ud3_p7_webdatos
sudo docker compose config
```

Respeta los espacios de sangrado. El archivo no utiliza `version:`, campo obsoleto. `external: true` indica que el volumen ya existe y se administra fuera de este proyecto; `name` identifica el de la parte básica. Si no existe, vuelve a comprobar la práctica antes de continuar.

### B.2. Arranca, detén y recrea

Ejecuta desde la carpeta que contiene `compose.yaml`:

```bash
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs web
```

Abre `http://127.0.0.1:8083` dentro de Ubuntu y comprueba que aparece la página personalizada guardada en el volumen. Antes de detenerla registra el ID con `sudo docker compose ps -q web`. Después ejecuta:

```bash
sudo docker compose stop
sudo docker compose ps -a
sudo docker compose start
sudo docker compose ps -q web
```

El ID se conserva. Ahora compara con una retirada completa de los recursos del proyecto:

```bash
sudo docker compose down
sudo docker volume inspect ud3_p7_webdatos
sudo docker compose up -d
sudo docker compose ps -q web
```

El nuevo ID debe ser distinto y la página personalizada debe continuar al recargar Firefox. `down` elimina los contenedores y redes del proyecto por defecto; no equivale a `stop`. Este volumen es externo, por lo que Compose no lo elimina. No generalices ese resultado a todos los montajes o a órdenes que soliciten borrar volúmenes.

**Capturas P7-B1 y P7-B2:** configuración validada, servicio, identificadores antes y después, volumen conservado y web. Explica qué partes de `docker run` has trasladado a YAML. Al finalizar usa `sudo docker compose down` desde esta carpeta para retirar solo el proyecto de ampliación y conservar el volumen de P7.

Las ampliaciones se añaden al mismo `P7_Apellidos_Nombre.pdf` con sus capturas y explicaciones. La rúbrica sobre 10 se aplica a la parte obligatoria; no se penaliza omitir estas ampliaciones. No realices limpiezas globales.

## Criterios de evaluación · Sobre 10

| Criterio | Puntos |
| --- | ---: |
| Preparación, entorno y ciclo de vida básico con hello-world | 2 |
| Creación del servidor y personalización | 3 |
| Persistencia comprobada con otro contenedor y diagnóstico | 3 |
| Capturas explicadas, comparación de kernel y conclusión | 2 |

Referencias: [ejecución de contenedores](https://docs.docker.com/engine/containers/run/) y [volúmenes de Docker](https://docs.docker.com/engine/storage/volumes/).

[Vídeo explicativo y preguntas de visionado](../videos.md)
