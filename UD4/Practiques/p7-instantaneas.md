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
mkdir -p ~/ud4-recuperacion
printf 'ESTADO A\n' > ~/ud4-recuperacion/estado.txt
cat ~/ud4-recuperacion/estado.txt
```

Apaga desde Ubuntu. En VirtualBox comprueba **Apagada**. Selecciona esta VM, abre la vista **Instantáneas** y pulsa **Tomar**. Escribe `P7-A` y una descripción: «estado.txt contiene A; posterior.txt no existe». Confirma. Así defines un criterio que luego podrás verificar.

## 2. Introduce un cambio controlado

Arranca Ubuntu y ejecuta:

```bash
printf 'ESTADO B\n' > ~/ud4-recuperacion/estado.txt
printf 'Creado después de P7-A\n' > ~/ud4-recuperacion/posterior.txt
ls -l ~/ud4-recuperacion
cat ~/ud4-recuperacion/estado.txt
```

Guarda las capturas y notas que necesites fuera del estado que vas a restaurar: por ejemplo, mediante la carpeta de evidencias aprobada. Escribe antes del retorno qué esperas encontrar y qué esperas perder.

## 4. Restaura la instantánea correcta

Apaga Ubuntu. En el administrador selecciona la VM → **Instantáneas**. Haz clic en `P7-A`, no en el estado actual, y pulsa **Restaurar** o utiliza botón derecho → **Restaurar instantánea**. Lee el diálogo: puede ofrecer crear una instantánea del estado actual antes del retorno. Anota si conservas ese estado adicional y por qué.

No pulses **Eliminar** pensando que significa volver. Tampoco borres manualmente archivos de la carpeta `Snapshots`. Confirma la restauración elegida y arranca.

## 4. Comprueba y explica

Abre la terminal, lista la carpeta y lee estado.txt. Debe corresponder al estado A; posterior.txt no formaba parte de ese punto de retorno. Si el resultado difiere, comprueba nombre de la instantánea, ruta de archivos y si realmente trabajaste dentro del disco del invitado.

Crea después un estado C y explica cómo continúa el trabajo. Desde el administrador abre la carpeta de la VM para observar su ocupación, sin editar sus componentes. Una cadena de instantáneas puede crecer aunque sus nombres sugieran «fotos» pequeñas.

Entrega predicción, evidencias de A/B y resultado de restauración. Explica una avería que esta operación no cubre. El experimento opcional con una carpeta compartida se realiza solo en una carpeta vacía de prueba: los archivos externos no retroceden al restaurar el invitado.

## Entrega independiente de la práctica

Guarda `P7_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.

<div class="video-card" markdown>

## Vídeo explicativo · Instantáneas de VirtualBox

V4: compara retorno de estado y copia independiente. En P7 tomamos la instantánea apagada.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/zgauof85771q51t9/fs" title="Instantáneas de VirtualBox" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/zgauof85771q51t9) · [Ficha y preguntas de visionado](../videos.md)

</div>
