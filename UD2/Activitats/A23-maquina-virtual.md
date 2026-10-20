# Tarea 2.3.1 · Ficha de una máquina virtual reproducible

<div class="lesson-banner" markdown>
<div class="lesson-number">2.3.1</div>
<div markdown>
**Reto de laboratorio**

Diseña una máquina virtual para pruebas de DAM y documenta cómo repetirla.
</div>
</div>

<div class="activity-meta" markdown>
<span>60 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

Los 60 minutos corresponden a configurar y documentar una VM con una imagen
ya descargada y preparada por el profesorado. Si se instala desde cero, añade
el tiempo de descarga, instalación y actualización indicado en clase.

## Producto final

PDF llamado `Tarea_2_3_1_Apellidos_Nombre.pdf`, con ficha técnica, capturas y
decisiones justificadas. No se entrega la máquina virtual.

## Fase 1 · Objetivo

Define para qué usarás la VM:

- practicar instalación de GNU/Linux;
- probar una aplicación sin modificar el equipo anfitrión;
- montar un servidor web local;
- experimentar con usuarios, permisos y red;
- preparar un entorno reproducible de clase.

## Fase 2 · Ficha técnica

| Elemento | Decisión | Justificación |
|---|---|---|
| Hipervisor |  |  |
| Sistema invitado |  |  |
| Versión y arquitectura de anfitrión e invitado |  |  |
| CPU virtual |  |  |
| RAM |  |  |
| Disco virtual |  |  |
| Red |  |  |
| Carpetas compartidas |  |  |
| Instantáneas |  |  |

Añade también si usarás firmware BIOS o UEFI y si activarás funciones como EFI,
Secure Boot o TPM virtual cuando el sistema invitado lo requiera.

## Fase 3 · Seguridad y límites

Responde:

1. ¿Qué diferencia hay entre anfitrión e invitado?
2. ¿Qué se aísla bien en una VM y qué no debes dar por seguro?
3. ¿Por qué una instantánea no sustituye a una copia de seguridad?
4. ¿Cuándo elegirías un contenedor en lugar de una VM?

## Fase 4 · Evidencias

Incluye capturas de configuración y del sistema invitado arrancado. Añade la URL
oficial de descarga del sistema elegido y fecha de consulta.

## Evidencias mínimas

Tu ficha debe permitir que otra persona cree una VM equivalente. Incluye:

- captura de la configuración general, sistema, almacenamiento y red;
- captura del sistema invitado arrancado;
- usuario inicial previsto, sin escribir contraseñas;
- URL oficial de descarga y fecha de consulta;
- explicación de qué instantánea crearías y cuándo.

Anota también versión del hipervisor, RAM total del anfitrión y margen que le
dejas, capacidad máxima del disco virtual y espacio disponible en el disco
físico. Comprueba arranque y conectividad según el modo elegido; una red interna
sin salida a Internet puede ser correcta si ese es el objetivo documentado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Ficha técnica completa | 3 |
| Justificación de recursos | 2 |
| Seguridad, snapshots y aislamiento | 2 |
| Evidencias y fuente oficial | 2 |
| Presentación | 1 |
