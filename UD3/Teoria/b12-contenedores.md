# B12. Contenedores como conexión con DAM

> **Del concepto al laboratorio:** [X2 · Web con Docker](practicas/x2-docker.md)

## 12.1. Imagen, contenedor y volumen

Una imagen es una plantilla para crear contenedores. Un contenedor es una instancia con procesos y una capa de escritura. Un volumen permite conservar datos con un ciclo de vida separado del contenedor. Una etiqueta ayuda a elegir imagen, pero puede cambiar de contenido; para máxima reproducibilidad se registra también su digest.

Un contenedor detenido puede conservar su capa de escritura hasta que se elimina. Al eliminarlo, no debes confiar en esa capa para conservar datos importantes. Un volumen no se borra simplemente por recrear el contenedor, pero también necesita respaldo si contiene información valiosa.

## 12.2. Aplicación de aula

En la ampliación X2 se ejecuta un servidor web dentro de la VM Ubuntu. La instalación del motor sigue la documentación oficial elegida por el docente; no se mezclan paquetes incompatibles ni se pega un script remoto sin revisarlo. Se utilizan comandos con sudo, sin añadir a toda la clase al grupo docker como si fuera un permiso ordinario.

Publicar 127.0.0.1:8081:80 hace accesible el puerto 80 del contenedor a través de 8081 en el bucle local de la VM. Desde el anfitrión físico, 127.0.0.1 identifica otro sistema; por eso la prueba inicial se hace con el navegador de Ubuntu. Esta distinción enlaza con las redes de P5.

## 12.3. Qué comparar

Compara kernel, tiempo de preparación, espacio y persistencia. No concluyas que un contenedor equivale a instalar un sistema completo. Tampoco concluyas que siempre es más adecuado: para aprender el instalador y el arranque de Windows o Linux se necesita un sistema invitado completo. Las aplicaciones web son un contexto apropiado para explorar la alternativa de contenedores. Referencias F10 y F11.

## Actividad A11 · Desmontar una afirmación

«He descargado una imagen Ubuntu en Docker, por tanto he instalado otra VM con un kernel Ubuntu independiente». Identifica las dos confusiones y escribe una corrección de seis líneas. Continúa con X2 si has completado el itinerario básico.
