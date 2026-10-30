# 1. Planificación, arranque y particionado

## 1.1 Instalar es tomar decisiones

Una instalación profesional empieza antes del instalador. Se define función, software, requisitos, disponibilidad, usuarios, datos, red, seguridad y mantenimiento.

```mermaid
flowchart LR
    N["Necesidades"] --> R["Requisitos"]
    R --> B["Copia y reversión"]
    B --> M["Medio verificado"]
    M --> P["Particionado"]
    P --> I["Instalación"]
    I --> V["Validación y documentación"]
```

### Hoja de planificación

- Sistema, edición, versión y arquitectura.
- Requisitos mínimos, recomendados y margen.
- Origen de ISO y SHA-256 esperado.
- UEFI, Secure Boot y virtualización de hardware.
- Disco de destino y datos que contiene.
- GPT/MBR, particiones, tamaños y sistemas de archivos.
- Nombre del equipo, zona horaria, cuentas y red.
- Aplicaciones, controladores y actualizaciones.
- Copia previa, recuperación y pruebas finales.

## 1.2 Verificación de la imagen

Descargar desde una fuente oficial reduce riesgo. La suma detecta corrupción:

```powershell
Get-FileHash .\ubuntu.iso -Algorithm SHA256
```

```bash
sha256sum ubuntu.iso
```

El valor debe compararse carácter por carácter con el publicado por una fuente confiable. Una suma obtenida del mismo sitio comprometido no aporta una garantía completa; las firmas digitales añaden autenticidad.

## 1.3 UEFI y cadena de arranque

UEFI carga un ejecutable desde la partición EFI. Secure Boot verifica firmas de componentes de arranque. Desactivarlo sin necesidad reduce protección; si un sistema o controlador no es compatible, se documenta la excepción.

```mermaid
flowchart LR
    U["UEFI"] --> E["Partición EFI"]
    E --> G["Gestor de arranque"]
    G --> K["Kernel"]
    K --> ROOT["Sistema raíz"]
```

## 1.4 MBR y GPT

MBR guarda información en el primer sector y presenta limitaciones de tamaño y particiones. GPT utiliza identificadores, copias de cabecera y comprobaciones; es la elección habitual con UEFI.

| Aspecto | MBR | GPT |
| --- | --- | --- |
| Entorno típico | BIOS heredado | UEFI |
| Discos grandes | Limitado | Admitidos |
| Particiones | Cuatro primarias sin extensión | Numerosas entradas |
| Redundancia | No | Cabecera y tabla de respaldo |

## 1.5 Diseñar particiones

Separar datos puede facilitar reinstalación y cuotas, pero añade decisiones de tamaño. Un único volumen es más sencillo. La solución depende del uso.

Ejemplo de VM Linux de 80 GiB:

- EFI: 512 MiB, FAT32;
- `/`: 30 GiB, ext4;
- `/home`: resto, ext4;
- intercambio: archivo administrado por el sistema.

Para un servidor se podrían separar `/var` o datos de aplicación para evitar que registros llenen la raíz.

## Caso resuelto: arranque dual

1. Copia verificada de datos.
2. Confirmación de UEFI/GPT en ambos sistemas.
3. Reducción del volumen existente desde su propia herramienta.
4. Creación de espacio sin asignar, sin borrar partición EFI.
5. Instalación del segundo sistema en ese espacio.
6. Verificación de ambos arranques, hora y acceso a datos.
7. Creación de medio de recuperación.

El cifrado y el inicio rápido pueden afectar al acceso compartido; se revisan antes de modificar volúmenes.

## Errores críticos

- Elegir el disco equivocado.
- Formatear una partición de datos.
- Crear un medio desde una ISO no verificada.
- Asignar todos los recursos del anfitrión a una VM.
- No disponer de copia ni medio de recuperación.
