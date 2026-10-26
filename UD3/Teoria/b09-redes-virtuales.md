# 3.5 · Redes virtuales con una finalidad

<div class="lesson-banner" markdown>
<div class="lesson-number">3.5</div>
<div markdown>
**Redes del laboratorio**

Redes virtuales y servicio web: explicación, ejemplos y comprobaciones.
</div>
</div>

## Las preguntas que decide una red

Antes de elegir modo, determina quién debe iniciar la comunicación: invitado hacia Internet, anfitrión hacia invitado o un invitado hacia otro. NAT individual sirve para salida habitual; no crea por defecto una red compartida entre todas las VM. Red NAT permite agrupar invitados con salida. Solo anfitrión comunica el anfitrión y las VM de esa red, sin salida exterior por ese adaptador. Red interna comunica las VM conectadas al mismo nombre de red. Puente incorpora el invitado a la red física y requiere permiso del centro. Referencia F7.

## Diseño del laboratorio

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

## IP, puerta de enlace y DNS

La IP identifica una interfaz en una red. La máscara determina qué destinos se consideran locales. La puerta de enlace permite salir hacia otras redes. DNS traduce nombres a direcciones. Tener IP no demuestra que DNS funcione; que falle un ping a un nombre tampoco prueba que «Internet está caído».

Diagnostica por capas: interfaz activa, dirección y máscara, ruta, resolución de nombre y servicio final. Un servidor puede rechazar ICMP y aceptar HTTPS. La aceptación se basa en la comunicación que necesita la tarea, no en un único ping.

## Publicar un servicio de prueba

En Ubuntu, dentro de una carpeta que contenga solamente archivos del ejercicio:

```bash
mkdir -p ~/ud3-web
cd ~/ud3-web
printf '<h1>Laboratorio UD3</h1>\n' > index.html
python3 -m http.server 8000 --bind 0.0.0.0
```

El proceso se queda activo en la terminal; se detiene con Ctrl+C. 0.0.0.0 indica escucha en las interfaces IPv4 disponibles. En una red solo anfitrión, abre desde el anfitrión <http://192.168.56.10:8000> usando la IP real. No es un servidor de producción. Si hay firewall, autoriza exclusivamente el tráfico necesario en la red de laboratorio.

Con NAT individual puedes definir reenvío TCP desde 127.0.0.1:8080 del anfitrión al puerto 8000 del invitado. Entonces el navegador del anfitrión abre <http://127.0.0.1:8080>. Esta dirección representa al anfitrión para ese navegador; la regla decide qué servicio del invitado recibe la conexión.

## Diagnosticar con dos navegadores y una terminal

La primera petición se hace desde el invitado a su bucle local: comprueba proceso y puerto sin atravesar la red virtual. La segunda llega desde el anfitrión a la IP del adaptador de laboratorio: añade tarjeta, dirección, ruta y firewall. La tercera utiliza el bucle local del anfitrión y una regla NAT: comprueba además la traducción de puerto.

Comparar estos resultados permite acotar un fallo. Si no responde ni dentro del invitado, el primer sospechoso es el servicio, su carpeta o su puerto. Si funciona allí pero no por la ruta externa, no hay que reinstalar Ubuntu: se revisan las condiciones que esa segunda ruta incorpora.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 3.9 · Elegir una red virtual para cada encargo](actividades/A09-elegir-una-red-virtual-para-cada-encargo.md)

## Prácticas relacionadas

- [P5 · Redes y página web](practicas/p5-redes.md)

<div class="video-card" markdown>

## Vídeo explicativo · Red NAT y reenvío

V5: el ejemplo utiliza SSH. Traduce su recorrido al HTTP de P5 con tus direcciones y puertos.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/amomshvzq7iz1llo/fs" title="Red NAT y reenvío" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/amomshvzq7iz1llo) · [Ficha y preguntas de visionado](videos.md)

</div>
