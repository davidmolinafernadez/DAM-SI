# P5. Redes virtuales y una web accesible

**Teoría relacionada:** [Redes virtuales y servicio web](../b09-redes-virtuales.md)

Duración: 180 minutos. Teoría: B9. Vídeo V5. Producto: mapa de red y pruebas HTTP por dos rutas.

## Preparación

VM Ubuntu con python3 disponible. Usa únicamente la red del laboratorio. En esta práctica no hace falta puente. Predice desde qué sistema será accesible 127.0.0.1 en cada prueba.

## Fase A · NAT y diagnóstico

1. Arranca con un adaptador NAT. Registra ip -br address e ip route. Identifica interfaz, IP y puerta de enlace.
2. Comprueba resolución con getent hosts ubuntu.com y conexión con el navegador a <https://ubuntu.com>. Si curl ya está instalado puedes usar curl -I <https://ubuntu.com>. Distingue resolución y respuesta del servicio.
3. Desconecta el «cable» del adaptador desde VirtualBox, observa el fallo y recoge el estado de la interfaz. Reconecta y comprueba recuperación. No alteres la tarjeta física del anfitrión.

## Fase B · Solo anfitrión

1. Apaga Ubuntu. En el gestor de red de VirtualBox crea o identifica una red solo anfitrión. Documenta IP y máscara del adaptador del anfitrión. El ejemplo usa 192.168.56.1/24, pero debes adaptarlo si hay solapamiento.
2. Decide con el docente: DHCP de esa red con direcciones asignadas automáticamente, o direcciones estáticas sin solapar el rango DHCP. Si trabajas con estáticas 192.168.56.10/24 y .11/24, evita que DHCP las reparta.
3. Añade un segundo adaptador a Ubuntu conectado a esa red. Mantén el primero en NAT para salida. Arranca y localiza ambas interfaces por su MAC y configuración; no supongas un nombre fijo como enp0s8.
4. Configura el segundo adaptador con la IP de aula mediante la interfaz de Ubuntu. En la red solo anfitrión no añadas una segunda puerta de enlace por defecto ni DNS innecesario. Consulta ip route para comprobarlo.
5. Crea ~/ud3-web e index.html siguiendo B9, con un mensaje que incluya el código de tu máquina. Ejecuta python3 -m http.server 8000 --bind 0.0.0.0 desde esa carpeta. Mantén la terminal abierta.
6. En Ubuntu visita <http://127.0.0.1:8000>. Desde el anfitrión visita <http://IP_REAL_DE_UBUNTU:8000>. Sustituye el texto por la IP del segundo adaptador. Registra el acceso que aparece en la terminal del servidor.
7. Detén el servidor con Ctrl+C y repite desde el anfitrión. Explica por qué una IP correcta no garantiza que haya un servicio escuchando.

## Fase C · NAT con reenvío

1. Apaga la VM y desactiva temporalmente el segundo adaptador. En el NAT del primero crea la regla TCP: IP anfitrión 127.0.0.1, puerto anfitrión 8080, puerto invitado 8000. Si pide IP invitado, usa la IP NAT actual de esa VM y revisa que no cambie. No vincules la regla a todas las interfaces del equipo.
2. Arranca y ejecuta de nuevo el servidor dentro de Ubuntu. Desde el anfitrión abre <http://127.0.0.1:8080>. Si el puerto está ocupado, elige otro y documenta ambos extremos.
3. Explica el recorrido navegador anfitrión → 127.0.0.1:8080 → regla NAT → invitado:8000. Borra o deshabilita la regla al terminar si no será necesaria para el proyecto.

## Aceptación e incidencia

Aceptación: salida NAT comprobada, acceso por solo anfitrión y acceso mediante reenvío, con las IP/puertos reales y sin puente. Entrega diagrama, tabla de interfaces y tres pruebas con explicación.

Incidencia: el servidor responde dentro de Ubuntu, pero no desde el anfitrión. Comprueba primero si escucha en 127.0.0.1 en lugar de 0.0.0.0; después interfaz elegida, IP, regla, puerto y firewall. Si el firewall está activo, utiliza una regla limitada a la red y puerto necesarios y documenta su retirada. No lo desactives globalmente.

Ampliación: conecta un clon Ubuntu a la misma red solo anfitrión y prueba acceso entre invitados. Evita IP repetida y MAC duplicada. Después explica la diferencia con Red NAT y con Red interna.
