# Reto 1 · ParqueFET · Comparación

## Líneas de cada salida
- Prompt malo: 74 líneas
- Prompt con fórmula (5 bloques + <reglas>): 47 líneas
- Variante (sin [RESTRICCIONES]): 64 líneas

## Prompt malo vs prompt con fórmula
- Reglas que ahora cumple: carné vigente, capacidad 120 carros / 300 motos, un vehículo por carné, 14 horas, retorno (bool, motivo).
- Lo que sigue fallando: superó las 30 líneas, uso incorrecto de Literal[Motivo], mezcla len(ocupados) con len(vehiculos_dentro) sin separar carros y motos, la regla de 14 horas se aplica al vehículo que entra y no a los que están dentro, y no calcula la tarifa de visitantes ($3.000 carro / $1.500 moto).
- Por qué cambió: al dar [CONTEXTO] con <reglas>, el modelo ya no tuvo que inventar las reglas del negocio, y [FORMATO] fijó el retorno (bool, motivo), por eso la firma coincide con la pedida.

## Variante: se quitó [RESTRICCIONES]
- Qué cambió: la salida pasó de 47 a 64 líneas. Agregó imports de datetime y timedelta y más código para manejar el tiempo.
- Solo usa la biblioteca estándar (datetime, enum, typing). No usa librerías externas ni base de datos, y no agregó texto explicativo extra.
- Conclusión: quitar [RESTRICCIONES] no rompió la regla de dependencias, pero sí el tamaño: sin el límite de 30 líneas el código creció. Una restricción solo frena lo que el modelo haría por su cuenta; para controlar el tamaño sí es necesaria.
