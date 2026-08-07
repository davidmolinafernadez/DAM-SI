# 2. Componentes, prestaciones y compatibilidad

## 2.1 La placa base como sistema de interconexión

La placa base distribuye alimentación y comunica CPU, RAM, almacenamiento, tarjetas y periféricos. Su formato determina dimensiones, puntos de anclaje y capacidad de expansión.

```mermaid
flowchart TB
    CPU["CPU"] <--> RAM["RAM"]
    CPU <--> PCIE["PCI Express · GPU y expansión"]
    CPU <--> CHIP["Chipset / controladores de E/S"]
    CHIP <--> SATA["SATA"]
    CHIP <--> USB["USB y periféricos"]
    CHIP <--> NET["Red y audio"]
    FIRM["UEFI"] --> CPU
```

El diagrama es conceptual: en plataformas modernas muchas funciones antes situadas en el chipset están integradas en la CPU.

### Qué mirar en una ficha técnica

- formato y dimensiones;
- zócalo y generaciones de CPU admitidas;
- chipset y versión de firmware necesaria;
- tipo, número de canales y capacidad máxima de RAM;
- distribución de líneas PCIe;
- conectores M.2 y sus modos SATA/PCIe;
- puertos, red, audio y cabeceras internas;
- conectores de alimentación y límites térmicos.

## 2.2 Procesador y refrigeración

Los núcleos ejecutan flujos de instrucciones. SMT o tecnologías equivalentes permiten mantener más de un hilo lógico por núcleo, mejorando la utilización, pero un hilo lógico no equivale a un núcleo completo.

El consumo real varía con la carga. La potencia térmica orienta el diseño de refrigeración, aunque no siempre coincide con el máximo eléctrico. Si se alcanza un límite térmico, el procesador reduce frecuencia para protegerse: es el *thermal throttling*.

### Ejemplo de decisión

Un equipo para compilación, máquinas virtuales y contenedores se beneficia de más núcleos y RAM. Un puesto destinado a tareas ofimáticas puede priorizar eficiencia, silencio y coste. Una estación 3D debe equilibrar CPU y GPU y asegurar potencia y refrigeración.

## 2.3 Memoria RAM

La compatibilidad exige que coincidan generación, formato y soporte de plataforma. DDR4 y DDR5 no son intercambiables física ni eléctricamente.

La capacidad evita paginación; la velocidad y latencia afectan el tiempo de acceso; los canales aumentan ancho de banda. Instalar módulos en ranuras incorrectas puede dejar el sistema en un único canal.

### Cálculo sencillo

Una memoria anunciada como DDR5-5600 realiza 5.600 millones de transferencias por segundo por pin. Con un bus de 64 bits, el ancho de banda teórico de un canal es:

`5.600 MT/s × 8 bytes = 44.800 MB/s`

Dos canales pueden duplicar teóricamente esta cifra, aunque la carga real, el controlador y las latencias reducen el rendimiento efectivo.

## 2.4 Almacenamiento

Un HDD utiliza platos y cabezales mecánicos. Su latencia depende del movimiento. Un SSD usa memoria flash y un controlador; no tiene piezas móviles.

SATA limita el enlace a cifras próximas a 600 MB/s. NVMe trabaja sobre PCIe y permite muchas colas de órdenes paralelas. La mejora es especialmente visible en cargas aleatorias y concurrentes, pero no todas las aplicaciones aprovechan el máximo secuencial.

```mermaid
flowchart LR
    APP["Aplicación"] --> FS["Sistema de archivos"]
    FS --> DRIVER["Controlador"]
    DRIVER --> PROTO["SATA/AHCI o NVMe/PCIe"]
    PROTO --> DEVICE["HDD o SSD"]
```

### Capacidad y unidades

Un fabricante expresa 1 TB como `10¹²` bytes. Si una herramienta muestra TiB, divide por `2⁴⁰`. Por ello, 1 TB decimal equivale aproximadamente a 0,91 TiB. No faltan datos: se han usado unidades distintas.

## 2.5 Fuente de alimentación

La fuente debe aportar potencia estable y conectores adecuados. No basta sumar consumos nominales: se considera el pico de GPU, la línea de 12 V, eficiencia, temperatura, envejecimiento y margen.

La certificación 80 PLUS mide eficiencia en condiciones definidas. Una eficiencia del 90 % significa que para entregar 450 W el equipo toma aproximadamente 500 W de la red; los 50 W restantes se convierten principalmente en calor.

Protecciones deseables incluyen sobretensión, subtensión, sobrecorriente, sobrepotencia, cortocircuito y temperatura.

## 2.6 GPU y periféricos

Una GPU integra muchas unidades orientadas al paralelismo. Para seleccionarla se revisan carga, VRAM, API, controladores, dimensiones, alimentación y salidas de vídeo.

Los periféricos requieren interfaz física, protocolo y controlador. USB describe varias capas y versiones; la forma del conector no garantiza la velocidad ni funciones disponibles. Un USB-C puede ofrecer solo USB 2.0 o incluir datos rápidos, vídeo y carga, según el equipo.

## 2.7 Método de compatibilidad

```mermaid
flowchart TD
    USE["Definir uso y presupuesto"] --> CPU["Elegir plataforma y CPU"]
    CPU --> BOARD["Comprobar zócalo, chipset y UEFI"]
    BOARD --> RAM["Verificar RAM y canales"]
    RAM --> CASE["Comprobar caja y dimensiones"]
    CASE --> POWER["Dimensionar fuente y conectores"]
    POWER --> COOL["Validar refrigeración"]
    COOL --> IO["Confirmar almacenamiento, puertos y red"]
    IO --> REVIEW["Revisión cruzada de fichas técnicas"]
```

### Caso resuelto

Se desea instalar una CPU de 170 W, una GPU con recomendación de fuente de 650 W, dos módulos DDR5 y un SSD NVMe.

1. Se verifica que placa y CPU comparten zócalo y que UEFI admite el modelo.
2. Se confirma DDR5, capacidad y ranuras recomendadas para doble canal.
3. Se revisa que usar el M.2 no desactive un puerto o reduzca líneas de otra ranura.
4. Se comprueban longitud y grosor de GPU, altura del disipador y flujo de aire.
5. Se elige una fuente de calidad con margen y conectores nativos para GPU y CPU.
6. Se confirma que la regleta y el SAI soportan el consumo total.

## Errores frecuentes

- Confundir el conector M.2 con el protocolo NVMe.
- Comprar RAM de una generación incompatible.
- Suponer que cualquier CPU del mismo zócalo funciona sin revisar UEFI.
- Dimensionar la fuente únicamente por su potencia impresa.
- Montar módulos de RAM contiguos cuando la placa recomienda ranuras alternas.
- Olvidar dimensiones físicas y conectores.

## Comprobación de comprensión

Explica qué consultarías antes de añadir RAM, un SSD M.2 y una GPU a un equipo existente. La respuesta debe mencionar documentación, compatibilidad eléctrica, lógica, física y térmica.
