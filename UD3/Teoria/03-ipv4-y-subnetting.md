# 3. IPv4, máscaras y subnetting

## 3.1 Dirección y prefijo

IPv4 usa 32 bits. En `192.168.10.34/24`, 24 bits son red y 8 host.

```text
IP:      11000000.10101000.00001010.00100010
Máscara: 11111111.11111111.11111111.00000000
Red AND: 11000000.10101000.00001010.00000000
```

Red: `192.168.10.0`; broadcast: `192.168.10.255`; hosts ordinarios: `.1–.254`.

## 3.2 Máscaras frecuentes

| Prefijo | Máscara | Direcciones | Hosts ordinarios |
| ---: | --- | ---: | ---: |
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |

La regla de restar dos se aplica a subredes ordinarias; `/31` se usa en enlaces punto a punto y `/32` identifica un host.

## 3.3 Método por tamaño de bloque

Para `/27`, el octeto interesante de la máscara es 224. El bloque es `256 - 224 = 32`. Redes: 0, 32, 64, 96, 128, 160, 192 y 224.

Para `192.168.5.77/27`, 77 cae en el bloque 64–95:

- red: `192.168.5.64`;
- primer host: `.65`;
- último host: `.94`;
- broadcast: `.95`.

## 3.4 Dividir una red

Se necesitan al menos seis subredes desde `/24`. Se toman tres bits porque `2³=8`. Nuevo prefijo `/27`.

```mermaid
flowchart TB
    P["192.168.10.0/24"] --> S1[".0/27"]
    P --> S2[".32/27"]
    P --> S3[".64/27"]
    P --> S4[".96/27"]
    P --> S5[".128/27"]
    P --> S6[".160/27"]
    P --> S7[".192/27"]
    P --> S8[".224/27"]
```

## 3.5 VLSM

Para departamentos de 100, 50, 20 y 10 hosts se asigna de mayor a menor:

- 100 → `/25`, 126 hosts;
- 50 → `/26`, 62;
- 20 → `/27`, 30;
- 10 → `/28`, 14.

Sobre `10.0.0.0/24`:

| Necesidad | Subred | Rango útil |
| ---: | --- | --- |
| 100 | `10.0.0.0/25` | `.1–.126` |
| 50 | `10.0.0.128/26` | `.129–.190` |
| 20 | `10.0.0.192/27` | `.193–.222` |
| 10 | `10.0.0.224/28` | `.225–.238` |

Queda `10.0.0.240/28` para crecimiento.

## 3.6 Rangos especiales

- privados: `10/8`, `172.16/12`, `192.168/16`;
- loopback: `127/8`;
- enlace local: `169.254/16`;
- multicast: `224/4`.

NAT traduce direcciones y puertos; no es por sí mismo un firewall, aunque frecuentemente impide conexiones entrantes no solicitadas por falta de traducción.

## Práctica mental

Para cada IP, calcula red, broadcast y rango: `172.16.35.200/20`, `10.10.10.70/26` y `192.168.1.14/30`.

### Soluciones razonadas

| IP/prefijo | Máscara | Red | Broadcast | Hosts utilizables |
|---|---|---|---|---|
| `172.16.35.200/20` | `255.255.240.0` | `172.16.32.0` | `172.16.47.255` | `172.16.32.1–172.16.47.254` |
| `10.10.10.70/26` | `255.255.255.192` | `10.10.10.64` | `10.10.10.127` | `10.10.10.65–10.10.10.126` |
| `192.168.1.14/30` | `255.255.255.252` | `192.168.1.12` | `192.168.1.15` | `192.168.1.13–192.168.1.14` |

En `/20` el bloque del **tercer octeto** es 16: 35 está entre 32 y 47.
En `/26` el bloque del cuarto octeto es 64; en `/30`, 4. La puerta de enlace
no tiene por qué ser el primer host; se asigna según el diseño y consume una
dirección utilizable si se encuentra en la subred. En VLSM se cuenta también
la infraestructura y el margen de crecimiento.

## 3.7 Introducción a IPv6

IPv6 utiliza direcciones de **128 bits**, escritas como ocho grupos
hexadecimales de 16 bits. Se omiten ceros iniciales y se puede comprimir una
única secuencia de grupos cero mediante `::`:

```text
2001:0db8:0000:0000:0000:0000:0000:0025
2001:db8::25
```

Ambas formas representan la misma dirección. El prefijo `2001:db8::/32` se
reserva para documentación; los ejemplos no son direcciones para desplegar
servicios públicos.

| Concepto | IPv4 | IPv6 |
|---|---|---|
| Dirección de loopback | `127.0.0.1` | `::1` |
| Enlace local | `169.254.0.0/16` | `fe80::/10` |
| Resolución de vecinos | ARP | Neighbor Discovery sobre ICMPv6 |
| Broadcast | Existe | Se usan multicast y otros mecanismos |
| Configuración | Manual o DHCP | Manual, SLAAC y/o DHCPv6 |

En una LAN con SLAAC se utiliza habitualmente `/64`. Los anuncios de router
informan del prefijo y de la ruta por defecto; DHCPv6 no sustituye esos anuncios
para descubrir la puerta de enlace. No se aplica a IPv6 la regla IPv4 de restar
dos direcciones por red y broadcast.

Un equipo con **doble pila** puede utilizar IPv4 e IPv6. Diagnostica ambas:
que funcione una no demuestra que la otra esté correctamente configurada.

Fuentes: [especificación IPv6, RFC 8200](https://www.rfc-editor.org/rfc/rfc8200),
[Neighbor Discovery, RFC 4861](https://www.rfc-editor.org/rfc/rfc4861)
y [prefijo para documentación, RFC 3849](https://www.rfc-editor.org/rfc/rfc3849).
