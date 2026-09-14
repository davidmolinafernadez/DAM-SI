# Tarea 1.2.1 · Auditoría de compatibilidad

<div class="activity-meta" markdown>
<span>110 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

[:material-download: **Descargar actividad editable para LibreOffice (.odt)**](descargas/Tarea_1_2_1_Compatibilidad_Apellidos_Nombre.odt){ .md-button .md-button--primary download }
[:material-file-pdf-box: **Abrir o descargar en PDF**](descargas/Tarea_1_2_1_Compatibilidad_Apellidos_Nombre.pdf){ .md-button }

Descarga el documento, guárdalo en tu equipo, sustituye `Apellidos_Nombre` por
tus datos y complétalo con LibreOffice Writer. La entrega se realiza en Aules.

## Encargo

Una empresa necesita seis equipos para aplicaciones multiplataforma, bases de
datos locales, contenedores y dos máquinas virtuales simultáneas. Propón una
configuración equilibrada y demuestra su compatibilidad.

## Requisitos

- 32 GB de RAM ampliables como mínimo;
- SSD NVMe de 1 TB o más;
- red de 1 Gb/s o superior y dos monitores;
- virtualización por hardware;
- vida útil prevista de cuatro años;
- GPU dedicada únicamente si se justifica.

## Condiciones del encargo

- Presupuesto máximo orientativo por equipo: `1 050 €`, IVA incluido.
- La configuración debe poder comprarse y montarse en la fecha de realización.
- El equipo ejecutará Linux como anfitrión y una VM Windows para pruebas.
- No se acepta un configurador comercial como única prueba de compatibilidad.
- Una fuente secundaria puede orientar, pero cada decisión crítica necesita
  documentación oficial del fabricante.

## Matriz obligatoria

| Comprobación | Evidencia oficial | Resultado | Riesgo o condición |
|---|---|---|---|
| CPU y zócalo |  | Compatible / No |  |
| Chipset y CPU Support List |  |  |  |
| Versión mínima UEFI/BIOS |  |  |  |
| RAM, canales y capacidad |  |  |  |
| QVL o justificación |  |  |  |
| M.2, PCIe y recursos compartidos |  |  |  |
| Fuente y conectores |  |  |  |
| Caja y refrigeración |  |  |  |
| SO, virtualización y controladores |  |  |  |

Añade tres incompatibilidades descartadas y explica cómo las detectaste.

## Casos obligatorios que debes resolver

1. **Socket parecido, plataforma distinta:** explica por qué una CPU LGA1851 no
   funciona en una placa LGA1700 aunque sus dimensiones sean semejantes.
2. **Firmware:** encuentra una CPU admitida desde una versión concreta de UEFI y
   diseña el procedimiento si la placa llega con una versión anterior.
3. **RAM:** calcula el ancho de banda teórico por canal del kit elegido a partir
   de sus MT/s y explica QVL, XMP/EXPO y configuración de dos módulos.
4. **Líneas compartidas:** localiza una nota real del manual donde una ranura M.2
   comparta recursos o modifique otra ranura/puerto.
5. **Térmica y energía:** comprueba límites de CPU, VRM, refrigeración, conectores
   EPS y espacio en la caja.

## Evidencias mínimas

- ficha oficial de CPU;
- página del chipset o plataforma;
- CPU Support List y versión mínima de UEFI;
- manual de placa y QVL;
- ficha de RAM, SSD, fuente, caja y disipador;
- salida comentada de `lscpu`, `dmidecode`, `lsblk` o `lspci` en un equipo Linux.

## Entrega

Dictamen PDF y hoja de cálculo de componentes. Cada evidencia incluye modelo,
revisión, URL y fecha. Se valora el conjunto, no escoger lo más caro.

Archivo PDF: `Tarea_1_2_1_Apellidos_Nombre.pdf`.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Adecuación a DAM y presupuesto | 1,5 |
| CPU, socket, chipset y firmware | 2,5 |
| RAM, QVL y cálculo de ancho de banda | 1,5 |
| Almacenamiento, PCIe y líneas compartidas | 1,5 |
| Alimentación, VRM, medidas y refrigeración | 1,5 |
| Evidencias y trazabilidad | 1 |
| Claridad, autonomía y presentación | 0,5 |
