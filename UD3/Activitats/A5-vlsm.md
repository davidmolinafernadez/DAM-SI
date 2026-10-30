# Actividad 3.5 · Repartir direcciones con VLSM

**Tiempo orientativo:** 60 min · Individual · RA1/RA5 y documentación RA7.

## Encargo

Dispones de `192.168.40.0/24`. Debes alojar cuatro segmentos con 100, 50, 20 y 10 interfaces que necesitan dirección. Las cantidades ya incluyen las interfaces de puerta de enlace necesarias.

1. Ordena las necesidades de mayor a menor y elige el prefijo mínimo para cada una.
2. Asigna bloques alineados, contiguos si es posible, sin solaparse y dentro del /24.
3. Presenta red, máscara, rango útil, broadcast y direcciones disponibles no asignadas a ningún bloque.
4. Propón una dirección de puerta de enlace de cada segmento. Reservarla no crea encaminamiento por sí sola: indica qué elemento debe conectar las redes.
5. Explica qué tendría que cambiar si el departamento de 10 interfaces pasara a necesitar 18.
6. Compara el espacio consumido con cuatro subredes iguales capaces de alojar 100 interfaces. ¿Caben estas últimas en el /24?

## Entrega y valoración

Plan de direccionamiento. Capacidad y prefijos: 3 puntos; alineación y ausencia de solapes: 4; crecimiento y comparación: 2; claridad: 1. Debes poder explicar cómo verificaste los límites.

**Archivo:** `UD3_A5_Codigo.pdf`. [Índice de actividades](index.md) · [Cuaderno descargable](../descargas/UD3_Actividades.pdf)
