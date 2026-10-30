# P11. Protección del sistema y restauración en Windows

<div class="lesson-banner" markdown>
<div class="lesson-number">P11</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Instalar y comprobar Windows](../b08-instalar-windows.md) · [Recuperación y transferencia](../b11-recuperacion.md)

Duración orientativa: 90 minutos. Se trabaja en un **clon de Windows de laboratorio** con instantánea previa, nunca en el puesto anfitrión. El docente prepara una aplicación de prueba e instalador oficial autorizados y un estado sin esa aplicación. Si se necesita clave de recuperación del cifrado de la VM, debe estar disponible antes de empezar.

## 1. Diferencia los dos niveles de retorno

Apaga el clon. En el administrador de VirtualBox abre **Instantáneas → Tomar** y crea `P11-antes-restauracion`. Este punto devuelve la VM completa al estado previsto si el experimento falla. Después arranca Windows: el punto de restauración que crearás ahora pertenece al propio sistema invitado y tiene un alcance diferente.

## 2. Abre Protección del sistema

Dentro de Windows invitado pulsa **Inicio**, escribe **Crear un punto de restauración** y abre el resultado de configuración del sistema. También puedes pulsar **Windows + R**, escribir `SystemPropertiesProtection` y aceptar.

En la pestaña **Protección del sistema**, selecciona la unidad del sistema, normalmente C:. Comprueba el estado de protección. Si está desactivada y el docente ha preparado el ejercicio, pulsa **Configurar → Activar protección del sistema**, asigna el límite de espacio acordado y pulsa **Aplicar → Aceptar**. No actives o desactives protección de unidades desconocidas.

## 4. Crea un punto identificable

Pulsa **Crear**, escribe `P11-antes-aplicacion` y espera al mensaje de finalización. Anota fecha y nombre exactos. Guarda un documento testigo en **Explorador → Documentos** con una frase. Recuerda: Restaurar sistema se dirige a archivos y configuración del sistema; no debe utilizarse como sustituto de una copia de documentos.

## 4. Introduce un cambio de aplicación controlado

Abre **Explorador → Descargas** y ejecuta únicamente el instalador oficial de prueba que ha indicado el docente. Lee cada pantalla y conserva la configuración acordada. Comprueba la aplicación mediante su función básica y consulta **Inicio → Configuración → Aplicaciones → Aplicaciones instaladas** para anotar el estado. No utilices software desconocido para provocar una avería.

## 5. Inspecciona qué restaurará Windows

Vuelve a **Protección del sistema** y pulsa **Restaurar sistema**. Otra ruta es **Windows + R → rstrui.exe**. Pulsa **Siguiente**, elige `P11-antes-aplicacion` y utiliza **Detectar programas afectados**. Anota qué indica, en lugar de suponer que cualquier archivo desaparecerá.

Si el punto no existe o el programa de prueba no queda dentro del alcance indicado, no prometas una reversión que no has comprobado. Registra el caso y reajusta el experimento con el docente. Conserva evidencias fuera de la VM si las necesitas después.

## 6. Restaura el clon y comprueba el resultado

Cierra aplicaciones y guarda el trabajo. En el clon preparado, revisa el resumen y confirma la restauración del punto elegido. Espera al reinicio sin interrumpirlo. Al volver, comprueba el mensaje de resultado, el estado de la aplicación, los programas afectados y el documento testigo. Explica la diferencia entre archivos personales y estado del sistema según lo observado.

Si la restauración falla, registra el mensaje y utiliza el punto de retorno completo de VirtualBox preparado al principio bajo supervisión. No repitas reparaciones sin leer el resultado. Entrega la comparación de ambos mecanismos, el punto creado, la lista de programas afectados y la comprobación posterior.

## Entrega independiente de la práctica

Guarda `P11_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.
