# UD3. Instalación de sistemas y virtualización

## 1. Resultados de aprendizaje

El alumnado planificará, ejecutará y documentará instalaciones de sistemas operativos libres y propietarios, aplicará actualizaciones y recuperación, y utilizará virtualización para realizar pruebas seguras.

## 2. Planificación de la instalación

Antes de modificar un equipo se recopilan requisitos y se protege la información. Una planificación mínima debe registrar:

- finalidad del sistema y aplicaciones previstas;
- compatibilidad y requisitos de CPU, RAM, disco y firmware;
- arquitectura de 64 bits y opciones de virtualización;
- medio de instalación y comprobación de su integridad;
- esquema de particiones y sistema de archivos;
- nombre del equipo, idioma, zona horaria, red y cuentas;
- licencia, actualizaciones y controladores;
- copia de seguridad y plan de reversión.

Los requisitos recomendados son una referencia más útil que los mínimos. Debe reservarse margen para actualizaciones, datos y crecimiento.

## 3. Arranque y particionado

UEFI selecciona un cargador de arranque, normalmente desde una partición del sistema EFI. GPT es el esquema moderno y admite más particiones y discos grandes; MBR mantiene compatibilidad con sistemas antiguos.

En una instalación Linux son habituales una partición EFI, una raíz `/` y, opcionalmente, particiones separadas para datos o intercambio. En Windows, el instalador crea particiones de sistema y recuperación además del volumen principal.

Nunca debe alterarse un disco con datos importantes sin confirmar el dispositivo, disponer de copia y comprender qué particiones se eliminarán.

## 4. Instalación y configuración inicial

El proceso general es:

1. Obtener la imagen desde una fuente oficial.
2. Verificar su suma de comprobación.
3. Crear el medio de arranque.
4. Configurar UEFI y arrancar desde el medio.
5. Elegir idioma, edición, licencia y destino.
6. Crear cuentas y aplicar una política de contraseñas.
7. Instalar actualizaciones y controladores.
8. Configurar red, privacidad, zona horaria y energía.
9. Instalar aplicaciones autorizadas.
10. Verificar dispositivos, registros, reinicio y recuperación.

La documentación debe incluir versiones, decisiones, capturas relevantes, incidencias y pruebas finales; nunca debe contener contraseñas ni claves privadas.

## 5. VirtualBox y máquinas virtuales

Una máquina virtual dispone de CPU, RAM, disco, firmware y adaptadores virtuales. En un hipervisor de escritorio se deben asignar recursos sin comprometer el anfitrión.

Los modos de red más comunes son:

- **NAT:** acceso exterior sencillo, con aislamiento respecto de la red física.
- **Puente:** la máquina aparece como otro equipo de la red local.
- **Solo anfitrión:** comunicación entre anfitrión e invitados sin salida directa.
- **Red interna:** comunicación únicamente entre máquinas virtuales del mismo entorno.

Las Guest Additions mejoran vídeo, integración del puntero y carpetas compartidas. Una instantánea registra un estado para volver atrás; no sustituye una copia de seguridad porque depende de los archivos de la propia VM.

Clonar crea otra máquina a partir de una existente. Exportar en OVF/OVA facilita su transporte, pero conviene retirar secretos y regenerar identificadores de red cuando proceda.

## 6. Contenedores y Docker

Los contenedores aíslan procesos compartiendo el kernel del anfitrión. Una **imagen** es una plantilla inmutable; un **contenedor** es una instancia ejecutable; un **registro** almacena imágenes.

Comandos básicos:

```bash
docker pull ubuntu:24.04
docker run --name laboratorio -it ubuntu:24.04 bash
docker ps -a
docker stop laboratorio
docker rm laboratorio
docker images
```

Los volúmenes conservan datos fuera de la capa escribible del contenedor. Los puertos se publican explícitamente, por ejemplo `-p 8080:80`.

Un `Dockerfile` describe la construcción de una imagen:

```dockerfile
FROM nginx:alpine
COPY ./web /usr/share/nginx/html
EXPOSE 80
```

Docker Compose declara varios servicios, redes y volúmenes en YAML. Las imágenes deben fijar versiones razonables y evitar ejecutar procesos como `root` cuando no sea necesario.

## 7. Actualización y recuperación

Actualizar reduce vulnerabilidades, pero debe hacerse de forma controlada: inventario, copia, prueba, ventana de mantenimiento y verificación. Las técnicas de recuperación incluyen modo seguro, entorno de recuperación, restauración de paquetes, puntos de restauración, imágenes del sistema y reinstalación.

## 8. Lista de verificación

- La instalación arranca sin errores.
- Todos los dispositivos tienen controlador.
- El sistema está actualizado.
- La red y la resolución DNS funcionan.
- Existen cuentas separadas y privilegios mínimos.
- La fecha, zona horaria y sincronización son correctas.
- Se ha probado el mecanismo de recuperación.
- La memoria técnica permite repetir el proceso.

## 9. Resumen

Instalar no consiste solo en completar un asistente: implica planificar, proteger datos, validar el resultado y dejar evidencias. La virtualización permite repetir y recuperar prácticas, mientras que los contenedores facilitan entornos ligeros y reproducibles.

## Fuentes internas utilizadas

- `Jose_SO/UD2VB.pdf`.
- `Jose_SO/UD2Docker.pdf`.
- `Jose_SO/UD3.pdf`.
- `SI_Celia/Unit_2_Operating-Systems-Fundamentals-and-Virtualisation/`.
