# B9. Redes virtuales con una finalidad

> **Del concepto al laboratorio:** [P5 · Redes y página web](practicas/p5-redes.md) · [P9 · Proyecto integrador](practicas/p9-proyecto.md)

## 9.1. Las preguntas que decide una red

Antes de elegir modo, determina quién debe iniciar la comunicación: invitado hacia Internet, anfitrión hacia invitado o un invitado hacia otro. NAT individual sirve para salida habitual; no crea por defecto una red compartida entre todas las VM. Red NAT permite agrupar invitados con salida. Solo anfitrión comunica el anfitrión y las VM de esa red, sin salida exterior por ese adaptador. Red interna comunica las VM conectadas al mismo nombre de red. Puente incorpora el invitado a la red física y requiere permiso del centro. Referencia F7.

## 9.2. Diseño del laboratorio

| Modo | Salida a Internet | Inicio desde anfitrión | Comunicación entre invitados |
| --- | --- | --- | --- |
| NAT individual | Sí, según red del anfitrión | Con reenvío para el servicio | No como red compartida por defecto |
| Red NAT | Sí, según configuración | Con reenvío para el servicio | Sí, en la misma Red NAT |
| Solo anfitrión | No por ese adaptador solo | Sí, en esa red | Sí, en esa red |
| Red interna | No por ese adaptador solo | No directamente | Sí, con el mismo nombre de red |
| Puente | Según la red física | Según red y firewall | Según red y firewall |

La tabla resume el comportamiento ordinario sin rutas adicionales. «Sí» no garantiza que un servicio esté activo ni permitido por el firewall. NAT facilita conexiones salientes, pero no debe interpretarse como una política completa de aislamiento frente a todos los recursos del anfitrión o de la LAN.

Utilizaremos NAT para descargar y una red solo anfitrión para acceder a una web del invitado. Con dos adaptadores, cada uno cumple un propósito. El adaptador NAT obtiene normalmente configuración por DHCP. En el adaptador de laboratorio se utiliza la subred aprobada, sin una segunda puerta de enlace por defecto.

Ejemplo: anfitrión 192.168.56.1/24; Ubuntu 192.168.56.10/24; segundo invitado 192.168.56.11/24. Son direcciones de ejemplo: comprueba que no colisionan con la red real, una VPN u otra red virtual. Desactiva DHCP en esa red si se asignan manualmente esas direcciones, o acuerda un rango que no las solape.

## 9.3. IP, puerta de enlace y DNS

La IP identifica una interfaz en una red. La máscara determina qué destinos se consideran locales. La puerta de enlace permite salir hacia otras redes. DNS traduce nombres a direcciones. Tener IP no demuestra que DNS funcione; que falle un ping a un nombre tampoco prueba que «Internet está caído».

Diagnostica por capas: interfaz activa, dirección y máscara, ruta, resolución de nombre y servicio final. Un servidor puede rechazar ICMP y aceptar HTTPS. La aceptación se basa en la comunicación que necesita la tarea, no en un único ping.

## 9.4. Publicar un servicio de prueba

En Ubuntu, dentro de una carpeta que contenga solamente archivos del ejercicio:

```bash
mkdir -p ~/ud3-web
cd ~/ud3-web
printf '<h1>Laboratorio UD3</h1>\n' > index.html
python3 -m http.server 8000 --bind 0.0.0.0
```

El proceso se queda activo en la terminal; se detiene con Ctrl+C. 0.0.0.0 indica escucha en las interfaces IPv4 disponibles. En una red solo anfitrión, abre desde el anfitrión <http://192.168.56.10:8000> usando la IP real. No es un servidor de producción. Si hay firewall, autoriza exclusivamente el tráfico necesario en la red de laboratorio.

Con NAT individual puedes definir reenvío TCP desde 127.0.0.1:8080 del anfitrión al puerto 8000 del invitado. Entonces el navegador del anfitrión abre <http://127.0.0.1:8080>. Esta dirección representa al anfitrión para ese navegador; la regla decide qué servicio del invitado recibe la conexión.

## Actividad A9 · Elegir el modo

Elige red para: actualizar una VM; comunicar dos invitados sin anfitrión ni Internet; acceder desde el anfitrión a una web sin incorporar la VM a la LAN; probar una web desde otros ordenadores del aula. Justifica y señala en qué caso hace falta autorización de red. Continúa con P5.
