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

## 4. Exporta el estado elegido

Apaga el origen. En el administrador abre **Archivo → Exportar servicio virtualizado** o **Exportar máquina/appliance**, según la traducción. Selecciona únicamente Ubuntu, pulsa **Siguiente** y elige archivo **OVA** en la ubicación indicada. Registra versión del hipervisor, firmware, RAM, CPU, discos, red y archivo testigo antes de exportar.

Revisa los datos del paquete y confirma. No añadas credenciales personales. Un paquete de intercambio no garantiza conservar historia de instantáneas, secretos de TPM o todas las funciones de una plataforma.

## 4. Importa y revisa antes de iniciar

Abre **Archivo → Importar servicio virtualizado**. Selecciona el OVA, pulsa **Siguiente** y revisa la configuración propuesta. Cambia el nombre a `UD3-Ubuntu-Importada-codigo`, ajusta recursos al puesto y revisa la política de MAC. Comprueba la carpeta de destino para no confundirla con el origen.

Pulsa **Importar** y espera. Con la máquina todavía apagada, comprueba firmware, controlador de disco y adaptador de red. Arranca y verifica usuario, versión, archivo testigo y una aplicación o servicio. Si no puedes guardar origen e importación a la vez, el docente puede proporcionar otro equipo para importar; no se sacrifica la única copia válida para hacer sitio.

## 5. Entrega y diagnóstico

Entrega comparación origen/clon/importación, nuevas identidades, estado elegido, tamaño del paquete y resultados de pruebas. **Incidencia:** dos invitados conservan la misma IP estática aunque sus MAC sean diferentes. Explica qué campo debes revisar y por qué generar MAC nuevas no cambió esa configuración del sistema.

## Qué debes entregar

Entrega **un único informe PDF**, llamado `P8_Apellidos_Nombre.pdf`, que documente la práctica de principio a fin con **una sucesión ordenada de capturas de pantalla propias y una pequeña explicación de cada paso**. Toma las capturas mientras trabajas e insértalas junto al paso correspondiente; utiliza la lista de abajo para no olvidar las pruebas necesarias.

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
| P8-01 | Espacio disponible y origen apagado | Si cabe el clon, el OVA y la importación, y cómo has identificado el origen. |
| P8-02 | Asistente de clonación | Nombre y destino, clon completo, política de MAC y estado elegido. |
| P8-03 | MAC y nombre del equipo en origen y clon; IP si procede | Qué identidades has cambiado y qué configuración de red has comprobado. |
| P8-04 | Archivo creado solo en el clon y comprobación en el origen | Ruta y contenido en el clon y prueba de ausencia en el origen; usa dos capturas. |
| P8-05 | Estado y configuración del origen antes de exportar | Firmware, recursos, discos, red y archivo testigo que esperas recuperar. |
| P8-06 | Asistente de exportación y OVA generado | VM seleccionada, destino, nombre del paquete y tamaño final. |
| P8-07 | Asistente de importación y revisión con la VM apagada | Nombre, carpeta, recursos, política de MAC, firmware, controlador y red. |
| P8-08 | Arranque de la importada | Usuario, versión, archivo testigo y funcionamiento de una aplicación o servicio. Usa las imágenes necesarias. |

**Incluye además:** tabla comparativa de origen, clon e importación con nombre de VM, nombre del equipo, MAC, IP/modo de red, recursos, carpeta, archivo testigo y resultado de arranque. Indica qué estado exportaste y el tamaño del OVA. Responde a la incidencia de IP estática repetida aunque las MAC sean distintas.

**Ejemplo de pie:** «P8-04. El archivo [ruta] existe en el clon y no aparece al comprobar la misma ruta en el origen. La prueba muestra independencia de escrituras; ambas VM todavía pueden estar en el mismo disco físico». Incluye las dos comprobaciones reales.

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
