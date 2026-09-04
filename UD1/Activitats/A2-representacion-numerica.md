# T1-B · Laboratorio de representación numérica

<div class="activity-meta" markdown>
<span>55 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

## Misión

Una aplicación de monitorización recibe valores en distintas bases y unidades.
Debes normalizarlos y detectar dos mensajes técnicamente engañosos.

## Parte A · Conversiones

Muestra el procedimiento, no solo el resultado.

1. `11010110₂` a decimal y hexadecimal.
2. `375₁₀` a binario y hexadecimal.
3. `7B₁₆` a binario y decimal.
4. `10110101₂ + 00101110₂` en binario y decimal.
5. Representa `-37` en complemento a dos de 8 bits y verifica el resultado.

## Parte B · Capacidad y transferencia

1. Un SSD anuncia `1 TB`. Calcula cuántos GiB representa aproximadamente.
2. Una red negocia a `1 Gb/s`. Calcula el máximo teórico en MB/s.
3. Un archivo de `4,7 GiB` se copia a `80 MiB/s`. Estima el tiempo y explica por
   qué el valor real puede ser mayor.

## Parte C · Código y precisión

Este programa produce un resultado sorprendente:

```python
resultado = 0.1 + 0.2
print(resultado == 0.3)
```

Explica la causa y propone una comparación con tolerancia o una representación
decimal apropiada para cantidades monetarias.

## Entrega

PDF de 2–3 páginas, `T1B_Apellidos_Nombre.pdf`, con operaciones ordenadas y una
conclusión de cinco líneas.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Conversiones y procedimientos | 4 |
| Unidades y estimaciones | 3 |
| Explicación de precisión | 2 |
| Presentación y comprobación | 1 |
