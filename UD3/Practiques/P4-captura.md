# P4 · Leer una captura de red

**Tiempo orientativo:** 90 min · Laboratorio de aula · Entrega individual.

## Preparación

Abre la captura de referencia incluida: no necesitas permisos de captura. Como alternativa, el docente puede autorizar una captura breve del tráfico propio en el laboratorio.

## Archivo de referencia incluido

[Descargar captura sintética de P4](../descargas/UD3_P4_captura_sintetica.pcap){ .md-button .md-button--primary }

Son 11 tramas sintéticas de ARP, DNS, ICMP y TCP, sin tráfico real. Utiliza MAC ficticias, la LAN `192.168.50.0/24`, `www.example.test` y `203.0.113.10`. El nombre y el destino son ejemplos reservados: se interpretan en el archivo y no se prueban en Internet.

La captura termina tras el establecimiento TCP: no incluye TLS ni contenido HTTP. Sus marcas temporales son sintéticas y solo sirven para ordenar los paquetes.

## Procedimiento

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

## Aceptación y entrega

Entrega tres paquetes comentados, tabla capa/campo/función y una explicación de ausencia de tráfico. Adjunta solo la captura de referencia o una captura de laboratorio autorizada y revisada.

**Archivo:** `UD3_P4_Codigo.pdf`. [Índice de prácticas](index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)
