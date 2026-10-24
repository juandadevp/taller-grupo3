# Reto 4 · Explicación

## Parte A · Cadena de pensamiento (phi-demo)
- Sin paso a paso, en una línea, el modelo dio una explicación vaga: dijo que la función no consideraba que el carro ya estaba dentro, algo parecido a la regla de un vehículo por carné, pero sin mencionar el carné; no señaló un error concreto del código.
- Con paso a paso, evaluó mal la primera condición (dijo que `not vehiculo.carne_vigente` era True con el carné vigente), concluyó que el error estaba en esa línea y propuso una corrección que rompe la función. Encontró 0 errores reales y agregó uno falso.
- Conclusión: pedir el razonamiento por escrito lo hace visible, pero no lo hace correcto; en un modelo pequeño puede razonar mal con seguridad.

## Parte B · La instrucción que se olvida (qwen-demo)
- Con la regla «empieza siempre con "Veredicto ParqueFET:"» como mensaje del chat y como /set system, todas las respuestas la cumplieron.
- Esperaba que en el chat se perdiera al llenarse la ventana, pero mi versión de Ollama (0.40.10) usa un contexto mínimo de 2048 aunque pida num_ctx 512. Con respuestas de ~700 tokens, las lecturas fueron 35, 130 y 901 tokens, así que el historial nunca se recortó.
- Para forzar el recorte hicimos versiones "escalado" con respuestas más largas: la versión A leyó 2103 tokens en su último turno (supera 2048). Aun así la regla se cumplió en todas las respuestas, así que no pude reproducir el olvido. Las versiones A y B usaron parámetros distintos (1900 tokens y 1500 palabras contra 1800 y 1200), por lo que no son perfectamente comparables.
- Según la guía (práctica 14B), la instrucción debería perderse al superar la ventana y el system prompt debería conservarse; en nuestro equipo eso no se pudo comprobar.
- Una de las salidas (salida_B_B_regla_en_system.md, línea 24) dice que la tarifa es mensual en vez de por hora, y las dos de la versión B llaman a la FET «Federación Tecnológica de México»: el modelo inventa datos aunque la regla de formato se cumpla. Además, las respuestas se cortan por el límite de tokens: a los 700 en la corrida normal y a los 1800 o 1900 en las versiones escaladas.
