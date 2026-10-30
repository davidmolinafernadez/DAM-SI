# Actividad 3.6 · Justificar una configuración

**Tiempo orientativo:** 60 min · Individual · RA1/RA5 y documentación RA7.

## Encargo

Se propone para un laboratorio: equipo A `192.168.50.10/24`, equipo B `192.168.50.20/24` y puerta de enlace `192.168.60.1`. El segmento tiene un servidor DHCP autorizado, pero una interfaz obtiene `169.254.15.8/16`.

1. Localiza la incoherencia de la puerta de enlace y propón una corrección compatible con la topología. Indica qué información debes confirmar antes de aplicarla.
2. Explica por qué A y B pueden comunicarse localmente sin salida a Internet y qué pruebas lo demostrarían.
3. Para la interfaz con dirección de enlace local, formula dos causas posibles y una comprobación de cada una. No atribuyas automáticamente todo al servidor DHCP.
4. El DNS devuelve una dirección, pero el servidor no responde a ping. ¿Qué prueba de servicio harías antes de afirmar que DNS falla?
5. Relaciona tres encargos con NAT, puente o red interna: invitado que necesita descargar actualizaciones, invitado que debe aparecer como equipo de la LAN autorizada y dos invitados que solo deben hablar entre sí. Explica los límites del NAT sencillo para comunicar invitados.
6. Diseña un registro síntoma → hipótesis → prueba → resultado → cambio autorizado → verificación → restauración.

## P2 · Conectar dos equipos de laboratorio

**Tiempo orientativo:** 120 min · Laboratorio de aula · Entrega individual.

### Preparación

El docente proporciona dos equipos o dos entornos ya preparados y una red de laboratorio aislada. No se crea todavía ninguna máquina virtual. Confirma la interfaz de laboratorio; no se modifica la conexión de gestión, la del centro ni una sesión remota.

Topología: A `192.168.50.10/24` — switch aislado — B `192.168.50.20/24`. En este caso no hay router, DHCP ni salida a Internet: puerta de enlace y DNS se dejan vacíos. Las direcciones se emplean únicamente en el segmento de prueba autorizado.

### Procedimiento

1. Antes de cambiar nada, registra modo de asignación, dirección, máscara, puerta, DNS e interfaz seleccionada. Prepara cómo restaurarlo.
2. Predice si A y B están en la misma red y explica por qué DNS no interviene al usar direcciones IP.
3. En Windows: Configuración → Red e Internet → conexión de laboratorio → Asignación IP → Editar → Manual → IPv4. Introduce dirección y prefijo 24; si solicita máscara, usa `255.255.255.0`. Conserva IPv6 y los demás ajustes ajenos al ejercicio.
4. En Ubuntu Desktop: Configuración → Red → rueda de la conexión de laboratorio → IPv4 → Manual. Introduce dirección y máscara; guarda y vuelve a activar solo esa conexión si la interfaz lo requiere. Los nombres de menú pueden variar.
5. Consulta de nuevo la configuración mediante los comandos de P1. Comprueba enlace y prueba la dirección propia y después la del compañero:

    ```powershell
    Test-Connection 192.168.50.20 -Count 4
    Get-NetNeighbor -AddressFamily IPv4
    ```

    ```bash
    ping -c 4 192.168.50.10
    ip neigh
    ```

    Adapta el destino al equipo desde el que pruebas. Si ICMP está filtrado, pide una prueba o regla limitada preparada por el docente; no desactives el firewall. La observación de vecinos ayuda a distinguir alcance local de respuesta ICMP.

6. Con autorización, cambia únicamente B a `192.168.60.20/24`. Predice y comprueba el resultado sin inventar un router entre ambas subredes. Devuelve B a su dirección inicial.
7. Restaura al terminar el estado previo registrado, incluido el modo automático si existía, y confirma que recuperas la conexión esperada.

### Aceptación y entrega

Entrega una tabla antes/durante/después, pruebas en ambos sentidos, una incidencia interpretada y confirmación de restauración. La ausencia de Internet es el resultado previsto en este laboratorio aislado.

**Entrega conjunta con la actividad 3.6:** incorpora esta práctica como anexo P2 del archivo `UD3_A6_Codigo.pdf`. Entrega actividad y práctica a la vez en la misma tarea de Aules. Incluye capturas legibles de los pasos y resultados solicitados, con una breve explicación, además de las tablas, cálculos y conclusiones exigidos. Si utilizas salidas facilitadas por el docente, identifícalas. No se requiere un PDF independiente de esta práctica. [Índice de prácticas](../practicas/index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)


## P3 · Distinguir DHCP, puerta y DNS

**Tiempo orientativo:** 90 min · Laboratorio de aula · Entrega individual.

### Preparación

Usa un segmento de aula con DHCP y DNS gestionados por el docente, o sus registros de ejemplo. No se instala ni activa un servidor DHCP del alumnado en la LAN del centro. Si el entorno no permite cambios, realiza el diagnóstico con salidas proporcionadas.

### Procedimiento

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

### Aceptación y entrega

Tabla separada de parámetros DHCP, encaminamiento y DNS; evidencia de resolución y de servicio; diagnóstico de los tres casos y sus límites. No interpretes un ping fallido como prueba suficiente de fallo DNS.

**Entrega conjunta con la actividad 3.6:** incorpora esta práctica como anexo P3 del archivo `UD3_A6_Codigo.pdf`. Entrega actividad y práctica a la vez en la misma tarea de Aules. Incluye capturas legibles de los pasos y resultados solicitados, con una breve explicación, además de las tablas, cálculos y conclusiones exigidos. Si utilizas salidas facilitadas por el docente, identifícalas. No se requiere un PDF independiente de esta práctica. [Índice de prácticas](../practicas/index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)


## P5 · Diagnosticar y preparar el salto a UD4

**Tiempo orientativo:** 120 min · Laboratorio de aula · Entrega individual.

### Preparación

Trabaja con los equipos de prueba de P2 o con las salidas preparadas por el docente. Las averías se introducen únicamente en esa interfaz y se restauran antes de pasar al siguiente caso. No se modifica el router ni el firewall del centro.

### Método y casos

Para cada caso escribe predicción, síntoma, dos hipótesis, prueba que las diferencia, resultado, corrección propuesta y verificación. Se observa de abajo arriba: enlace → dirección y prefijo → red local → ruta → DNS → puerto → aplicación.

| Caso preparado | Qué debes averiguar |
| --- | --- |
| Sin enlace o interfaz de prueba desconectada | Si tiene sentido empezar consultando DNS |
| Dos equipos con prefijos incoherentes | Si el destino se considera local o requiere una ruta |
| Puerta de enlace fuera de la red conectada | Qué destino falla y cuál todavía puede funcionar |
| DNS incorrecto con conectividad IP demostrada | Qué prueba distingue resolución de acceso a servicio |
| Servicio que no responde a ping pero sí al puerto previsto | Por qué ICMP no determina la disponibilidad de la aplicación |

1. Utiliza solo comandos de consulta de P1 y pruebas puntuales al destino autorizado. No ejecutes barridos de direcciones.
2. Solicita al docente una demostración preparada de NAT, puente y red interna o sus esquemas. No es necesario instalar VirtualBox en esta unidad.
3. Para cada modo, indica quién puede hablar con quién, si hay salida y qué depende de DHCP, router o reenvío de puertos. Distingue NAT sencillo por invitado de una red NAT compartida.
4. Diseña el plan que reutilizarás en UD4: interfaces, direcciones, prefijos, servicio previsto y prueba de aceptación. No confundas conectar un adaptador virtual con haber configurado correctamente TCP/IP.
5. Restaura el laboratorio y repite la prueba que demostraba el funcionamiento inicial.

### Aceptación y entrega

Cinco fichas de incidencia, esquema comparado de modos y plan de laboratorio de UD4. Se valora la prueba que justifica el diagnóstico y el estado restaurado, además del resultado final.

**Entrega conjunta con la actividad 3.6:** incorpora esta práctica como anexo P5 del archivo `UD3_A6_Codigo.pdf`. Entrega actividad y práctica a la vez en la misma tarea de Aules. Incluye capturas legibles de los pasos y resultados solicitados, con una breve explicación, además de las tablas, cálculos y conclusiones exigidos. Si utilizas salidas facilitadas por el docente, identifícalas. No se requiere un PDF independiente de esta práctica. [Índice de prácticas](../practicas/index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)


## Entrega y valoración

**Entrega conjunta en Aules:** realiza también P2, P3 y P5 e incorpora sus resultados como anexos al PDF de esta actividad. Entrega ambas partes a la vez en la misma tarea de Aules. Incluye capturas legibles de las acciones y comprobaciones solicitadas, comentadas brevemente, junto con las tablas y conclusiones de cada práctica.

Informe con decisiones y pruebas. Diagnóstico: 4 puntos; elección de redes virtuales: 3; comprobación y restauración: 2; claridad: 1. Se completa con P2, P3 y P5; no requiere crear máquinas virtuales antes de UD4.

**Archivo:** `UD3_A6_Codigo.pdf`. [Índice de actividades](index.md) · [Cuaderno descargable](../descargas/UD3_Actividades.pdf)
