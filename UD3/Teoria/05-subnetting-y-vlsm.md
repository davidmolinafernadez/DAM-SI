# 3.4 · Subnetting y VLSM

## Antes de calcular

Escribe red base **con prefijo**, cantidad mínima de segmentos, capacidad de cada segmento y si incluye router e impresoras. «¿Cuántas subredes pueden crearse desde /24?» no tiene una respuesta única sin fijar el nuevo prefijo o la capacidad requerida.

## Subredes iguales: dos condiciones simultáneas

Si se toman `s` bits de host, se obtienen `2^s` subredes y el prefijo aumenta en `s`. En una LAN ordinaria con `h` bits de host quedan `2^h-2` direcciones utilizables. Deben cumplirse la cantidad de redes y la capacidad de cada una.

Ejemplo: al menos seis subredes de 25 hosts desde `192.168.1.0/24`. Dos bits solo dan cuatro redes. Tres bits dan ocho y dejan cinco bits para hosts: 30 hosts por /27. Cumple ambos requisitos. Se usan seis bloques y quedan dos libres; no existen exactamente seis bloques iguales que agoten un /24.

| Subred disponible | Rango útil | Broadcast |
| --- | --- | --- |
| 192.168.1.0/27 | .1–.30 | .31 |
| 192.168.1.32/27 | .33–.62 | .63 |
| 192.168.1.64/27 | .65–.94 | .95 |
| 192.168.1.96/27 | .97–.126 | .127 |
| 192.168.1.128/27 | .129–.158 | .159 |
| 192.168.1.160/27 | .161–.190 | .191 |
| 192.168.1.192/27 | .193–.222 | .223 |
| 192.168.1.224/27 | .225–.254 | .255 |

Las abreviaturas de la tabla comparten los tres primeros octetos `192.168.1`. Los ocho bloques son asignables como subredes en este modelo; no se resta dos al número de subredes.

## Diseñar por cantidad de hosts

Para al menos 100 hosts ordinarios, siete bits son suficientes: `2^7-2=126`; seis solo dan 62. El prefijo es /25. Si la base es /16, se toman nueve bits y caben 512 bloques /25. El criterio de hosts no fija cuántos bloques se van a utilizar: debe distinguirse capacidad disponible de asignación real.

## VLSM: necesidades distintas

VLSM asigna prefijos de longitudes diferentes. Se ordenan las necesidades de mayor a menor, se elige el menor bloque suficiente y se respeta su alineación. Para 100, 50, 20 y 10 interfaces dentro de `192.168.40.0/24`:

| Necesidad | Red | Capacidad ordinaria | Rango útil | Broadcast |
| ---: | --- | ---: | --- | --- |
| 100 | 192.168.40.0/25 | 126 | .1–.126 | .127 |
| 50 | 192.168.40.128/26 | 62 | .129–.190 | .191 |
| 20 | 192.168.40.192/27 | 30 | .193–.222 | .223 |
| 10 | 192.168.40.224/28 | 14 | .225–.238 | .239 |

Las abreviaturas comparten `192.168.40`. Queda libre `192.168.40.240/28`: son 16 direcciones del bloque, no 16 hosts utilizables en una LAN convencional.

Cambiar el último departamento a 18 interfaces requiere un /27. `192.168.40.224/27` puede ocupar los dos /28 finales si el segundo sigue libre; esto cambia el broadcast y exige actualizar el plan y las interfaces. No se anuncia una ampliación sin comprobar el espacio vecino.

## Lista de comprobación

1. Cada bloque empieza en una dirección alineada con su prefijo.
2. La última dirección cae dentro de la red base.
3. Ninguna dirección pertenece a dos bloques asignados.
4. La capacidad incluye las interfaces de infraestructura necesarias.
5. Red, rango útil y broadcast están diferenciados.
6. La puerta elegida pertenece a su subred y no se duplica.

Crear subredes en papel no crea automáticamente VLAN, aislamiento ni encaminamiento. Esos resultados requieren configuración de los dispositivos y una política de acceso coherente.

[Actividad 3.4](actividades/A4-subredes-iguales.md) · [Actividad 3.5](actividades/A5-vlsm.md) · [Ampliación de scripting](actividades/ampliacion-script.md)

Fuente: [RFC 4632 · CIDR](https://www.rfc-editor.org/rfc/rfc4632).
