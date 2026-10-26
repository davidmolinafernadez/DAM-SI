# P9. Proyecto integrador: laboratorio de un equipo de desarrollo

**Teoría relacionada:** [Repasar los doce bloques](../index.md#teoria-por-bloques)

Duración: 240 minutos. Teoría: toda la unidad. Producto: laboratorio verificable, memoria breve y defensa individual.

## Encargo

Una pequeña empresa necesita Windows para una herramienta de escritorio y Ubuntu para probar una página web. Debes preparar ambos sistemas, describir sus recursos, permitir al anfitrión acceder al servicio de Ubuntu y demostrar recuperación ante un cambio fallido. El equipo disponible lo determina el docente. No puedes prometer simultaneidad si tus medidas no la justifican.

## Requisitos verificables

1. Plan justificado con arquitectura, versiones, fuentes, derechos de uso, presupuesto de RAM/disco y decisión de ejecución simultánea o alterna.
2. Windows y Ubuntu arrancan desde sus discos, sin depender de la ISO. Sus nombres permiten distinguirlos.
3. Registro de particiones y sistemas de archivos, y explicación de una partición pequeña que no contiene documentos del usuario.
4. Ubuntu muestra una página propia de al menos diez líneas de HTML con nombre del proyecto y dos datos técnicos comprobables. El anfitrión la visita por solo anfitrión o reenvío NAT limitado a bucle local.
5. Actualización y aceptación documentadas con resultados reales. Cualquier pendiente material se declara y se cierra con el docente.
6. Instantánea anterior a un cambio, cambio observable y restauración demostrada. Los datos que deban conservarse tienen una copia fuera del estado restaurado.
7. Exportación e importación de Ubuntu probada, o restauración de una copia independiente aprobada si el puesto no tiene espacio para ambas a la vez.
8. Informe de una incidencia con síntoma, hipótesis, prueba, resultado y solución. Una reinstalación completa sin diagnóstico no es la primera respuesta.

## Organización de las cuatro horas

Primera hora: valida el plan y completa requisitos pendientes de las VM. Segunda hora: configura y comprueba la página. Tercera hora: realiza recuperación y transferencia. Cuarta hora: verifica, redacta y demuestra. Puedes reutilizar las máquinas de prácticas anteriores si acreditas su preparación; no hay que repetir instalaciones para acumular capturas.

## Entrega y defensa

Memoria recomendada de 6-10 páginas más anexos necesarios. Incluye tabla de aceptación con criterio, prueba, resultado y evidencia. Añade diagrama de red con IP y puertos reales. El docente puede pedir: retirar la ISO; localizar la raíz; explicar una ruta; detener el servidor y diagnosticar el fallo; predecir qué se perderá al restaurar. Cada integrante debe poder hacerlo individualmente.

La rúbrica valora planificación 15%, instalación y aceptación 25%, servicio y red 20%, recuperación/transferencia 25% y documentación/defensa 15%. La guía docente concreta niveles y recuperación. No hace falta diseñar una web visualmente compleja: aquí se evalúa la infraestructura que la ejecuta.
