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

## P4 · Leer una captura de red

**Tiempo orientativo:** 90 min · Laboratorio de aula · Entrega individual.

### Preparación

Abre la captura de referencia incluida: no necesitas permisos de captura. Como alternativa, el docente puede autorizar una captura breve del tráfico propio en el laboratorio.

### Archivo de referencia incluido

[Descargar captura sintética de P4](../descargas/UD3_P4_captura_sintetica.pcap){ .md-button .md-button--primary }

Son 11 tramas sintéticas de ARP, DNS, ICMP y TCP, sin tráfico real. Utiliza MAC ficticias, la LAN `192.168.50.0/24`, `www.example.test` y `203.0.113.10`. El nombre y el destino son ejemplos reservados: se interpretan en el archivo y no se prueban en Internet.

La captura termina tras el establecimiento TCP: no incluye TLS ni contenido HTTP. Sus marcas temporales son sintéticas y solo sirven para ordenar los paquetes.

### Procedimiento

1. Abre el archivo con Wireshark. Identifica número de paquete, instante relativo, origen, destino, protocolo y resumen. Guarda una copia de trabajo con código de aula.
2. Aplica filtros de visualización, uno por vez:

    ```text
    arp
    icmp
    dns
    tcp.flags.syn == 1
    ```

    Son filtros para lo que ya se ha capturado; ocultar paquetes en pantalla no los elimina del archivo. La existencia de resultados depende del tráfico incluido.

3. Elige una trama ARP o ICMP de laboratorio y despliega Ethernet, IP y el protocolo superior disponible. Distingue MAC, IPv4 y datos de diagnóstico.
4. En un intercambio TCP facilitado, localiza SYN, SYN-ACK y ACK y compara puertos. Explica que otros paquetes ACK pueden aparecer durante toda la conexión.
5. Si hay DNS, identifica consulta y respuesta. Si no aparece, formula una explicación y pide la captura de referencia: caché, DNS cifrado o una consulta anterior pueden explicar la ausencia.
6. Contrasta la topología con la captura: una comunicación en la misma LAN usa la MAC del destino local; hacia otra red se envía al siguiente salto. No deduzcas toda la topología a partir de un único paquete.
7. Entrega únicamente los extractos solicitados y revisados. En HTTPS no se espera leer el contenido HTTP cifrado sin claves; no se solicita descifrarlo.

### Aceptación y entrega

Entrega tres paquetes comentados, tabla capa/campo/función y una explicación de ausencia de tráfico. Adjunta solo la captura de referencia o una captura de laboratorio autorizada y revisada.

**Entrega conjunta con la actividad 3.2:** incorpora esta práctica como anexo P4 del archivo `UD3_A2_Codigo.pdf`. Entrega actividad y práctica a la vez en la misma tarea de Aules. Incluye capturas legibles de los pasos y resultados solicitados, con una breve explicación, además de las tablas, cálculos y conclusiones exigidos. Si utilizas salidas facilitadas por el docente, identifícalas. No se requiere un PDF independiente de esta práctica. [Índice de prácticas](../practicas/index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)


## Entrega y valoración

**Entrega conjunta en Aules:** realiza también P4 e incorpora sus resultados como anexos al PDF de esta actividad. Entrega ambas partes a la vez en la misma tarea de Aules. Incluye capturas legibles de las acciones y comprobaciones solicitadas, comentadas brevemente, junto con las tablas y conclusiones de cada práctica.

Tabla y recorrido comentado. Capas: 3 puntos; encapsulación y siguiente salto: 4; interpretación de captura: 2; claridad: 1. La evidencia se completa con P4.

**Archivo:** `UD3_A2_Codigo.pdf`. [Índice de actividades](index.md) · [Cuaderno descargable](../descargas/UD3_Actividades.pdf)
