# Reto 2 · Comparación de revisiones

Revisamos la misma función con errores de ParqueFET con dos modelos.

| | qwen-demo (sin system prompt) | revisor-parquefet (v1) |
|---|---|---|
| Error `> 120` en vez de `>= 120` | Lo corrigió, con duda | No lo encontró |
| No revisa las motos | No | Sí |
| Un vehículo por carné | No | Sí |
| Límite de 14 horas | No | Sí |
| Errores encontrados | 1 de 4 | 3 de 4 |
| Veredicto + hallazgos | No | Sí |
| Máximo 150 palabras | No, y la respuesta se cortó | Sí |

## Conclusión
- El revisor encontró más errores de las reglas del negocio y respetó el formato, porque su system prompt le dice qué revisar y cómo responder.
- qwen-demo se fue por errores generales (tipos de datos, docstrings) y reescribió toda la función en vez de revisarla.
- El revisor también falló: no vio el `>= 120`, los números de línea no coinciden con el código y varias veces terminó repitiendo «Envíe el código que desea revisar», aunque ya había código.
