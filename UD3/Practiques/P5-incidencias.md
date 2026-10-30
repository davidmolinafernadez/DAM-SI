# P5 · Diagnosticar y preparar el salto a UD4

**Tiempo orientativo:** 120 min · Laboratorio de aula · Entrega individual.

## Preparación

Trabaja con los equipos de prueba de P2 o con las salidas preparadas por el docente. Las averías se introducen únicamente en esa interfaz y se restauran antes de pasar al siguiente caso. No se modifica el router ni el firewall del centro.

## Método y casos

Para cada caso escribe predicción, síntoma, dos hipótesis, prueba que las diferencia, resultado, corrección propuesta y verificación. Se observa de abajo arriba: enlace → dirección y prefijo → red local → ruta → DNS → puerto → aplicación.

| Caso preparado | Qué debes averiguar |
| --- | --- |
| Sin enlace o interfaz de prueba desconectada | Si tiene sentido empezar consultando DNS |
| Dos equipos con prefijos incoherentes | Si el destino se considera local o requiere una ruta |
| Puerta de enlace fuera de la red conectada | Qué destino falla y cuál todavía puede funcionar |
| DNS incorrecto con conectividad IP demostrada | Qué prueba distingue resolución de acceso a servicio |
| Servicio que no responde a ping pero sí al puerto previsto | Por qué ICMP no determina la disponibilidad de la aplicación |

1. Utiliza solo comandos de consulta de P1 y pruebas puntuales al destino autorizado. No ejecutes barridos de direcciones.
2. Solicita al docente una demostración preparada de NAT, puente y red interna o sus esquemas. No es necesario instalar VirtualBox en esta unidad.
3. Para cada modo, indica quién puede hablar con quién, si hay salida y qué depende de DHCP, router o reenvío de puertos. Distingue NAT sencillo por invitado de una red NAT compartida.
4. Diseña el plan que reutilizarás en UD4: interfaces, direcciones, prefijos, servicio previsto y prueba de aceptación. No confundas conectar un adaptador virtual con haber configurado correctamente TCP/IP.
5. Restaura el laboratorio y repite la prueba que demostraba el funcionamiento inicial.

## Aceptación y entrega

Cinco fichas de incidencia, esquema comparado de modos y plan de laboratorio de UD4. Se valora la prueba que justifica el diagnóstico y el estado restaurado, además del resultado final.

**Archivo:** `UD3_P5_Codigo.pdf`. [Índice de prácticas](index.md) · [Cuaderno descargable](../descargas/UD3_Practicas.pdf)
