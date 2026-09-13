# 1.2 · Compatibilidad de CPU, placa base y RAM

<div class="lesson-banner" markdown>
<div class="lesson-number">1.2</div>
<div markdown>
**De “encaja” a “está verificado”**

Una configuración profesional se justifica con listas de soporte, manuales y
medidas, no con intuiciones ni con una única coincidencia.
</div>
</div>

## 1. Las cuatro capas de compatibilidad

<div class="component-grid" markdown>
<div markdown>**Física**  
Zócalo, formato, altura, longitud y anclajes.</div>
<div markdown>**Eléctrica**  
Potencia, conectores, regulación y límites.</div>
<div markdown>**Lógica**  
Chipset, buses, protocolos y recursos compartidos.</div>
<div markdown>**Firmware y software**  
UEFI/BIOS, controladores y sistema operativo.</div>
</div>

## 2. Ruta de comprobación

```mermaid
flowchart TD
  N[Necesidad DAM] --> C[CPU candidata]
  C --> S[Zócalo + chipset]
  S --> B[CPU Support List + UEFI]
  B --> R[RAM: tipo, capacidad y QVL]
  R --> X[PCIe, M.2, SATA y líneas]
  X --> F[Fuente y conectores]
  F --> M[Caja y refrigeración]
  M --> P[SO, virtualización y drivers]
  P --> E[Dictamen con evidencias]
```

## 3. CPU y placa base

El zócalo coincidente es necesario, pero no suficiente. El chipset debe admitir
la familia y la **CPU Support List** del modelo exacto debe incluir el procesador.
La lista suele indicar una versión mínima de UEFI/BIOS. Si la placa llega con
una versión anterior, hay que saber si admite actualización sin CPU compatible.

!!! example "Caso"
    La CPU aparece en la lista desde UEFI `2.10`, pero la placa tiene `1.40`.
    Físicamente encaja y aun así puede no arrancar. Primero se planifica la
actualización indicada por el fabricante.

Además de zócalo y chipset se revisan límites de potencia, refrigeración, versión
de firmware y prestaciones que dependen de la CPU instalada. Una placa puede
ofrecer físicamente una ranura o salida y no habilitarla con todas las CPU.

## 4. Memoria RAM

Hay que comprobar generación DDR, capacidad total y por módulo, número de
canales, velocidad oficial, perfiles y QVL. DDR4 y DDR5 no son intercambiables.
XMP o EXPO configura parámetros de rendimiento, pero no garantiza estabilidad
en cualquier combinación; poblar todos los bancos puede reducir la velocidad.
La velocidad anunciada en un kit puede corresponder a un perfil de overclock y
no a la velocidad estándar admitida oficialmente por el controlador de memoria.

## 5. Almacenamiento y expansión

M.2 describe un **formato**, mientras NVMe describe un protocolo sobre PCIe.
Una ranura M.2 puede admitir distintas interfaces. El manual revela si una
ranura comparte líneas con SATA o PCIe y si desactiva otros puertos.

PCIe mantiene compatibilidad entre generaciones en muchos casos, pero el enlace
negocia la combinación posible y queda limitado por el extremo más lento. La
forma `x16` de una ranura tampoco asegura que tenga dieciséis líneas eléctricas.

## 6. Alimentación, refrigeración y caja

Se verifican potencia continua, conectores ATX/EPS/GPU, protecciones, formato de
placa, altura del disipador, longitud y grosor de GPU, radiadores y flujo de aire.
Una fuente sobredimensionada no corrige un conector inexistente.

## 7. Compatibilidad para virtualización y DAM

Para el aula no basta con que el equipo arranque. Conviene comprobar:

- virtualización por hardware habilitable en UEFI;
- RAM suficiente para anfitrión, IDE, navegador y máquinas virtuales;
- SSD con espacio para discos virtuales e instantáneas;
- controladores compatibles con el sistema anfitrión;
- firmware actualizado y posibilidad de recuperación;
- conectividad de red adecuada para descargar imágenes y dependencias.

Una configuración con 8 GB puede ejecutar herramientas por separado, pero queda
muy limitada al combinar IDE, navegador y una VM. La necesidad real se justifica
por la carga de trabajo y no solo por el requisito mínimo de cada producto.

## 8. Evidencias de calidad

Una auditoría debe registrar fabricante, modelo, revisión, URL y fecha. Las
fuentes prioritarias son manual, lista de CPU, QVL, ficha de procesador y
documentación del sistema operativo. Una tienda o comparador ayuda a localizar,
pero no sustituye la fuente técnica.

<div class="video-card" markdown>

### Vídeo · Reconocer los elementos antes de comprobarlos

Este repaso visual de 2026 identifica VRM, zócalo, DIMM, chipset, PCIe, M.2 y
alimentación. Úsalo para localizar componentes; las decisiones de compatibilidad
deben verificarse después en documentación oficial.

<div class="video-frame">
<iframe src="https://www.youtube-nocookie.com/embed/jfKOl1W8Ml4"
title="Every Motherboard Component Explained" loading="lazy"
allowfullscreen></iframe>
</div>

[Abrir el vídeo en YouTube](https://www.youtube.com/watch?v=jfKOl1W8Ml4)

</div>

## Comprueba que lo entiendes

1. Enumera las cuatro capas de compatibilidad.
2. Diferencia M.2 y NVMe.
3. ¿Por qué se guarda la versión de UEFI?
4. ¿Qué información aporta una QVL y qué no garantiza?

<div class="activity-card" markdown>

## :material-clipboard-search-outline: Tarea 1.2.1 · Auditoría de compatibilidad

<div class="activity-meta" markdown>
<span>110 min</span><span>Individual</span><span>Entrega en Aules</span>
</div>

Diseñarás un equipo para desarrollo multiplataforma y demostrarás cada decisión
con documentación oficial y una matriz visual de compatibilidad.

[Abrir la Tarea 1.2.1](actividades/A12-compatibilidad.md){ .md-button .md-button--primary }

</div>

## Fuentes de consulta

- [Intel: localizar chipsets compatibles](https://www.intel.com/content/www/us/en/support/articles/000092715/processors.html)
- [Intel: zócalos y soporte de BIOS](https://www.intel.com/content/www/us/en/support/articles/000005670/processors.html)
- Manual, CPU Support List y QVL de la placa concreta.
- [PCI-SIG: información oficial de PCI Express](https://pcisig.com/pci-express)
