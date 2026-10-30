# Actividad 3.1 · Comprender una red

**Tiempo orientativo:** 45 min · Individual · RA1/RA5 y documentación RA7.

## Encargo

Un aula tiene 20 equipos conectados a un switch, una impresora, un punto de acceso y un router de salida. Una persona afirma: «Si falla Internet, todos los equipos dejan de poder comunicarse».

1. Dibuja los elementos y sus conexiones. Diferencia equipo final, medio y dispositivo de interconexión.
2. Clasifica la red por alcance, medio, relación funcional y topología. Justifica cada clasificación: una red puede pertenecer a varias categorías a la vez.
3. Identifica emisor, receptor, mensaje, canal y protocolo en una impresión en red.
4. Explica qué podría seguir funcionando si se desconecta únicamente el enlace del router hacia el proveedor.
5. Compara el fallo de un cable de puesto con el fallo del switch central. No presupongas redundancia.
6. Distingue 100 Mbit/s de 100 MB/s y calcula el mínimo teórico para transmitir 1 GiB por 100 Mbit/s. Señala por qué una transferencia real tarda más.

## P1 · Inventario de la conexión

**Tiempo orientativo:** 60 min · Laboratorio de aula · Entrega individual.

### Preparación

Utiliza un puesto autorizado. Esta práctica es de consulta: identifica la interfaz que usas sin cambiar su configuración. El docente facilitará salidas de ejemplo si no se dispone de permisos o de ambos sistemas.

### Procedimiento

1. Dibuja puesto → toma o Wi-Fi → switch/punto de acceso → router. Indica qué conexiones conoces por observación y cuáles requieren confirmación.
2. En Windows abre Configuración → Red e Internet → Ethernet o Wi-Fi → propiedades de la conexión. Registra dirección IPv4, prefijo o máscara, puerta de enlace y DNS. Comprueba la asignación IP automática o manual sin pulsar Guardar.
3. Contrasta con PowerShell:

    ```powershell
    Get-NetIPConfiguration
    Get-NetAdapter
    Get-NetIPAddress -AddressFamily IPv4
    Get-DnsClientServerAddress -AddressFamily IPv4
    Get-NetRoute -AddressFamily IPv4
    ```

4. En Linux abre la configuración de la conexión activa y compara con:

    ```bash
    ip -br link
    ip -br address
    ip route
    resolvectl status
    ```

    `resolvectl` depende de que el sistema use systemd-resolved. Si no existe, utiliza la información DNS de la conexión del escritorio o la salida facilitada por el docente. No instales herramientas durante la práctica sin indicación.

5. Calcula la red de la interfaz activa y comprueba si la puerta de enlace es alcanzable directamente según el prefijo. Distingue la ruta conectada de la ruta por defecto.

### Aceptación y entrega

Entrega tabla Windows/Linux, cálculo de red, diagrama y una diferencia entre los datos observados. Usa identificadores de aula y oculta MAC, nombres o direcciones que identifiquen infraestructura real si el informe sale del entorno docente. No entregues listados completos de adaptadores ajenos al caso.

**Entrega conjunta con la actividad 3.1:** incorpora esta práctica como anexo P1 del archivo `UD3_A1_Codigo.pdf`. Entrega actividad y práctica a la vez en la misma tarea de Aules. Incluye capturas legibles de los pasos y resultados solicitados, con una breve explicación, además de las tablas, cálculos y conclusiones exigidos. Si utilizas salidas facilitadas por el docente, identifícalas. No se requiere un PDF independiente de esta práctica. [Índice de prácticas](../practicas/index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)

## Entrega y valoración

**Entrega conjunta en Aules:** realiza también P1 e incorpora sus resultados como anexos al PDF de esta actividad. Entrega ambas partes a la vez en la misma tarea de Aules. Incluye capturas legibles de las acciones y comprobaciones solicitadas, comentadas brevemente, junto con las tablas y conclusiones de cada práctica.

Esquema y explicación individual. Componentes y clasificación: 4 puntos; razonamiento de los dos fallos: 3; cálculo con unidades: 2; claridad: 1. La evidencia se completa con P1.

**Archivo:** `UD3_A1_Codigo.pdf`. [Índice de actividades](index.md) · [Cuaderno descargable](../descargas/UD3_Actividades.pdf)
