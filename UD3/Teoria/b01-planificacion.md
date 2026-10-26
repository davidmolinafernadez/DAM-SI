# 3.1.1 · Instalar es tomar decisiones

<div class="lesson-banner" markdown>
<div class="lesson-number">3.1.1</div>
<div markdown>
**Planificación, medios y arranque**

Planificar una instalación: explicación, ejemplos y comprobaciones.
</div>
</div>

## Un encargo real

Un estudio de desarrollo web necesita un equipo Windows para una herramienta de diseño y un entorno Linux para probar aplicaciones. Las personas desarrolladoras deben poder ensayar cambios sin perder su entorno de trabajo. Antes de descargar nada, hay que decidir si conviene utilizar dos equipos, arranque dual, máquinas virtuales o contenedores.

La decisión depende del uso. Un programa que necesita una GPU concreta puede requerir instalación física. Un ejercicio que compara sistemas completos encaja en máquinas virtuales. Una aplicación con dependencias repetibles puede distribuirse en un contenedor. Ninguna opción elimina la necesidad de actualizar, controlar accesos y respaldar datos.

## Tipos de instalación

Una instalación limpia crea un sistema nuevo sobre un destino elegido. Puede borrar particiones o reutilizar algunas: «limpia» describe el sistema resultante, pero no garantiza que los datos estén protegidos. Una actualización conserva parte del entorno y cambia componentes del sistema; puede fallar por incompatibilidad o falta de espacio. Una reparación intenta restablecer el arranque o los archivos dañados. Un despliegue desde imagen reproduce una preparación previa y exige atender a las identidades, el hardware y las licencias del destino.

En el arranque dual dos sistemas comparten el equipo y se elige uno al encender. No se ejecutan simultáneamente. Una VM ejecuta un sistema invitado mientras el anfitrión continúa funcionando. El arranque dual reparte espacio de disco; la virtualización también reparte RAM y CPU durante la ejecución.

## Plan de instalación

Un plan útil identifica destinatario, aplicaciones, arquitectura, requisitos, fuente de instalación, licencias, esquema de almacenamiento, configuración de red, cuentas, pruebas de aceptación y recuperación. Tiene que ser lo bastante concreto para que otra persona lo ejecute sin adivinar decisiones.

Ejemplo: «Ubuntu para prácticas» es insuficiente. «VM Ubuntu Desktop 24.04 LTS amd64; 2 vCPU; 4 GiB de RAM; disco virtual dinámico de 50 GiB; NAT; usuario alumno; zona Europe/Madrid; verificar inicio sin ISO y actualización de paquetes» permite comprobar el resultado. Estas cifras son una propuesta de aula, no requisitos oficiales universales.

## Mínimo, recomendado y disponible

El mínimo permite cumplir una condición de instalación; el recomendado busca una experiencia razonable. Lo disponible es lo que queda después de atender al anfitrión y a las demás cargas. Un ordenador con 8 GiB no dispone de 8 GiB libres para invitados. Si el anfitrión pagina continuamente, una VM con muchos recursos asignados puede funcionar peor.

Reserva orientativa para un anfitrión de 16 GiB: 6 GiB para el sistema y aplicaciones, 4 GiB para Ubuntu, 4 GiB para Windows y 2 GiB de margen. Es una hipótesis que debe medirse. En equipos de 8 GiB se trabajará con una VM cada vez y se ajustará el escritorio o se utilizará un equipo del aula. No se rebajan los requisitos de Windows para forzar el ejercicio.

## Convertir una necesidad en una prueba

Un requisito expresa una necesidad; una prueba muestra si se satisface. «Necesito Linux para desarrollar» todavía no concreta arquitectura, memoria ni aplicaciones. «Necesito ejecutar Python y servir una página local a un navegador del anfitrión» permite decidir sistema, red y comprobación. La prueba no debe depender de una opinión como «va rápido» sin describir la carga y las condiciones.

Un plan tiene además un orden. Descargar antes de comprobar arquitectura puede obligar a repetir una descarga de varios gigabytes. Instalar antes de identificar los discos puede afectar datos que no eran el destino. Actualizar sin un estado de retorno dificulta separar un fallo previo de uno introducido por el cambio.

| Decisión | Qué información necesita | Cómo se comprobará |
| --- | --- | --- |
| Sistema y arquitectura | Aplicación, CPU y soporte | Versión instalada y aplicación ejecutada |
| Memoria del invitado | Carga y reserva del anfitrión | Consumo observado sin presión excesiva |
| Destino de instalación | Discos, particiones y datos existentes | Resumen antes de escribir y mapa posterior |
| Red | Quién inicia la conexión | Petición al servicio desde el origen previsto |
| Recuperación | Tipo de fallo que debe cubrirse | Retorno o restauración con archivo testigo |

## Tres instalaciones con efectos diferentes

Una instalación nueva sobre un disco vacío no tiene los mismos riesgos que reinstalar un equipo de trabajo. En el segundo caso importan datos, licencias, configuración y recuperación. Actualizar conservando programas tampoco elimina riesgos: puede haber incompatibilidades, cambios de controladores y espacio temporal insuficiente. Por eso el inventario y la copia previa se deciden antes de abrir el asistente.

En el aula se elige una VM con disco vacío para estudiar el proceso con un destino claro. Esta elección no autoriza a trasladar «Borrar disco» al ordenador familiar. Lo que se aprende es a identificar el destino y razonar el efecto de cada pantalla, de forma que luego pueda aplicarse el mismo criterio a otro entorno.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 3.1 · Decidir antes de instalar](actividades/A01-decidir-antes-de-instalar.md)
- [Actividad 3.13 · Presupuesto profesional de laboratorio](actividades/A13-presupuesto-profesional-de-laboratorio.md)

## Prácticas relacionadas

- [P0 · Auditoría e ISO](practicas/p0-auditoria.md)

<div class="video-card" markdown>

## Vídeo explicativo · Máquinas virtuales con VirtualBox

V1: observa la relación entre necesidad y recursos; el plan se razona en A1 y se verifica en P0.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/bh97chmwc7d66tfd/fs" title="Máquinas virtuales con VirtualBox" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/bh97chmwc7d66tfd) · [Ficha y preguntas de visionado](videos.md)

</div>
