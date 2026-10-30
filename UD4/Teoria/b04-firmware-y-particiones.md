# 4.1.3 · Firmware, arranque y particiones

<div class="lesson-banner" markdown>
<div class="lesson-number">4.1.3</div>
<div markdown>
**Planificación, medios y arranque**

Firmware, arranque y particiones: explicación, ejemplos y comprobaciones.
</div>
</div>

## Del botón al escritorio

En un arranque normal, el firmware inicializa dispositivos y selecciona un medio. Después se ejecuta un cargador, se carga el kernel y se inicia el sistema de servicios y la sesión. Un error temprano puede impedir que aparezca siquiera el logotipo del sistema. Un error posterior puede permitir arrancar, pero impedir la sesión gráfica.

En una VM la selección de medios es virtual: disco duro, unidad óptica o red. Si el disco está vacío y no hay ISO arrancable, no existe un sistema que cargar. Si se deja la ISO conectada, puede reaparecer el instalador aunque la instalación en el disco sea correcta.

## BIOS, UEFI, Secure Boot y TPM

BIOS heredada y UEFI son modelos de firmware. UEFI puede gestionar entradas de arranque que apuntan a cargadores en una partición EFI. Secure Boot comprueba firmas de componentes de arranque según las claves configuradas. TPM aporta funciones criptográficas, como protección de claves y medición. UEFI, Secure Boot y TPM son conceptos diferentes, aunque aparezcan juntos en los requisitos de un sistema.

Para Windows 11 hay que comprobar CPU compatible, al menos dos procesadores virtuales, 4 GB de memoria, 64 GB de almacenamiento, firmware UEFI con capacidad de arranque seguro y TPM 2.0. La compatibilidad del anfitrión también importa. Son condiciones mínimas; la práctica propone más margen de disco. Consulta F2 y configura las opciones que exija la edición y el hipervisor empleados.

No se modifica el firmware de una VM instalada como si fuera una preferencia visual. Un sistema preparado para un modo puede dejar de arrancar si se cambia a otro. Antes de experimentar, crea un clon completo de prueba y documenta la configuración original.

## Disco, tabla, partición y sistema de archivos

El disco es el dispositivo de almacenamiento. La tabla describe divisiones. Una partición es una región del disco. El sistema de archivos organiza archivos y directorios dentro de un volumen. Formatear una partición no es lo mismo que crear la tabla de particiones de todo el disco.

Ejemplo didáctico de disco Linux UEFI de 50 GiB: partición EFI de 1 GiB en FAT32, raíz de 30 GiB en ext4 y /home con el resto. Los tamaños son decisiones del laboratorio, no un estándar obligatorio. Los metadatos, alineación y unidades pueden producir pequeñas diferencias. El instalador automático puede elegir otro reparto válido.

## MBR y GPT sin reglas falsas

MBR utiliza entradas para hasta cuatro particiones primarias; una puede actuar como extendida que contiene unidades lógicas. Su límite de direccionamiento habitual, con sectores lógicos de 512 bytes, ronda los 2 TiB. No debe expresarse sin indicar el contexto del tamaño de sector.

GPT usa identificadores y mantiene información redundante de la tabla. El número de particiones depende de la implementación y la tabla disponible; no es «infinito». Windows permite habitualmente hasta 128 en una unidad GPT. GPT no exige universalmente UEFI: existen combinaciones con BIOS y cargadores compatibles. Para la instalación moderna de Windows en modo UEFI se utiliza GPT. Referencia F3.

## Qué hace cada partición

La ESP contiene archivos de arranque UEFI y usa FAT32. La raíz Linux, montada en /, contiene el árbol principal del sistema. /home contiene los directorios personales cuando se separa en otra partición. La swap amplía opciones de memoria y puede ser archivo o partición; no reemplaza una cantidad adecuada de RAM. Windows suele crear ESP, MSR, partición del sistema y recuperación; no borres las pequeñas porque no tengan letra.

Una partición de datos en el mismo disco facilita separar contenidos, pero no protege frente a la pérdida del disco. Un /home separado tampoco sustituye una copia. Un reinstalador puede formatearlo si se selecciona la opción equivocada.

## Localizar el fallo en la cadena de arranque

Si el firmware no encuentra medio, todavía no tiene sentido diagnosticar un servicio del escritorio. Si aparece un cargador pero no encuentra raíz, ya se han superado etapas anteriores. Si el kernel y los servicios arrancan y falla la sesión gráfica, la investigación se sitúa en otro nivel. El síntoma se interpreta por el punto alcanzado, no por una solución repetida para todos los errores.

| Etapa observada | Pregunta inicial | Comprobación de lectura |
| --- | --- | --- |
| No aparece medio arrancable | ¿Hay disco instalado o ISO válida? | Configuración de almacenamiento y orden |
| Se abre el instalador otra vez | ¿Sigue conectada la ISO? | Unidad óptica y destino de arranque |
| Cargador con error | ¿El modo de firmware y destino son coherentes? | Entradas y disco esperado |
| Escritorio sin persistencia | ¿Es una sesión Live? | Raíz montada y prueba tras reinicio sin ISO |

## Primaria, extendida y lógica en su contexto

La partición extendida es un mecanismo del esquema MBR para alojar unidades lógicas dentro de una de sus entradas principales. No es una partición que se formatea directamente para guardar documentos. GPT organiza sus entradas de otra manera; no hay que forzar la terminología primaria/extendida para explicar un disco GPT moderno.

Tampoco debe memorizarse un máximo de unidades lógicas como si fuera idéntico en todos los sistemas. El soporte depende de herramientas, controladores y convenciones. En el laboratorio importa reconocer la estructura que realmente muestra el disco y justificar por qué se elige GPT para el itinerario UEFI.

## Actividades de este apartado

Las respuestas se entregan en el archivo de cada actividad; aquí no se ejecutan las instalaciones.

- [Actividad 4.4 · Diseñar el arranque y las particiones](actividades/A04-disenar-el-arranque-y-las-particiones.md)

## Prácticas relacionadas

- [P2 · Instalar Ubuntu](practicas/p2-ubuntu.md)
- [P4 · Particionar y montar](practicas/p4-particionado.md)
- [X1 · Arranque dual](practicas/x1-arranque-dual.md)

<div class="video-card" markdown>

## Vídeo explicativo · Particionar con GParted

V10: observa tabla y partición. Su ejemplo usa MBR; nuestra práctica usa GPT en otro disco.

<div class="video-frame">
<iframe src="https://mediateca.educa.madrid.org/video/417dd5j5i92wjmop/fs" title="Particionar con GParted" loading="lazy" allowfullscreen></iframe>
</div>

[Abrir el vídeo en su página original](https://mediateca.educa.madrid.org/video/417dd5j5i92wjmop) · [Ficha y preguntas de visionado](videos.md)

</div>
