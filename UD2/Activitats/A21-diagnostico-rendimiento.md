# Tarea 2.1.1 · Diagnóstico de rendimiento

<div class="lesson-banner" markdown>
<div class="lesson-number">2.1.1</div>
<div markdown>
**Reto técnico**

Analiza un síntoma de lentitud y distingue entre CPU, memoria, disco y procesos.
</div>
</div>

<div class="activity-meta" markdown>
<span>50 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

## Producto final

Informe PDF llamado `Tarea_2_1_1_Apellidos_Nombre.pdf`.

## Escenario

Un equipo tarda en cambiar entre aplicaciones. El usuario afirma: “el procesador
está mal porque todo va lento”. Durante la observación se detecta:

| Indicador | Valor |
|---|---:|
| CPU media | 18 % |
| RAM usada | 94 % |
| Disco | 100 % durante varios minutos |
| Red | 2 % |
| Proceso con más memoria | Navegador |
| Espacio libre en SSD | 11 GB |

## Fase 1 · Hipótesis

Explica por qué la CPU no parece el cuello de botella principal. Formula dos
hipótesis: una relacionada con memoria/paginación y otra con almacenamiento.

## Fase 2 · Plan de diagnóstico

Propón una secuencia de 6 pasos. Para cada paso indica herramienta, dato que
mirarías y qué conclusión permitiría sacar.

| Paso | Herramienta | Dato | Conclusión posible |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

## Fase 3 · Medidas correctoras

Clasifica medidas inmediatas, de configuración y de ampliación:

- cerrar o sustituir aplicaciones;
- revisar inicio automático;
- liberar espacio;
- comprobar salud del disco;
- ampliar RAM;
- reinstalar solo si hay evidencia.

Justifica cuáles aplicarías primero y cuáles dejarías para el final.

## Evidencias mínimas

Tu informe debe dejar claro:

- por qué la CPU no es la primera sospecha;
- qué datos apuntan a memoria, paginación o almacenamiento;
- qué seis comprobaciones harías y en qué orden;
- qué medidas son reversibles y cuáles implican coste o riesgo;
- qué información faltaría antes de comprar hardware o reinstalar.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Hipótesis coherentes | 2 |
| Plan de diagnóstico ordenado | 3 |
| Interpretación de memoria virtual y E/S | 2 |
| Medidas correctoras proporcionadas | 2 |
| Claridad y vocabulario | 1 |
