# Tarea 2.2 · Comparativa de gestión de procesos

<div class="lesson-banner" markdown>
<div class="lesson-number">2.2</div>
<div markdown>
**¿Cómo organizan el trabajo Windows, GNU/Linux y macOS?**

Compara sus mecanismos de gestión de procesos y explica cómo se relacionan
con memoria, entrada/salida, archivos y dispositivos.
</div>
</div>

<div class="activity-meta" markdown>
<span>110 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

## Objetivo y producto final

Entrega `Tarea_2_2_Apellidos_Nombre.pdf`, con una tabla comparativa, respuestas
razonadas, los casos prácticos y las fuentes utilizadas. Extensión orientativa:
4–6 páginas. Usa vocabulario propio y ejemplos concretos; no basta copiar
una definición en las tres columnas.

Compara **Windows, GNU/Linux (una distribución concreta, como Ubuntu) y macOS**.
Indica la versión estudiada de cada uno y, en GNU/Linux, la versión del kernel
si haces afirmaciones sobre su planificador. No es necesario instalar los tres:
puedes combinar observación del sistema disponible con investigación documental.
Distingue siempre lo observado de lo consultado. Android o iOS pueden añadirse
como ampliación voluntaria, sin sustituir las tres plataformas principales.

## Fase 1 · Sitúa los sistemas (10 min)

Anota sistema, versión, herramienta de observación y fuente principal. Consulta
al menos una fuente oficial por plataforma. Si una documentación es histórica,
indica su fecha y úsala para conceptos, sin atribuir automáticamente todos sus
detalles a una versión actual.

## Fase 2 · Investiga y compara (45 min)

Responde a las siguientes preguntas **para cada sistema**. Puedes desarrollar
las respuestas debajo de la tabla y utilizar esta como resumen.

| Aspecto | Windows | GNU/Linux | macOS |
|---|---|---|---|
| Versión y herramienta consultada | | | |
| Estados de proceso o hilo y cómo se observan | | | |
| Unidad de planificación, prioridades y reparto de CPU | | | |
| Creación de procesos y relación padre-hijo | | | |
| Finalización normal, forzada y código de salida | | | |
| Sincronización y comunicación | | | |
| Multitarea, concurrencia y paralelismo | | | |
| Relación con memoria, archivos y dispositivos | | | |

### 1. Estados del proceso

- ¿Qué significan preparado, en ejecución y bloqueado? Relaciona estos estados
  con los nombres que usa la documentación o herramienta de cada SO.
- ¿La herramienta muestra el estado del proceso completo o el de sus hilos?
  ¿Por qué no siempre existe una equivalencia exacta con el modelo de cinco estados?
- Cuando una tarea espera una lectura de disco, ¿qué transición puede producirse?
  ¿Vuelve directamente a ejecutar al terminar la lectura?
- Distingue espera, suspensión y finalización. Investiga qué significa zombi en
  Unix y por qué no es sinónimo de aplicación bloqueada.

### 2. Planificación

- ¿Qué entidad recibe CPU: proceso, hilo o tarea planificable? Explica el vocabulario.
- ¿Cómo influyen las prioridades y cuándo puede retirarse la CPU a una tarea?
- ¿Qué intenta equilibrar el sistema: respuesta, reparto justo o rendimiento?
  Cita una característica documentada para la versión elegida.
- ¿Por qué no es correcto afirmar sin matices que todos usan únicamente Round Robin?
  En GNU/Linux, distingue la clase de planificación normal de las de tiempo real;
  no atribuyas CFS o EEVDF a cualquier kernel sin comprobarlo.

### 3. Creación y finalización

- ¿Cómo se crea un proceso? Identifica una API o mecanismo de cada plataforma
  y explica qué recursos inicializa. Distingue la API del comando del usuario.
- Compara `CreateProcess` con el modelo `fork`/`exec` y consulta `posix_spawn`
  donde corresponda. ¿Crear un hilo equivale a crear un proceso?
- ¿Qué diferencia hay entre cerrar normalmente y forzar la terminación?
  ¿Qué puede ocurrir con los datos sin guardar?
- ¿Para qué sirve el código de salida? ¿Cómo puede el proceso que lanzó otro
  conocer su finalización? No supongas que cerrar una ventana termina todos sus hijos.

### 4. Sincronización

- Identifica mecanismos disponibles: mutex, semáforos, variables de condición,
  operaciones atómicas u otros documentados. Explica dos por plataforma.
- ¿Cómo protegerías un contador compartido entre dos hilos? ¿Y cómo limitarías
  a tres el número de tareas que usan simultáneamente un recurso?
- ¿Qué diferencia hay entre condición de carrera e interbloqueo? Incluye un
  ejemplo y una medida para evitar cada problema.
- ¿Cómo pueden comunicarse dos procesos? Cita un mecanismo y distingue
  comunicación de exclusión mutua.

### 5. Multitarea

- ¿Es apropiativa o cooperativa? Explica quién decide ceder o retirar la CPU.
- ¿Cómo pueden progresar navegador, reproductor de audio y editor en un equipo
  con un único procesador lógico? ¿Qué cambia al disponer de varios?
- ¿Muchos procesos abiertos garantizan paralelismo? ¿Un hilo esperando E/S
  necesita ocupar continuamente la CPU?

## Fase 3 · Aplica lo investigado (30 min)

### Caso A · Turnos de CPU

A y B llegan en el instante 0; A necesita 5 ms y B, 3 ms. A entra primero.
No hay E/S y se ignora el coste de cambio de contexto.

1. Dibuja la ejecución con FCFS y con Round Robin de quantum 2 ms.
2. Calcula primera respuesta, espera y retorno de ambos procesos en cada política.
3. Explica qué mejora y qué coste podría aparecer al reducir el quantum.
4. Aclara por qué esta simulación no identifica el algoritmo completo de ninguno
   de los tres sistemas reales.

### Caso B · Abrir, guardar e imprimir

Un usuario abre un PDF desde una memoria USB, lo imprime y cierra el visor.
Describe la intervención de procesos e hilos, memoria, archivos, E/S y
controladores. Explica por qué la impresión puede continuar tras cerrar el visor,
qué tarea podría estar bloqueada y por qué debe completarse la escritura
pendiente antes de retirar una unidad. Relaciona el caso con cada plataforma:
indica una herramienta o servicio documentado que permita observar alguna fase.

### Caso C · Dos actualizaciones al mismo dato

Dos hilos leen un contador con valor 10 y cada uno intenta incrementarlo.
Muestra una secuencia que termine en 11, explica por qué es incorrecta y
propón una protección. Después plantea un interbloqueo con dos recursos y
explica cómo un orden común de adquisición evita ese caso.

## Fase 4 · Evidencia y conclusión (25 min)

En el sistema que tengas disponible, abre una aplicación sencilla propia,
localiza su PID, observa sus hilos si la herramienta lo permite y ciérrala
normalmente. Incluye dos capturas legibles o registros equivalentes, antes y
después, con herramienta y versión. No fuerces el cierre de procesos del sistema.
Si no dispones de un entorno para la práctica, sustituye esta evidencia por
un ejemplo documentado, con enlace y explicación, identificado como documental.

Herramientas orientativas: Administrador de tareas o `Get-Process` en Windows;
monitor del sistema, `ps` o `top` en GNU/Linux; Monitor de Actividad en macOS.
Un 0 % de CPU no permite distinguir por sí solo preparado de bloqueado.
`CPU` de `Get-Process` son segundos acumulados; `%cpu` de `ps` tampoco es
necesariamente una medida instantánea comparable con otros monitores.

Concluye con **tres semejanzas, tres diferencias documentadas y una limitación**
de tu investigación. Explica qué mecanismos ayudan a que el equipo responda
mientras hay tareas esperando E/S. No se pide elegir un “ganador” por popularidad.

## Fuentes de partida

- [Microsoft Learn · Procesos e hilos](https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads).
- [Microsoft Learn · Planificación](https://learn.microsoft.com/en-us/windows/win32/procthread/scheduling).
- [Linux · Documentación del planificador](https://docs.kernel.org/scheduler/index.html).
- [Linux · EEVDF](https://docs.kernel.org/scheduler/sched-eevdf.html).
- [Manuales Linux · fork](https://man7.org/linux/man-pages/man2/fork.2.html) y [wait](https://man7.org/linux/man-pages/man2/wait.2.html).
- [Apple · Mach: tareas, hilos y comunicación](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Mach/Mach.html) (documentación de archivo).
- [Apple · Guía de Monitor de Actividad](https://support.apple.com/es-es/guide/activity-monitor/welcome/mac).

Para cada fuente utilizada, anota título, enlace, fecha de consulta y qué
respuesta respalda. Si no encuentras un detalle verificable, decláralo como
no confirmado en lugar de inventarlo.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Estados y transiciones comparados correctamente | 1,5 |
| Planificación y caso de reparto de CPU | 2 |
| Creación y finalización de procesos | 1,5 |
| Sincronización, carrera e interbloqueo | 1,5 |
| Multitarea, concurrencia y paralelismo | 1 |
| Integración de memoria, archivos, E/S y dispositivos | 1 |
| Evidencia, fuentes, versiones y conclusión comparativa | 1,5 |
| **Total** | **10** |
