# A1.1 · Viaje de una instrucción

<div class="activity-meta" markdown>
<span>55 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

## Programa simulado

```text
Dirección  Instrucción
100        LOAD R1, [500]
104        ADD  R1, R2
108        STORE [504], R1
112        JZ   200
```

Estado inicial: `PC=100`, memoria `[500]=7`, `R2=-7` y bandera `Z=0`.

## Trabajo

1. Completa por instrucción: `PC inicial`, búsqueda, decodificación, ejecución,
   escritura, `PC final` y banderas.
2. Señala cuándo intervienen `MAR` y `MDR` y cuándo no.
3. Dibuja el recorrido de una instrucción con acceso a memoria.
4. Explica si se toma el salto y cuál será la dirección siguiente.
5. Diferencia instrucción, etapa de *pipeline* y ciclo de reloj.

## Entrega

PDF de 2–3 páginas, `A11_Apellidos_Nombre.pdf`, con tabla, diagrama propio y
explicación. Una captura sin interpretación no sirve como evidencia.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Secuencia y PC | 3 |
| Registros y accesos a memoria | 3 |
| Diagrama | 2 |
| Explicación técnica | 1,5 |
| Presentación | 0,5 |
