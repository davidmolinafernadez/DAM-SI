# Actividad 3.5 · Elegir un sistema de archivos

<div class="lesson-banner" markdown>
<div class="lesson-number">3.5</div>
<div markdown>
**Actividad escrita · Elegir un sistema de archivos**

Razonar, interpretar y justificar antes de ejecutar.
</div>
</div>

<div class="activity-meta" markdown>
<span>20 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

**Código: A5.** Actividad escrita con entrega propia.

**Teoría relacionada:** [Teoría 3.4: Sistemas de archivos y montaje](../b05-sistemas-de-archivos.md)

[Descargar actividad en PDF](descargas/Actividad_3_5_Apellidos_Nombre.pdf){ .md-button .md-button--primary }
[Original editable en texto](descargas/Actividad_3_5_Apellidos_Nombre.txt){ .md-button download }

Tiempo orientativo: 20 minutos. Modalidad: individual. Valoración formativa: 10 puntos.

## Antes de responder

Consulta la teoría relacionada antes de responder. Identifica qué información aporta el caso y qué datos faltan. Las soluciones no se deducen por repetir un nombre de herramienta: hay que explicar qué comprobaría y con qué resultado.

## Caso de trabajo

Hay cuatro destinos: raíz de Ubuntu, sistema de Windows, partición EFI y memoria de intercambio que guardará vídeos de 8 GiB. Debes justificar el formato según la función de cada destino.

## Cuestiones

1. Elige entre ext4, NTFS, FAT32 y exFAT para los cuatro destinos. Explica si hay condiciones de compatibilidad que comprobar.
2. Razona por qué tener 20 GiB libres no garantiza poder copiar un archivo de 8 GiB en cualquier formato.
3. Explica diferencia entre volumen, sistema de archivos y punto de montaje.
4. Un disco aparece en lsblk y no en df. Propón dos situaciones que lo expliquen sin concluir que la herramienta falla.

## Entrega de esta actividad

Tabla de decisiones y explicación de los dos listados. No hace falta instalar una herramienta de particionado. Guarda el archivo como `Actividad_3_5_Apellidos_Nombre.pdf`. Incluye las preguntas numeradas, razonamiento propio y fuentes concretas cuando consultes información adicional. No se pide añadir una portada vacía ni capturas de asistentes que no ejecutas.

## Revisión y valoración

| Criterio | Puntos |
| --- | ---: |
| Conceptos y datos interpretados correctamente | 4 |
| Justificación y relación entre causa y resultado | 3 |
| Tabla, esquema o propuesta solicitada | 2 |
| Claridad, fuentes y entrega | 1 |
