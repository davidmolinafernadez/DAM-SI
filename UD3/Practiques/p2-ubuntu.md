# P2. Ubuntu Desktop: de la ISO al sistema instalado

**Teoría relacionada:** [Firmware, arranque y particiones](../b04-firmware-y-particiones.md) · [Instalar y comprobar Ubuntu](../b07-instalar-ubuntu.md)

Duración: 180 minutos. Teoría: B4 y B7. Vídeo V3. Producto: Ubuntu instalado con pruebas de aceptación.

## Estado inicial

VM P1 con un único VDI vacío de 50 GiB, ISO verificada, NAT y configuración registrada. No hay otros discos conectados. Identifica el tamaño del disco antes de confirmar cualquier operación de borrado.

## Procedimiento

1. Arranca la ISO y entra en el entorno de prueba. Localiza el instalador. Anota una característica que permita reconocer la sesión Live.
2. Elige instalación interactiva. Configura idioma y prueba el teclado escribiendo símbolos, arroba y caracteres habituales. Ajusta accesibilidad si la necesitas.
3. Comprueba la conexión del invitado. Para esta práctica no es necesario activar puente ni conectarlo como otro equipo de la red del centro.
4. Elige la selección de aplicaciones acordada. Si se ofrecen descargas durante la instalación, decide según la conexión del aula y anótalo. Si se aplazan, se realizarán en P6.
5. Selecciona instalación automática usando todo el disco virtual vacío. Antes de aceptar, comprueba que el resumen afecta al único VDI de 50 GiB. Explica por qué este paso destruiría datos si el destino ya contuviera información.
6. Configura un nombre de equipo identificable y un usuario de aula. Usa una contraseña adecuada; no la incluyas en el informe. Selecciona Europe/Madrid.
7. Anota dos decisiones del resumen final y confirma. Espera sin interrumpir el proceso. Registra cualquier error con texto, momento y operación en curso.
8. Tras la instalación, sigue la indicación para retirar el medio. Si es necesario, apaga y retira la ISO desde el almacenamiento de VirtualBox. Arranca desde el disco.
9. Crea ~/comprobacion-ud3.txt con el código de alumno y una frase explicativa. Reinicia desde Ubuntu y verifica que permanece.
10. Ejecuta los comandos de comprobación de B7. Para cada uno, extrae un dato y explícalo: distribución, kernel, nombre, hora, memoria, particiones, dirección y ruta.

## Integración con el anfitrión

Comprueba si la resolución se adapta al tamaño de ventana. Si el centro pide Guest Additions, sigue una sola ruta aprobada. Ruta con ISO de complementos: actualiza índices, instala build-essential, dkms y las cabeceras que correspondan al kernel en ejecución; utiliza Dispositivos → Insertar imagen de CD de Guest Additions; ejecuta su instalador desde la ruta de montaje real y revisa el registro. No inventes una ruta /media común a todos los equipos.

Si Secure Boot impide cargar módulos, detén esa parte y registra el diagnóstico para que el docente siga el procedimiento de firma o la ruta de paquetes del centro. No cambies ajustes de seguridad del anfitrión. Tras instalar, reinicia y prueba la función de integración. La instalación básica sigue siendo evaluable aunque la integración quede pendiente por compatibilidad documentada.

## Aceptación, evidencias e incidencia

Aceptación: arranque sin ISO, usuario correcto, archivo persistente, versión y recursos coherentes, particiones montadas y reloj razonable. Evidencias: resumen previo al borrado, arranque desde disco y tabla de resultados de los comandos. Incluye incidencias y solución; no hace falta capturar cada pantalla del asistente.

Incidencia: vuelve a conectar la ISO con la VM apagada y observa el menú inicial. Comprueba el orden de arranque, explica por qué reaparece el instalador y vuelve a dejar el arranque desde disco. No reinstales.

Preguntas: ¿qué diferencia hay entre uname -r y /etc/os-release?, ¿qué perderías si hubieras trabajado solamente en modo Live?, ¿qué dispositivo físico real contiene finalmente tu archivo de prueba?
