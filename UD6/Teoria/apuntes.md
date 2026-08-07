# UD6. Redes TCP/IP y diagnóstico

## 1. Resultados de aprendizaje

Esta unidad permite reconocer componentes de red, interpretar modelos y protocolos, configurar TCP/IP, realizar subnetting y diagnosticar conectividad con un método reproducible.

## 2. Comunicación y clasificación

Una comunicación necesita emisor, receptor, mensaje, código, canal y protocolos. Las redes pueden clasificarse por alcance, propiedad, medio, topología y relación funcional.

- **LAN:** entorno local, normalmente Ethernet o Wi-Fi.
- **WAN:** conecta ubicaciones distantes.
- **Cliente-servidor:** servidores ofrecen recursos a clientes.
- **Entre iguales:** los nodos pueden compartir funciones sin servidor dedicado.

Los medios guiados incluyen par trenzado y fibra; los no guiados emplean ondas electromagnéticas. Ancho de banda es capacidad teórica; rendimiento útil, latencia, variación y pérdida describen la experiencia real.

## 3. Dispositivos

- **Tarjeta de red:** conecta el equipo y posee una dirección de enlace.
- **Switch:** reenvía tramas según direcciones MAC.
- **Router:** comunica redes IP distintas.
- **Punto de acceso:** conecta clientes inalámbricos a una red.
- **Firewall:** filtra tráfico según una política.
- **Módem/ONT:** adapta la conexión del proveedor.

Un switch no sustituye a un router: operan principalmente en capas distintas y resuelven problemas diferentes.

## 4. Modelos OSI y TCP/IP

OSI organiza la comunicación en siete capas: física, enlace, red, transporte, sesión, presentación y aplicación. TCP/IP agrupa funciones en acceso a red, Internet, transporte y aplicación.

La encapsulación añade información de control en cada capa. En el receptor se desencapsula en orden inverso.

| Capa funcional | Unidad | Ejemplos |
| --- | --- | --- |
| Aplicación | Datos | HTTP, DNS, SSH, DHCP |
| Transporte | Segmento/datagrama | TCP, UDP |
| Internet | Paquete | IPv4, IPv6, ICMP |
| Enlace | Trama | Ethernet, Wi-Fi |

TCP ofrece conexión, confirmaciones y control de orden. UDP reduce sobrecarga y deja esas garantías a la aplicación.

## 5. Direccionamiento IPv4

Una IPv4 tiene 32 bits. La máscara o prefijo separa red y host. En `192.168.10.34/24`, los primeros 24 bits identifican la red.

Rangos privados:

- `10.0.0.0/8`;
- `172.16.0.0/12`;
- `192.168.0.0/16`.

Para una subred IPv4 tradicional, la primera dirección identifica la red y la última es broadcast. Las restantes se asignan a interfaces, salvo casos especiales.

## 6. Subnetting

Un prefijo `/n` deja `32-n` bits para hosts. El total de direcciones es `2^(32-n)`.

Ejemplo: dividir `192.168.20.0/24` en cuatro subredes requiere tomar dos bits. El nuevo prefijo es `/26`, con bloques de 64 direcciones:

- `192.168.20.0/26`;
- `192.168.20.64/26`;
- `192.168.20.128/26`;
- `192.168.20.192/26`.

La primera subred ofrece hosts de `.1` a `.62` y broadcast `.63`.

## 7. Configuración TCP/IP

Una configuración manual necesita dirección, prefijo, puerta de enlace y DNS. DHCP puede suministrar estos parámetros. DNS traduce nombres a direcciones; la puerta de enlace se usa para destinos fuera de la red local.

Consultas habituales:

```bash
ip address
ip route
resolvectl status
ss -tulpen
```

```powershell
Get-NetIPConfiguration
Get-NetIPAddress
Get-NetRoute
Get-DnsClientServerAddress
```

## 8. Diagnóstico por capas

1. Comprobar alimentación, enlace, cable o asociación Wi-Fi.
2. Revisar dirección, prefijo y duplicados.
3. Probar la pila local y la propia dirección.
4. Probar la puerta de enlace.
5. Probar una IP remota.
6. Comprobar DNS con un nombre.
7. Revisar ruta, puertos, firewall y aplicación.

Herramientas:

```bash
ping -c 4 192.168.1.1
traceroute example.com
dig example.com
curl -I https://example.com
```

```powershell
Test-Connection 192.168.1.1 -Count 4
Test-NetConnection example.com -Port 443
Resolve-DnsName example.com
tracert example.com
```

`ping` puede estar filtrado; su fallo no demuestra por sí solo que el destino esté apagado.

## 9. Wi-Fi y seguridad básica

Las redes inalámbricas comparten el medio y sufren interferencias. Deben usarse WPA2-AES o WPA3, claves robustas, firmware actualizado y redes separadas para invitados o dispositivos no confiables. WPS debe desactivarse cuando no sea necesario.

## 10. Resumen

El diagnóstico eficaz sigue las capas y separa conectividad, encaminamiento, resolución de nombres y servicio. El subnetting permite dimensionar dominios de red y usar direcciones con criterio.

## Fuentes internas utilizadas

- `SI_Celia/Unit_4_Networks/UD2-Computer network.pdf`.
- `SI_Celia/Unit_4_Networks/Tasques/Task_4_2_Subnetting exercicis-1.pdf`.
- `Programacion_Didactica_SI_David_Moli.docx`.
