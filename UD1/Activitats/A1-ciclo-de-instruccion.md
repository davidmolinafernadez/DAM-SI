# A1 · Viaje de una instrucción

## Reto

Explica qué sucede en una CPU sencilla al ejecutar:

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
2. Señala cuándo se usan `MAR` y `MDR` y cuándo no.
3. Dibuja el recorrido de una instrucción con acceso a memoria.
4. Explica si se toma el salto y cuál será la siguiente dirección.
5. Diferencia instrucción, etapa de *pipeline* y ciclo de reloj.

## Entrega en Aules

PDF de 2–3 páginas, `A1_Apellidos_Nombre.pdf`, con tabla, diagrama propio y
explicación. No se acepta una captura sin interpretación.

## Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---:|
| Secuencia y PC | 3 |
| Registros y accesos a memoria | 3 |
| Diagrama | 2 |
| Explicación y vocabulario | 1,5 |
| Presentación y fuentes | 0,5 |
