# Tarea 1.1.1 · Viaje de una instrucción

<div class="activity-meta" markdown>
<span>110 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

[:material-download: **Descargar actividad editable para LibreOffice (.odt)**](descargas/Tarea_1_1_1_Ciclo_Instruccion_Apellidos_Nombre.odt){ .md-button .md-button--primary download }
[:material-file-pdf-box: **Abrir o descargar en PDF**](descargas/Tarea_1_1_1_Ciclo_Instruccion_Apellidos_Nombre.pdf){ .md-button }

Descarga el documento, guárdalo en tu equipo, sustituye `Apellidos_Nombre` por
tus datos y complétalo con LibreOffice Writer. La entrega se realiza en Aules.

## Programa simulado

```text
Dirección  Instrucción
100        LOAD R1, [500]
104        ADD  R1, R2
108        STORE [504], R1
112        JZ   200
```

Estado inicial: `PC=100`, memoria `[500]=7`, `R2=-7` y bandera `Z=0`.

## Trabajo

### Parte A · Radiografía de la CPU del equipo

Realiza esta parte desde **Windows** siguiendo los pasos de abajo. Si utilizas
Linux, puedes obtener los datos con `lscpu`. Documenta modelo, arquitectura/ISA,
sockets, núcleos, hilos por núcleo, cachés y virtualización. Explica con tus
palabras la diferencia entre socket físico, núcleo e hilo lógico. No publiques
números de serie ni otros identificadores personales.

#### En Windows: Administrador de tareas

1. Pulsa **Ctrl + Mayús + Esc** para abrir el Administrador de tareas.
2. Si aparece la vista reducida, pulsa **Más detalles**.
3. Entra en **Rendimiento → CPU**.
4. Anota el modelo que aparece en la parte superior y los valores de **Sockets**,
   **Núcleos**, **Procesadores lógicos**, **Virtualización** y **Caché L1, L2 y L3**
   que se muestren debajo del gráfico. Amplía la ventana si es necesario.
5. Incluye una captura de ese panel y explica los datos. Si algún campo no
   aparece, escribe «no mostrado» y completa lo posible con PowerShell.

#### En Windows: completar los datos con PowerShell

Busca **PowerShell** en Inicio y ábrelo. Copia y ejecuta este comando de consulta:

```powershell
Get-CimInstance Win32_Processor |
    Select-Object Name, Architecture, SocketDesignation, NumberOfCores,
        NumberOfLogicalProcessors, L2CacheSize, L3CacheSize,
        VirtualizationFirmwareEnabled |
    Format-List
```

Interpreta la salida así:

- **Name:** modelo del procesador.
- **Architecture:** 9 significa x64 (x86-64), 12 significa ARM64 y 0 significa
  x86. No confundas la arquitectura de la CPU con la versión de Windows.
- **SocketDesignation:** etiqueta del socket informada por el firmware, no su
  cantidad. Para el recuento utiliza Sockets en el Administrador de tareas.
- **NumberOfCores / NumberOfLogicalProcessors:** núcleos y procesadores lógicos
  del procesador mostrado. Si aparecen varios bloques, interpreta cada uno.
- **L2CacheSize / L3CacheSize:** tamaños informados en KB. Para L1 utiliza el
  Administrador de tareas. Un valor vacío o 0 no permite asegurar por sí solo
  que esa caché no exista; anótalo como «no informado» si no puedes confirmarlo.
- **VirtualizationFirmwareEnabled:** indica si la virtualización está habilitada
  en el firmware. Contrasta el resultado con el panel de CPU; en entornos
  virtualizados la información puede estar limitada.

**Hilos por núcleo:** en una CPU de topología uniforme, divide procesadores
lógicos entre núcleos. Por ejemplo, 16 lógicos ÷ 8 núcleos = 2 hilos por núcleo.
En procesadores híbridos esa división puede ser solo un promedio: si obtienes
20 lógicos y 14 núcleos, no escribas «1,43 hilos por núcleo». Indica ambos
recuentos y que los núcleos pueden tener distinta capacidad de hilos; consulta
la ficha oficial del modelo si necesitas el desglose.

Un **socket físico** es el conector de la placa donde se instala el procesador;
un **núcleo** es una unidad física de procesamiento; un **hilo lógico** es un
contexto que el sistema operativo puede planificar. Los hilos de un mismo núcleo
comparten recursos y no equivalen a núcleos físicos independientes.

Indica si utilizas Windows directamente o dentro de una máquina virtual.
Recorta las capturas al panel necesario. El comando selecciona únicamente los
campos de la actividad, sin pedir números de serie ni identificadores de CPU.

Referencia: [propiedades de Win32_Processor, Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-processor).


### Parte B · Sigue el programa

1. Completa por instrucción: `PC inicial`, búsqueda, decodificación, ejecución,
   escritura, `PC final` y banderas.
2. Señala cuándo intervienen `MAR` y `MDR` y cuándo no.
3. Dibuja el recorrido de una instrucción con acceso a memoria.
4. Explica si se toma el salto y cuál será la dirección siguiente.
5. Diferencia instrucción, etapa de *pipeline* y ciclo de reloj.

### Parte C · Pipeline y rendimiento

1. Representa las cuatro instrucciones en un pipeline de cinco etapas.
2. Marca la dependencia de datos entre `LOAD` y `ADD` y explica una solución.
3. Supón que el salto se predice como no tomado. Explica qué debe descartarse si
   finalmente se toma.
4. Razona por qué una CPU de 4 GHz no ejecuta necesariamente cuatro mil millones
   de instrucciones completas por segundo.
5. Relaciona el recorrido con una aplicación Java: fuente, bytecode, JIT, código
   máquina y llamada al sistema.

## Entrega

PDF de 4–6 páginas, `Tarea_1_1_1_Apellidos_Nombre.pdf`, con tabla, diagrama propio y
explicación. Una captura sin interpretación no sirve como evidencia.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Inventario e interpretación de la CPU | 1,5 |
| Secuencia, PC y banderas | 2,5 |
| Registros y accesos a memoria | 2 |
| Pipeline, riesgos y rendimiento | 2 |
| Relación con Java y diagrama | 1,5 |
| Presentación | 0,5 |
