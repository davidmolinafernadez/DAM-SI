# 3.6 · De la red física a la red virtual

## El mismo razonamiento TCP/IP

Un adaptador virtual sigue necesitando enlace, dirección, prefijo y, según el destino, puerta de enlace y DNS. En UD3 elegimos y justificamos el plan; en UD4 creamos y configuramos las máquinas. Puede usarse una demostración ya preparada para observar los resultados.

| Modo de VirtualBox | Encargo habitual | Qué se debe comprobar |
| --- | --- | --- |
| NAT sencillo | Un invitado necesita salida a través del anfitrión | Configuración recibida, salida y límites de acceso entrante |
| Adaptador puente | El invitado participa en una LAN autorizada | Interfaz física seleccionada, política de la red y dirección válida |
| Red interna | Invitados del mismo anfitrión deben comunicarse entre sí en un segmento separado | Nombre de red interna coincidente y direcciones compatibles |

## NAT no significa una LAN común entre todos los invitados

El NAT sencillo proporciona a cada invitado su propio entorno traducido. Dos máquinas configuradas con NAT por separado no se consideran conectadas automáticamente al mismo segmento. Una **red NAT** es otra opción que puede agrupar invitados; debe diseñarse y comprobarse explícitamente. El acceso entrante puede necesitar reglas de reenvío de puertos; no se presupone que publicar un puerto sea necesario en todos los ejercicios.

## Puente implica participar en la red seleccionada

La máquina se comporta como otro equipo de esa LAN en los aspectos permitidos por la red y el medio. No se activa puente sobre la red del centro sin indicación docente. La obtención de dirección y la conectividad dependen de la infraestructura y sus restricciones; no se promete que cualquier invitado tenga acceso por elegir este modo.

## Red interna no añade un router ni DHCP por sí sola

El mismo nombre de red interna conecta los adaptadores de los invitados a un segmento virtual. Si no hay un servicio DHCP preparado, se configura direccionamiento manual. Una dirección `192.168.50.10/24` y otra `192.168.50.20/24` permiten plantear comunicación local; poner una puerta de enlace inventada no crea salida a Internet. La red interna de VirtualBox no incorpora al anfitrión como miembro del segmento.

## Ficha previa que se reutiliza en UD4

Anota equipo, adaptador, modo, nombre de segmento, dirección/prefijo, asignación manual o DHCP, puerta, DNS, servicio esperado, prueba y restauración. Dibuja cada enlace y señala dónde existe realmente un router. Comprueba primero la red local y después la salida o el servicio.

[Actividad 3.6](actividades/A6-diagnostico-y-red-virtual.md) · [Práctica P5](practicas/P5-incidencias.md) · [Continuidad en UD4](../ud4/itinerario.md)

Fuente: [Manual de VirtualBox · Redes virtuales](https://docs.oracle.com/en/virtualization/virtualbox/7.1/user/networkingdetails.html).

## Actividad y aplicación práctica

- [Actividad 3.6 · Justificar una configuración](actividades/A6-diagnostico-y-red-virtual.md)

Encontrarás los pasos prácticos asociados junto al enunciado de la actividad. Incorpora sus evidencias al mismo PDF y entrega todo junto en la tarea de Aules correspondiente.
