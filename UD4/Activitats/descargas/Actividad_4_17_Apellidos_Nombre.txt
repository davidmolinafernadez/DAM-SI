# Actividad 4.17 · Identificar paquetes y repositorios

<div class="lesson-banner" markdown>
<div class="lesson-number">4.17</div>
<div markdown>
**Actividad escrita · Identificar paquetes y repositorios**

Razonar, interpretar y justificar antes de ejecutar.
</div>
</div>

<div class="activity-meta" markdown>
<span>25 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

**Código: A17.** Actividad escrita con entrega propia.

**Teoría relacionada:** [Teoría 4.6: Actualizaciones y aceptación](../b10-actualizaciones.md)

[Descargar actividad en PDF](descargas/Actividad_4_17_Apellidos_Nombre.pdf){ .md-button .md-button--primary }
[Original editable en texto](descargas/Actividad_4_17_Apellidos_Nombre.txt){ .md-button download }

Tiempo orientativo: 25 minutos. Modalidad: individual. Valoración formativa: 10 puntos.

## Antes de responder

Consulta la teoría relacionada antes de responder. Identifica qué información aporta el caso y qué datos faltan. Las soluciones no se deducen por repetir un nombre de herramienta: hay que explicar qué comprobaría y con qué resultado.

## Caso de trabajo

Tienes un archivo programa_1.4_amd64.deb, un programa instalado con APT y una aplicación que aparece en snap list. Además, una guía antigua propone renombrar una clave descargada y añadir un PPA sin comprobar la versión de Ubuntu.

## Cuestiones

1. Distingue archivo descargado, nombre de paquete e instalación disponible.
2. Asocia dpkg-deb --info, dpkg-query -W, apt install ./archivo.deb y snap list con la información o acción correspondiente.
3. Explica los campos Types, URIs, Suites, Components y Signed-By de una definición .sources.
4. Indica qué revisarías antes de añadir un origen externo y por qué cambiar la extensión no convierte el formato de una clave.
5. Compara retirar una aplicación y eliminar sus documentos personales.

## Entrega de esta actividad

Mapa de herramientas y revisión de la propuesta de repositorio. No se añade ningún origen ni se importa ninguna clave. Guarda el archivo como `Actividad_4_17_Apellidos_Nombre.pdf`. Incluye las preguntas numeradas, razonamiento propio y fuentes concretas cuando consultes información adicional. No se pide añadir una portada vacía ni capturas de asistentes que no ejecutas.

## Revisión y valoración

| Criterio | Puntos |
| --- | ---: |
| Conceptos y datos interpretados correctamente | 4 |
| Justificación y relación entre causa y resultado | 3 |
| Tabla, esquema o propuesta solicitada | 2 |
| Claridad, fuentes y entrega | 1 |
