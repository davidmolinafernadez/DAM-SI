# Ampliación · Diseñar un calculador de subredes

Adaptación del encargo de Bash del curso anterior. Es ampliación y se puede retomar en UD6 al trabajar automatización; no añade horas obligatorias a UD3.

## Requisitos del encargo

1. Solicitar una red base **con prefijo**, por ejemplo `192.168.1.0/24`, y una cantidad de subredes iguales.
2. Validar que la entrada es IPv4, que el prefijo es válido y que la dirección corresponde a una red; si se acepta una dirección de host, mostrar de forma explícita su normalización antes de seguir.
3. Aceptar inicialmente cantidades potencia de dos. Si se amplía a «al menos N», distinguir N solicitado del número de subredes realmente generado.
4. Rechazar cantidades que dejen menos de dos bits de host para este ejercicio de LAN ordinarias. No aplicar ciegamente la resta de dos a /31 y /32.
5. Mostrar red/prefijo, máscara, primer host, último host y broadcast. Limitar la salida a 256 subredes; para cantidades mayores, ofrecer resumen o pedir una entrada menor.
6. No configurar adaptadores ni ejecutar comandos recibidos como datos. Utilizar solo cálculo local.

## Casos de aceptación

| Entrada | Resultado que debe comprobarse |
| --- | --- |
| 192.168.1.0/24, 4 | Cuatro bloques /26, 62 hosts ordinarios por bloque |
| 192.168.1.0/24, 3 | Rechazo en versión inicial; en ampliada, explicación de cuatro bloques /26 |
| 192.168.1.5/24, 4 | Rechazo o normalización explícita a 192.168.1.0/24 |
| 192.168.1.0/24, 256 | Rechazo por capacidad para LAN ordinarias |
| 192.168.1.0/24; comando | Rechazo como entrada inválida |

Antes de programar, resuelve los casos a mano. La herramienta sirve para contrastar el razonamiento, no para sustituirlo. Entrega pseudocódigo, validaciones y pruebas; el lenguaje se concretará al abordar scripting.
