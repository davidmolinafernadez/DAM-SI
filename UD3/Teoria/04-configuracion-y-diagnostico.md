# 3.5 · Configuración y diagnóstico

## 3.5.1 Parámetros

Una interfaz necesita IP/prefijo. Para salir de la subred usa puerta de enlace. Para nombres usa DNS. DHCP puede proporcionar todo.

```mermaid
flowchart LR
    PC["192.168.1.50/24"] --> SW["Switch"] --> GW["192.168.1.1 Router"] --> NET["Internet"]
    PC --> DNS["Servidor DNS"]
```

La puerta debe pertenecer a una red directamente conectada; de lo contrario el equipo no sabe cómo alcanzarla.

## 3.5.2 Inspección

Linux:

```bash
ip -br address
ip route
resolvectl status
ip neigh
ss -tulpen
```

Windows:

```powershell
Get-NetIPConfiguration
Get-NetRoute -AddressFamily IPv4
Get-DnsClientServerAddress
Get-NetNeighbor
Get-NetTCPConnection -State Listen
```

## 3.5.3 Diagnóstico por escalones

```mermaid
flowchart TD
    PHY["1 Enlace físico/Wi-Fi"] --> IP["2 IP y máscara"]
    IP --> LOCAL["3 Pila y red local"]
    LOCAL --> GW["4 Puerta de enlace"]
    GW --> ROUTE["5 IP remota"]
    ROUTE --> DNS["6 DNS"]
    DNS --> PORT["7 Puerto/servicio"]
    PORT --> APP["8 Aplicación"]
```

No se empieza reinstalando. Se localiza la primera prueba que falla.

## 3.5.4 Herramientas

```bash
ping -c 4 127.0.0.1
ping -c 4 192.168.1.1
tracepath example.com
dig example.com
curl -v https://example.com/
nc -vz example.com 443
```

```powershell
Test-Connection 192.168.1.1 -Count 4
tracert example.com
Resolve-DnsName example.com
Test-NetConnection example.com -Port 443
```

## 3.5.5 Interpretación

- Sin enlace: cable, puerto, adaptador, Wi-Fi o controlador.
- `169.254.x.x`: dirección de enlace local; puede indicar autoconfiguración por falta de respuesta DHCP, aunque también puede haberse configurado expresamente.
- Gateway responde, IP remota no: ruta, proveedor o filtrado.
- IP remota responde, nombre no: DNS.
- Nombre resuelve y ping funciona, puerto no: servicio o firewall.
- Puerto abre, aplicación falla: protocolo, TLS, autenticación o aplicación.

Son pistas para formular hipótesis. Un equipo puede filtrar ICMP y servir HTTPS
correctamente; por tanto, un `ping` fallido no demuestra que esté apagado ni
que la ruta esté rota. Si un nombre resuelve pero no responde al ping, comprueba
el puerto y la aplicación antes de atribuir el fallo a DNS.

## 3.5.6 Captura

Wireshark permite ver tramas. Se captura con autorización y filtro mínimo. Ejemplo de un acceso web:

1. ARP para localizar gateway.
2. DNS para resolver nombre.
3. SYN/SYN-ACK/ACK a 443.
4. negociación TLS.
5. intercambio HTTP cifrado.

Este recorrido supone una conexión nueva, IPv4 y HTTPS sobre TCP. Las cachés
pueden evitar ARP o DNS visibles, y HTTP/3 utiliza QUIC sobre UDP. Una captura
no tiene por qué mostrar todas esas fases en cada petición.

La captura puede contener datos sensibles. Se limita, anonimiza y no se publica sin revisar.

## Caso completo

Un PC accede por IP pero no por nombre. `Get-NetIPConfiguration` muestra DNS antiguo. `Resolve-DnsName` agota tiempo. Se configura el DNS correcto mediante DHCP, se renueva concesión, se limpia caché y se verifica. Cambiar navegador no habría corregido la capa afectada.

## Documentación de incidencia

Registrar síntoma, alcance, topología, hora, comandos y salidas relevantes, hipótesis, cambio, resultado y prevención. Una captura sin explicación no es una memoria técnica.

## Del ajuste gráfico a la evidencia

Antes de guardar cambios, identifica interfaz y perfil. Registra si el origen es DHCP o manual; cambiar a manual sin recordar puerta y DNS puede interrumpir la conexión. Usa una interfaz de laboratorio y conserva el plan de restauración. En Windows puedes consultar Configuración → Red e Internet → propiedades de la conexión; en Ubuntu Desktop, Configuración → Red → opciones de la conexión → IPv4.

Una LAN aislada entre dos equipos del mismo prefijo puede funcionar sin puerta ni DNS. Para consultar un nombre hace falta un mecanismo de resolución; para llegar a otra red hace falta una ruta. Ninguno se crea por escribir un valor cualquiera en la interfaz gráfica.

[P1 · Consulta](practicas/P1-inspeccion.md) · [P2 · Configuración manual](practicas/P2-lan-estatica.md) · [P3 · DHCP y DNS](practicas/P3-dhcp-dns.md) · [P5 · Incidencias](practicas/P5-incidencias.md)

Fuente: [Microsoft · Get-NetIPConfiguration](https://learn.microsoft.com/en-us/powershell/module/nettcpip/get-netipconfiguration).
