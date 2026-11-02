# 3.6 · De la red física a la red virtual

Una máquina virtual tiene su propio sistema operativo y sus adaptadores. El modo de red decide a qué entorno se conectan esos adaptadores. Elegir el modo es una decisión de topología; configurar IP, prefijo y servicios es el paso siguiente. Aquí lo razonamos con esquemas y demostraciones para reutilizarlo al crear máquinas en UD4.

## El mismo razonamiento TCP/IP

Un adaptador virtual sigue necesitando enlace, dirección, prefijo y, según el destino, puerta de enlace y DNS. En UD3 elegimos y justificamos el plan; en UD4 creamos y configuramos las máquinas. Puede usarse una demostración ya preparada para observar los resultados.

El **anfitrión** es el equipo donde se ejecuta VirtualBox; el **invitado** es el sistema de la máquina virtual. El switch virtual conecta adaptadores y el router, cuando existe, permite pasar entre redes. Una interfaz virtual desconectada equivale a un enlace sin conexión aunque la dirección IP esté escrita correctamente.

Antes de seleccionar una opción formula el objetivo: solo salida a Internet, participación en la LAN autorizada o comunicación aislada entre invitados. Esa necesidad permite justificar el modo, en lugar de probar opciones hasta que parezca funcionar.

| Modo de VirtualBox | Encargo habitual | Qué se debe comprobar |
| --- | --- | --- |
| NAT sencillo | Un invitado necesita salida a través del anfitrión | Configuración recibida, salida y límites de acceso entrante |
| Adaptador puente | El invitado participa en una LAN autorizada | Interfaz física seleccionada, política de la red y dirección válida |
| Red interna | Invitados del mismo anfitrión deben comunicarse entre sí en un segmento separado | Nombre de red interna coincidente y direcciones compatibles |

## NAT no significa una LAN común entre todos los invitados

El NAT sencillo proporciona a cada invitado su propio entorno traducido. Dos máquinas configuradas con NAT por separado no se consideran conectadas automáticamente al mismo segmento. Una **red NAT** es otra opción que puede agrupar invitados; debe diseñarse y comprobarse explícitamente. El acceso entrante puede necesitar reglas de reenvío de puertos; no se presupone que publicar un puerto sea necesario en todos los ejercicios.

En NAT sencillo, una conexión iniciada por el invitado puede salir mediante la traducción que hace VirtualBox. Un cliente externo no puede iniciar sin más una conexión al servicio del invitado: necesitaría un camino de entrada previsto. El reenvío de puertos relaciona un puerto de entrada con una dirección y puerto internos.

Dos invitados con NAT sencillo pueden mostrar la misma dirección privada porque están en entornos NAT separados. No es el mismo caso que duplicar una dirección dentro de una LAN común. Si el objetivo es que se comuniquen entre sí y tengan salida, se puede diseñar una red NAT compartida, con su servicio DHCP y sus pruebas.

## Puente implica participar en la red seleccionada

La máquina se comporta como otro equipo de esa LAN en los aspectos permitidos por la red y el medio. No se activa puente sobre la red del centro sin indicación docente. La obtención de dirección y la conectividad dependen de la infraestructura y sus restricciones; no se promete que cualquier invitado tenga acceso por elegir este modo.

En puente, el invitado necesita una dirección válida para la LAN seleccionada. Puede obtenerla mediante su DHCP autorizado o mediante un plan manual. La interfaz física elegida importa: un puente sobre un adaptador sin conexión no proporciona un enlace útil.

Este modo resulta apropiado cuando un servicio del invitado debe ser accesible desde equipos de esa LAN y la política lo permite. La accesibilidad también depende del firewall del invitado, del servicio en escucha y de las restricciones de la red. Tener IP no demuestra que el servicio funcione.

## Red interna no añade un router ni DHCP por sí sola

El mismo nombre de red interna conecta los adaptadores de los invitados a un segmento virtual. Si no hay un servicio DHCP preparado, se configura direccionamiento manual. Una dirección `192.168.50.10/24` y otra `192.168.50.20/24` permiten plantear comunicación local; poner una puerta de enlace inventada no crea salida a Internet. La red interna de VirtualBox no incorpora al anfitrión como miembro del segmento.

Por ejemplo, A `192.168.50.10/24` y B `192.168.50.20/24`, con el mismo nombre de red interna, pueden intercambiar tráfico local. Si B pasa a `192.168.60.20/24`, deja de pertenecer a la subred de A. Mantener el mismo switch virtual no crea un router entre ellas.

El modo «solo anfitrión» es otra opción: puede conectar al anfitrión con invitados en un segmento específico. No equivale a red interna ni proporciona salida por sí solo. Se menciona para interpretar los vídeos; el diseño obligatorio de UD3 se centra en NAT, puente y red interna.

## Ficha previa que se reutiliza en UD4

Anota equipo, adaptador, modo, nombre de segmento, dirección/prefijo, asignación manual o DHCP, puerta, DNS, servicio esperado, prueba y restauración. Dibuja cada enlace y señala dónde existe realmente un router. Comprueba primero la red local y después la salida o el servicio.

Fuente: [Manual de VirtualBox · Redes virtuales](https://docs.oracle.com/en/virtualization/virtualbox/7.1/user/networkingdetails.html).

## Tres encargos resueltos

| Necesidad | Elección inicial | Prueba de aceptación |
| --- | --- | --- |
| Un invitado descarga actualizaciones | NAT sencillo | Configuración válida, resolución y acceso al servicio de actualización |
| Un servicio del invitado debe atender a otro equipo de la LAN autorizada | Puente sobre la interfaz acordada | IP válida de esa LAN y conexión desde el cliente al puerto previsto |
| Dos invitados practican entre sí sin salida | Red interna con el mismo nombre | Direcciones compatibles, prueba local y ausencia de una ruta de salida prevista |

En el tercer caso no hace falta puerta de enlace para comunicar A y B localmente. Si el encargo cambiara y pidiera salida, habría que diseñar un camino real, por ejemplo un equipo que encaminara con las interfaces adecuadas; escribir una dirección ficticia como puerta no lo sustituye.

**Comprueba que lo entiendes:** dibuja dónde está el invitado, dónde está el anfitrión y qué dispositivo realiza la traducción o el encaminamiento. Después distingue «el adaptador está conectado», «tengo dirección» y «el servicio responde»: son comprobaciones diferentes.

## Vídeo de apoyo · NAT, adaptador puente y red interna en VirtualBox · Marc Venteo

Demostración en castellano del autor Marc Venteo. Para esta unidad interesa el tramo conceptual: 2:20–6:00, que compara puente, red interna, NAT y red NAT. La creación de máquinas se realizará en UD4.

<div class="video-card" markdown>
<div class="video-frame">
<iframe src="https://www.youtube-nocookie.com/embed/mOuKtZVMwbw" title="NAT, adaptador puente y red interna en VirtualBox · Marc Venteo" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en YouTube](https://www.youtube.com/watch?v=mOuKtZVMwbw)

</div>

**Durante el visionado:** dibuja quién comparte segmento en cada modo y explica por qué NAT sencillo y red NAT no son la misma opción. No copies direcciones sin relacionarlas con la topología.

## Ahora aplica lo aprendido

[Completar la actividad 3.6 y P5 · Justificar el diseño y las incidencias](actividades/A6-diagnostico-y-red-virtual.md).

Añade estas decisiones al mismo documento que contiene P2 y P3. La entrega completa es `UD3_A6_Codigo.pdf`, con sus tres anexos prácticos, en una sola tarea de Aules. Después puedes consultar el [itinerario de UD4](../ud4/itinerario.md).
