# P6. Actualizaciones y control de cambios

<div class="lesson-banner" markdown>
<div class="lesson-number">P6</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Actualizaciones y aceptación](../b10-actualizaciones.md)

Duración orientativa: 120 minutos. Trabaja en Ubuntu instalado y conserva un punto de retorno. Una actualización es una operación que se debe comprobar después, no solo una barra de progreso.

## 1. Guarda el estado inicial

Abre **Archivos → Carpeta personal** y comprueba que puedes crear un archivo. En la terminal ejecuta `df -hT` y `uname -r`. Apaga Ubuntu. En el administrador de VirtualBox, selecciona la VM y cambia de **Detalles** a **Instantáneas** mediante su menú de herramientas o vista. Pulsa **Tomar**, escribe `P6-antes-actualizar` y añade fecha y estado observado. Arranca de nuevo.

## 2. Refresca información y lee la propuesta

Pulsa **Ctrl + Alt + T**. Ejecuta `sudo apt update`. Cuando pida la contraseña, escríbela y pulsa **Intro**: normalmente no aparecen puntos ni asteriscos. Es un comportamiento previsto, no una falta de respuesta.

Lee el resultado. Si hay errores de descarga o se usan índices antiguos, no concluyas que la consulta fue correcta. Comprueba conexión, reloj y repositorios. Después ejecuta `apt list --upgradable`. Anota dos paquetes con versión disponible, o registra que no hay actualizaciones si ese es el caso.

## 4. Actualiza y verifica tras reinicio

Ejecuta `sudo apt upgrade`. Antes de aceptar, identifica cuánto se descargará, qué se instalará y si hay dependencias nuevas. No añadas `-y`: queremos leer la propuesta. Cuando termine, revisa si solicita reinicio y utiliza **menú de estado → Apagar/Cerrar sesión → Reiniciar** cuando corresponda.

Vuelve a abrir la terminal y ejecuta `uname -r`. Puede mantenerse si no se actualizó el kernel. Compara una aplicación o paquete seleccionado antes y después; no inventes un cambio para que la tabla parezca completa.

## 4. Instala una herramienta y comprueba su uso

```bash
apt show tree
sudo apt install tree
tree --version
mkdir -p ~/ud3-arbol/proyecto/src
tree ~/ud3-arbol
```

`apt show` permite inspeccionar el paquete antes de instalarlo. `tree --version` comprueba que el programa responde y `tree` sobre una ruta propia demuestra un uso real. No necesitas aplicar `full-upgrade`, `purge` o `autoremove` para terminar.

## 5. Incidencia y entrega

Con la VM de pruebas, desconecta únicamente su cable virtual: menú de la VM **Dispositivos → Red → Conectar adaptador** si existe, o control de red equivalente. Ejecuta `apt update`, conserva el mensaje, reconecta y repite. No borres los archivos de bloqueo de APT si otra actualización está trabajando.

Entrega tabla antes/después, propuesta interpretada, reinicio cuando proceda y comprobación de tree. Añade una explicación de `update` frente a `upgrade` y por qué el número del kernel no cambia siempre.

## Qué debes entregar

Entrega **un único informe PDF**, llamado `P6_Apellidos_Nombre.pdf`, que documente la práctica de principio a fin con **una sucesión ordenada de capturas de pantalla propias y una pequeña explicación de cada paso**. Toma las capturas mientras trabajas e insértalas junto al paso correspondiente; utiliza la lista de abajo para no olvidar las pruebas necesarias.

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
| P6-01 | Estado inicial: archivo de prueba, espacio libre y kernel | Valores previos y por qué interesa registrarlos antes de actualizar. |
| P6-02 | Instantánea `P6-antes-actualizar` | Nombre, fecha, VM y estado que permite recuperar. |
| P6-03 | Resultado de `sudo apt update` | Si se han podido refrescar los índices y si hay avisos o errores. |
| P6-04 | `apt list --upgradable` y propuesta de `sudo apt upgrade` antes de aceptar | Dos paquetes y sus versiones si aparecen, volumen de descarga y cambios propuestos. Si no hay actualizaciones, documenta ese resultado real. |
| P6-05 | Final de la actualización y reinicio cuando proceda | Resultado de la operación y si se solicitó reiniciar. |
| P6-06 | Kernel y paquete elegido después de actualizar | Comparación con los valores previos, aunque no cambien. |
| P6-07 | Consulta, instalación y versión de `tree` | Qué paquete has inspeccionado, resultado de instalación y versión que responde. |
| P6-08 | Uso de `tree` sobre la carpeta de prueba | Qué estructura aparece y por qué demuestra un uso real. |
| P6-09 | Fallo de consulta con cable virtual desconectado y repetición tras reconectar | Mensaje observado, causa comprobada y resultado posterior. Usa dos capturas. |

**Incluye además:** tabla antes/después con kernel y paquete seleccionado (versiones reales y capturas), interpretación de la propuesta, diferencia entre `update` y `upgrade` y explicación de por qué el kernel puede mantenerse. Documenta también la incidencia de red y su resolución.

**Ejemplo de pie:** «P6-06. Después de actualizar, `uname -r` devuelve [valor]. Al compararlo con [valor anterior], observo [cambio o ausencia de cambio]. Compruebo también la versión del paquete seleccionado». No inventes actualizaciones ni reinicios.

### Antes de entregar

Guarda las capturas en la carpeta de evidencias autorizada, fuera de la VM que puedas restaurar. Numéralas como en la tabla; si necesitas varias para un punto, utiliza `a`, `b`, etc. Deben verse los valores y mensajes necesarios, sin contraseñas ni claves. Si una pantalla cambia según la versión, documenta la equivalente y explícalo; si un paso no puede completarse, registra el error y la comprobación pendiente.

Revisa que el PDF incluya todos los pasos, que sus imágenes se lean y que cada una tenga explicación. **Sube el informe PDF a la tarea de la práctica en Aules; las capturas deben ir dentro del informe.** No subas capturas sueltas, ISO, VDI ni OVA. Las respuestas y tablas de esta práctica van en el mismo PDF y no generan otra entrega.
