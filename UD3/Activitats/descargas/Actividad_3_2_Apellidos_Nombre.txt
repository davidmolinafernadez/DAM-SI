# Actividad 3.2 · El recorrido de un archivo en una VM

<div class="lesson-banner" markdown>
<div class="lesson-number">3.2</div>
<div markdown>
**Actividad escrita · El recorrido de un archivo en una VM**

Razonar, interpretar y justificar antes de ejecutar.
</div>
</div>

<div class="activity-meta" markdown>
<span>20 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

**Código: A2.** Actividad escrita con entrega propia.

**Teoría relacionada:** [Teoría 3.2.1: Comprender la virtualización](../b02-virtualizacion.md)

[Descargar actividad en PDF](descargas/Actividad_3_2_Apellidos_Nombre.pdf){ .md-button .md-button--primary }
[Original editable en texto](descargas/Actividad_3_2_Apellidos_Nombre.txt){ .md-button download }

Tiempo orientativo: 20 minutos. Modalidad: individual. Valoración formativa: 10 puntos.

## Antes de responder

Consulta la teoría relacionada antes de responder. Identifica qué información aporta el caso y qué datos faltan. Las soluciones no se deducen por repetir un nombre de herramienta: hay que explicar qué comprobaría y con qué resultado.

## Caso de trabajo

Una persona guarda index.html dentro de Ubuntu virtualizado. El disco de Ubuntu indica 18 GiB libres; al mismo tiempo, el SSD del anfitrión se está llenando. El VDI es dinámico y hay una instantánea anterior.

## Cuestiones

1. Dibuja el recorrido archivo → sistema de archivos invitado → partición → disco virtual y diferenciales → archivo anfitrión → SSD.
2. Explica en qué nivel se mide cada espacio libre y por qué pueden ser diferentes.
3. Indica qué comprobarías primero si una escritura falla aunque Ubuntu muestre espacio.
4. Relaciona anfitrión, invitado e hipervisor con los recursos que aparecen en el dibujo.

## Entrega de esta actividad

Esquema comentado y respuesta al caso. No se debe llenar realmente el disco para comprobarlo. Guarda el archivo como `Actividad_3_2_Apellidos_Nombre.pdf`. Incluye las preguntas numeradas, razonamiento propio y fuentes concretas cuando consultes información adicional. No se pide añadir una portada vacía ni capturas de asistentes que no ejecutas.

## Revisión y valoración

| Criterio | Puntos |
| --- | ---: |
| Conceptos y datos interpretados correctamente | 4 |
| Justificación y relación entre causa y resultado | 3 |
| Tabla, esquema o propuesta solicitada | 2 |
| Claridad, fuentes y entrega | 1 |
