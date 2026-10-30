# Actividad 3.3 · Leer direcciones IPv4

**Tiempo orientativo:** 60 min · Individual · RA1/RA5 y documentación RA7.

## Encargo

En cada caso calcula máscara decimal, dirección de red, broadcast, primer y último host ordinario y número de hosts. Muestra al menos una operación AND en binario y otra solución por tamaño de bloque.

| Caso | Dirección de interfaz |
| --- | --- |
| A | 192.168.5.100/25 |
| B | 192.168.100.25/30 |
| C | 192.168.100.37/28 |
| D | 192.168.37.99/26 |
| E | 192.168.192.10/29 |
| F | 172.30.1.33/16 |
| G | 10.13.124.32/11 |
| H | 192.168.3.25/21 |

1. Explica por qué `192.168.3.25` sin máscara no permite determinar una única red.
2. Clasifica como privada RFC 1918, loopback o enlace local: `10.2.3.4`, `172.22.156.32`, `172.32.1.5`, `192.168.1.55`, `127.0.0.1` y `169.254.10.20`. Que una dirección no pertenezca a esas tres categorías no demuestra por sí solo que sea asignable públicamente.
3. Corrige: «La máscara de /21 es 255.255.31.0». Comprueba que una máscara tiene unos contiguos seguidos de ceros.
4. Compara `191.168.1.55/24` con `192.168.1.55/24`. No corrijas una dirección cambiando dígitos sin justificarlo.

## Entrega y valoración

Tabla de resultados y procedimientos. Cálculos: 6 puntos; métodos y unidades: 2; razonamiento de casos especiales: 2. Las clases A/B/C solo se comparan como contexto histórico; se utiliza siempre el prefijo explícito.

**Archivo:** `UD3_A3_Codigo.pdf`. [Índice de actividades](index.md) · [Cuaderno descargable](../descargas/UD3_Actividades.pdf)
