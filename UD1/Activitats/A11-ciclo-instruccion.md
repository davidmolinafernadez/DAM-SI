# Tarea 1.1.1 · Viaje de una instrucción

<div class="activity-meta" markdown>
<span>110 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

Vamos a seguir programas pequeños en una máquina de Von Neumann. Primero
**predice en papel** qué ocurrirá; después **compruébalo en el simulador**.
El objetivo es explicar qué cambia en PC, IR, ACC y memoria después de cada
instrucción, no copiar una captura del resultado.

[:material-download: Descargar plantilla editable (.odt)](descargas/Tarea_1_1_1_Ciclo_Instruccion_Apellidos_Nombre.odt){ .md-button .md-button--primary download }
[:material-file-pdf-box: Abrir la actividad en PDF](descargas/Tarea_1_1_1_Ciclo_Instruccion_Apellidos_Nombre.pdf){ .md-button }

## 1. Preparación y reglas

Consulta el [tema 1.1](../11-instrucciones-cpu.md), especialmente los apartados
2 a 6. Los ejemplos resueltos de la teoría utilizan datos diferentes.

[Abrir Von Neumann Machine Simulator](https://vnmsim.c2r0b.ovh/en-us){ .md-button .md-button--primary target="_blank" }

Usaremos exclusivamente esta versión y estas reglas:

- **ACC** es el acumulador; **X, Y y Z** son variables de memoria.
- `LOD X` carga X; `STO Z` guarda ACC en Z; `#n` representa un número literal.
- `JMZ` salta si **ACC = 0**. Z no es una bandera.
- Las direcciones empiezan en **0** y el PC avanza de uno en uno.
- Copia el código sin números delante, comentarios ni líneas vacías adicionales.
- Una fila de la tabla representa **una instrucción terminada**, no un ciclo de reloj.
- Usa **Single iteration** para completar una instrucción y espera a que acabe
  la animación antes de registrar los datos. **Single step** muestra pasos internos.
- `HLT` detiene el programa y, en esta versión, devuelve PC a 0. Anota
  «0; detenido», no «vuelve a ejecutar».
- Para cada programa utiliza **New project**, pega el código y establece sus
  datos iniciales. Comprueba PC = 0, incremento = 1 y ACC = 0.

Distribución orientativa: vídeos y esquema, 15 min; programas A y B, 30 min;
programa C, 30 min; recorrido de una instrucción, 15 min; CPU real, 10 min;
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

## 3. Programa A · Cargar, multiplicar y guardar

Datos iniciales: **X = 4, Y = 3, Z = 0**.

```asm
LOD X
MUL Y
STO Z
HLT
```

Antes de abrir la ejecución, completa tu predicción. Después comprueba cada
fila en el simulador y corrige las diferencias explicando el motivo.

| Dirección ejecutada | Instrucción / IR | ACC al terminar | X | Y | Z | PC al terminar | ¿Qué cambia? |
|---:|---|---|---|---|---|---|---|
| 0 | LOD X | | | | | | |
| 1 | MUL Y | | | | | | |
| 2 | STO Z | | | | | | |
| 3 | HLT | | | | | | |

1. ¿En qué instrucción aparece el resultado en ACC?
2. ¿En cuál se guarda en Z? ¿Qué vale Z justo antes?
3. ¿Se modifican X o Y? Justifica la respuesta.
4. Incluye una captura después de MUL y otra después de STO; explica la diferencia.

## 4. Programa B · Un número literal no es una variable

Datos iniciales: **X = 10, Y = 0, Z = 0**.

```asm
LOD X
SUB #2
ADD #5
STO Z
HLT
```

1. Predice el resultado y completa una tabla como la del programa A, con cinco filas.
2. Ejecútalo por instrucciones y compara con tu predicción.
3. Explica qué significa `#2` y por qué no representa la dirección de una variable.
4. Repite desde el estado inicial con X = 7. ¿Qué instrucciones cambian?
   ¿Qué valores cambian? No necesitas otra captura de todas las filas.

## 5. Programa C · Seguir dos caminos

Este programa compara X e Y. Se ejecuta dos veces, restableciendo el estado
antes de cada prueba:

- **Prueba 1:** X = 9, Y = 9, Z = 0.
- **Prueba 2:** X = 9, Y = 4, Z = 0.

```asm
LOD X
SUB Y
JMZ 5
LOD #1
JMP 6
LOD #0
STO Z
HLT
```

Las direcciones van de 0 a 7: **5 corresponde a LOD #0** y **6 a STO Z**.
No cambies el espaciado entre líneas ni añadas una línea vacía al principio.

1. Sin simular, escribe el orden de direcciones que crees que se ejecutará
   en cada prueba. Una instrucción saltada no lleva fila de ejecución.
2. Completa una traza de cada prueba con dirección ejecutada, IR, ACC, Z y PC
   al terminar. Añade «salta» o «no salta» cuando ejecutes JMZ.
3. Comprueba ambos recorridos con **Single iteration**. Captura el estado
   justo después de JMZ en cada prueba y explica qué valor se ha consultado.
4. ¿Qué significa el valor final de Z? ¿Qué función cumple JMP 6?
5. Explica qué error aparecería al sustituir JMP 6 por una continuación normal
   hacia la dirección 5.

No basta con escribir el valor final: debe quedar claro por qué se ejecutan
unas direcciones y se omiten otras.

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
comprobación de A y B, las dos trazas de C, explicación de STO y ficha de CPU.
En cada traza distingue dirección ejecutada y PC al terminar. Si tu predicción
no coincidió, conserva el error inicial y explica cómo lo corregiste.

Antes de entregar, comprueba que las tablas se leen, que las capturas muestran
el momento indicado y que no has confundido Z con una bandera ni una
instrucción con un ciclo de reloj.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Vídeos y esquema de búsqueda | 1 |
| Programa A: predicción, traza y almacenamiento | 2 |
| Programa B: traza y operandos inmediatos | 1,5 |
| Programa C: dos recorridos y justificación de saltos | 2,5 |
| Explicación de STO e instrucción frente a ciclo | 1,5 |
| Ficha de CPU e interpretación | 1 |
| Claridad y presentación de evidencias | 0,5 |
