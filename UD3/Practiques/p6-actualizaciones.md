# P6. Actualizaciones y control de cambios

**Teoría relacionada:** [Actualizaciones y aceptación](../b10-actualizaciones.md)

Duración: 120 minutos. Teoría: B10. Producto: registro antes/después y Ubuntu actualizado.

## Procedimiento

1. Comprueba espacio en anfitrión e invitado. Crea una instantánea apagada llamada P6-antes-actualizar y anota su alcance.
2. Arranca Ubuntu. Registra distribución, kernel y hora. Ejecuta sudo apt update y lee si todos los repositorios se consultan correctamente.
3. Consulta apt list --upgradable. Selecciona dos paquetes propuestos, si los hay, y anota versión anterior/candidata. Si no hay actualizaciones, registra ese resultado válido.
4. Ejecuta sudo apt upgrade. Antes de confirmar, lee paquetes nuevos, actualizaciones, descarga y espacio adicional. No utilices -y en esta práctica. Anota si el gestor propone algún conflicto.
5. Comprueba si se solicita reinicio y realízalo si corresponde. Vuelve a registrar uname -r; el kernel puede mantenerse si no se actualizó.
6. Consulta apt show tree; instala con sudo apt install tree. Ejecuta tree --version y utilízalo sobre una carpeta de prueba de tres niveles que tú hayas creado.
7. Consulta apt show antes de elegir otra aplicación. Explica qué información ayuda a decidir si es el paquete correcto.
8. Compara estado inicial y final. No ejecutes full-upgrade, autoremove o purge por rutina: explica qué revisarías antes de usarlos.

## Incidencia y aceptación

Incidencia controlada: desconecta el cable virtual, ejecuta apt update, registra el error de red y reconecta. Repite y compara. No interpretes «se usan índices anteriores» como una actualización de metadatos correcta.

Aceptación: metadatos consultados sin fallos de red sin resolver, actualización revisada, reinicio cuando proceda y aplicación comprobada. Entrega registro con comandos, resultados, decisiones y reversión disponible. Preguntas: ¿update instala nuevas versiones?, ¿upgrade puede añadir dependencias?, ¿por qué no se debe borrar un bloqueo de APT sin saber qué proceso lo mantiene?
