# 3.3 · IPv4, prefijo y máscara

La dirección IP y el prefijo se interpretan juntos. No basta con que dos direcciones «se parezcan»: el prefijo determina qué bits se comparan para decidir si el destino pertenece a la red local. Aprenderemos a calcularlo a mano y a comprobar el resultado por dos métodos.

## Una dirección necesita contexto

Una IPv4 tiene 32 bits, escritos habitualmente como cuatro octetos decimales. El prefijo indica cuántos bits identifican la red. `192.168.3.25/24` y `192.168.3.25/21` tienen los mismos 32 bits de dirección y distinto límite entre red y host.

Sin prefijo o máscara no podemos deducir una única red. Las clases A, B y C explican una distribución histórica; para resolver los ejercicios usamos CIDR y el prefijo indicado.

Cada octeto contiene ocho bits. Sus posiciones valen `128, 64, 32, 16, 8, 4, 2 y 1`. Para convertir 77 a binario, se descompone como `64+8+4+1`: `01001101`. Esta lectura permite entender qué bits conserva una máscara y cuáles pertenecen al host.

Un prefijo /26 fija 26 bits para la red y deja seis para hosts. Cuanto mayor es el número del prefijo, menor es el bloque. Pasar de /24 a /25 divide por dos el número total de direcciones de cada bloque. No se deduce que una dirección sea privada por pertenecer a una supuesta «clase C».

## La máscara y la operación AND

Una máscara IPv4 válida tiene unos contiguos a la izquierda y ceros a la derecha.

La operación AND conserva un bit solo cuando ambos bits son uno. Al aplicar la máscara, los bits de red permanecen y los bits de host quedan a cero. Ese resultado es la dirección de red. Para obtener el broadcast de una LAN ordinaria se mantienen los bits de red y se ponen a uno los bits de host.

En /26, los primeros tres octetos de la máscara son 255 y el cuarto contiene dos unos: `11000000`, es decir 192. Por tanto, la máscara decimal es `255.255.255.192`. Se cuentan bits, no cifras decimales. Para /21 hay 21 unos:

```text
IP:      11000000.10101000.00000011.00011001  192.168.3.25
Máscara: 11111111.11111111.11111000.00000000  255.255.248.0
AND:     11000000.10101000.00000000.00000000  192.168.0.0
```

`255.255.31.0` no es una máscara /21: 31 tiene el patrón binario `00011111`, que rompe la continuidad. En este ejemplo la red es `192.168.0.0/21`, el broadcast `192.168.7.255`, los hosts ordinarios `192.168.0.1–192.168.7.254` y la capacidad 2046 hosts. Con /24, la red sería `192.168.3.0` y el broadcast `192.168.3.255`.

## Red, host y broadcast

En una LAN IPv4 ordinaria, todos los bits de host a cero identifican la red; todos a uno, el broadcast dirigido de esa subred. Las direcciones intermedias se pueden asignar a interfaces, respetando reservas y ausencia de duplicados. No se asigna automáticamente la primera a un router: es una convención del plan de red.

La dirección identifica una interfaz. Un equipo con Ethernet y Wi-Fi puede tener varias direcciones y rutas. Antes de copiar un dato al informe, comprueba a qué interfaz pertenece y si está activa. Tampoco debe repetirse una misma dirección dentro del segmento: el duplicado puede producir comunicación irregular.

Una dirección que termina en `.0` no es siempre una dirección de red y una que termina en `.255` no es siempre broadcast. Esas funciones dependen del prefijo y del bloque completo. En `192.168.0.0/23`, por ejemplo, `192.168.0.255` y `192.168.1.0` están dentro del rango de hosts ordinarios.

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

Para comprobar si dos interfaces están en la misma subred, calcula la red de ambas con el prefijo que utiliza cada una. Si A y B tienen prefijos distintos, pueden interpretar de forma diferente si la otra dirección es local. Eso explica fallos que parecen intermitentes o asimétricos aunque los cables estén bien.

Por ejemplo, `192.168.5.77/27` pertenece a `192.168.5.64/27`; `192.168.5.100/27` pertenece a `192.168.5.96/27`. Compartir los tres primeros octetos no las convierte en la misma subred.

## Direcciones privadas y otros ámbitos

| Bloque | Función |
| --- | --- |
| 10.0.0.0/8 | Direcciones privadas RFC 1918 |
| 172.16.0.0/12 | Privadas: segundos octetos de 16 a 31 |
| 192.168.0.0/16 | Direcciones privadas RFC 1918 |
| 127.0.0.0/8 | Loopback del propio equipo |
| 169.254.0.0/16 | Direccionamiento IPv4 de enlace local |

Una dirección de enlace local puede aparecer cuando no se obtiene una concesión DHCP útil; no demuestra por sí sola la causa. `0.0.0.0/0` identifica la ruta por defecto en una tabla; no equivale a decir que todo `0.0.0.0/8` sea una red de enrutamiento utilizable por el alumnado.

Privado/público, estático/dinámico e IPv4/IPv6 responden a preguntas distintas. Una dirección privada puede asignarse manualmente o mediante DHCP.

Una dirección privada puede repetirse en organizaciones diferentes, pero debe ser única dentro del ámbito donde se utiliza. Para acceder a Internet con IPv4 privado suele intervenir NAT en un router. La traducción no convierte la dirección privada en pública dentro de la interfaz del puesto.

El bloque privado que empieza por 172 va de `172.16.0.0` a `172.31.255.255`: `172.32.1.5` ya queda fuera. Loopback sirve para comunicarse con el propio sistema; una prueba a `127.0.0.1` no recorre el cable ni demuestra acceso al switch. En el laboratorio no se utiliza una dirección pública real como si perteneciera al centro.

## IPv6 como lectura inicial

IPv6 utiliza 128 bits y se representa en hexadecimal. `::1` es loopback. IPv6 no utiliza broadcast; usa multicast para funciones que en IPv4 pueden recurrir a broadcast. El estudio detallado de su configuración puede ampliarse sin trasladar mecánicamente las reglas de IPv4.

## Fuentes

- [RFC 4632 · CIDR](https://www.rfc-editor.org/rfc/rfc4632).
- [RFC 1918 · Direccionamiento privado](https://www.rfc-editor.org/rfc/rfc1918).
- [RFC 3021 · Prefijos /31 en enlaces punto a punto](https://www.rfc-editor.org/rfc/rfc3021).
- [RFC 4291 · Arquitectura de direcciones IPv6](https://www.rfc-editor.org/rfc/rfc4291).

## Ejemplo resuelto · 192.168.5.77/27

1. **Máscara:** /27 deja cinco bits de host y utiliza `255.255.255.224`.
2. **Tamaño:** `2^5=32` direcciones. Los bloques del último octeto empiezan en 0, 32, 64, 96 y así sucesivamente.
3. **Bloque que contiene 77:** desde 64 hasta 95. La red es `192.168.5.64/27`.
4. **Límites:** broadcast `192.168.5.95`, primer host `.65`, último `.94` y 30 hosts ordinarios.
5. **Comprobación binaria:** `01001101 AND 11100000 = 01000000`; 64 coincide con el método del bloque.

Si la puerta propuesta fuera `192.168.5.1`, quedaría fuera de esa red conectada. Antes de aplicar cambios habría que confirmar el direccionamiento previsto del laboratorio.

**Comprueba que lo entiendes:** resuelve `192.168.5.100/27`. Debes obtener la red `.96`, broadcast `.127`, rango `.97–.126` y 30 hosts. Justifica los límites.

## Vídeo de apoyo · Direccionamiento IPv4 con y sin clases (CIDR) · UPV

Vídeo en castellano de la Universitat Politècnica de València sobre la separación entre red y host y la necesidad de máscaras y prefijos. Las clases se estudian como antecedente histórico.

<div class="video-card" markdown>
<div class="video-frame">
<iframe src="https://www.youtube-nocookie.com/embed/f3bwe88iBHQ" title="Direccionamiento IPv4 con y sin clases (CIDR) · UPV" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en YouTube](https://www.youtube.com/watch?v=f3bwe88iBHQ)

</div>

**Durante el visionado:** explica por qué necesitas conocer el prefijo y dibuja el límite entre los 26 bits de red y los seis de host de un /26.

## Ahora aplica lo aprendido

[Actividad 3.3 · Leer direcciones IPv4](actividades/A3-ipv4-y-mascaras.md).

Esta actividad no tiene práctica adicional. Entrega la tabla y los procedimientos en `UD3_A3_Codigo.pdf`; muestra cómo has obtenido los resultados.
