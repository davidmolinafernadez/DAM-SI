# UD7. Recursos en red, seguridad y documentación

## 1. Resultados de aprendizaje

El alumnado administrará recursos compartidos, aplicará medidas básicas de seguridad y elaborará documentación técnica que permita operar, verificar y recuperar un sistema.

## 2. Servicios y recursos en red

Un servicio de red escucha en una interfaz y puerto y responde a un protocolo. El hecho de que un proceso esté activo no garantiza que el servicio sea accesible: deben comprobarse dirección de escucha, firewall, ruta, resolución de nombres y permisos.

Servicios habituales:

| Servicio | Función | Puerto habitual |
| --- | --- | --- |
| DNS | Resolución de nombres | 53 TCP/UDP |
| DHCP | Configuración automática | 67/68 UDP |
| HTTP/HTTPS | Aplicaciones web | 80/443 TCP |
| SSH | Administración remota segura | 22 TCP |
| SMB | Archivos e impresoras | 445 TCP |

Los puertos conocidos son valores predeterminados, no una garantía. La configuración real debe verificarse.

## 3. Compartición de archivos

SMB es común en entornos Windows y mixtos. NFS es habitual entre sistemas Unix/Linux. Al publicar una carpeta deben definirse:

- usuarios o grupos autorizados;
- permisos del recurso y del sistema de archivos;
- lectura o escritura necesaria;
- límites, auditoría y copias;
- nombre DNS y disponibilidad esperada.

El permiso efectivo resulta de combinar varias capas. Una configuración permisiva en la compartición no supera una ACL local restrictiva.

## 4. Administración remota

SSH cifra la sesión y admite autenticación por clave. La clave privada nunca se comparte; la pública se instala en el servidor.

```bash
ssh-keygen -t ed25519
ssh-copy-id usuari@servidor
ssh usuari@servidor
```

Tras verificar el acceso con clave puede limitarse el uso de contraseñas. La cuenta `root` no debería iniciar sesión remotamente de forma directa. En Windows, PowerShell Remoting y OpenSSH deben configurarse con reglas de firewall y autenticación adecuadas.

## 5. Principios de seguridad

La seguridad persigue:

- **confidencialidad:** solo acceden personas autorizadas;
- **integridad:** los datos no se modifican sin control;
- **disponibilidad:** servicios y datos están accesibles cuando se necesitan;
- **autenticidad y trazabilidad:** se conoce la identidad y queda evidencia de acciones.

La defensa en profundidad combina controles. Ninguna medida aislada es suficiente.

## 6. Gestión de riesgos

Un activo tiene valor; una amenaza puede dañarlo; una vulnerabilidad permite que la amenaza se materialice. El riesgo combina probabilidad e impacto.

Proceso básico:

1. Inventariar activos y responsables.
2. Identificar amenazas y vulnerabilidades.
3. Estimar probabilidad e impacto.
4. Priorizar riesgos.
5. Aplicar controles preventivos, detectivos y correctivos.
6. Verificar y revisar periódicamente.

Los riesgos pueden mitigarse, evitarse, transferirse o aceptarse de forma justificada.

## 7. Bastionado

Una línea base de endurecimiento incluye:

- actualizar sistema, aplicaciones y firmware;
- retirar software, cuentas y servicios innecesarios;
- aplicar privilegio mínimo y separación de funciones;
- usar MFA y gestores de contraseñas;
- configurar firewall con política restrictiva;
- cifrar dispositivos y comunicaciones;
- proteger y probar copias de seguridad;
- centralizar registros y revisar alertas;
- sincronizar la hora;
- documentar excepciones y cambios.

Los secretos no deben guardarse en repositorios. Se usan almacenes de credenciales, variables protegidas o gestores de secretos.

## 8. Firewall y segmentación

Un firewall decide tráfico según origen, destino, protocolo, puerto y estado. Debe permitirse solo lo necesario y documentar cada excepción.

La segmentación separa equipos por función o nivel de confianza. Una red de invitados, servidores y puestos de administración no debería compartir el mismo dominio sin controles. Las reglas deben verificarse desde ambos lados y revisarse tras cualquier cambio.

## 9. Copias y respuesta a incidentes

Las copias deben estar aisladas de las credenciales ordinarias y contar con versiones inmutables o desconectadas. La restauración se prueba con objetivos RPO y RTO.

Ante un incidente:

1. Detectar y registrar hora, alcance y síntomas.
2. Contener sin destruir evidencias.
3. Preservar registros y copias relevantes.
4. Erradicar la causa.
5. Recuperar desde un estado confiable.
6. Verificar servicios y monitorizar recurrencias.
7. Documentar lecciones y acciones preventivas.

No se deben improvisar acciones destructivas antes de preservar evidencias y confirmar el alcance.

## 10. Documentación técnica

Una memoria técnica útil incluye:

- objetivo, alcance y responsables;
- inventario y diagrama de red;
- versiones y dependencias;
- procedimiento reproducible;
- decisiones y alternativas descartadas;
- configuración sin secretos;
- pruebas, resultados y criterios de aceptación;
- copia, restauración y reversión;
- incidencias conocidas y mantenimiento.

Los comandos se presentan en bloques copiables y se explica el resultado esperado. Las capturas deben mostrar solo información necesaria y ocultar datos personales, tokens, direcciones públicas o credenciales.

## 11. Proyecto integrador

Como cierre se propone desplegar dos máquinas virtuales o contenedores, configurar red y nombres, publicar un recurso, crear grupos y permisos, limitar el firewall, automatizar una copia y entregar una memoria con pruebas de recuperación.

La aceptación exige que otro compañero pueda reproducir el despliegue únicamente con la documentación entregada.

## 12. Resumen

Compartir recursos de forma profesional implica controlar identidades, permisos, red, cifrado, copias y registros. La documentación forma parte del sistema: sin ella no hay operación repetible ni recuperación fiable.

## Fuentes internas utilizadas

- `Programacion_Didactica_SI_David_Moli.docx`.
- `SI_Celia/Unit_3_Administracio_de_SO_Linux/`.
- `SI_Celia/Unit_4_Networks/`.
- Materiales de copias y administración incluidos en `Jose_SO/UD4.pdf`.
