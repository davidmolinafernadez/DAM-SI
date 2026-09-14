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

Desde Linux ejecuta `lscpu` y documenta modelo, arquitectura/ISA, sockets,
núcleos, hilos por núcleo, cachés y virtualización. Explica con tus palabras la
diferencia entre socket físico, núcleo e hilo lógico. No publiques número de
serie ni otros identificadores personales.

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
