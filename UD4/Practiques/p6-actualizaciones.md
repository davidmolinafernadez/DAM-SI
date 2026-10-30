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
mkdir -p ~/ud4-arbol/proyecto/src
tree ~/ud4-arbol
```

`apt show` permite inspeccionar el paquete antes de instalarlo. `tree --version` comprueba que el programa responde y `tree` sobre una ruta propia demuestra un uso real. No necesitas aplicar `full-upgrade`, `purge` o `autoremove` para terminar.

## 5. Incidencia y entrega

Con la VM de pruebas, desconecta únicamente su cable virtual: menú de la VM **Dispositivos → Red → Conectar adaptador** si existe, o control de red equivalente. Ejecuta `apt update`, conserva el mensaje, reconecta y repite. No borres los archivos de bloqueo de APT si otra actualización está trabajando.

Entrega tabla antes/después, propuesta interpretada, reinicio cuando proceda y comprobación de tree. Añade una explicación de `update` frente a `upgrade` y por qué el número del kernel no cambia siempre.

## Entrega independiente de la práctica

Guarda `P6_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.
