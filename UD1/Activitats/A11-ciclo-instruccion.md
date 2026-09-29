# Tarea 1.1.1 · Viaje de una instrucción

<div class="activity-meta" markdown>
<span>110 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

Vamos a seguir programas pequeños en una máquina de Von Neumann. En A y C,
**predice en papel** y después **comprueba en el simulador**. El programa B
se resuelve **solo a mano, sin simulador**, como preparación para el examen.
El objetivo es explicar qué cambia en PC, IR, ACC y memoria después de cada
instrucción, no copiar una captura del resultado.

[:material-download: Descargar plantilla editable (.odt)](descargas/Tarea_1_1_1_Ciclo_Instruccion_Apellidos_Nombre.odt){ .md-button .md-button--primary download }
[:material-file-pdf-box: Abrir la actividad en PDF](descargas/Tarea_1_1_1_Ciclo_Instruccion_Apellidos_Nombre.pdf){ .md-button }

## 1. Preparación y reglas

Consulta el [tema 1.1](../11-instrucciones-cpu.md), especialmente los apartados
2 a 6. Los ejemplos resueltos de la teoría utilizan datos diferentes.

[Abrir Von Neumann Machine Simulator](https://vnmsim.c2r0b.ovh/en-us){ .md-button .md-button--primary target="_blank" }

Para A y C usaremos esta versión del simulador. Las instrucciones tienen el
mismo significado en el ejercicio manual B. Ten en cuenta estas reglas:

- **ACC** es el acumulador; **X, Y y Z** son variables de memoria.
- **W y T0** son otras variables disponibles. Déjalas en **0** en todas las
  pruebas: estos programas no las utilizan. T0 se escribe con el número cero,
  no con la letra O. No hay que añadirlas a las tablas.
- `LOD X` carga X; `STO Z` guarda ACC en Z; `#n` representa un número literal.
- `JMZ` salta si **ACC = 0**. Z no es una bandera.
- Las direcciones empiezan en **0** y el PC avanza de uno en uno.
- En A y C, copia el código sin números delante ni líneas vacías adicionales.
- Una fila de la tabla representa **una instrucción terminada**, no un ciclo de reloj.
- En A y C, usa **Single iteration** para completar una instrucción y espera a que acabe
  la animación antes de registrar los datos. **Single step** muestra pasos internos.
- `HLT` detiene el programa. En el simulador devuelve PC a 0: en A y C anota
  «0; detenido». En B escribe simplemente «detenido»; no se pide un PC numérico tras HLT.
- Para A y C utiliza **New project**, pega el código y establece sus
  datos iniciales. Comprueba PC = 0, incremento = 1 y ACC = 0.

Distribución orientativa: vídeos y esquema, 10 min; programa A, 25 min; B, 10 min;
programa C, 35 min; recorrido de una instrucción, 10 min; CPU real, 10 min;
revisión y entrega, 10 min.

## 2. Observa los vídeos y dibuja el recorrido

Míralos en este orden:

1. [Fase de búsqueda de ciclo de instrucción](https://www.youtube.com/watch?v=uxvswp1lOis).
2. [Estructura de un computador · Ciclo de instrucción](https://www.youtube.com/watch?v=q4MAxVeNny4).

Responde con tus palabras:

- ¿Qué guarda PC y qué guarda IR?
- ¿Qué diferencia hay entre buscar una instrucción y ejecutarla?
- Dibuja `PC → MAR → memoria → MDR → IR`. Indica dónde viaja una dirección
  y dónde viaja el contenido de la instrucción.

Los vídeos pueden usar otra notación. Para programar, utiliza la de esta
actividad; MAR y MDR se explican en el esquema aunque el simulador no muestre
campos independientes con esos nombres.

## 3. Programa A · Operar y reutilizar resultados

Datos iniciales: **X = 4, Y = 3, Z = 0, ACC = 0 y PC = 0**.

```asm
LOD X
ADD #2
MUL Y
STO Z
SUB X
STO Y
HLT
```

Primero calcula a mano qué ocurrirá. Después comprueba cada instrucción en el
simulador. Hay dos escrituras en memoria: distingue el resultado intermedio
que se guarda en Z del valor que termina en Y.

| Dirección ejecutada | Instrucción / IR | ACC al terminar | X | Y | Z | PC al terminar | ¿Qué cambia? |
|---:   |---|---|---|---|---|---|---|
| 0 | LOD X | | | | | | |
| 1 | ADD #2 | | | | | | |
| 2 | MUL Y | | | | | | |
| 3 | STO Z | | | | | | |
| 4 | SUB X | | | | | | |
| 5 | STO Y | | | | | | |
| 6 | HLT | | | | | | |

1. Escribe la expresión aritmética que calcula Z, usando los valores iniciales
   de X e Y. ¿Qué cálculo adicional produce el valor final de Y?
2. Justo después de SUB X, ¿por qué ACC y Z pueden contener valores distintos?
3. ¿Qué valor de Y utiliza MUL Y: el inicial o el que se guarda después?
   Justifica la respuesta según el orden de ejecución.
4. Incluye una captura después de STO Z y otra después de STO Y; explica
   qué ha cambiado entre ambas.
5. Sin volver a ejecutar, predice qué pasaría si la instrucción de la dirección
   1 fuese ADD X en vez de ADD #2. Indica los nuevos valores finales de Z e Y.

## 4. Programa B · Ejercicio de examen sin simulador

**Tiempo orientativo: 10 minutos. Resuélvelo en papel, sin ordenador ni
simulador, tampoco para comprobar el resultado.** Incorpora la hoja manuscrita
escaneada o fotografiada de forma legible a tu entrega.

Son cinco instrucciones, sin saltos. Datos iniciales:
**PC = 0, ACC = 0 y X = 6**.

```asm
LOD X
SUB #2
STO X
ADD X
HLT
```

Completa la tabla **después de cada instrucción**. PC avanza una posición en
las cuatro primeras; en la última fila escribe «detenido». Presta atención:
una instrucción modifica X antes de que otra vuelva a utilizarla.

| Dirección ejecutada | Instrucción / IR | ACC al terminar | X | PC al terminar |
|---:|---|---|---|---|
| 0 | LOD X | | | |
| 1 | SUB #2 | | | |
| 2 | STO X | | | |
| 3 | ADD X | | | |
| 4 | HLT | | | |

1. ¿Qué significa #2 y en qué se diferencia de X como operando?
2. ¿Qué valor de X utiliza ADD X? Explica qué instrucción lo ha establecido.
3. ¿STO X borra ACC? ¿Cuál sería el ACC final si ADD X se sustituyera por ADD #2?

No basta con escribir el resultado: explica los cambios. **No se pide ejecutar
este programa ni adjuntar capturas del simulador.**

## 5. Programa C · Un bucle con contador

Ahora hay un salto hacia atrás: algunas instrucciones se repiten. Usa Y como
contador, siempre un entero mayor o igual que cero, y realiza estas pruebas
restableciendo PC = 0, ACC = 0 y los datos antes de cada una:

- **Prueba 1:** X = 4, Y = 3, Z = 0.
- **Prueba 2:** X = 4, Y = 0, Z = 0.

```asm
LOD Y
JMZ 9
LOD Z
ADD X
STO Z
LOD Y
SUB #1
STO Y
JMP 0
HLT
```

Las direcciones van de 0 a 9. **JMZ 9 llega a HLT** y **JMP 0 vuelve a LOD Y**.
No añadas líneas vacías ni números delante del código.

1. Antes de simular, explica qué resultado crees que se guardará en Z y cuántas
   veces se ejecutará ADD X en cada prueba.
2. En la prueba 1, haz una traza detallada de la **primera vuelta**, desde
   LOD Y hasta JMP 0: dirección ejecutada, IR, ACC, Y, Z y PC al terminar.
3. Para las siguientes vueltas, usa la tabla resumen de abajo. Anota el estado
   justo después de cada JMP 0 y añade una fila final tras HLT. No copies
   una tabla de treinta filas.

   | Momento | ACC | Y | Z | PC | Explicación |
   |---|---|---|---|---|---|
   | Estado inicial | 0 | 3 | 0 | 0 | Todavía no se ha ejecutado nada |
   | Tras la primera vuelta | | | | | |
   | Tras la segunda vuelta | | | | | |
   | Tras la tercera vuelta | | | | | |
   | Tras HLT | | | | | |

4. En la prueba 2, registra todas las instrucciones que se ejecutan. ¿Por qué
   no se realiza ninguna suma? ¿Qué comprueba JMZ exactamente?
5. Comprueba ambas pruebas con el simulador. Incluye una captura al terminar
   la primera vuelta y otra cuando JMZ toma el salto a HLT.
6. Explica la función de Z y la de Y. ¿Por qué hace falta STO Y después de SUB #1?
7. **Detecta el fallo sin ejecutarlo:** si sustituyes SUB #1 por SUB #0 en la
   prueba 1, ¿terminaría el programa? Justifica qué ocurriría con el contador.

Ayuda: un bucle necesita comprobar una condición, realizar el trabajo,
actualizar el contador y volver a comprobar. Puedes repasar la explicación
sobre bucles al final del apartado 6 de la teoría.

## 6. Explica una instrucción por dentro

Elige **STO Z del programa A** y describe:

1. **Búsqueda:** qué dirección contiene PC antes de buscarla y qué llega a IR.
2. **Decodificación:** qué operación reconoce la unidad de control.
3. **Ejecución:** qué valor sale de ACC, qué variable recibe la escritura y
   si cambia ACC.

Añade al dibujo del apartado 2 el recorrido de esta escritura. MAR contiene
la dirección de Z y MDR transporta el dato. No inventes una dirección numérica
para Z: el simulador la identifica por su nombre.

Termina con dos frases: una que diferencie instrucción y ciclo de reloj, y
otra que explique por qué 3 GHz no significa necesariamente 3 000 millones de
instrucciones terminadas por segundo. No se pide dibujar un pipeline.

## 7. Conexión con tu equipo · Windows

Pulsa **Ctrl + Mayús + Esc → Rendimiento → CPU**. Si aparece la vista reducida,
pulsa **Más detalles**. Anota el modelo, sockets, núcleos, procesadores lógicos,
cachés L1/L2/L3 y virtualización que muestre el panel.

Para completar la arquitectura y contrastar los datos, abre **PowerShell**:

```powershell
Get-CimInstance Win32_Processor |
    Select-Object Name, Architecture, SocketDesignation, NumberOfCores,
        NumberOfLogicalProcessors, L2CacheSize, L3CacheSize,
        VirtualizationFirmwareEnabled |
    Format-List
```

| Campo | Cómo interpretarlo |
|---|---|
| Name | Modelo de CPU |
| Architecture | 9 = x86-64; 12 = ARM64; 0 = x86 |
| SocketDesignation | Etiqueta del socket, no cantidad; usa el panel para el recuento |
| NumberOfCores | Núcleos del procesador mostrado |
| NumberOfLogicalProcessors | Procesadores lógicos del procesador mostrado |
| L2CacheSize y L3CacheSize | Tamaños informados en KB; para L1 consulta el panel |
| VirtualizationFirmwareEnabled | Estado informado de la virtualización en firmware |

Si un campo no aparece, indica «no mostrado». Un tamaño de caché vacío o 0 no
prueba por sí solo que no exista. Si hay varios bloques de CPU, identifica a
cuál corresponde cada dato. En una máquina virtual, documenta que observas
el hardware expuesto al invitado.

En una CPU uniforme puedes calcular hilos por núcleo dividiendo lógicos entre
núcleos. Por ejemplo, 8 lógicos / 4 núcleos = 2. En una CPU híbrida no supongas
que todos los núcleos tienen la misma proporción: anota ambos recuentos y
consulta la ficha oficial si necesitas el desglose.

Incluye una captura recortada al panel y explica en tres frases la diferencia
entre socket físico, núcleo e hilo lógico. No publiques números de serie ni
identificadores personales. **Alternativa en Linux:** ejecuta `lscpu` y
recoge los mismos datos; no necesitas instalar Linux si utilizas Windows.

Referencia: [Win32_Processor, Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-processor).

## 8. Entrega y revisión

Entrega en Aules un PDF llamado **Tarea_1_1_1_Apellidos_Nombre.pdf**. Puedes
completar la plantilla ODT en LibreOffice Writer y exportarla a PDF. Escribe
lo necesario para explicar tus resultados; no añadas una portada vacía ni
capturas repetidas para ocupar páginas.

Debe incluir: respuestas sobre los vídeos, esquema propio, predicción y
comprobación de A, **hoja manuscrita de B resuelta sin simulador**, la traza y el resumen del bucle de C, su prueba con contador cero, explicación de STO y ficha de CPU. En cada traza distingue
dirección ejecutada y PC al terminar. En A y C, si tu predicción no coincidió,
conserva el error inicial y explica cómo lo corregiste.

Antes de entregar, comprueba que las tablas se leen, que las capturas muestran
el momento indicado y que no has confundido Z con una bandera ni una
instrucción con un ciclo de reloj.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Vídeos y esquema de búsqueda | 1 |
| Programa A: operaciones, escrituras y predicción de la variante | 2 |
| Programa B sin simulador: traza manual (1) e interpretación (0,5) | 1,5 |
| Programa C: bucle, contador cero y detección del fallo | 2,5 |
| Explicación de STO e instrucción frente a ciclo | 1,5 |
| Ficha de CPU e interpretación | 1 |
| Claridad y presentación de evidencias | 0,5 |
