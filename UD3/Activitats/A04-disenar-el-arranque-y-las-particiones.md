# Actividad 3.4 · Diseñar el arranque y las particiones

<div class="lesson-banner" markdown>
<div class="lesson-number">3.4</div>
<div markdown>
**Actividad escrita · Diseñar el arranque y las particiones**

Razonar, interpretar y justificar antes de ejecutar.
</div>
</div>

<div class="activity-meta" markdown>
<span>25 min</span><span>Individual</span><span>Sin entrega</span>
</div>

**Código: A4.** Ejercicio de aula o refuerzo, sin entrega independiente.

**Teoría relacionada:** [Teoría 3.1.3: Firmware, arranque y particiones](../b04-firmware-y-particiones.md)

Tiempo orientativo: 25 minutos. Modalidad: individual. Revisión formativa en clase, sin calificación independiente.

## Antes de responder

Consulta la teoría relacionada antes de responder. Identifica qué información aporta el caso y qué datos faltan. Las soluciones no se deducen por repetir un nombre de herramienta: hay que explicar qué comprobaría y con qué resultado.

## Caso de trabajo

Debes proponer un disco Linux UEFI de 60 GiB. Se quiere separar /home para facilitar futuras reinstalaciones y conservar un registro de qué se formateará. Todavía no se ha abierto ningún instalador.

## Cuestiones

1. Dibuja tabla, particiones, tamaños aproximados, formatos y puntos de montaje.
2. Identifica la ESP y explica por qué no se trata como otra partición de documentos.
3. Compara tu diseño con uno de una sola raíz y razona una ventaja y un límite de separar /home.
4. Explica qué se perdería si se marca formatear /home durante una reinstalación.
5. Corrige las frases «GPT siempre exige UEFI» y «una partición de datos ya es una copia de seguridad».

## Trabajo en clase

Resuelve las cuestiones que seleccione el docente y contrasta las respuestas en clase. No entregues un PDF ni un archivo separado. Esta ficha queda como banco de refuerzo; no es obligatorio completar todas las actividades.
