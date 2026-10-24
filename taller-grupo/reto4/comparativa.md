# Reto 4 · Comparativa contra el enunciado (Caso 1 · ParqueFET)

Revisión hecha solo leyendo los archivos de `reto4/`. Las salidas del modelo no se editaron; las citas son literales.

## 1. Qué cumple y qué no

| Pide el enunciado | Estado | Detalle |
|---|---|---|
| Parte A: pregunta en una línea con phi-demo | Cumple | `parteA_sin_cot.txt` → `salida_A_sin_cot.md` |
| Parte A: evaluar paso a paso con datos concretos (cada if, condición, valor) | Cumple el prompt | `parteA_con_cot.txt` da `carne_vigente = True`, `tipo = "carro"`, `ocupados["carros"] = 120` |
| Parte A: phi-demo **sin** `--think=false` | Cumple a medias | La salida guardada viene de `correr.py`, que envía `think=False` por la API (si phi lo rechaza, `comun.py` reintenta sin él; no se comprobó cuál de los dos pasó). La primera corrida sí fue con `ollama run phi-demo < archivo`, pero se sobrescribió porque traía códigos de escape de la terminal |
| Parte A: comparar cuántos errores encontró cada versión | Hecho aquí (sección 2) | Resultado: 0 y 0 |
| Parte B: qwen-demo con `--think=false` | Cumple | Por script (`think=False`) |
| Parte B: en el **chat** `ollama run`, con `/set parameter num_ctx 512` | **No cumple** | No se usó el chat interactivo; se simuló con `parteB_chat.py`, que reenvía todo el historial en cada turno como hace el CLI. Se pidió `num_ctx 512`, pero no se aplicó (sección 3) |
| Parte B: regla de formato propia del caso | Cumple | «Empieza SIEMPRE tu respuesta con «Veredicto ParqueFET:».» |
| Parte B: dos preguntas de al menos 400 palabras | Cumple en el prompt; en las respuestas no del todo | Las respuestas se cortan en 700 tokens (`num_predict` del Modelfile), varias a mitad de frase |
| Parte B: repetir con la regla en `/set system` (antes `/clear`) | Cumple, equivalente | La versión B empieza con un historial nuevo y la regla como mensaje `system` |
| Explicación con sus palabras de cada parte | **Falta** | No hay archivo de explicación. Este documento es la comparativa; la explicación la deben escribir ustedes |

## 2. Comparación de resultados

### Parte A · sin y con paso a paso (phi-demo)

| | Sin paso a paso | Con paso a paso |
|---|---|---|
| ¿Encontró el `> 120` (debe ser `>= 120`)? | No | No |
| Errores reales encontrados | 0 | 0 |
| Qué dijo | «La función no consideró que el carro ya estaba dentro del parque, por lo que no impidió su ingreso.» | Evaluó mal las condiciones: dijo que `not vehiculo.carne_vigente` vale `True` y que `ocupados["carros"] > 120` es `True` con 120. Concluyó: «El error está en la primera línea de la función» (la del carné, que está bien) |

- El paso a paso **no ayudó** con phi-demo en este equipo: hizo la evaluación pero con valores equivocados, y llegó a una conclusión falsa con más seguridad.
- Como control se corrió una vez el ejemplo de la guía (`prompts/06_cot_con.txt`): phi-demo también falló (dijo que `not True` retorna `False` y propuso borrar las condiciones). Esa salida quedó solo en el scratchpad de la sesión, **no está en `reto4/`**, así que no es evidencia entregable.
- La guía espera que la versión con pasos encuentre el error. Aquí no ocurrió: el límite parece estar en el modelo, no en el prompt.
- Nota: los prompts solo preguntan por un caso inválido (capacidad de carros). Los otros errores de la función del Caso 1 (motos, un vehículo por carné, 14 horas) no se pidieron, así que no cuentan aquí.

### Parte B · regla en el chat contra regla en el system (qwen-demo)

Hay **dos pares** de salidas, y el par «escalado» mezcla parámetros (ver sección 3).

| Archivo | Parámetros reales | Tokens leídos por turno | ¿Empieza con «Veredicto ParqueFET:»? |
|---|---|---|---|
| `salida_B_A_regla_en_chat.md` | num_ctx pedido 512, num_predict 700, 400 palabras | 35 → 130 → **901** | Sí, Sí, Sí |
| `salida_B_B_regla_en_system.md` | igual | 87 → **858** | Sí, Sí |
| `salida_B_A_regla_en_chat_escalado.md` | num_ctx 2048, num_predict **1900**, **1500** palabras | 35 → 131 → **2103** | Sí, Sí, Sí |
| `salida_B_B_regla_en_system_escalado.md` | num_ctx 2048, num_predict **1800**, **1200** palabras | 88 → **1960** | Sí, Sí |

- **No se reprodujo el efecto de la práctica 14B.** En las cuatro conversaciones la regla se cumplió en todas las respuestas, también en la versión A.
- La razón se ve en los tokens: con `num_ctx 512` el último turno leyó 901 tokens, y en la corrida escalada leyó 2103 con `num_ctx 2048`. **El historial nunca se recortó**: la regla y la primera respuesta siguieron visibles.
- En la versión A, la segunda respuesta empieza «Veredicto ParqueFET: Entendido. A continuación…», es decir, copia también el «Entendido» de la primera respuesta. Es compatible con lo que la guía llama imitación, pero con estos datos no se puede separar «sigue la regla» de «imita la respuesta anterior».
- Por eso **no se puede concluir nada sobre chat contra system** con estas salidas.
- Otras observaciones de las salidas (sin relación con la regla): el modelo inventa qué es la FET («Facultad de Ingeniería y Tecnología», «Federación Tecnológica de México») y varias respuestas terminan cortadas a mitad de frase por el límite de `num_predict` (por ejemplo, `salida_B_B_regla_en_system_escalado.md` termina en «En conclusión, el»).

## 3. Desviaciones del enunciado

1. **El contexto de 512 no se aplicó.** Ollama 0.40.10 con el motor MLX (Mac) mostró `CONTEXT 2048` en `ollama ps` con una petición de `num_ctx 512`. Además, la corrida escalada leyó 2103 tokens con `num_ctx 2048`, así que **ni siquiera 2048 se está respetando como límite de recorte**. No se averiguó cuál es la ventana real.
2. **Parte B por script, no en el chat interactivo** de `ollama run`.
3. **Corrida escalada fuera del enunciado:** se cambiaron `num_ctx` (2048), `num_predict` (1800/1900) y las palabras pedidas (1200/1500).
4. **El par escalado no es comparable entre sí:** la versión B es de la corrida con 1800/1200 y la versión A de una corrida posterior con 1900/1500, que solo alcanzó a terminar la versión A antes de interrumpirse. La versión A de la corrida 1800/1200 quedó sobrescrita y ya no existe. `parteB_chat.py` quedó con los valores 1900/1500, y su docstring sigue diciendo «2048 y 1500 palabras».
5. **Corrección a un reporte anterior:** antes dije que el último cambio (1900/1500) no se había aplicado. Es falso: el script y `salida_B_A_regla_en_chat_escalado.md` (10:45) muestran que sí se aplicó y que la versión A llegó a ejecutarse.
6. **Parte A con `think=False`** por la API en lugar de `ollama run phi-demo` sin el flag.
7. **`parteB_chat.txt`** (el guion para el chat) no menciona el problema del contexto.

## 4. Qué falta

- **La explicación con sus palabras** de las dos partes (obligatoria).
- **Parte B válida:** hacerla en el chat real `ollama run qwen-demo --think=false` y comprobar con `ollama ps` qué contexto carga. Si sigue sin recortar, documentarlo como resultado del equipo o probar en otro equipo o motor donde `num_ctx 512` sí se aplique.
- Decidir qué hacer con las salidas `_escalado` (mezclan parámetros): borrarlas o dejarlas como evidencia, explicando por qué no sirven.
- Opcional: guardar en `reto4/` la corrida de control de la Práctica 9 si quieren usarla como evidencia de que el límite es de phi-demo.
