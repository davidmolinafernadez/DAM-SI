# Actividad 3.4 · Diseñar subredes iguales

**Tiempo orientativo:** 90 min · Individual · RA1/RA5 y documentación RA7.

## Encargo

Para cada caso indica red base con prefijo, necesidad, bits tomados, prefijo nuevo, máscara, subredes disponibles y hosts ordinarios por subred. Después presenta las tablas solicitadas.

1. Divide `192.168.20.0/24` en cuatro subredes iguales. Presenta todas.
2. Desde `172.16.0.0/16`, obtén 64 subredes iguales. Presenta las dos primeras y la última; explica cómo obtener las restantes sin enumerarlas.
3. Desde `10.0.0.0/8`, obtén 32 subredes iguales. Presenta las dos primeras y la última.
4. Una empresa necesita al menos seis subredes y al menos 25 hosts por subred dentro de `192.168.1.0/24`. ¿Cuántas subredes produce realmente la máscara elegida? Presenta las ocho y diferencia disponibles, utilizadas y libres.
5. Desde `172.30.0.0/16`, crea subredes que admitan al menos 100 hosts ordinarios. Calcula cuántas caben y muestra las dos primeras.
6. Dentro de `172.23.0.0/16` se requieren ocho subredes, cada una capaz de alojar entre 2000 y 3000 equipos previstos. Reserva capacidad para 3000 hosts por subred. Calcula prefijo, subredes disponibles y subredes libres tras asignar ocho.
7. Corrige el enunciado «Dada la red 192.168.0.0/24, ¿cuántas subredes se pueden crear?». Explica qué dato falta para que tenga una respuesta única.

## Entrega y valoración

Cada fila de tabla incluirá red/prefijo, primer host, último host, broadcast y capacidad. Diseño y comprobación de requisitos: 4 puntos; tablas: 4; explicación de ambigüedades: 2. No se descartan las subredes cero y de todos unos: el número se calcula con 2 elevado a los bits tomados.

**Archivo:** `UD3_A4_Codigo.pdf`. [Índice de actividades](index.md) · [Cuaderno descargable](../descargas/UD3_Actividades.pdf)
