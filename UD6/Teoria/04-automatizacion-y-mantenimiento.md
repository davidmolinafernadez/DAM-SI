# 4. Automatización y mantenimiento

## 4.1 Propiedades de un buen script

- repetible e idempotente cuando sea posible;
- entradas validadas;
- rutas citadas;
- errores controlados;
- registro sin secretos;
- código de salida útil;
- modo de simulación para operaciones sensibles;
- documentación y control de versiones.

## 4.2 Ejemplo Bash

```bash
#!/usr/bin/env bash
set -euo pipefail
service_name="nginx"
if ! systemctl is-active --quiet "$service_name"; then
  logger -t service-check "$service_name no está activo"
  exit 1
fi
echo "$service_name correcto"
```

## 4.3 Ejemplo PowerShell

```powershell
param([string]$ServiceName = 'sshd')
$service = Get-Service -Name $ServiceName -ErrorAction Stop
if ($service.Status -ne 'Running') {
    Write-Error "$ServiceName no está activo"
    exit 1
}
Write-Output "$ServiceName correcto"
```

## 4.4 Programación

Cron ejecuta con entorno reducido. Se usan rutas absolutas y se redirigen resultados.

```cron
15 2 * * * /usr/local/sbin/copia.sh >> /var/log/copia.log 2>&1
```

Los temporizadores systemd añaden dependencias, estado y logs. En Windows, el Programador de tareas permite disparadores, cuenta, condiciones y acciones.

## 4.5 Gestión de cambios

```mermaid
flowchart LR
    REQ["Solicitud"] --> IMP["Impacto y riesgo"]
    IMP --> PLAN["Plan y reversión"]
    PLAN --> TEST["Prueba"]
    TEST --> APPLY["Aplicación"]
    APPLY --> VERIFY["Verificación"]
    VERIFY --> CLOSE["Documentación"]
```

Un cambio urgente también se registra después. La documentación incluye quién, qué, cuándo, por qué, resultado y vuelta atrás.

## 4.6 Mantenimiento periódico

| Frecuencia | Comprobaciones |
| --- | --- |
| Diaria | alertas, copias, capacidad crítica, servicios |
| Semanal | actualizaciones, registros, cuentas nuevas, tendencias |
| Mensual | restauración de muestra, privilegios, inventario, certificados |
| Trimestral | recuperación completa, firmware, capacidad y riesgos |

La frecuencia se adapta a criticidad. Automatizar la comprobación no elimina la revisión humana ni la prueba de recuperación.
