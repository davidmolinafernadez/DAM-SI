# 3.4 · Subnetting y VLSM

Calcular a qué red pertenece una interfaz y diseñar un reparto de redes son problemas distintos. Aquí partimos de un bloque disponible y unas necesidades. Elegiremos prefijos que permitan alojar los equipos sin solapamientos y justificaremos qué espacio queda libre.

## Antes de calcular

Escribe red base **con prefijo**, cantidad mínima de segmentos, capacidad de cada segmento y si incluye router e impresoras.

El inventario cuenta interfaces que necesitan dirección: puestos, impresoras, servidores y, si existe, la interfaz de puerta de enlace. Si el enunciado pide 25 puestos y además un router y una impresora, se necesitan al menos 27 direcciones de host. También conviene conocer el crecimiento previsto antes de fijar un tamaño.

Dividir un bloque en subredes permite planificar segmentos. La separación efectiva del tráfico exige una topología y configuración coherentes: un cálculo escrito no crea VLAN ni reglas de seguridad. «¿Cuántas subredes pueden crearse desde /24?» no tiene una respuesta única sin fijar el nuevo prefijo o la capacidad requerida.

## Subredes iguales: dos condiciones simultáneas

Si se toman `s` bits de host, se obtienen `2^s` subredes y el prefijo aumenta en `s`. En una LAN ordinaria con `h` bits de host quedan `2^h-2` direcciones utilizables. Deben cumplirse la cantidad de redes y la capacidad de cada una.

El procedimiento es: determina cuántos bits necesitas para numerar las subredes, suma esos bits al prefijo base y comprueba la capacidad que queda. Si necesitas al menos seis redes, pruebas `2^2=4`, que no basta, y `2^3=8`, que sí. La cantidad disponible es ocho aunque solo se utilicen seis.

Si la capacidad restante fuera insuficiente, no se arregla escogiendo direcciones a mano dentro de los bloques: habría que revisar el tamaño de la red base o los requisitos. La dirección de red y el broadcast consumen dos direcciones por LAN ordinaria, pero no se restan dos al número de subredes.

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

Para diseñar desde los hosts, busca el menor número de bits `h` que cumpla `2^h-2 >= hosts necesarios`. Después calcula el prefijo `32-h`. Por último compara ese prefijo con el de la red base. La diferencia indica cuántos bits se han dedicado a distinguir subredes.

Un /25 contiene 128 direcciones y admite 126 hosts ordinarios. Si cada segmento necesitara 130 interfaces, siete bits ya no bastarían: harían falta ocho bits y un /24 por segmento.

## VLSM: necesidades distintas

VLSM asigna prefijos de longitudes diferentes. Se ordenan las necesidades de mayor a menor, se elige el menor bloque suficiente y se respeta su alineación.

Ordenar de mayor a menor facilita que los bloques grandes encuentren un espacio contiguo y alineado. Alineación significa que todos los bits de host de la dirección de red valen cero. Un /26 tiene bloques de 64 direcciones: en el último octeto de este /24 puede empezar en 0, 64, 128 o 192, pero no en 150.

Tras asignar un bloque, anota su última dirección y busca el siguiente comienzo válido para el bloque siguiente. No basta con que el comienzo esté libre: todo el intervalo debe caber y no cruzarse con ninguna asignación previa. Para 100, 50, 20 y 10 interfaces dentro de `192.168.40.0/24`:

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

Fuente: [RFC 4632 · CIDR](https://www.rfc-editor.org/rfc/rfc4632).

## Ejemplo paso a paso · Tres necesidades diferentes

Disponemos de `192.168.80.0/24` y necesitamos segmentos de 60, 28 y 12 interfaces, incluyendo su infraestructura.

| Paso | Decisión | Justificación |
| --- | --- | --- |
| 1 | 60 interfaces: /26 | Seis bits de host proporcionan 62 direcciones útiles |
| 2 | 28 interfaces: /27 | Cinco bits proporcionan 30 direcciones útiles |
| 3 | 12 interfaces: /28 | Cuatro bits proporcionan 14 direcciones útiles |
| 4 | Asignar /26 en `.0` | Ocupa `.0–.63`; hosts `.1–.62` |
| 5 | Asignar /27 en `.64` | Ocupa `.64–.95`; hosts `.65–.94` |
| 6 | Asignar /28 en `.96` | Ocupa `.96–.111`; hosts `.97–.110` |

El espacio restante va de `.112` a `.255`: 144 direcciones sin asignar. No forman un único bloque CIDR; pueden describirse como `.112/28` y `.128/25`. Tres bloques /26 consumirían 192 direcciones, frente a las 112 utilizadas con VLSM.

**Comprueba que lo entiendes:** el segmento de 12 crece a 18 interfaces. Necesita /27; comprueba que ampliar a `192.168.80.96/27` es posible si `.112/28` sigue libre. El nuevo broadcast sería `.127`.

## Vídeo de apoyo · Cálculo de subredes IPv4 del mismo tamaño · UPV

Vídeo en castellano de M. Eugenia Baydal, Universitat Politècnica de València. Refuerza el reparto en bloques iguales antes de pasar a necesidades distintas.

[Ver el vídeo en el portal de su autor](https://www.upv.es/visor/media/73f8b330-8ce9-11ec-b9b8-5fa8a1a9fe15/c)

**Durante el visionado:** detén la explicación antes del resultado, calcula el nuevo prefijo y verifica cantidad de subredes y hosts por separado. Después compara ese método con el ejemplo VLSM de esta página.

## Ahora aplica lo aprendido

[Actividad 3.4 · Diseñar subredes iguales](actividades/A4-subredes-iguales.md). Al terminar, continúa con [Actividad 3.5 · Repartir direcciones con VLSM](actividades/A5-vlsm.md).

Son dos actividades de cálculo, sin prácticas adicionales: entrega `UD3_A4_Codigo.pdf` y `UD3_A5_Codigo.pdf` en sus respectivas tareas de Aules. La [ampliación de scripting](actividades/ampliacion-script.md) es opcional y se retoma en UD6.
