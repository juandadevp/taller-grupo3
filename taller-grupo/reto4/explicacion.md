# Reto 4 · Explicación

## Parte A · Cadena de pensamiento (phi-demo)
- **Sin paso a paso** (una línea): el modelo dio una respuesta vaga. Dijo que la función no tenía en cuenta que el carro ya estaba dentro, parecido a la regla de un vehículo por carné, pero sin hablar del carné y sin señalar un error concreto del código.
- **Con paso a paso:** evaluó mal la primera condición. Dijo que `not vehiculo.carne_vigente` era True aunque el carné estaba vigente, concluyó que el error estaba en esa línea y propuso una corrección que dañaba la función. Encontró 0 errores reales y además inventó uno falso.
- **Conclusión:** pedirle que razone por escrito hace visible su razonamiento, pero no lo hace correcto. Un modelo pequeño puede razonar mal y sonar muy seguro.

## Parte B · La instrucción que se olvida (qwen-demo)

**La idea:** el modelo solo "recuerda" lo que cabe en su ventana de contexto. Cuando la conversación se hace más larga que la ventana, lo más viejo se corta, y ahí puede quedar la regla de formato que dimos al principio. El system prompt, en cambio, se mantiene siempre al inicio, por eso debería seguir cumpliéndose.

**Lo que pasó en nuestro equipo:**
- Con la regla «empieza siempre con "Veredicto ParqueFET:"», tanto en el chat como en `/set system`, todas las respuestas la cumplieron. No logramos ver el olvido.
- Pedimos `num_ctx 512`, pero con Ollama 0.40.10 `ollama ps` mostró 2048. Además, ni siquiera cuando el último turno leyó 2103 tokens se recortó el historial. Las lecturas fueron 35, 130 y 901 tokens con respuestas de unos 700 tokens.
- Por eso hicimos versiones «escalado» con respuestas más largas. La versión A leyó 2103 tokens en su último turno y aun así cumplió la regla. Las versiones A y B usaron parámetros distintos (1900 tokens y 1500 palabras contra 1800 y 1200), así que no se pueden comparar de forma exacta.
- Según la guía (práctica 14B), la regla en el chat debería perderse al pasarse de la ventana y la del system prompt debería conservarse. En nuestro equipo no pudimos comprobarlo.

**Otras cosas que notamos:**
- El modelo inventa datos aunque cumpla el formato. En `salida_B_B_regla_en_system.md` (línea 24) dijo que la tarifa es mensual en vez de por hora, y en las dos de la versión B llamó a la FET «Federación Tecnológica de México».
- Varias respuestas se cortan a mitad de frase por el límite de tokens: a los 700 en la corrida normal y a los 1800 o 1900 en las escaladas.
