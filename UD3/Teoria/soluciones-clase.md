# UD3 · Ejercicios resueltos para trabajar en clase

**Sin entrega y sin calificación independiente.** El docente selecciona los casos que necesita, plantea las preguntas y despliega la solución para comentarla. No hay que completar todo este banco ni subir archivos a Aules. Los casos de redes se retoman en UD4.

A1 y A10 son entregables y no incluyen soluciones en esta página. Las siete prácticas conservan sus guías, sin respuestas modelo del informe.

## Caso A2 · El recorrido de un archivo en una VM

Una persona guarda index.html dentro de Ubuntu virtualizado. El disco de Ubuntu indica 18 GiB libres; al mismo tiempo, el SSD del anfitrión se está llenando. El VDI es dinámico y hay una instantánea anterior.

### A2 · Preguntas para comentar

1. Dibuja el recorrido archivo → sistema de archivos invitado → partición → disco virtual y diferenciales → archivo anfitrión → SSD.
2. Explica en qué nivel se mide cada espacio libre y por qué pueden ser diferentes.
3. Indica qué comprobarías primero si una escritura falla aunque Ubuntu muestre espacio.
4. Relaciona anfitrión, invitado e hipervisor con los recursos que aparecen en el dibujo.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Recorrido: archivo index.html → ext4 del invitado → partición → bloques del VDI y sus diferenciales → archivos del anfitrión → SSD.
2. Ubuntu mide espacio disponible dentro de su sistema de archivos. Windows mide espacio real de la unidad donde residen VDI, instantáneas y otros archivos. Son capas diferentes.
3. Comprobar primero el espacio del anfitrión y dónde están los VDI y las instantáneas; después revisar el espacio y los permisos del invitado. Un VDI dinámico necesita poder crecer físicamente.
4. El anfitrión administra el SSD real; el hipervisor presenta el disco virtual y asigna CPU y RAM; el invitado administra el sistema de archivos que utiliza la aplicación.

</details>

## Caso A3 · Integridad y autenticidad de una ISO

El equipo A descarga ISO y hash desde un foro. El equipo B obtiene la imagen desde un espejo, comprueba la firma del listado oficial de hashes y contrasta la identidad de la clave. Ambos dicen: «Mi archivo es auténtico porque dos cadenas coinciden».

### A3 · Preguntas para comentar

1. Distingue archivo descargado, hash esperado, hash calculado y firma.
2. Explica qué ha probado cada equipo y qué confianza falta en el caso del foro.
3. Describe qué ocurriría si se usase el hash de otra revisión con el mismo nombre comercial.
4. Diseña una ficha de verificación con fuente, versión, arquitectura, nombre exacto y conclusión.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. La ISO es el archivo; el hash esperado es la referencia publicada; el calculado se obtiene de los bytes descargados. Una firma comprobada con una clave de identidad verificada permite autenticar la referencia firmada.
2. A solo comprueba coincidencia con lo que dice el foro: ambos archivos podrían haberse sustituido. B añade confianza en el origen del listado firmado. La coincidencia no demuestra que el software carezca de fallos.
3. Otra revisión produce normalmente otro hash. Una discrepancia obliga a comprobar versión, arquitectura y archivo exacto antes de usar la ISO.
4. Ficha modelo: URL oficial y fecha; sistema, revisión y arquitectura; nombre exacto; algoritmo; hash oficial; hash calculado; firma y clave verificadas cuando proceda; conclusión «coincide/no coincide» y acción. Los valores deben ser reales, no inventados.

</details>

## Caso A4 · Diseñar el arranque y las particiones

Debes proponer un disco Linux UEFI de 60 GiB. Se quiere separar /home para facilitar futuras reinstalaciones y conservar un registro de qué se formateará. Todavía no se ha abierto ningún instalador.

### A4 · Preguntas para comentar

1. Dibuja tabla, particiones, tamaños aproximados, formatos y puntos de montaje.
2. Identifica la ESP y explica por qué no se trata como otra partición de documentos.
3. Compara tu diseño con uno de una sola raíz y razona una ventaja y un límite de separar /home.
4. Explica qué se perdería si se marca formatear /home durante una reinstalación.
5. Corrige las frases «GPT siempre exige UEFI» y «una partición de datos ya es una copia de seguridad».

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Propuesta para 60 GiB: tabla GPT; ESP de 0,5 GiB FAT32 montada en /boot/efi; raíz de 30 GiB ext4 en /; resto aproximado de 29,5 GiB ext4 en /home. Los tamaños son orientativos y se ajustan al alineado y al uso. Puede utilizarse un archivo de intercambio dentro de la raíz si corresponde al sistema elegido.
2. La ESP contiene archivos de arranque que utiliza UEFI; no es una carpeta de documentos ni debe formatearse por rutina si contiene el arranque de otros sistemas.
3. Una sola raíz facilita repartir espacio sin anticipar necesidades. Separar /home facilita conservarlo al reinstalar, pero exige montarlo correctamente y evitar formatearlo; también puede dejar una partición llena y otra con espacio.
4. Formatear /home destruye su sistema de archivos y los datos que contiene. Antes de cualquier reinstalación hay que verificar la copia y las opciones de cada partición.
5. GPT es un esquema de particionado y no equivale a UEFI: existen arranques BIOS sobre GPT con el soporte apropiado. Otra partición del mismo disco no protege de la avería de ese disco.

</details>

## Caso A5 · Elegir un sistema de archivos

Hay cuatro destinos: raíz de Ubuntu, sistema de Windows, partición EFI y memoria de intercambio que guardará vídeos de 8 GiB. Debes justificar el formato según la función de cada destino.

### A5 · Preguntas para comentar

1. Elige entre ext4, NTFS, FAT32 y exFAT para los cuatro destinos. Explica si hay condiciones de compatibilidad que comprobar.
2. Razona por qué tener 20 GiB libres no garantiza poder copiar un archivo de 8 GiB en cualquier formato.
3. Explica diferencia entre volumen, sistema de archivos y punto de montaje.
4. Un disco aparece en lsblk y no en df. Propón dos situaciones que lo expliquen sin concluir que la herramienta falla.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Raíz Ubuntu: ext4; sistema Windows: NTFS; ESP: FAT32; memoria USB de intercambio con vídeos de 8 GiB: exFAT, comprobando soporte de lectura y escritura en los equipos de destino. No se refiere aquí al área swap de Linux.
2. FAT32 limita el tamaño de cada archivo a menos de 4 GiB. Aunque sobren 20 GiB no admite ese vídeo de 8 GiB en un solo archivo.
3. Un volumen es una unidad lógica de almacenamiento; el sistema de archivos organiza su contenido; el punto de montaje es la ruta por la que se accede a él.
4. lsblk puede mostrar una partición sin montar, o un disco todavía sin sistema de archivos. df informa principalmente sobre sistemas de archivos montados, no sobre todos los dispositivos detectados.

</details>

## Caso A6 · Prever el crecimiento de discos virtuales

Un ordenador tiene 100 GiB libres. Dos VDI dinámicos tienen capacidad lógica de 80 GiB cada uno, pero hoy ocupan 20 GiB cada uno. Se quieren conservar varios puntos de retorno y exportar una máquina.

### A6 · Preguntas para comentar

1. Separa capacidad lógica máxima, ocupación actual y espacio físico restante.
2. Explica por qué los discos dinámicos no garantizan que el laboratorio siempre quepa.
3. Incluye en tu previsión exportación, importación e instantáneas. Declara qué tamaños son estimaciones.
4. Propón una política de revisión y un umbral de aviso razonado, sin presentarlo como regla universal.
5. Explica por qué no se deben borrar manualmente los discos diferenciales para liberar espacio.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Capacidad lógica conjunta: 160 GiB; ocupación actual de los dos VDI: 40 GiB. El enunciado dice que actualmente quedan 100 GiB libres: no hay que volver a restar esos 40 GiB. Se dispone de 100 GiB para crecimiento adicional y nuevas copias.
2. Los VDI podrían crecer otros 120 GiB en conjunto, incluso sin contar instantáneas: no está garantizado que quepan en los 100 GiB disponibles.
3. Ejemplo de previsión adicional: crecimiento 30 GiB, instantáneas 15 GiB, exportación 20 GiB, importación 25 GiB y margen 10 GiB: 100 GiB. Son estimaciones y el plan queda demasiado justo; se valida midiendo y buscando otro destino para copias.
4. Revisar espacio antes de crear una instantánea, exportar o importar y al terminar cada sesión. Un aviso a 30 GiB puede servir en este escenario si la siguiente operación necesita 25 GiB, pero el umbral se calcula según el trabajo previsto.
5. Los diferenciales contienen cambios necesarios para reconstruir estados. Se gestionan desde el hipervisor; borrarlos a mano puede romper la cadena y perder datos.

</details>

## Caso A7 · Detectar una falsa instalación

Un compañero ve el escritorio Ubuntu, crea un documento y concluye que ya está instalado. Al apagar y retirar la ISO aparece un mensaje de medio no arrancable. Conservas una ficha que dice «VDI nuevo y vacío».

### A7 · Preguntas para comentar

1. Propón dos hipótesis coherentes y una comprobación para cada una.
2. Explica qué diferencia hay entre el escritorio Live y el sistema del disco.
3. Diseña una secuencia de tres pruebas que acrediten arranque independiente y persistencia.
4. Indica por qué una captura del escritorio no permite resolver por sí sola el caso.
5. Escribe una respuesta técnica al compañero que evite reinstalar antes de diagnosticar.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Hipótesis A: se utilizó una sesión Live sin instalar; comprobar si el VDI sigue vacío y si aparece el instalador. Hipótesis B: existe una instalación pero el firmware, el disco conectado o el orden de arranque no corresponden; revisar configuración y particiones antes de escribir nada. Con la ficha de VDI vacío, A es la explicación mejor apoyada inicialmente.
2. El Live arranca desde la ISO; el sistema instalado arranca desde el disco virtual. El escritorio puede parecer idéntico.
3. Crear un archivo en la carpeta personal del sistema instalado; apagar y retirar la ISO; arrancar desde el disco y comprobar que el archivo sigue presente. Si no arranca, revisar destino y arranque antes de dar la prueba por superada.
4. Una captura del escritorio no identifica el medio de arranque ni acredita persistencia tras apagar.
5. Respuesta al compañero: «Primero revisemos si se instaló en el VDI y desde dónde arranca. Después comprobaremos el arranque sin ISO y la persistencia. No hace falta reinstalar sin conocer la causa».

</details>

## Caso A8 · Aceptar una instalación de Windows

Windows llega al escritorio. Administrador de dispositivos muestra un dispositivo desconocido, Windows Update pide reiniciar y Activación indica un estado pendiente. El informe solo contiene una captura del fondo de pantalla.

### A8 · Preguntas para comentar

1. Identifica los tres asuntos pendientes y qué información falta para resolver cada uno.
2. Asocia winver, msinfo32, tpm.msc, diskmgmt.msc y devmgmt.msc con el dato que permiten comprobar.
3. Redacta una incidencia con estado, hipótesis, acción y criterio de cierre.
4. Explica instalación, activación y derecho de uso sin dar por hecho que omitir clave crea una evaluación.
5. Decide qué evidencia pedirías antes de entregar ese puesto como terminado.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Pendientes: identificar el dispositivo desconocido por sus identificadores y controlador; completar el reinicio y revisar actualizaciones; comprobar edición, estado de activación y licencia disponible. El escritorio no cierra ninguno de estos asuntos.
2. winver: versión y compilación; msinfo32: resumen del sistema y modo de firmware; tpm.msc: estado y versión del TPM; diskmgmt.msc: discos y particiones; devmgmt.msc: dispositivos y controladores.
3. Incidencia modelo: «Dispositivo desconocido en el invitado; posible controlador ausente. Leer identificadores, localizar el controlador apropiado en la fuente autorizada e instalarlo si corresponde. Cerrar cuando el dispositivo quede identificado y funcione sin error». La causa sigue siendo una hipótesis hasta comprobarla.
4. Instalar copia y configura el sistema; activar comprueba el estado de activación; el derecho de uso depende de la licencia aplicable. Omitir la clave durante el asistente no concede por sí solo una licencia ni una evaluación.
5. Pedir versión y edición, dispositivos sin errores pendientes, resultado de actualización tras reiniciar, estado de activación documentado y prueba de arranque sin ISO con archivo persistente. No incluir claves en evidencias.

</details>

## Caso A11 · Máquina virtual o contenedor

Un desarrollador afirma: «He descargado una imagen Ubuntu en Docker, así que he instalado otra VM con un kernel Ubuntu independiente». También guarda datos importantes solamente dentro de la capa escribible del contenedor.

### A11 · Preguntas para comentar

1. Identifica las dos confusiones en la primera afirmación y corrígela.
2. Dibuja hardware, anfitrión, VM Ubuntu y contenedores del laboratorio P7. Señala dónde está el kernel.
3. Distingue imagen, contenedor y volumen con un ejemplo de servicio web.
4. Predice qué ocurre al detener, volver a iniciar y eliminar un contenedor.
5. Justifica cuándo elegirías VM completa y cuándo contenedor para un trabajo de DAM.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Descargar una imagen no crea por sí solo una VM ni inicia un contenedor. Una imagen Ubuntu aporta espacio de usuario; los contenedores Linux comparten el kernel del entorno Linux donde se ejecutan.
2. En el laboratorio conceptual: hardware → anfitrión e hipervisor → VM Linux con su kernel → motor de contenedores → contenedores. Si el motor corre en Linux físico, no hace falta esa VM intermedia. En Docker Desktop puede existir un entorno Linux intermedio.
3. Imagen: plantilla de la aplicación; contenedor: instancia creada desde ella con su capa escribible; volumen: almacenamiento persistente separado de la vida de esa instancia. Ejemplo: servidor web en contenedor y contenido en un volumen.
4. Detener no equivale a eliminar: la capa escribible del mismo contenedor permanece al pararlo y volverlo a iniciar. Eliminarlo pierde esa capa; un volumen conservado puede seguir existiendo. Hay que revisar las opciones de borrado y mantener respaldo de los datos.
5. VM para estudiar un sistema completo, su arranque y kernel. Contenedor para distribuir una aplicación y sus dependencias. Ninguno elimina la necesidad de administrar y respaldar datos.

</details>

## Caso A12 · Diagnóstico escrito de ocho incidencias

Resuelve ocho fichas: VM sin medio de arranque; escritorio que no adapta resolución; servicio accesible por IP y no por nombre; invitado con espacio y SSD lleno; archivo posterior perdido tras restaurar; clones con conectividad intermitente; menú ISO que reaparece; y apt update con avisos e índices anteriores.

### A12 · Preguntas para comentar

1. Para cada ficha escribe el síntoma sin inventar datos no aportados.
2. Plantea dos hipótesis diferenciadas y selecciona la primera prueba de lectura.
3. Explica qué resultado apoyaría cada hipótesis.
4. Propón una corrección limitada al problema y una prueba de cierre. No utilices formatear como respuesta inicial.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

Las hipótesis siguientes son posibilidades para comprobar; no diagnósticos confirmados.

| Síntoma | Dos hipótesis | Primera comprobación y resultado orientativo | Corrección y cierre |
| --- | --- | --- | --- |
| Sin medio de arranque | ISO no conectada; disco sin sistema o no arrancable | Leer almacenamiento y orden de arranque: ausencia de ISO apoya la primera; VDI vacío apoya la segunda | Conectar el medio correcto o completar la instalación después de verificar el destino; probar el arranque previsto |
| Resolución no se adapta | Integración del invitado ausente; ajuste automático desactivado | Revisar integración y opción de redimensionado | Instalar integración compatible o activar el ajuste; comprobar varias dimensiones de ventana |
| Servicio por IP pero no por nombre | DNS incorrecto; nombre o registro equivocado | Resolver el nombre y comparar su IP con la que funciona | Corregir DNS o registro; repetir la misma petición por nombre |
| Invitado con espacio, SSD lleno | VDI o diferenciales crecidos; otros archivos del anfitrión ocupan la unidad | Medir espacio y tamaños en el anfitrión | Liberar o mover archivos por el procedimiento apropiado; repetir escritura y revisar margen |
| Archivo posterior perdido tras restaurar | Se volvió a un estado anterior; se está mirando otra ruta o VM | Comprobar instantánea seleccionada, identidad y ruta | Recuperar desde un estado conservado o respaldo si existe; verificar contenido, sin prometer recuperar datos sin copia |
| Clones con red intermitente | MAC repetidas; IP fija repetida | Comparar MAC y configuración de IP de ambos clones | Generar identidades únicas; probar conexiones con ambos activos |
| Menú ISO reaparece | ISO sigue primero en el arranque; instalación no completada en el disco | Apagar, revisar disco y retirar ISO para probar | Corregir orden o terminar la instalación según diagnóstico; arrancar desde disco |
| apt update avisa y conserva índices antiguos | Red o DNS fallan; repositorio o firma no válidos | Leer el aviso completo y comprobar acceso al origen | Corregir conectividad u origen y repetir update sin ese error antes de evaluar versiones |

</details>

## Caso A13 · Presupuesto profesional de laboratorio

Dispones de un anfitrión de 16 GiB y 220 GiB libres en su unidad de trabajo. Debes prever Ubuntu, Windows, un disco de datos, un clon y una exportación con importación de comprobación. La carga de aplicaciones todavía puede variar.

### A13 · Preguntas para comentar

1. Diseña un presupuesto de RAM que incluya anfitrión y margen y declara si propones simultaneidad.
2. Diseña otro de disco que distinga capacidad lógica, ocupación estimada y crecimiento.
3. Señala qué medida real falta antes de aceptar que todo cabe.
4. Propón qué trasladarías a otro destino si la importación no cabe, manteniendo una copia válida.
5. Redacta una condición de aceptación que el cliente pueda comprobar sin saber VirtualBox.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. RAM de ejemplo con ambas VM activas: anfitrión 6 GiB, Ubuntu 4 GiB, Windows 4 GiB y margen 2 GiB: 16 GiB. Se comprueba bajo la carga prevista; si no resulta suficiente, se usa una VM cada vez o un equipo con más recursos.
2. Ejemplo de ocupación física prevista: Ubuntu 25 GiB, Windows 40 GiB, datos 10 GiB, clon 25 GiB, exportación 20 GiB e importación 25 GiB: 145 GiB; reserva de crecimiento e instantáneas 45 GiB; margen 30 GiB: 220 GiB. Las capacidades lógicas pueden ser 50, 80, 20, 50 y 50 GiB respectivamente; no se confunden con ocupaciones reales ni se garantiza que todas puedan llenarse a la vez. El ejemplo presupone que aún no se han descontado esos archivos del espacio libre inicial.
3. Medir memoria bajo carga, tamaño real de discos y diferenciales, ocupación del paquete, espacio temporal de importación y espacio libre del destino. Los valores anteriores no sustituyen esas medidas.
4. Exportar o importar en otro soporte con espacio suficiente, conservando el original hasta que la importación funcione. No borrar la única copia válida para hacer sitio.
5. Aceptación: ambas VM arrancan según el plan, conservan el archivo testigo y ejecutan la aplicación prevista; la copia importada también funciona y queda el margen de disco y RAM acordado.

</details>

## Caso A14 · Explicar un mecanismo con evidencia

Debes explicar a otra persona uno de estos mecanismos: recorrido de una petición web, instantánea frente a respaldo independiente, o Live frente a instalación persistente. Puede ser una explicación presencial o una grabación autorizada de 3-5 minutos.

### A14 · Preguntas para comentar

1. Prepara un guion con una pregunta inicial y una predicción.
2. Dibuja las capas, rutas o estados implicados sin saltarte el nivel del anfitrión.
3. Selecciona una evidencia ya obtenida en una práctica y explica qué demuestra.
4. Termina con una limitación o caso que tu evidencia no acredita.
5. Revisa que no aparezcan credenciales, terceros sin permiso ni datos personales innecesarios.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Guion de ejemplo: «¿Lo que guardamos en el escritorio permanece al retirar la ISO? Predigo que solo permanecerá si se escribió en un sistema persistente y se arranca el destino correcto».
2. Dibujar hardware → anfitrión → archivo VDI → disco y sistema de archivos invitado → documento. Añadir la ISO como medio de arranque separado.
3. Utilizar una evidencia real ya obtenida: documento antes de apagar y después de arrancar sin ISO. Explicar por qué demuestra persistencia en ese ensayo.
4. Límite: esa prueba no demuestra que exista un respaldo ni que los datos sobrevivan a la avería del SSD. No pedir una práctica nueva para ilustrarlo.
5. Mostrar solo la VM y el archivo de prueba, ocultando credenciales y datos personales. La explicación oral en clase es suficiente; no se exige grabación ni entrega.

</details>

## Caso A15 · Autoevaluación razonada de salida

Comprueba qué conceptos puedes explicar sin tener abierto el asistente. Responde primero sin apuntes; después contrasta con la teoría y conserva tus correcciones con otra marca o color.

### A15 · Preguntas para comentar

1. Distingue ISO, VDI, ESP, raíz y /home.
2. Explica anfitrión, invitado e hipervisor y un límite del aislamiento.
3. Relaciona IP, ruta, DNS y servicio con una prueba de cada nivel.
4. Distingue apt update de apt upgrade y explica cuándo puede no cambiar el kernel.
5. Explica instantánea, clon enlazado y copia independiente; di cómo validarías un respaldo.
6. Indica una idea que aún necesites comprobar y la página de teoría que consultarás.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. ISO: imagen de medio de instalación; VDI: disco virtual; ESP: partición de arranque EFI; raíz /: inicio del árbol Linux; /home: ubicación habitual de carpetas personales, con o sin partición separada.
2. Anfitrión: sistema que aloja el entorno; invitado: sistema de la VM; hipervisor: presenta hardware virtual y arbitra recursos. Una carpeta compartida y la red cruzan parte del aislamiento y deben administrarse.
3. IP: revisar dirección y máscara; ruta: consultar tabla de rutas; DNS: resolver el nombre; servicio: realizar una petición a su puerto o aplicación. Un ping aislado no demuestra todo el recorrido ni que el servicio funcione. Este punto se retoma en UD4.
4. update refresca índices; upgrade instala actualizaciones disponibles. Puede no haber kernel nuevo, estar retenido o no haberse reiniciado para arrancarlo. Registrar versión instalada y en ejecución cuando proceda.
5. Instantánea: retorno a un estado dependiente del entorno; clon enlazado: diferencias dependientes de una base; respaldo independiente: copia separada de los riesgos previstos. Se valida restaurando y comprobando archivos y funcionamiento.
6. La última respuesta es personal: aceptar una duda concreta y una referencia pertinente de teoría, no imponer que todo esté comprendido.

</details>

## Caso A16 · Leer una actualización antes de aceptarla

Una propuesta de actualización anuncia 18 paquetes actualizados, 2 nuevos y 0 eliminados. Una compañera cree que eso demuestra que se ha ejecutado full-upgrade. Otra ejecuta update con la red caída y afirma que todos los programas ya están al día.

### A16 · Preguntas para comentar

1. Explica qué puedes y qué no puedes deducir de los números de la propuesta.
2. Distingue refrescar índices, actualizar paquetes y cambiar de versión de distribución.
3. Razona si la instalación de dependencias nuevas es compatible con apt upgrade.
4. Indica qué mensaje buscarías para detectar que se han usado índices antiguos.
5. Diseña una tabla antes/después con versión, propuesta, reinicio y prueba de funcionamiento.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Los números describen una propuesta de cambios, no identifican de forma única el comando empleado ni prueban que se haya completado. full-upgrade no está obligado a eliminar paquetes en todas las ejecuciones.
2. update descarga índices; upgrade actualiza paquetes; cambiar de versión de distribución es otro procedimiento, que debe planificarse y verificarse.
3. Sí: apt upgrade puede instalar dependencias nuevas, pero no elimina paquetes ya instalados para completar la actualización. No confundir su comportamiento con opciones de otras herramientas.
4. Buscar mensajes de fallo al descargar índices y de reutilización de índices anteriores. Con red caída no se puede concluir que las referencias de actualización estén al día.
5. Tabla modelo: fecha; versión anterior; propuesta de paquetes; operación y resultado; reinicio solicitado y realizado; versión posterior y prueba funcional. Completar con datos observados, no con cifras inventadas.

</details>

## Caso A17 · Identificar paquetes y repositorios

Tienes un archivo programa_1.4_amd64.deb, un programa instalado con APT y una aplicación que aparece en snap list. Además, una guía antigua propone renombrar una clave descargada y añadir un PPA sin comprobar la versión de Ubuntu.

### A17 · Preguntas para comentar

1. Distingue archivo descargado, nombre de paquete e instalación disponible.
2. Asocia dpkg-deb --info, dpkg-query -W, apt install ./archivo.deb y snap list con la información o acción correspondiente.
3. Explica los campos Types, URIs, Suites, Components y Signed-By de una definición .sources.
4. Indica qué revisarías antes de añadir un origen externo y por qué cambiar la extensión no convierte el formato de una clave.
5. Compara retirar una aplicación y eliminar sus documentos personales.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. El .deb es un archivo de paquete, su nombre no prueba que esté instalado. El nombre interno y su versión se consultan en metadatos; el estado de instalación se comprueba en el equipo. APT y Snap mantienen mecanismos de gestión diferentes.
2. dpkg-deb --info: metadatos de un .deb; dpkg-query -W: datos de paquetes conocidos por dpkg (revisar estado cuando se necesite confirmar instalación); apt install ./archivo.deb: instalar el paquete local resolviendo dependencias disponibles; snap list: listar snaps instalados.
3. Types: tipo de origen, por ejemplo deb; URIs: ubicación; Suites: distribución o suites; Components: componentes seleccionados; Signed-By: clave o referencia que limita qué firma se acepta para ese origen.
4. Revisar autor, confianza de la clave, versión de Ubuntu compatible, arquitectura, mantenimiento y necesidad real del origen. Renombrar .asc a .gpg no cambia la codificación: debe utilizarse el formato y el procedimiento documentados.
5. Desinstalar un paquete no equivale a eliminar sus documentos de usuario. Revisar datos, configuración y respaldo antes de borrar contenido personal; no prometer que todas las aplicaciones se comporten igual.

</details>

## Caso A18 · Punto de restauración o instantánea de VM

Un usuario ha borrado un documento; otro instaló un programa que altera el sistema; un tercero perdió el SSD donde tenía VM e instantáneas. Todos quieren pulsar «Restaurar sistema» para resolverlo.

### A18 · Preguntas para comentar

1. Identifica qué información falta en cada caso y qué mecanismo podría ayudar.
2. Explica alcance de un punto de Windows, instantánea de VirtualBox y copia independiente de documentos.
3. Justifica por qué hay que revisar protección activada, punto disponible y programas afectados antes de prometer una reversión.
4. Compara Timeshift con una copia de la carpeta personal sin afirmar que incluyen siempre los mismos datos.
5. Diseña una evidencia antes/después que no se pierda con el propio retorno.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. Documento borrado: comprobar papelera, historial y respaldo de documentos. Cambio de programa: revisar un punto previo o copia del sistema apropiada. SSD perdido: buscar una copia en otro soporte; las instantáneas del mismo SSD no solucionan la pérdida física.
2. Restaurar sistema de Windows revierte determinados componentes del sistema; no es un respaldo de documentos. La instantánea devuelve los elementos incluidos de la VM a un estado. Una copia independiente de documentos protege los archivos seleccionados según su fecha y soporte.
3. Revisar protección habilitada, existencia y fecha del punto, unidad afectada y lista de programas que cambiarán. Sin un punto válido no puede prometerse la reversión.
4. Timeshift se orienta a estados del sistema y su cobertura depende de modo, filtros y configuración. Una copia de la carpeta personal tiene otra selección de datos; ninguna debe suponerse completa sin revisar lo incluido y probarla.
5. Registrar antes el estado de la aplicación y un archivo testigo; guardar el registro fuera del destino que va a retroceder; efectuar el retorno autorizado y comparar. Mantener respaldo previo de cualquier documento que se quiera conservar.

</details>

## Caso A19 · Leer un instalador MSI o EXE

Dos descargas se llaman editor.msi y editor-setup.exe. Una persona concluye que el MSI es necesariamente seguro, que siempre creará un punto de restauración y que el EXE nunca puede contener un MSI.

### A19 · Preguntas para comentar

1. Revisa las tres afirmaciones y señala qué se puede deducir realmente de la extensión.
2. Propón una lista de datos que comprobarías en origen, editor, arquitectura y licencia antes de ejecutar.
3. Describe qué decisiones revisarías en carpeta, componentes, opciones adicionales y reinicio.
4. Define prueba funcional y ruta de desinstalación sin inventar que todos los instaladores ofrecen idénticas pantallas.

<details markdown="1">
<summary>Mostrar solución razonada para clase</summary>

1. MSI es un formato de paquete para Windows Installer; EXE es un ejecutable que puede contener un instalador o incluso invocar un MSI. Ninguna extensión garantiza seguridad ni creación de un punto de restauración.
2. Comprobar URL del proveedor, firma y editor cuando existan, producto y versión, arquitectura compatible, licencia y requisitos. Detenerse si el origen o los datos no coinciden con lo esperado.
3. Revisar destino, espacio, componentes necesarios, asociaciones, accesos, programas adicionales y reinicio. Leer las opciones reales del asistente sin asumir que todos muestran las mismas pantallas.
4. Abrir la aplicación instalada, comprobar su versión y una función concreta; localizar la desinstalación en Configuración de Windows o el método documentado. Registrar resultado y ruta real, sin inventar pantallas.

</details>

## Referencias para las explicaciones de paquetes

[Manual oficial de apt en Ubuntu 24.04](https://manpages.ubuntu.com/manpages/noble/man8/apt.8.html) · [Gestión de paquetes en Ubuntu](https://ubuntu.com/server/docs/how-to/software/package-management/).
