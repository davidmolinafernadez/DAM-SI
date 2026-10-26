# P8. Clonar, exportar e importar con comprobación

**Teoría relacionada:** [Hardware virtual y recursos](../b06-hardware-virtual.md) · [Recuperación y transferencia](../b11-recuperacion.md)

Duración: 150 minutos. Teoría: B6 y B11. Vídeo V6. Producto: clon completo e importación comprobada.

## Preparación

Calcula espacio antes de empezar. Apaga Ubuntu y retira ISO y discos secundarios innecesarios desde configuración, sin borrar archivos. El volumen de datos de P4 se conserva desconectado para evitar confundir la prueba. No exportes credenciales personales. Revisa la instantánea o estado actual que utilizarás.

## Procedimiento

1. Crea un clon completo llamado UD3-Ubuntu-Clon-codigo. Selecciona la opción para generar nuevas MAC y clonar el estado elegido. Escribe qué diferencia habría con un clon enlazado.
2. Antes de encender origen y clon a la vez, comprueba IP estáticas, MAC y nombre. Inicialmente arranca el clon con red desconectada si necesitas modificar su identidad sin conflicto.
3. Cambia el nombre del clon desde la herramienta de sistema acordada. Si conserva una IP estática, asígnale otra del rango de laboratorio. Comprueba el nombre y conectividad al reiniciar.
4. Crea solo en el clon ~/archivo-del-clon.txt. Apaga. Arranca el origen y comprueba que no aparece allí. Explica qué independencia demuestra y qué riesgo físico sigue compartiendo.
5. Apaga el origen y expórtalo a OVA en la ubicación indicada por el docente. Registra tamaño, tiempo aproximado y configuración importante en una ficha externa. No asumas que el paquete conserva la historia de instantáneas ni todos los dispositivos específicos.
6. Importa como UD3-Ubuntu-Importada-codigo, con nuevas MAC. Si el espacio escasea, el docente puede hacer la importación en otro equipo; no borres el único original para liberar espacio antes de probar el respaldo.
7. Antes de arrancar, revisa RAM, firmware, controladores y red. Comprueba arranque, versión, archivo testigo y un servicio o aplicación utilizada en clase.
8. Registra diferencias respecto al origen. Si la importación necesita ajustes, anótalos para que la transferencia sea reproducible.

## Aceptación e incidencia

Aceptación: clon independiente a nivel de archivos, identidad revisada e importación que arranca y conserva el archivo testigo. Una exportación completada sin probar no supera por sí sola la práctica.

Incidencia de análisis: «El clon no obtiene red y tiene la misma IP fija que el origen». Formula diagnóstico y corrección. Pregunta: ¿un OVA guardado en el mismo SSD protege frente a la avería de ese SSD? Diseña destino alternativo y prueba de restauración.
