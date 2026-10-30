# P5. Redes virtuales y una web accesible

<div class="lesson-banner" markdown>
<div class="lesson-number">P5</div>
<div markdown>
**Práctica guiada de laboratorio**

Sigue los menús, registra las decisiones y comprueba el resultado.
</div>
</div>

**Teoría relacionada:** [Redes virtuales y servicio web](../b09-redes-virtuales.md)

Duración orientativa: 180 minutos. Se usa Ubuntu instalado, Python 3 y dos rutas de acceso. Anota siempre desde qué ordenador abres el navegador: `127.0.0.1` representa a ese sistema concreto.

## 1. Comprueba el adaptador NAT

Con Ubuntu apagado, selecciona su VM → **Configuración → Red → Adaptador 1**. Comprueba **Habilitar adaptador**, **Conectado a: NAT** y, en opciones avanzadas si procede, **Cable conectado**. Guarda con **Aceptar** y arranca.

Dentro de Ubuntu abre una terminal con **Ctrl + Alt + T**. Ejecuta `ip -br address`, `ip route` y `getent hosts ubuntu.com`. Distingue interfaz, dirección, ruta por defecto y resolución. Abre Firefox desde el dock o **Mostrar aplicaciones → Firefox** y visita la web indicada en la teoría. Un ping aislado no es una prueba suficiente del servicio HTTPS.

## 2. Crea la red solo anfitrión

1. Apaga Ubuntu. Vuelve al administrador de VirtualBox: no busques este gestor dentro del invitado.
2. Abre **Archivo → Herramientas → Administrador de red**, o la herramienta global **Red** que muestre tu versión. En la pestaña **Redes solo anfitrión / Host-only Networks**, pulsa **Crear**. Windows puede solicitar autorización para crear un adaptador virtual; en el aula lo gestiona el docente.
3. Selecciona la red creada y abre **Propiedades**. En el adaptador utiliza la dirección y máscara aprobadas; el ejemplo es `192.168.56.1` y `255.255.255.0`.
4. En la pestaña **Servidor DHCP**, elige con el docente una de dos rutas: DHCP con rango documentado, o asignación estática sin un servidor que pueda repartir las mismas direcciones. Para este ejemplo estático no debe haber solapamiento con `.10` y `.11`.
5. Guarda. Antes de usar la subred, comprueba que no colisiona con una VPN u otra red del puesto. Si el rango es distinto, sustituye todas las direcciones del ejercicio de manera coherente.

## 4. Conecta el segundo adaptador a Ubuntu

Selecciona la VM → **Configuración → Red → Adaptador 2**. Marca **Habilitar adaptador** y elige **Adaptador solo anfitrión** o equivalente en **Conectado a**. En **Nombre**, selecciona la red creada. No cambies el Adaptador 1, que mantiene la salida NAT.

Arranca Ubuntu y consulta `ip -br address`. Localiza el nuevo adaptador contrastando la MAC de VirtualBox con la interfaz del invitado. No supongas que se llama siempre `enp0s8`.

## 4. Configura IPv4 en el escritorio Ubuntu

Abre el menú de estado superior derecho → **Configuración** → **Red**. Localiza la conexión cableada del segundo adaptador y pulsa su **engranaje**. En **IPv4**, elige **Manual**. Escribe dirección `192.168.56.10` y máscara `255.255.255.0` o prefijo `24`, según el campo. Deja vacía la puerta de enlace de esta conexión y no añadas DNS innecesario. La salida seguirá por NAT.

Pulsa **Aplicar**. Si no se actualiza el perfil, desactiva y activa esa conexión desde su interruptor. Ejecuta otra vez `ip -br address` e `ip route`. Debes ver la red de laboratorio y una ruta por defecto asociada a NAT. Si configuraste por error otra puerta de enlace, corrige ese perfil antes de continuar.

## 5. Crea y prueba el servidor web

Abre una terminal del Ubuntu invitado y ejecuta una orden cada vez:

```bash
mkdir -p ~/ud4-web
cd ~/ud4-web
printf '<h1>Web del laboratorio UD4</h1>\n' > index.html
python3 -m http.server 8000 --bind 0.0.0.0
```

La última orden mantiene el proceso activo: que no vuelva a aparecer el prompt no significa que se haya bloqueado. Abre el navegador **dentro de Ubuntu** y visita `http://127.0.0.1:8000`. Después abre el navegador **del anfitrión** y visita `http://192.168.56.10:8000`, usando la IP real si es distinta. Mira la terminal del servidor: debe registrar las peticiones recibidas.

Pulsa **Ctrl + C** en la terminal del servidor y recarga la página del anfitrión. Ahora el proceso no escucha. Explica por qué la IP puede seguir bien configurada aunque la web falle. Vuelve a ejecutar el servidor para recuperar el servicio.

## 6. Prueba una segunda ruta con reenvío NAT

Apaga Ubuntu. En **Configuración → Red → Adaptador 2** desmarca temporalmente su habilitación. Abre **Adaptador 1**, que sigue en NAT, despliega **Avanzadas** y pulsa **Reenvío de puertos**. Añade una regla con el botón **+**:

| Campo | Valor del ejercicio | Significado |
| --- | --- | --- |
| Nombre | web-ud4 | Etiqueta de la regla |
| Protocolo | TCP | Transporte utilizado por HTTP |
| IP anfitrión | 127.0.0.1 | Acceso desde el propio anfitrión |
| Puerto anfitrión | 8080 | Puerto que abrirá su navegador |
| IP invitado | IP NAT real, si es necesaria | Destino dentro de esa VM |
| Puerto invitado | 8000 | Puerto del servidor Python |

No uses en la regla la dirección solo anfitrión del adaptador desactivado. Puedes dejar la IP del invitado sin fijar si la versión y configuración NAT lo permiten; si la escribes, compruébala y documenta su vigencia. Guarda ambos diálogos con **Aceptar**. Arranca, inicia el servidor desde `~/ud4-web` y abre `http://127.0.0.1:8080` **en el anfitrión**.

## 7. Diagnóstico y entrega

Si responde dentro de Ubuntu y falla desde fuera, comprueba dirección de escucha, IP utilizada, adaptador, regla y firewall. No desactives globalmente la protección: cualquier regla se limita a red y puerto necesarios. Si 8080 está ocupado en el anfitrión, acuerda otro puerto y cambia la URL correspondiente, sin cambiar por ello el puerto 8000 del servidor.

Entrega diagrama con IP y puertos reales, prueba por solo anfitrión, prueba por NAT y explicación del fallo al detener Python. Al terminar, detén el servidor y retira la regla si no la utilizarás para P9. La ampliación conecta un segundo invitado a la misma red con MAC e IP diferentes.

## Entrega independiente de la práctica

Guarda `P5_Apellidos_Nombre.pdf`. Incluye preparación, decisiones, comprobaciones e incidencia, con las evidencias que pide esta guía. Las actividades escritas tienen su propio archivo; no sustituyen la demostración funcional de la práctica.

<div class="video-card" markdown>

## Vídeo explicativo · Red NAT y reenvío

V5: el ejemplo utiliza SSH. Traduce su recorrido al HTTP de P5 con tus direcciones y puertos.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/amomshvzq7iz1llo/fs" title="Red NAT y reenvío" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/amomshvzq7iz1llo) · [Ficha y preguntas de visionado](../videos.md)

</div>
