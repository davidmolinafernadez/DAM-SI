# UD2. Fundamentos de sistemas operativos

## 1. Resultados de aprendizaje

Esta unidad permite analizar la arquitectura, funciones, requisitos, campos de aplicación y licencias de los sistemas operativos, preparando la posterior instalación en equipos físicos o virtuales.

## 2. Qué es un sistema operativo

Un sistema operativo es el conjunto de programas que administra los recursos del equipo y proporciona servicios a usuarios y aplicaciones. Sus objetivos son facilitar el uso del hardware, repartir recursos de forma eficiente, proteger la información y ofrecer un entorno estable.

Sus componentes principales son:

- **Núcleo o kernel:** controla CPU, memoria, dispositivos y mecanismos de protección.
- **Controladores:** adaptan las operaciones genéricas del sistema a cada dispositivo.
- **Servicios del sistema:** funciones ejecutadas en segundo plano.
- **Bibliotecas y llamadas al sistema:** interfaz usada por las aplicaciones.
- **Shell e interfaz gráfica:** medios de interacción con el usuario.
- **Utilidades:** herramientas de configuración, diagnóstico y mantenimiento.

## 3. Funciones esenciales

### Gestión de procesos

Un programa es un conjunto de instrucciones; un proceso es una instancia en ejecución. El planificador reparte tiempo de CPU, cambia procesos de estado y coordina su prioridad. Los hilos permiten varias líneas de ejecución dentro de un proceso.

### Gestión de memoria

El sistema asigna memoria, impide accesos indebidos y libera recursos. La memoria
virtual proporciona espacios de direcciones propios y traducción a memoria
física; no es sinónimo de intercambio. Algunas páginas pueden respaldarse en
almacenamiento, mucho más lento que la RAM. Un fallo de página no implica
necesariamente una lectura de disco.

### Gestión de archivos

El sistema organiza datos en archivos y directorios, mantiene metadatos y aplica permisos. La implementación concreta depende del sistema de archivos.

### Entrada/salida y seguridad

Los controladores gestionan dispositivos y el sistema ofrece abstracciones comunes. La identificación, autenticación, autorización y auditoría controlan quién puede realizar cada operación.

## 4. Evolución

Los primeros ordenadores se operaban manualmente. El procesamiento por lotes agrupó trabajos; la multiprogramación mantuvo varios programas en memoria; los sistemas de tiempo compartido introdujeron interacción concurrente. Después aparecieron sistemas personales, de red, distribuidos, móviles, empotrados y orientados a la nube.

## 5. Clasificaciones

Un sistema puede clasificarse según distintos criterios:

- monousuario o multiusuario;
- monotarea o multitarea;
- monoprocesador o multiprocesador;
- centralizado, de red o distribuido;
- de propósito general, tiempo real, móvil o empotrado;
- con núcleo monolítico, micronúcleo o arquitectura híbrida.

Estas categorías pueden combinarse. Un sistema de escritorio moderno suele ser multiusuario, multitarea y multiprocesador.

## 6. Comparación de familias

| Aspecto | Windows | GNU/Linux | macOS |
| --- | --- | --- | --- |
| Licencia | Propietaria | Libre en la mayoría de distribuciones | Propietaria |
| Hardware | Amplio ecosistema | Muy flexible | Integración controlada por Apple |
| Administración | GUI, PowerShell | Shell y múltiples GUI | GUI y shell Unix |
| Uso frecuente | Escritorio y empresa | Servidores, nube y desarrollo | Escritorio creativo y desarrollo |

La elección debe considerar requisitos, compatibilidad, soporte, coste total, seguridad, aplicaciones necesarias y experiencia del equipo humano.

## 7. Licencias de software

El copyright protege una obra automáticamente. Una licencia define los permisos de uso, copia, modificación y distribución.

- **Software propietario:** código y derechos de modificación restringidos.
- **Freeware:** uso gratuito, sin implicar acceso al código.
- **Software libre:** garantiza uso, estudio, modificación y redistribución.
- **Código abierto:** licencias aprobadas que permiten inspección y redistribución.
- **Copyleft:** exige conservar determinadas libertades en obras derivadas.

Ejemplos frecuentes son GPL, LGPL, MIT, BSD y Apache 2.0. Antes de incorporar una dependencia debe revisarse su compatibilidad con el proyecto.

## 8. Introducción a la virtualización

La virtualización desacopla un entorno lógico del hardware físico. Un hipervisor de tipo 1 se ejecuta directamente sobre el hardware; uno de tipo 2 funciona sobre un sistema anfitrión.

Una máquina virtual incluye un sistema operativo invitado completo. Un contenedor comparte el kernel del anfitrión y aísla procesos, por lo que suele iniciar más rápido y ocupar menos espacio. No son tecnologías equivalentes: se elige según el aislamiento, la compatibilidad y el despliegue requerido.

En una máquina virtual hay tres conceptos que deben diferenciarse:

- **anfitrión:** sistema físico que presta recursos;
- **invitado:** sistema operativo que se ejecuta dentro de la VM;
- **hipervisor:** capa que crea y controla las máquinas virtuales.

En contenedores Linux ejecutados desde Windows o macOS, una capa virtualizada
aporta el kernel Linux compartido por los contenedores.

La red de una VM puede configurarse en modo NAT, puente, interna o solo
anfitrión. NAT suele ser suficiente para actualizar y navegar; puente hace que la
VM aparezca como otro equipo de la red y debe elegirse con más cuidado. Las
instantáneas ayudan a volver a un estado anterior, pero no sustituyen a una copia
de seguridad externa.

## 9. Criterios para elegir un sistema

1. Identificar aplicaciones y servicios necesarios.
2. Revisar requisitos mínimos y recomendados.
3. Confirmar compatibilidad de hardware y periféricos.
4. Evaluar licencia, soporte y ciclo de actualizaciones.
5. Analizar seguridad, administración y recuperación.
6. Probar en una máquina virtual antes de adoptar.
7. Documentar la decisión y sus evidencias.

## 10. Resumen

### Conceptos que debes saber distinguir

| Conceptos | Diferencia esencial |
|---|---|
| API / llamada al sistema | Interfaz para programar / entrada controlada al kernel |
| Programa / proceso / hilo | Instrucciones / instancia con recursos / línea de ejecución |
| Preparado / bloqueado | Espera CPU / espera un evento |
| Concurrencia / paralelismo | Progreso en un intervalo / ejecución simultánea |
| RAM / memoria virtual / intercambio | Recurso físico / direcciones y traducción / respaldo en almacenamiento |
| Búfer / caché / spool | Adaptar ritmos / reutilizar copias / mantener una cola de trabajos |
| Libre / gratuito / comercial | Derechos / precio / actividad económica |
| Instantánea / copia | Retorno dependiente de la VM / recuperación independiente |

Para estudiar los ejemplos desarrollados, vuelve a
[arquitectura](01-arquitectura-y-funciones.md),
[procesos y memoria](02-procesos-memoria-e-io.md),
[elección del sistema](03-familias-licencias-y-eleccion.md) y
[virtualización](04-virtualizacion-y-arranque.md).

El sistema operativo actúa como gestor de recursos y plataforma de servicios. Comprender procesos, memoria, archivos, seguridad y licencias permite seleccionar con criterio y preparar una instalación reproducible.

## 11. Actividades de la unidad

| Actividad | Evidencia principal |
|---|---|
| Tarea 2.1 · Mapa de capas del sistema operativo | Diagrama de capas y explicación de una operación real |
| Tarea 2.2 · Comparativa de gestión de procesos | Comparación de Windows, GNU/Linux y macOS con casos y fuentes |
| Tarea 2.3 · Elección justificada de sistema operativo | Matriz ponderada y decisión documentada |
| Tarea 2.1.1 · Diagnóstico de rendimiento | Hipótesis, plan de diagnóstico y medidas correctoras |
| Tarea 2.3.1 · Ficha de una máquina virtual reproducible | Configuración justificada y evidencias de arranque |

## Fuentes internas utilizadas

- `Jose_SO/UD2.pdf`.
- `SI_Celia/Unit_2_Operating-Systems-Fundamentals-and-Virtualisation/UP_2_1_TEORIA_Sistemes_operatius.pdf`.
- `Programacion_Didactica_SI_David_Moli.docx`.

## Fuentes externas de comprobación

- [Microsoft Learn · Requisitos de Windows 11](https://learn.microsoft.com/es-es/windows/whats-new/windows-11-requirements).
- [Ubuntu · Ciclo de versiones](https://ubuntu.com/about/release-cycle).
- [Open Source Initiative · Licencias aprobadas](https://opensource.org/licenses).
- [GNU · ¿Qué es el software libre?](https://www.gnu.org/philosophy/free-sw.es.html).
- [Apache Software Foundation · Licencias](https://www.apache.org/licenses/).
