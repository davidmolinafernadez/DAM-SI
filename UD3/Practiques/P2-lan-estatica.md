# P2 · Conectar dos equipos de laboratorio

**Tiempo orientativo:** 120 min · Laboratorio de aula · Entrega individual.

## Preparación

El docente proporciona dos equipos o dos entornos ya preparados y una red de laboratorio aislada. No se crea todavía ninguna máquina virtual. Confirma la interfaz de laboratorio; no se modifica la conexión de gestión, la del centro ni una sesión remota.

Topología: A `192.168.50.10/24` — switch aislado — B `192.168.50.20/24`. En este caso no hay router, DHCP ni salida a Internet: puerta de enlace y DNS se dejan vacíos. Las direcciones se emplean únicamente en el segmento de prueba autorizado.

## Procedimiento

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

## Aceptación y entrega

Entrega una tabla antes/durante/después, pruebas en ambos sentidos, una incidencia interpretada y confirmación de restauración. La ausencia de Internet es el resultado previsto en este laboratorio aislado.

**Archivo:** `UD3_P2_Codigo.pdf`. [Índice de prácticas](index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)
