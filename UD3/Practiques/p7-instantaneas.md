# P7. Instantáneas: recuperar y delimitar la pérdida

**Teoría relacionada:** [Recuperación y transferencia](../b11-recuperacion.md)

Duración: 120 minutos. Teoría: B11. Vídeo V4. Producto: experimento documentado de retorno a un estado anterior.

## Procedimiento

1. Dentro de Ubuntu crea ~/ud3-recuperacion/estado.txt con «ESTADO A». Apaga ordenadamente. En VirtualBox toma instantánea P7-A y describe el estado esperado.
2. Arranca, modifica el contenido a «ESTADO B» y crea posterior.txt. Comprueba ambos. Guarda fuera de la VM las capturas o notas que necesitas para demostrar este estado.
3. Predice qué existirá al regresar a P7-A. Apaga. Selecciona la instantánea correcta y la acción restaurar; lee si se ofrece conservar el estado actual en otra instantánea y registra tu elección.
4. Arranca. Comprueba que estado.txt vuelve al estado A y posterior.txt no forma parte del estado restaurado. Si el resultado difiere, revisa qué instantánea seleccionaste y dónde se guardaron realmente los archivos.
5. Crea ESTADO C y explica cómo continúa el trabajo desde el estado restaurado. No elimines archivos de instantáneas desde el explorador del anfitrión.
6. Anota el espacio que ocupa la carpeta de la VM. Explica por qué sucesivas instantáneas pueden aumentar el consumo y por qué no se deben conservar indefinidamente sin una política.

## Experimento opcional de alcance externo

Con una carpeta compartida de prueba expresamente preparada por el docente, crea un archivo en el anfitrión después de la instantánea. Restaura y observa que el archivo externo no retrocede. No utilices Documentos personales ni carpetas compartidas con información real.

Aceptación: predicción, estados A/B observables, restauración y explicación de pérdida posterior. Preguntas: ¿borrar una instantánea equivale a restaurarla?, ¿qué ocurre si falla el disco físico donde están base y diferenciales?, ¿por qué guardamos evidencias fuera antes de restaurar?
