# P3 · Distinguir DHCP, puerta y DNS

**Tiempo orientativo:** 90 min · Laboratorio de aula · Entrega individual.

## Preparación

Usa un segmento de aula con DHCP y DNS gestionados por el docente, o sus registros de ejemplo. No se instala ni activa un servidor DHCP del alumnado en la LAN del centro. Si el entorno no permite cambios, realiza el diagnóstico con salidas proporcionadas.

## Procedimiento

1. Identifica la interfaz autorizada. Registra si obtiene dirección automáticamente, el prefijo, puerta y servidores DNS. En Windows consulta `ipconfig /all`; en Linux, los datos de la conexión activa y `ip route`.
2. En los datos proporcionados por el docente identifica concesión y servidor DHCP. Explica qué ofrece DHCP y qué hace DNS. No supongas que el servidor DHCP y el router son siempre el mismo equipo.
3. Consulta un nombre indicado por el docente:

    ```powershell
    Resolve-DnsName example.com
    Test-NetConnection example.com -Port 443
    ```

    En Linux, usa `resolvectl query example.com` y, si está disponible, `curl -I https://example.com/`. Si el laboratorio no tiene salida, utiliza el nombre y servicio internos proporcionados.

4. Compara tres juegos de salidas: dirección de enlace local sin concesión útil; dirección válida con puerta de enlace incorrecta; resolución DNS fallida con un servicio local accesible por IP. Identifica qué funciona y qué falta por probar en cada uno.
5. Dibuja Discover → Offer → Request → Acknowledge como intercambio inicial habitual de DHCPv4. Explica por qué una renovación no tiene que mostrar todas esas fases.
6. Verifica que el estado final de la conexión coincide con el inicial. No ejecutes liberaciones de dirección sobre conexiones remotas o de gestión.

## Aceptación y entrega

Tabla separada de parámetros DHCP, encaminamiento y DNS; evidencia de resolución y de servicio; diagnóstico de los tres casos y sus límites. No interpretes un ping fallido como prueba suficiente de fallo DNS.

**Archivo:** `UD3_P3_Codigo.pdf`. [Índice de prácticas](index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)
