# Actividad 3.2 · El recorrido de un archivo en una VM

<div class="lesson-banner" markdown>
<div class="lesson-number">3.2</div>
<div markdown>
**Actividad escrita · El recorrido de un archivo en una VM**

Razonar, interpretar y justificar antes de ejecutar.
</div>
</div>

<div class="activity-meta" markdown>
<span>20 min</span><span>Individual</span><span>Sin entrega</span>
</div>

**Código: A2.** Ejercicio de aula o refuerzo, sin entrega independiente.

**Teoría relacionada:** [Teoría 3.2.1: Comprender la virtualización](../b02-virtualizacion.md)


Tiempo orientativo: 20 minutos. Modalidad: individual. Revisión formativa en clase, sin calificación independiente.

## Antes de responder

Consulta la teoría relacionada antes de responder. Identifica qué información aporta el caso y qué datos faltan. Las soluciones no se deducen por repetir un nombre de herramienta: hay que explicar qué comprobaría y con qué resultado.

## Caso de trabajo

Una persona guarda index.html dentro de Ubuntu virtualizado. El disco de Ubuntu indica 18 GiB libres; al mismo tiempo, el SSD del anfitrión se está llenando. El VDI es dinámico y hay una instantánea anterior.

## Cuestiones

1. Dibuja el recorrido archivo → sistema de archivos invitado → partición → disco virtual y diferenciales → archivo anfitrión → SSD.
2. Explica en qué nivel se mide cada espacio libre y por qué pueden ser diferentes.
3. Indica qué comprobarías primero si una escritura falla aunque Ubuntu muestre espacio.
4. Relaciona anfitrión, invitado e hipervisor con los recursos que aparecen en el dibujo.

## Trabajo en clase

Resuelve las cuestiones que seleccione el docente y contrasta las respuestas en clase. No entregues un PDF ni un archivo separado. Esta ficha queda como banco de refuerzo; no es obligatorio completar todas las actividades.
