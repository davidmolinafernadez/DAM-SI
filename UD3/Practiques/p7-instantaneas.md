# P7. Instantáneas: recuperar y delimitar la pérdida

<div class="lesson-banner" markdown>
<div class="lesson-number">P7</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Recuperación y transferencia](../b11-recuperacion.md)

Duración orientativa: 120 minutos. Usaremos archivos dentro del disco del invitado, no una carpeta compartida, para que la restauración tenga un alcance claro.

## 1. Prepara un estado que puedas reconocer

En Ubuntu pulsa **Ctrl + Alt + T** y ejecuta:

```bash
mkdir -p ~/ud3-recuperacion
printf 'ESTADO A\n' > ~/ud3-recuperacion/estado.txt
cat ~/ud3-recuperacion/estado.txt
```

Apaga desde Ubuntu. En VirtualBox comprueba **Apagada**. Selecciona esta VM, abre la vista **Instantáneas** y pulsa **Tomar**. Escribe `P7-A` y una descripción: «estado.txt contiene A; posterior.txt no existe». Confirma. Así defines un criterio que luego podrás verificar.

## 2. Introduce un cambio controlado

Arranca Ubuntu y ejecuta:

```bash
printf 'ESTADO B\n' > ~/ud3-recuperacion/estado.txt
printf 'Creado después de P7-A\n' > ~/ud3-recuperacion/posterior.txt
ls -l ~/ud3-recuperacion
cat ~/ud3-recuperacion/estado.txt
```

Guarda las capturas y notas que necesites fuera del estado que vas a restaurar: por ejemplo, mediante la carpeta de evidencias aprobada. Escribe antes del retorno qué esperas encontrar y qué esperas perder.

## 4. Restaura la instantánea correcta

Apaga Ubuntu. En el administrador selecciona la VM → **Instantáneas**. Haz clic en `P7-A`, no en el estado actual, y pulsa **Restaurar** o utiliza botón derecho → **Restaurar instantánea**. Lee el diálogo: puede ofrecer crear una instantánea del estado actual antes del retorno. Anota si conservas ese estado adicional y por qué.

No pulses **Eliminar** pensando que significa volver. Tampoco borres manualmente archivos de la carpeta `Snapshots`. Confirma la restauración elegida y arranca.

## 4. Comprueba y explica

Abre la terminal, lista la carpeta y lee estado.txt. Debe corresponder al estado A; posterior.txt no formaba parte de ese punto de retorno. Si el resultado difiere, comprueba nombre de la instantánea, ruta de archivos y si realmente trabajaste dentro del disco del invitado.

Crea después un estado C y explica cómo continúa el trabajo. Desde el administrador abre la carpeta de la VM para observar su ocupación, sin editar sus componentes. Una cadena de instantáneas puede crecer aunque sus nombres sugieran «fotos» pequeñas.

Entrega predicción, evidencias de A/B y resultado de restauración. Explica una avería que esta operación no cubre. El experimento opcional con una carpeta compartida se realiza solo en una carpeta vacía de prueba: los archivos externos no retroceden al restaurar el invitado.

## Qué debes entregar

Entrega **un único informe PDF**, llamado `P7_Apellidos_Nombre.pdf`, que documente la práctica de principio a fin con **una sucesión ordenada de capturas de pantalla propias y una pequeña explicación de cada paso**. Toma las capturas mientras trabajas e insértalas junto al paso correspondiente; utiliza la lista de abajo para no olvidar las pruebas necesarias.

### Estructura del informe

1. **Portada:** práctica, nombre y apellidos, grupo, fecha, VM utilizada y sistema anfitrión.
2. **Preparación:** estado inicial, materiales y configuración necesarios.
3. **Proceso paso a paso:** sigue el orden de los apartados de esta guía. En cada paso escribe qué has hecho, añade la captura o capturas y explica el resultado observado en 2–4 líneas. Si una decisión no genera una pantalla propia, escríbela igualmente.
4. **Comprobaciones finales:** presenta las pruebas solicitadas y sus resultados; una barra de progreso o un escritorio por sí solos no acreditan todas las comprobaciones.
5. **Incidencias y conclusión:** responde al caso planteado y registra los problemas reales, las pruebas y su resultado. Si no hubo problemas reales, indícalo. Explica qué has conseguido y qué queda pendiente.

**Modelo para repetir en cada paso:**

- **Paso y título:** [número y acción].
- **Acción realizada:** [qué has hecho y qué opción o comando has utilizado].
- **Captura:** [inserta aquí la imagen propia con su código].
- **Explicación:** [qué se ve, por qué has elegido esa opción y qué demuestra el resultado].

### Capturas y explicaciones que debe contener

| Captura | Momento del proceso | Explicación que debes escribir |
| --- | --- | --- |
| P7-01 | Carpeta de prueba y lectura de `estado.txt` con A | Ruta dentro del disco del invitado y contenido inicial. |
| P7-02 | VM apagada e instantánea `P7-A` con descripción | Qué estado se ha guardado y qué archivo aún no existe. |
| P7-03 | Estado B y archivo `posterior.txt` | Qué ha cambiado después de tomar la instantánea. |
| P7-04 | Evidencias conservadas fuera del invitado y predicción escrita antes de restaurar | Qué esperas recuperar, qué esperas perder y dónde has guardado el informe para conservarlo. |
| P7-05 | Selección de `P7-A` y diálogo de restauración | Qué punto restauras y si conservas otra instantánea del estado actual. |
| P7-06 | Carpeta y contenido después de restaurar | Si vuelve A y si desaparece `posterior.txt`; compara con tu predicción. |
| P7-07 | Nuevo estado C y ocupación de la carpeta de la VM | Cómo continúa el trabajo y qué observas sobre el espacio utilizado, sin editar componentes de la VM. |

**Incluye además:** tabla con filas para `estado.txt` y `posterior.txt`, y columnas «estado A», «estado B», «predicción» y «resultado tras restaurar». Explica una avería que una instantánea no cubre. Si haces el experimento opcional de carpeta compartida, añade su captura y explica por qué los archivos externos no retroceden.

**Ejemplo de pie:** «P7-06. Tras restaurar `P7-A`, `estado.txt` vuelve a contener A y `posterior.txt` ya no aparece. Coincide con mi predicción porque ambos cambios posteriores estaban en el disco del invitado». Escribe el resultado real si difiere y documenta qué has revisado.

### Antes de entregar

Guarda las capturas en la carpeta de evidencias autorizada, fuera de la VM que puedas restaurar. Numéralas como en la tabla; si necesitas varias para un punto, utiliza `a`, `b`, etc. Deben verse los valores y mensajes necesarios, sin contraseñas ni claves. Si una pantalla cambia según la versión, documenta la equivalente y explícalo; si un paso no puede completarse, registra el error y la comprobación pendiente.

Revisa que el PDF incluya todos los pasos, que sus imágenes se lean y que cada una tenga explicación. **Sube el informe PDF a la tarea de la práctica en Aules; las capturas deben ir dentro del informe.** No subas capturas sueltas, ISO, VDI ni OVA. Las respuestas y tablas de esta práctica van en el mismo PDF y no generan otra entrega.
<div class="video-card" markdown>

## Vídeo explicativo · Instantáneas de VirtualBox

V4: compara retorno de estado y copia independiente. En P7 tomamos la instantánea apagada.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/zgauof85771q51t9/fs" title="Instantáneas de VirtualBox" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/zgauof85771q51t9) · [Ficha y preguntas de visionado](../videos.md)

</div>
