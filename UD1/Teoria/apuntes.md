# UD1. Arquitectura HW/SW, PRL y diagnóstico

## 1. Resultados de aprendizaje

Al finalizar la unidad, el alumnado será capaz de identificar los elementos de un sistema informático, relacionar sus características con las prestaciones del conjunto, interpretar documentación técnica y trabajar aplicando medidas de prevención de riesgos.

## 2. El sistema informático

Un sistema informático integra cuatro elementos:

- **Hardware:** componentes físicos: placa base, procesador, memoria, almacenamiento y periféricos.
- **Software:** instrucciones y datos: sistema operativo, controladores y aplicaciones.
- **Información:** datos que el sistema almacena, procesa y comunica.
- **Personas y procedimientos:** usuarios, administración, normas de uso y mantenimiento.

El sistema operativo coordina el hardware y ofrece servicios a las aplicaciones. Sin esta capa, cada programa tendría que controlar directamente todos los dispositivos.

## 3. Arquitectura de Von Neumann

La mayoría de ordenadores siguen un modelo formado por CPU, memoria, entrada/salida y buses. Las instrucciones y los datos comparten la memoria principal.

La CPU contiene:

- **Unidad de control:** interpreta instrucciones y coordina su ejecución.
- **ALU:** realiza operaciones aritméticas y lógicas.
- **Registros:** almacenamiento interno extremadamente rápido, como el contador de programa y el registro de instrucción.
- **Memoria caché:** reduce la diferencia de velocidad entre CPU y RAM.

El ciclo de instrucción se resume en búsqueda, decodificación, ejecución y almacenamiento del resultado. El reloj sincroniza estas operaciones, pero la frecuencia por sí sola no permite comparar procesadores de arquitecturas distintas.

## 4. Placa base y firmware

La placa base comunica todos los componentes. Al analizarla deben identificarse:

- formato físico, como ATX o microATX;
- zócalo del procesador y chipset;
- ranuras DIMM para RAM;
- ranuras PCI Express;
- conectores SATA y M.2;
- alimentación ATX y EPS;
- puertos externos y cabeceras internas.

El firmware UEFI inicializa el hardware, ejecuta el autodiagnóstico y localiza un dispositivo de arranque. Frente al BIOS tradicional, UEFI admite discos GPT, arranque seguro e interfaces más completas.

## 5. Procesador, memoria y almacenamiento

Para seleccionar una CPU se consideran arquitectura, número de núcleos e hilos, frecuencia, memoria caché, consumo térmico y compatibilidad con placa y RAM.

La jerarquía de memoria ordena los niveles por velocidad, capacidad y coste: registros, caché, RAM y almacenamiento secundario. La RAM es volátil. Su generación, capacidad, frecuencia y formato deben ser compatibles con la placa y el procesador.

El almacenamiento permanente puede usar:

| Tecnología | Interfaz habitual | Rasgo principal |
| --- | --- | --- |
| HDD | SATA | Gran capacidad y bajo coste |
| SSD SATA | SATA | Menor latencia que un HDD |
| SSD NVMe | PCIe/M.2 | Alto rendimiento y paralelismo |

La capacidad anunciada por fabricantes suele expresarse en unidades decimales; los sistemas pueden mostrar unidades binarias, lo que explica parte de la diferencia visible.

## 6. Alimentación, refrigeración y periféricos

La fuente convierte corriente alterna en tensiones continuas estables. Debe dimensionarse con margen, disponer de conectores adecuados y ofrecer protecciones eléctricas. La certificación 80 PLUS informa de eficiencia, no de calidad total.

La refrigeración extrae el calor de CPU, GPU y otros componentes. Un flujo habitual introduce aire por la parte frontal o inferior y lo expulsa por la trasera o superior.

Los periféricos se clasifican en entrada, salida y entrada/salida. Su funcionamiento depende del controlador, que permite al sistema operativo comunicarse con el dispositivo.

## 7. Representación de la información

El bit es la unidad mínima. Ocho bits forman un byte. Los sistemas de numeración más utilizados son decimal, binario, octal y hexadecimal.

Para convertir de binario a hexadecimal se agrupan bits de cuatro en cuatro. Por ejemplo, `11010110₂` se divide en `1101 0110`, equivalente a `D6₁₆`.

Los caracteres se representan mediante códigos. ASCII cubre un conjunto limitado; Unicode asigna puntos de código universales y UTF-8 los codifica con longitud variable.

## 8. Compatibilidad y diagnóstico

Antes de montar o ampliar un equipo se verifica la cadena completa de compatibilidad: formato de caja y placa, zócalo y chipset, versión de UEFI, tipo de RAM, dimensiones, conectores y potencia disponible.

Un diagnóstico ordenado sigue este proceso:

1. Registrar el síntoma y cuándo aparece.
2. Comprobar alimentación, conexiones e indicadores.
3. Consultar mensajes, códigos acústicos y registros.
4. Aislar variables y probar un cambio cada vez.
5. Verificar la solución y documentarla.

## 9. Prevención de riesgos

- Desconectar el equipo y descargar la energía residual antes de abrirlo.
- Evitar descargas electrostáticas mediante pulsera ESD o contacto con una superficie conectada a tierra.
- No abrir fuentes de alimentación ni otros equipos con condensadores peligrosos.
- Mantener orden, ventilación e iluminación adecuadas.
- Ajustar pantalla, silla y teclado para reducir riesgos ergonómicos.
- Gestionar residuos electrónicos mediante canales autorizados.

## 10. Resumen

El rendimiento y la fiabilidad dependen del equilibrio entre componentes, no de una única cifra. La documentación técnica, la compatibilidad y un método de diagnóstico reproducible son tan importantes como conocer el nombre de cada pieza.

## Fuentes internas utilizadas

- `Jose_SO/UD1.pdf`.
- `SI_Celia/Unidad_1_/Unidad_1_Componentes-del-sistema-informatico.pdf`.
- `Programacion_Didactica_SI_David_Moli.docx`.
