# Tarea 2.2 · Observatorio de procesos y memoria

<div class="lesson-banner" markdown>
<div class="lesson-number">2.2</div>
<div markdown>
**Reto de observación**

Mide procesos, hilos, memoria y disco antes y después de ejecutar una carga.
</div>
</div>

<div class="activity-meta" markdown>
<span>60 min</span><span>Individual</span><span>10 puntos</span><span>Aules</span>
</div>

## Producto final

PDF llamado `Tarea_2_2_Apellidos_Nombre.pdf`, con capturas, tabla comparativa y
conclusión técnica breve.

## Fase 1 · Estado inicial

Registra el estado del equipo recién iniciado o con pocas aplicaciones abiertas.

En Windows puedes usar Administrador de tareas, Monitor de recursos o PowerShell:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10
```

En GNU/Linux puedes usar monitor del sistema o terminal:

```bash
ps -eo pid,ppid,stat,ni,%cpu,%mem,comm --sort=-%cpu | head
free -h
vmstat 1 5
```

## Fase 2 · Carga controlada

Abre tres aplicaciones de uso real en DAM: navegador con varias pestañas, IDE o
editor, y una máquina virtual o emulador si tu equipo lo permite. Espera un
minuto y vuelve a medir.

Si tu equipo no permite usar una máquina virtual, sustitúyela por otra carga
controlada y segura: varias pestañas con documentación, una base de datos local,
un proyecto abierto en el IDE o una compresión de archivos. Indica qué has usado
para que la comparación sea honesta.

| Medida | Antes | Después | Interpretación |
|---|---:|---:|---|
| Procesos visibles |  |  |  |
| Uso de CPU |  |  |  |
| RAM usada |  |  |  |
| Disco o E/S |  |  |  |
| Proceso más consumidor |  |  |  |

## Fase 3 · Interpreta

Responde:

1. Diferencia programa, proceso e hilo usando un ejemplo de tu medición.
2. ¿Qué proceso creció más en memoria? ¿Era esperable?
3. ¿Viste CPU alta, memoria alta o disco alto? Explica la hipótesis principal.
4. ¿Qué dato necesitarías observar durante más tiempo antes de diagnosticar?

## Fase 4 · Capturas

Incluye dos capturas: estado inicial y estado con carga. Recorta lo necesario
para que se lea el dato importante y oculta información personal si aparece.

## Evidencias mínimas

Tu entrega debe permitir comprobar:

- qué sistema operativo y equipo has usado;
- qué carga has abierto y durante cuánto tiempo;
- qué proceso consume más CPU y cuál más memoria;
- si el cuello de botella parece CPU, RAM, disco o ninguno claro;
- qué dato mirarías durante más tiempo antes de afirmar un diagnóstico.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Mediciones antes/después completas | 2 |
| Tabla e interpretación técnica | 3 |
| Diferencia programa/proceso/hilo | 1,5 |
| Capturas legibles y pertinentes | 1,5 |
| Conclusión y presentación | 2 |
