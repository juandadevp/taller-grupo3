# Reto 3 · Nota de corrección

**Dónde apareció el primer error:** en el paso 2 (los criterios). La historia del paso 1 salió bien.

**Qué salió mal en el paso 2:**
- Criterio 1: invirtió la regla del carné vigente.
- Criterio 3: cambió la regla de un vehículo por carné.
- Criterio 4: inventó que hay que pagar para ingresar, cuando la historia habla de pagar antes de salir.

**Por qué el error se arrastró:** la tabla del paso 3 usó esos criterios mal escritos tal cual. Su auto-verificación solo contó que hubiera un caso por criterio, pero no revisó si los criterios estaban bien.

**Qué corregimos:** en `prompt2_v2.txt` agregamos «Usa solo estas reglas de negocio; no inventes reglas nuevas» y «Los criterios tratan del pago antes de salir, no del ingreso». Guardamos la primera pasada como evidencia.

**Resultado:** mejoró, pero no del todo.
- Ya no aparece el criterio inventado de pagar para ingresar ni el criterio 1 invertido, y ahora sí sale que estudiantes y personal no pagan.
- Pero aparecieron errores nuevos: inventó mensajes de error, aplicó las reglas de un vehículo por carné y de las 14 horas al momento de salir (donde no corresponden), y el criterio 1 quedó confuso.

**Conclusión:** la frase «no inventes reglas nuevas» redujo lo que se inventaba, pero el modelo pequeño igual no entendió bien cuándo se aplica cada regla.
