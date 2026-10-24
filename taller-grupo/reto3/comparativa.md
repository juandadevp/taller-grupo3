# Reto 3 · Comparativa contra el enunciado (Caso 1 · ParqueFET)

Requisito nuevo: «Que los visitantes puedan pagar el parqueadero desde el celular antes de salir.»
Modelo: qwen-demo (temperatura 0, semilla 42, `think=False`), ejecutado con `taller-grupo/correr.py`.
Revisión hecha solo leyendo los archivos de `reto3/`. Las salidas del modelo no se editaron; las citas son literales.

## 1. Qué cumple y qué no

| Pide el enunciado | Estado | Archivo |
|---|---|---|
| Prompt 1 few-shot con 2 ejemplos propios (pedido → historia), formato «Como…, quiero…, para…» | Cumple | `prompt1.txt` → `salida1.md` |
| Prompt 2: historia dentro de `<historia>`, 3 a 5 criterios Dado / Cuando / Entonces, con las reglas del caso | Cumple (dio 4) | `prompt2.txt` → `salida2.md` |
| Prompt 3: tabla `Caso \| Entrada \| Resultado esperado \| Criterio que cubre` + frase de auto-verificación | Cumple | `prompt3.txt` → `salida3.md` |
| Encadenamiento: cada salida entra en el prompt siguiente | Cumple | La salida se pegó sin cambios en el hueco «pegue aquí» |
| Encontrar el paso del primer error, corregir ese prompt y repetir desde ahí | Cumple | `prompt2_v2.txt` → `salida2_v2.md`; `prompt3_v2.txt` → `salida3_v2.md` |
| Nota de qué paso se corrigió y por qué | Cumple | `nota_correccion.md` |

Notas sobre los archivos:
- `prompt2.txt` y `prompt3.txt` ya no son plantillas: tienen pegada la salida anterior (son el prompt exacto que se envió).
- `prompt3_v2.txt` es `prompt3.txt` con los criterios de `salida2_v2.md` en lugar de los de `salida2.md`; las instrucciones son idénticas.

## 2. Comparación v1 contra v2

Cambios de `prompt2.txt` a `prompt2_v2.txt` (dos a la vez):
- Se añadió «Los criterios tratan del pago antes de salir, no del ingreso.»
- «Usa las reglas de negocio del caso:» pasó a «Usa solo estas reglas de negocio; no inventes reglas nuevas:».

El paso 1 no cambió. La historia es correcta y no inventa nada: «Como visitante, quiero poder realizar el pago del parqueadero desde mi celular antes de salir, para evitar filas y gestionar mejor el tiempo de estacionamiento.»

### Paso 2 · criterios

| | v1 (`salida2.md`) | v2 (`salida2_v2.md`) |
|---|---|---|
| ¿De qué tratan? | Mezclan pago con **ingreso** | Los 4 tratan del pago y la salida |
| Regla invertida | Sí. Criterio 1: «el vehículo no está registrado en un carné vigente… Entonces el sistema le permite ingresar» | No |
| Regla inventada | Sí. Criterio 4: pagar y luego «intenta ingresar»; ninguna regla pide pagar para entrar | Ninguna regla nueva, pero sí una consecuencia inventada. Criterio 4: «permitirá la salida si el tiempo de permanencia total es menor o igual a 14 horas» (la regla no dice que se bloquee la salida) |
| Regla mal aplicada | Criterio 3: «vehículo ya registrado en otro carné activo» (no es lo que dice la regla) | Criterio 4 revisa «un solo vehículo por carné» al **salir**, cuando es una regla de ingreso |
| Contradicción | — | Criterio 1: el visitante intenta pagar y recibe un error que dice que los visitantes deben pagar |
| Estudiantes y personal no pagan | No aparece | Sí (criterio 3) |
| Cobro por hora **o fracción** con un cálculo | No | No |

### Paso 3 · tabla

| | v1 (`salida3.md`) | v2 (`salida3_v2.md`) |
|---|---|---|
| Casos | 4, uno por criterio | 4, uno por criterio |
| Datos concretos (horas, montos) | No; las entradas son descripciones | No; las entradas son descripciones |
| Errores heredados | Sí. CP-01 espera «El sistema permite la entrada» de un vehículo no registrado | Sí. CP-01 repite la contradicción del criterio 1 |
| Error propio | — | CP-04: la entrada dice «tiempo <14h» y el resultado esperado «≤ 14 horas» |
| Auto-verificación | «No fue necesario agregar casos adicionales» | «No fue necesario agregar casos adicionales» |

**Lectura:**
- El primer error está en el **paso 2**, y fue el paso que se corrigió.
- La v2 arregló el foco (pago antes de salir) y quitó la regla inventada de pagar para entrar.
- Pero dejó errores nuevos o distintos: una contradicción, una regla de ingreso aplicada en la salida y una consecuencia inventada para las 14 horas.
- La auto-verificación del paso 3 hizo lo que pedía la frase (un caso por criterio), pero **no detecta criterios equivocados**: valida la cobertura, no la corrección.

## 3. Desviaciones del enunciado

- **Dos cambios a la vez en el prompt 2.** El enunciado pide corregir el prompt, sin especificar cuántos cambios. Al aplicar dos juntos no se puede saber cuál de los dos produjo la mejora.
- **Primera pasada con los prompts simples del enunciado, por decisión del equipo.** Se quitaron de forma deliberada la frase de «no inventes reglas» (prompt 2) y la petición de datos concretos (prompt 3).
- **El prompt 3 no se corrigió en la v2**, solo se volvió a ejecutar con los criterios nuevos. Por eso las entradas siguen sin datos concretos.
- **El modelo no lo fija el enunciado.** Se usó qwen-demo con `think=False`, igual que en el Reto 1.

## 4. Qué falta

- Decidir si se hace otra iteración. Los criterios v2 todavía no son correctos del todo (criterio 1 contradictorio, criterio 4 mal aplicado) y ningún criterio calcula el cobro por fracción. Si el objetivo es una cadena correcta y no solo documentar el primer error, falta al menos una corrección más del prompt 2 y, quizá, pedir datos concretos en el prompt 3.
- Observación: las reglas del caso no dicen cómo entra un visitante, cuando «solo ingresan vehículos registrados a un carné vigente». Esa tensión en las reglas puede explicar parte de la confusión del criterio 1.
