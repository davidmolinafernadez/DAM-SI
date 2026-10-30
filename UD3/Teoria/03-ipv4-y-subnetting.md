# 3.3 · IPv4, prefijo y máscara

## Una dirección necesita contexto

Una IPv4 tiene 32 bits, escritos habitualmente como cuatro octetos decimales. El prefijo indica cuántos bits identifican la red. `192.168.3.25/24` y `192.168.3.25/21` tienen los mismos 32 bits de dirección y distinto límite entre red y host.

Sin prefijo o máscara no podemos deducir una única red. Las clases A, B y C explican una distribución histórica; para resolver los ejercicios usamos CIDR y el prefijo indicado. No se deduce que una dirección sea privada por pertenecer a una supuesta «clase C».

## La máscara y la operación AND

Una máscara IPv4 válida tiene unos contiguos a la izquierda y ceros a la derecha. Para /21 hay 21 unos:

```text
IP:      11000000.10101000.00000011.00011001  192.168.3.25
Máscara: 11111111.11111111.11111000.00000000  255.255.248.0
AND:     11000000.10101000.00000000.00000000  192.168.0.0
```

`255.255.31.0` no es una máscara /21: 31 tiene el patrón binario `00011111`, que rompe la continuidad. En este ejemplo la red es `192.168.0.0/21`, el broadcast `192.168.7.255`, los hosts ordinarios `192.168.0.1–192.168.7.254` y la capacidad 2046 hosts. Con /24, la red sería `192.168.3.0` y el broadcast `192.168.3.255`.

## Red, host y broadcast

En una LAN IPv4 ordinaria, todos los bits de host a cero identifican la red; todos a uno, el broadcast dirigido de esa subred. Las direcciones intermedias se pueden asignar a interfaces, respetando reservas y ausencia de duplicados. No se asigna automáticamente la primera a un router: es una convención del plan de red.

| Prefijo | Máscara | Direcciones | Hosts ordinarios |
| --- | --- | ---: | ---: |
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |

El total es `2^(32-prefijo)`. Restar dos sirve para las subredes ordinarias de esta tabla. /31 tiene un uso específico en enlaces punto a punto y /32 representa una dirección individual; no se tratan como LAN convencionales en estos ejercicios.

## Método del bloque, también fuera del último octeto

En /27, el octeto parcial de la máscara es 224: salto `256-224=32`. Para `192.168.5.77/27`, 77 pertenece al intervalo 64–95. Red `.64`, hosts `.65–.94`, broadcast `.95`.

En /21, el octeto parcial es el tercero, 248: salto 8 en ese octeto. `192.168.13.25/21` pertenece al bloque de terceros octetos 8–15: red `192.168.8.0`, broadcast `192.168.15.255`. El cuarto octeto recorre todo su rango; no se aplica un salto 8 al octeto equivocado.

## Direcciones privadas y otros ámbitos

| Bloque | Función |
| --- | --- |
| 10.0.0.0/8 | Direcciones privadas RFC 1918 |
| 172.16.0.0/12 | Privadas: segundos octetos de 16 a 31 |
| 192.168.0.0/16 | Direcciones privadas RFC 1918 |
| 127.0.0.0/8 | Loopback del propio equipo |
| 169.254.0.0/16 | Direccionamiento IPv4 de enlace local |

Una dirección de enlace local puede aparecer cuando no se obtiene una concesión DHCP útil; no demuestra por sí sola la causa. `0.0.0.0/0` identifica la ruta por defecto en una tabla; no equivale a decir que todo `0.0.0.0/8` sea una red de enrutamiento utilizable por el alumnado.

Privado/público, estático/dinámico e IPv4/IPv6 responden a preguntas distintas. Una dirección privada puede asignarse manualmente o mediante DHCP. En el laboratorio no se utiliza una dirección pública real como si perteneciera al centro.

## IPv6 como lectura inicial

IPv6 utiliza 128 bits y se representa en hexadecimal. `::1` es loopback. IPv6 no utiliza broadcast; usa multicast para funciones que en IPv4 pueden recurrir a broadcast. El estudio detallado de su configuración puede ampliarse sin trasladar mecánicamente las reglas de IPv4.

[Actividad 3.3](actividades/A3-ipv4-y-mascaras.md) · [Continuar con subnetting y VLSM](05-subnetting-y-vlsm.md)

## Fuentes

- [RFC 4632 · CIDR](https://www.rfc-editor.org/rfc/rfc4632).
- [RFC 1918 · Direccionamiento privado](https://www.rfc-editor.org/rfc/rfc1918).
- [RFC 3021 · Prefijos /31 en enlaces punto a punto](https://www.rfc-editor.org/rfc/rfc3021).
- [RFC 4291 · Arquitectura de direcciones IPv6](https://www.rfc-editor.org/rfc/rfc4291).


## Actividad y aplicación práctica

- [Actividad 3.3 · Leer direcciones IPv4](actividades/A3-ipv4-y-mascaras.md)

Encontrarás los pasos prácticos asociados junto al enunciado de la actividad. Incorpora sus evidencias al mismo PDF y entrega todo junto en la tarea de Aules correspondiente.
