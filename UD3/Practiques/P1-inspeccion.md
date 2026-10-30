# P1 · Inventario de la conexión

**Tiempo orientativo:** 60 min · Laboratorio de aula · Entrega individual.

## Preparación

Utiliza un puesto autorizado. Esta práctica es de consulta: identifica la interfaz que usas sin cambiar su configuración. El docente facilitará salidas de ejemplo si no se dispone de permisos o de ambos sistemas.

## Procedimiento

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

## Aceptación y entrega

Entrega tabla Windows/Linux, cálculo de red, diagrama y una diferencia entre los datos observados. Usa identificadores de aula y oculta MAC, nombres o direcciones que identifiquen infraestructura real si el informe sale del entorno docente. No entregues listados completos de adaptadores ajenos al caso.

**Archivo:** `UD3_P1_Codigo.pdf`. [Índice de prácticas](index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)
