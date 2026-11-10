# UD3 · Soluciones y explicación para clase

Esta página es pública y puede abrirse en otra pestaña para la corrección colectiva. Contiene respuestas modelo y resultados esperados; no son evidencias reales de un equipo. Cada alumno debe aportar sus propias comprobaciones.

## A1 · Decidir antes de instalar

### 1. Comparación

| Alternativa | Simultaneidad y reinicios | Recursos | Efecto sobre los datos |
| --- | --- | --- | --- |
| Linux físico sustituyendo Windows | Un sistema; reiniciar para arrancar | Todos los recursos para Linux | Puede borrar Windows y documentos; no cumple el caso |
| Arranque dual | Solo un sistema a la vez; reiniciar para cambiar | RAM y CPU completas para el sistema activo; disco repartido | Requiere copia previa, espacio y particionado seguro |
| Linux en una VM sobre Windows | Ambos funcionan a la vez; no reiniciar el anfitrión | Se comparten RAM, CPU y espacio | Conserva Windows; sigue necesitando copia de datos |

### 2. Dos alternativas condicionadas

La VM es la primera opción si hay virtualización disponible y memoria suficiente durante la carga real. El arranque dual es una alternativa si se acepta interrumpir Windows, existe una copia verificada y se puede preparar espacio sin comprometer los datos. No debe prometerse que 90 GiB libres bastan sin medir las necesidades y el margen de ambos sistemas.

### 3. Presupuesto de RAM

| Uso | Propuesta orientativa |
| --- | ---: |
| Windows y aplicaciones del anfitrión | 4 GiB |
| Linux invitado | 3 GiB |
| Margen | 1 GiB |
| Total | 8 GiB |

Es una hipótesis para un Linux ligero y una carga reducida, no un requisito oficial ni una garantía. Se comprueba con el monitor del anfitrión y del invitado. Si la imagen de aula exige más memoria o el equipo pagina continuamente, se emplea otro puesto o se reduce la carga; no se fuerza una asignación inviable.

### 4. Recomendación modelo

Recomiendo conservar Windows como sistema anfitrión y utilizar una máquina virtual Linux para las prácticas. Así se mantiene disponible la aplicación exclusiva de Windows y se evita modificar las particiones del portátil. Antes de crearla comprobaría la virtualización del procesador, la memoria disponible con las aplicaciones habituales abiertas y el espacio que necesitan la imagen, el disco virtual y las copias.

Con 8 GiB de RAM, el presupuesto es ajustado. Como punto de partida reservaría 4 GiB para Windows, asignaría 3 GiB a un Linux ligero y dejaría 1 GiB de margen. Esa distribución debe medirse y adaptarse a la imagen del aula; si no permite trabajar con fluidez, utilizaría un equipo del centro. Un disco dinámico también consume espacio real a medida que crece.

El arranque dual sería una segunda opción si se acepta reiniciar y detener el trabajo en Windows. Requiere una copia de seguridad comprobada y planificar cuidadosamente las particiones.

Como prueba de aceptación, arrancaría Linux desde su disco virtual, crearía un archivo, apagaría la VM y volvería a iniciarla sin ISO. Comprobaría que el archivo permanece, que la aplicación de Windows sigue funcionando y que el anfitrión no presenta una presión de memoria excesiva durante la carga prevista.

## A10 · Escoger una estrategia de recuperación

### 1. Matriz resuelta

| Necesidad | Solución y límite |
| --- | --- |
| Deshacer una prueba fallida | Instantánea anterior a la prueba; no protege de perder el SSD |
| Llevar una VM a otro equipo | Exportación e importación comprobada; también puede servir una copia completa compatible |
| Protegerse de una avería del SSD | Respaldo independiente en otro soporte y restauración probada |
| Ahorrar espacio con una base común de aula | Clon enlazado mientras se conserven la base y sus dependencias |
| Trabajar con una copia independiente del disco de origen | Clon completo; comprobar también discos externos y configuración |

### 2. Dependencias del clon enlazado

Guarda diferencias respecto a una base. Si se pierde o modifica de forma incompatible esa base, puede quedar inutilizable. No basta con copiar el archivo diferencial a otro equipo. Un clon completo consume más espacio pero evita esa dependencia de la cadena de discos del origen.

### 3. Qué retrocede al restaurar

Los cambios posteriores en los discos incluidos en la instantánea se descartan al volver al estado anterior. Los archivos de una carpeta compartida del anfitrión, los mensajes enviados y los cambios en servicios externos no retroceden. Tampoco debe suponerse que todos los discos quedan incluidos: se revisa su configuración.

### 4. Protocolo de aceptación

1. Crear un archivo testigo y registrar contenido, versión del sistema y aplicación que debe funcionar.
2. Apagar correctamente y preparar el respaldo o la exportación.
3. Restaurar o importar en un destino separado, conservando el original.
4. Revisar recursos, firmware, discos y MAC antes de iniciar.
5. Arrancar, comprobar el archivo testigo y ejecutar la aplicación.
6. Registrar resultado, ubicación y fecha. Solo aceptar la copia si supera las pruebas.

### 5. Por qué no basta otro clon en el SSD

Si falla el soporte, pueden perderse tanto el original como el clon. Independencia entre archivos no equivale a independencia frente a una avería física.

## Resultados esperados de las prácticas guiadas

Las prácticas se realizan en clase. El docente demuestra el paso clave, el alumnado lo ejecuta y registra su resultado. Los menús detallados están en cada ficha; esta tabla sirve para corregir y explicar, sin añadir entregas.

| Entrega | Resultado que debe poder demostrarse | Error que conviene explicar |
| --- | --- | --- |
| P0–P1 | Inventario real, ISO identificada y hash coincidente con una referencia oficial; VM creada con recursos justificados | Una VM vacía todavía no tiene un sistema instalado; un hash de un foro no acredita autenticidad |
| P2 | Ubuntu arranca sin la ISO y conserva un archivo tras apagar y encender | Una sesión Live puede funcionar sin haber instalado nada |
| P3 | Windows instalado en el disco virtual, edición y recursos registrados; reinicio y archivo persistente comprobados | No confundir el disco de la VM con el disco físico ni el estado de activación con la instalación |
| P6 | Estado anterior y posterior registrados; actualización completada y prueba funcional tras reiniciar cuando corresponda | Que no haya paquetes pendientes también puede ser correcto: se documenta, no se inventa una actualización |
| P7 | Tras volver a la instantánea A, estado.txt contiene A y posterior.txt no existe | Eliminar una instantánea no es restaurarla; los archivos externos no retroceden |
| P8 | Clon con escrituras independientes; OVA importado que arranca y conserva el archivo testigo | Tener un OVA sin probar no demuestra recuperación; dos VM con identidades repetidas pueden entrar en conflicto |

### Guion breve para la demostración

1. **Preparar:** preguntar qué puede cambiar y dónde están los datos. Mostrar el inventario y el destino antes de instalar.
2. **Instalar:** diferenciar ISO de disco virtual. Retirar la ISO y reiniciar para demostrar persistencia.
3. **Actualizar:** anotar qué se va a modificar, establecer retorno y repetir una prueba funcional después.
4. **Recuperar:** crear el estado A, tomar la instantánea, generar B y predecir el resultado antes de restaurar.
5. **Transferir:** distinguir clon completo, clon enlazado, OVA y respaldo externo. Probar la importación antes de darla por válida.

## Cómo corregir sin pedir más trabajo

A1 y A10 se valoran con la rúbrica de sus fichas. Para las prácticas, comprobar que el resultado funciona y que la evidencia lo demuestra; una captura del asistente no sustituye la prueba final. Si algo falla, pedir síntoma, causa probable, comprobación y corrección dentro del mismo informe. No se generan actividades ni archivos adicionales.
