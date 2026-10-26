# P3. Windows 11 con instalación y licencia diferenciadas

**Teoría relacionada:** [Instalar y comprobar Windows](../b08-instalar-windows.md)

Duración: 180 minutos. Teoría: B8. Apoyo: guía ilustrada del año pasado y fuentes F2/F3. Producto: Windows con informe de aceptación.

## Preparación

Se necesita medio oficial, edición y derecho de uso acordados por el centro. El docente prepara el método de cuenta compatible con esa edición. No se exige una cuenta personal del alumno ni se distribuyen claves en documentos. Comprueba recursos del anfitrión antes de encender también Ubuntu.

## Procedimiento

1. Crea UD3-Windows-codigo con su propio VDI dinámico de 80 GiB, 2 vCPU y 4-6 GiB de RAM según viabilidad. Selecciona la plantilla de Windows 11 y registra opciones de firmware, TPM 2.0 virtual y arranque seguro.
2. Conecta la ISO y desactiva el modo desatendido si lo propone el asistente. Arranca el instalador de forma interactiva.
3. Verifica idioma y teclado. Identifica edición. Introduce una clave únicamente por el procedimiento del centro; si el instalador permite aplazarla y el docente lo ha previsto, registra que la activación sigue siendo una comprobación pendiente.
4. Selecciona instalación limpia o personalizada según lo que muestre la versión. En el disco virtual vacío, permite crear automáticamente las particiones. Documenta el destino antes de confirmar.
5. Completa copia y reinicios. Si vuelve a pedir arrancar desde el medio, deja que continúe desde disco. No empieces otra instalación por confundir ese aviso.
6. Completa región, red y cuenta de aula según la preparación docente. No utilices guías de omisión de requisitos ni comandos antiguos para eludir el asistente.
7. Retira la ISO y comprueba arranque. Crea un archivo en Documentos, reinicia y verifica persistencia.
8. Abre winver, msinfo32, tpm.msc, Administración de discos y Administrador de dispositivos. Completa una tabla con versión, modo de firmware, estado observado de arranque seguro, TPM, particiones y dispositivos con incidencia.
9. Consulta activación sin exponer claves. Completa Windows Update y los reinicios necesarios dentro de la ventana de clase. Si quedan descargas, anota el estado exacto para continuar.
10. Si el docente pide integración, instala Guest Additions dentro de Windows, revisa el instalador y reinicia. Comprueba resolución y dispositivo gráfico.

## Aceptación e incidencia

Aceptación: arranque sin ISO, persistencia, particiones interpretadas, requisitos acreditados y actualización completada o pendiente claramente delimitada para el cierre docente. Un error de requisitos no se resuelve ocultándolo: se revisa firmware, TPM, RAM, CPU y compatibilidad del anfitrión.

Incidencia de análisis: el docente entrega una ficha ficticia con 2 GiB de RAM, sin TPM virtual y firmware heredado. Explica por qué no cumple y qué cambios habría que comprobar antes de instalar. No modifiques la VM ya instalada para producir el fallo.

Entrega: ficha técnica, mapa de particiones con función de ESP/MSR/sistema/recuperación si aparecen, estado de dispositivos y actualizaciones, y explicación de instalación frente a activación. Pregunta: ¿por qué una partición sin letra puede ser esencial?
