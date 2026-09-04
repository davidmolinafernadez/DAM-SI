# Tarea 1.2 · Representación numérica y unidades

<div class="activity-meta" markdown>
<span>55 min de aula + finalización</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

## Situación

Una aplicación de diagnóstico recibe direcciones, máscaras, tamaños y
velocidades en formatos diferentes. Debes normalizar los datos, mostrar el
procedimiento y detectar resultados imposibles. La calculadora puede utilizarse
únicamente al final para comprobar.

## Reglas de trabajo

1. Escribe todas las operaciones y unidades.
2. En conversiones, muestra potencias, divisiones o agrupaciones de bits.
3. Comprueba cada resultado mediante una conversión inversa.
4. Redondea a dos decimales cuando sea necesario.
5. Señala cualquier desbordamiento en lugar de ocultarlo.

## Parte A · Binario, decimal y hexadecimal

Convierte cada valor a las otras dos bases.

| Ejercicio | Valor inicial | Binario | Decimal | Hexadecimal |
|---:|---|---|---:|---|
| 1 | `10101101₂` |  |  |  |
| 2 | `111100001010₂` |  |  |  |
| 3 | `10000001₂` |  |  |  |
| 4 | `375₁₀` |  |  |  |
| 5 | `1023₁₀` |  |  |  |
| 6 | `2026₁₀` |  |  |  |
| 7 | `7B₁₆` |  |  |  |
| 8 | `A5F₁₆` |  |  |  |
| 9 | `10E₁₆` |  |  |  |

## Parte B · Operaciones binarias

Resuelve en binario y verifica en decimal.

1. `10110101₂ + 00101110₂`
2. `11101101₂ - 01011110₂`
3. `00110110₂ × 00000101₂`
4. `11011000₂ ÷ 00000100₂`
5. Aplica `AND`, `OR` y `XOR` a `11001010₂` y `10110100₂`.
6. Desplaza `00110111₂` dos posiciones a la izquierda y una a la derecha.
   Explica la relación con multiplicar o dividir por potencias de dos.

## Parte C · Enteros con signo y desbordamiento

Trabaja con complemento a dos de 8 bits.

1. Representa `-37`, `-85` y `-128`.
2. Recupera el valor decimal de `11100110₂` y `10000001₂`.
3. Calcula `01100100₂ + 00111100₂`. ¿Es correcto como entero con signo?
4. Calcula `10011100₂ + 11110000₂` e interpreta el resultado.
5. Indica el rango representable con 8, 16 y 32 bits con signo.

## Parte D · Capacidad y velocidad

1. Un SSD anuncia `1 TB`. Convierte su capacidad aproximada a GiB.
2. Una red negocia a `1 Gb/s`. Calcula el máximo teórico en MB/s.
3. Un archivo de `4,7 GiB` se copia a `80 MiB/s`. Estima el tiempo.
4. Una imagen de `3840 × 2160` usa 24 bits por píxel. Calcula el tamaño sin
   compresión en MiB.
5. Un audio estéreo se muestrea a 48 kHz y 24 bits durante 3 minutos. Calcula
   el tamaño sin compresión.
6. Una copia contiene 275 archivos de 18 MiB y 40 archivos de 1,2 GiB. Calcula
   el total en GiB y el tiempo teórico a 110 MB/s.
7. Explica tres motivos por los que una transferencia real tarda más.

## Parte E · Aplicación a programación

### Precisión decimal

```python
resultado = 0.1 + 0.2
print(resultado)
print(resultado == 0.3)
```

Explica la salida y propone:

- una comparación con tolerancia;
- una representación adecuada para cantidades monetarias.

### Máscaras de bits

Un byte de permisos usa: bit 0 lectura, bit 1 escritura, bit 2 ejecución y bit 3
administración.

1. Interpreta `00001011₂`.
2. Construye el valor para lectura + ejecución.
3. Activa escritura sobre `00001001₂` usando `OR`.
4. Desactiva administración usando `AND` y una máscara apropiada.

## Reto final

Una aplicación muestra: «Descarga de 6 GB completada en 40 segundos mediante
una conexión de 1 Gb/s; velocidad media: 150 MB/s».

Decide si las tres cifras pueden ser simultáneamente ciertas. Presenta cálculo,
supuestos y una explicación comprensible para una persona no técnica.

## Entrega en Aules

- Archivo: `Tarea_1_2_Apellidos_Nombre.pdf`.
- Extensión orientativa: 6–9 páginas.
- Incluye portada breve, operaciones, comprobaciones y conclusión.
- No se acepta una hoja de resultados sin procedimiento.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Conversiones y comprobaciones | 2,5 |
| Operaciones binarias | 2 |
| Signo y desbordamiento | 1,5 |
| Capacidad, velocidad y unidades | 2 |
| Programación, máscaras y reto final | 1,5 |
| Orden, notación y presentación | 0,5 |
