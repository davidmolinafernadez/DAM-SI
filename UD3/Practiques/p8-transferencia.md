# P8. Clonar, exportar e importar con comprobación

<div class="lesson-banner" markdown>
<div class="lesson-number">P8</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Hardware virtual y recursos](../b06-hardware-virtual.md) · [Recuperación y transferencia](../b11-recuperacion.md)

Duración orientativa: 150 minutos. Antes de comenzar, mide espacio libre para copia, paquete e importación. No borres el único original antes de probar otra copia.

## 1. Crea un clon completo

Apaga Ubuntu y comprueba su estado en VirtualBox. Si tiene conectado el disco de datos que no se necesita, retíralo desde **Configuración → Almacenamiento** sin borrar el archivo VDI. Selecciona el origen → botón derecho → **Clonar**. Si esa acción aparece en **Máquina** en tu versión, utiliza la misma función.

Escribe `UD3-Ubuntu-Clon-codigo` y selecciona **Clon completo**. En política de direcciones MAC elige generar nuevas direcciones para los adaptadores necesarios. Selecciona el estado que vas a clonar y registra qué se incluirá. Completa el asistente y espera a la creación del disco independiente.

## 2. Evita identidades repetidas

Antes de iniciar origen y clon simultáneamente, revisa **Configuración → Red → Avanzadas → Dirección MAC** en cada uno. Si hay IP fija, debe ser diferente en el clon. Puedes arrancarlo con red desconectada para ajustar la identidad sin conflicto.

Dentro del clon, abre **Configuración → Sistema → Acerca de**, o la sección **Acerca de** que incluya **Nombre del dispositivo**, y cambia su nombre si la interfaz lo permite. La alternativa de terminal acordada es `sudo hostnamectl set-hostname ud3-clon-codigo`. Reinicia y comprueba con `hostnamectl`. En la conexión de laboratorio modifica la IPv4 mediante el engranaje de **Red**, igual que en P5.

Crea `~/archivo-del-clon.txt` solamente en el clon. Apágalo, arranca el origen y comprueba que ese archivo no aparece allí. Esta prueba acredita independencia de escrituras, pero ambas VM pueden seguir dependiendo del mismo SSD físico.

## 3. Exporta el estado elegido

Apaga el origen. En el administrador abre **Archivo → Exportar servicio virtualizado** o **Exportar máquina/appliance**, según la traducción. Selecciona únicamente Ubuntu, pulsa **Siguiente** y elige archivo **OVA** en la ubicación indicada. Registra versión del hipervisor, firmware, RAM, CPU, discos, red y archivo testigo antes de exportar.

Revisa los datos del paquete y confirma. No añadas credenciales personales. Un paquete de intercambio no garantiza conservar historia de instantáneas, secretos de TPM o todas las funciones de una plataforma.

## 4. Importa y revisa antes de iniciar

Abre **Archivo → Importar servicio virtualizado**. Selecciona el OVA, pulsa **Siguiente** y revisa la configuración propuesta. Cambia el nombre a `UD3-Ubuntu-Importada-codigo`, ajusta recursos al puesto y revisa la política de MAC. Comprueba la carpeta de destino para no confundirla con el origen.

Pulsa **Importar** y espera. Con la máquina todavía apagada, comprueba firmware, controlador de disco y adaptador de red. Arranca y verifica usuario, versión, archivo testigo y una aplicación o servicio. Si no puedes guardar origen e importación a la vez, el docente puede proporcionar otro equipo para importar; no se sacrifica la única copia válida para hacer sitio.

## 5. Entrega y diagnóstico

Entrega comparación origen/clon/importación, nuevas identidades, estado elegido, tamaño del paquete y resultados de pruebas. **Incidencia:** dos invitados conservan la misma IP estática aunque sus MAC sean diferentes. Explica qué campo debes revisar y por qué generar MAC nuevas no cambió esa configuración del sistema.

## Entrega independiente de la práctica

Guarda `P8_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.

<div class="video-card" markdown>

## Vídeo explicativo · Instantáneas de VirtualBox

V4: compara retorno de estado y copia independiente. En P7 tomamos la instantánea apagada.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/zgauof85771q51t9/fs" title="Instantáneas de VirtualBox" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/zgauof85771q51t9) · [Ficha y preguntas de visionado](../videos.md)

</div>
