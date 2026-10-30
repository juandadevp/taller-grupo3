# Análisis · Reto 5 (bonus) · ParqueFET

Scripts: `reporte_json.py` (parte A) y `evalua.py` (parte B). Salidas: `salida_parteA.md`, `salida_parteB_qwen3.5_4b.md` y `salida_parteB_qwen3.5_0.8b.md`. Todo se ejecutó con temperatura 0 y semilla 42.

## Parte A · JSON validado

Hicimos un script que lee notas del vigilante y las convierte en JSON con cuatro campos: `placa`, `tipo` (carro/moto), `evento` (entrada/salida) y `hora`. Probamos con 6 notas. Las 4 que tenían todos los datos las sacó bien. Incluso cambió "5:10 pm" a "17:10" sin que se lo pidiéramos.

Las otras 2 notas eran incompletas:
- *"Un carro blanco, no alcancé a ver la placa"*: el modelo dejó la placa y la hora en `null`, que es lo correcto. Dedujo que era una "entrada" por la palabra "llegar", y eso sí tiene respaldo en la nota.
- *"La moto PQR12C pasó por la portería hace un rato"*: dejó la hora en `null`, pero puso que era una "entrada" cuando la nota no dice si entró o salió. **Se lo inventó.**

**Lo que entendimos:** el esquema de Pydantic solo revisa que el JSON tenga la forma correcta (por ejemplo, que `tipo` sea "carro" o "moto"), pero no revisa que lo que dice sea verdad. Por eso un dato inventado igual pasa la validación.

Lo que ayudó fue pedirle explícitamente "si un dato no aparece, déjalo en null; no lo inventes" y permitir `null` en los campos. Aun así falló en el campo que más tentaba rellenar. Una mejora posible sería agregar un valor `"desconocido"` en `evento`.

## Parte B · Comparar prompts (v1 contra v2)

Armamos 10 mensajes del parqueadero con su respuesta correcta (4 de ellos ambiguos) y los clasificamos en PERMITIDO, NEGADO, COBRO o INCIDENTE. Probamos dos prompts: v1 solo pide clasificar, y v2 además explica las reglas del parqueadero y da 4 ejemplos.

| Modelo | v1 (zero-shot) | v2 (definiciones + ejemplos) |
|---|---|---|
| qwen3.5:4b | 5/10 | 10/10 |
| qwen3.5:0.8b | 7/10 | 10/10 |

**Casos que fallaron en v1 y no en v2**
- Con el 4b: "visitante en moto sin carné" (→ INCIDENTE), "visitante sale tras 2 h 10 min" (→ NEGADO), y tres ambiguos: carné con otro vehículo adentro (→ PERMITIDO), "¿me toca pagar?" (→ NEGADO) y parqueadero lleno (→ PERMITIDO).
- Con el 0.8b: "sale tras 2 h 10 min" (→ NEGADO), "una moto lleva 15 horas dentro" (→ COBRO) y "vidrio roto" (→ NEGADO).

**Por qué fallaba v1:** no le dice al modelo las reglas del parqueadero (cupo, un vehículo por carné, quién paga, el límite de 14 horas), entonces tenía que adivinar. Los casos ambiguos fallaron justo donde hacía falta una regla. En v2 le dimos esas reglas y acertó todo.

## Lo que nos llamó la atención

- En v1 el modelo pequeño (0.8b) sacó más que el grande (4b). Con solo 10 casos pudo ser casualidad, así que no podemos decir que el pequeño sea mejor.
- Con v2 los dos modelos llegaron a 10/10: explicarle bien la tarea al modelo pesó más que el tamaño del modelo.

## Limitaciones

- Las reglas de v2 coinciden con los casos de prueba (por ejemplo "más de 14 horas" o "120 carros"), así que el modelo casi tenía la respuesta a la vista. El 10/10 mide en parte eso y no solo si generaliza. Para medirlo mejor habría que probar con casos que las reglas no mencionen.
- 10 casos es una muestra pequeña, y los casos "ambiguos" los definimos nosotros.
