# 3. Representación de la información

## 3.1 Bits, bytes y palabras

Un bit representa dos estados. Con `n` bits pueden codificarse `2ⁿ` combinaciones. Un byte contiene ocho bits y puede representar 256 patrones.

Una palabra es la cantidad de bits que una arquitectura maneja de forma natural en determinadas operaciones. No debe confundirse directamente con el tamaño de un archivo o la capacidad máxima de RAM.

## 3.2 Sistemas posicionales

En base `b`, cada posición tiene peso `bⁿ`. El número `352₁₀` significa:

`3 × 10² + 5 × 10¹ + 2 × 10⁰`

En hexadecimal se utilizan `0–9` y `A–F`. Es compacto y se relaciona bien con el binario porque cada dígito hexadecimal representa cuatro bits.

| Hex | Binario | Decimal |
| ---: | :---: | ---: |
| 0 | 0000 | 0 |
| 7 | 0111 | 7 |
| A | 1010 | 10 |
| F | 1111 | 15 |

## 3.3 Conversión entre bases

### Binario a decimal

`101101₂ = 1×2⁵ + 0×2⁴ + 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 45₁₀`

### Decimal a binario

Se divide sucesivamente por dos y se leen los restos de abajo arriba:

| División | Cociente | Resto |
| --- | ---: | ---: |
| 45 ÷ 2 | 22 | 1 |
| 22 ÷ 2 | 11 | 0 |
| 11 ÷ 2 | 5 | 1 |
| 5 ÷ 2 | 2 | 1 |
| 2 ÷ 2 | 1 | 0 |
| 1 ÷ 2 | 0 | 1 |

Resultado: `101101₂`.

### Binario a hexadecimal

`1101 0110 0011₂ = D63₁₆`.

## 3.4 Operaciones binarias

Reglas de suma:

- `0 + 0 = 0`;
- `0 + 1 = 1`;
- `1 + 1 = 10`;
- `1 + 1 + 1 = 11`.

Ejemplo:

```text
  1011
+ 0110
------
 10001
```

`11 + 6 = 17`, por lo que el resultado es correcto.

## 3.5 Enteros con signo

El complemento a dos permite representar positivos y negativos y simplifica la aritmética.

Para representar `-5` con ocho bits:

1. `5 = 00000101`.
2. Invertir: `11111010`.
3. Sumar uno: `11111011`.

Con ocho bits, el rango es de `-128` a `127`. Sumar dos positivos puede producir un patrón con signo negativo: es un desbordamiento.

## 3.6 Reales y precisión

Los números en coma flotante se representan aproximadamente mediante signo, exponente y fracción. Muchos decimales, como `0,1`, no tienen representación binaria finita.

### Ejemplo para programación

En algunos lenguajes, `0.1 + 0.2` no resulta exactamente `0.3`. No es un fallo de la CPU: es una consecuencia de la representación finita. Para dinero se prefieren tipos decimales o enteros en la unidad mínima.

## 3.7 Texto y Unicode

ASCII asigna códigos a letras inglesas, dígitos y controles. Unicode define puntos de código para escrituras de todo el mundo. UTF-8 codifica cada punto con uno a cuatro bytes y conserva compatibilidad con ASCII.

La letra `A` es U+0041 y ocupa un byte en UTF-8. El carácter `€` es U+20AC y ocupa tres. Por eso “un carácter” no siempre equivale a un byte ni a una posición visual.

## 3.8 Imágenes y color

Una imagen raster se divide en píxeles. Con 24 bits de color suelen asignarse ocho bits a rojo, verde y azul. El color `#FF8000` contiene:

- rojo `FF₁₆ = 255`;
- verde `80₁₆ = 128`;
- azul `00₁₆ = 0`.

Una imagen sin comprimir de 1920 × 1080 píxeles y 24 bits requiere aproximadamente:

`1920 × 1080 × 3 = 6.220.800 bytes`, cerca de 5,93 MiB.

La compresión puede reducir mucho el tamaño. PNG suele ser sin pérdida; JPEG sacrifica información para lograr mayor reducción en fotografías.

## 3.9 Aplicaciones prácticas

- Las direcciones IPv4 se interpretan como 32 bits.
- Las máscaras y permisos usan operaciones lógicas.
- Los volcados de memoria se muestran en hexadecimal.
- Los colores web usan notación hexadecimal.
- Las sumas de comprobación se expresan como largas cadenas hexadecimales.

## Comprobación de comprensión

1. Convierte `173₁₀` a binario y hexadecimal.
2. Interpreta `11110110₂` como entero sin signo y como complemento a dos de ocho bits.
3. Calcula el tamaño sin comprimir de una imagen de 800 × 600 a 32 bits por píxel.
4. Explica por qué UTF-8 no permite asumir un byte por carácter.
