# X1. Ampliación: Windows y Ubuntu en arranque dual virtual

**Teoría relacionada:** [Firmware, arranque y particiones](../b04-firmware-y-particiones.md) · [Recuperación y transferencia](../b11-recuperacion.md)

Duración adicional: 180 minutos. Se realiza después del itinerario básico, en una VM nueva de 120 GiB. No se modifica el arranque del ordenador personal.

1. Prepara VM compatible con Windows 11, UEFI y sus requisitos de seguridad. Instala Windows en una partición de aproximadamente 70 GiB y deja al menos 45 GiB sin asignar. Permite que el instalador cree sus particiones auxiliares. Verifica el espacio real en el resumen antes de confirmar.
2. Completa aceptación de Windows y apaga. Si se ha activado cifrado de dispositivo, verifica que tienes el procedimiento y clave de recuperación de aula antes de continuar. No cifres con una cuenta personal una imagen compartida.
3. Haz una copia o clon completo recuperable de esta VM. Arranca Ubuntu desde ISO en el mismo modo UEFI.
4. Selecciona instalación manual en el espacio sin asignar. Crea raíz ext4 con el espacio suficiente. Reutiliza la ESP existente como /boot/efi sin formatearla. No selecciones «borrar disco» ni modifiques la partición de Windows.
5. Revisa el resumen: solo se formatea la nueva raíz Linux. Si el instalador no permite identificar claramente el destino, vuelve atrás y consulta la configuración, en lugar de aceptar por intuición.
6. Instala, retira ISO y prueba arranque de Ubuntu y Windows. Si no hay menú GRUB visible, utiliza el gestor UEFI de la VM para localizar las entradas. No borres ni reinstales Windows por esa ausencia.
7. Desde ambos sistemas comprueba que un archivo testigo de Windows permanece y que Ubuntu utiliza su propia raíz. Dibuja el mapa final.

Aceptación: ambos sistemas arrancan, Windows conserva testigo y particiones esenciales, Ubuntu usa su raíz y la ESP se conserva. Entrega secuencia de decisiones y diferencia entre arranque dual y dos VM simultáneas.
