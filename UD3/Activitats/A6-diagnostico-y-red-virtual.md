# Actividad 3.6 · Justificar una configuración

**Tiempo orientativo:** 60 min · Individual · RA1/RA5 y documentación RA7.

## Encargo

Se propone para un laboratorio: equipo A `192.168.50.10/24`, equipo B `192.168.50.20/24` y puerta de enlace `192.168.60.1`. El segmento tiene un servidor DHCP autorizado, pero una interfaz obtiene `169.254.15.8/16`.

1. Localiza la incoherencia de la puerta de enlace y propón una corrección compatible con la topología. Indica qué información debes confirmar antes de aplicarla.
2. Explica por qué A y B pueden comunicarse localmente sin salida a Internet y qué pruebas lo demostrarían.
3. Para la interfaz con dirección de enlace local, formula dos causas posibles y una comprobación de cada una. No atribuyas automáticamente todo al servidor DHCP.
4. El DNS devuelve una dirección, pero el servidor no responde a ping. ¿Qué prueba de servicio harías antes de afirmar que DNS falla?
5. Relaciona tres encargos con NAT, puente o red interna: invitado que necesita descargar actualizaciones, invitado que debe aparecer como equipo de la LAN autorizada y dos invitados que solo deben hablar entre sí. Explica los límites del NAT sencillo para comunicar invitados.
6. Diseña un registro síntoma → hipótesis → prueba → resultado → cambio autorizado → verificación → restauración.

## Entrega y valoración

Informe con decisiones y pruebas. Diagnóstico: 4 puntos; elección de redes virtuales: 3; comprobación y restauración: 2; claridad: 1. Se completa con P2, P3 y P5; no requiere crear máquinas virtuales antes de UD4.

**Archivo:** `UD3_A6_Codigo.pdf`. [Índice de actividades](index.md) · [Cuaderno descargable](../descargas/UD3_Actividades.pdf)
