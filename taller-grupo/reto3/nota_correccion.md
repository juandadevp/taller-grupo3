# Reto 3 · Nota de corrección

**Primer error:** apareció en el paso 2 (criterios). La historia del paso 1 salió bien.

**Errores del paso 2:**
- Criterio 1: invirtió la regla del carné vigente.
- Criterio 3: cambió la regla de un vehículo por carné.
- Criterio 4: inventó que hay que pagar para ingresar (la historia habla de pagar antes de salir).

**Por qué se arrastró:** la tabla del paso 3 heredó los criterios mal escritos, y su auto-verificación solo contó casos, no revisó si eran correctos.

**Corrección:** en `prompt2_v2.txt` añadí «Usa solo estas reglas de negocio; no inventes reglas nuevas» y «Los criterios tratan del pago antes de salir, no del ingreso». Guardé la primera pasada como evidencia.

**Resultado:** mejoró parcialmente. En salida2_v2.md los criterios ya tratan del pago antes de salir y desapareció el criterio inventado de pagar para ingresar y el criterio 1 invertido; además aparece el caso de estudiantes y personal, que no pagan. Pero aparecieron errores nuevos: inventó mensajes de error entre comillas, aplicó la regla de un vehículo por carné y el límite de 14 horas al momento de salir (donde no corresponden) y el criterio 1 es confuso. Conclusión: la frase «no inventes reglas nuevas» redujo las invenciones, pero el modelo pequeño igual malinterpretó cuándo aplica cada regla.
