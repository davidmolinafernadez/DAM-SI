# Actividad 3.2 · Seguir una petición

**Tiempo orientativo:** 45 min · Individual · RA1/RA5 y documentación RA7.

## Encargo

Un cliente `192.168.50.20/24` consulta una web situada fuera de su red. Su puerta de enlace es `192.168.50.1`. El nombre ya está resuelto; se estudia HTTPS sobre TCP.

1. Construye una tabla OSI / TCP-IP / función / unidad de datos / ejemplo.
2. Dibuja datos → segmento TCP → paquete IP → trama Ethernet. Añade los puertos, direcciones IP y MAC donde corresponda.
3. Explica por qué el primer destino MAC es la puerta de enlace y no el servidor remoto.
4. Compara un switch que conoce la MAC destino, un switch que todavía no la conoce y un hub. Indica qué ocurre con broadcast y con el unicast desconocido.
5. Explica qué cambia en el siguiente enlace tras un router. En este apartado se supone encaminamiento sin NAT; señala aparte qué puede cambiar si hay NAT.
6. Una captura no muestra DNS ni un establecimiento TCP nuevo. Formula dos hipótesis compatibles con cachés o conexiones reutilizadas. ¿Podría una petición HTTP/3 usar UDP?

## Entrega y valoración

Tabla y recorrido comentado. Capas: 3 puntos; encapsulación y siguiente salto: 4; interpretación de captura: 2; claridad: 1. La evidencia se completa con P4.

**Archivo:** `UD3_A2_Codigo.pdf`. [Índice de actividades](index.md) · [Cuaderno descargable](../descargas/UD3_Actividades.pdf)
