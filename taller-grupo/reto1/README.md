# Reto 1 · Rescatar un prompt malo (Caso 1 · ParqueFET)

## Entregables
| Pieza | Archivo |
|---|---|
| Prompt malo | [prompt_malo.txt](prompt_malo.txt) |
| Salida del prompt malo | [salida_mala.md](salida_mala.md) |
| Decisiones que el modelo adivinó | [decisiones_adivinadas.md](decisiones_adivinadas.md) |
| Prompt nuevo (5 bloques + reglas) | [prompt_formula.txt](prompt_formula.txt) |
| Salida del prompt nuevo | [salida_formula.md](salida_formula.md) |
| Variante (sin RESTRICCIONES) | [prompt_variante.txt](prompt_variante.txt) |
| Salida de la variante | [salida_variante.md](salida_variante.md) |
| Comparación | [comparacion.md](comparacion.md) |

Modelo: qwen-demo (temperatura 0, semilla 42), ejecutado con taller-grupo/correr.py.

## Prompt malo
```
Hazme una función para registrar la entrada de un vehículo.
```

## Prompt nuevo
```
[QUÉ QUIERO] Escribe la función puede_ingresar(vehiculo, ocupados, vehiculos_dentro) en Python 3.12 que decide si un vehículo puede entrar al parqueadero de ParqueFET.

[PARA QUIÉN] La usará el sistema de control de acceso del campus y la mantendrán desarrolladores junior.

[CONTEXTO] ParqueFET controla el parqueadero de la FET. La función debe aplicar estas reglas:
<reglas>
- Solo ingresan vehículos registrados a un carné vigente.
- Capacidad: 120 carros y 300 motos.
- Estudiantes y personal no pagan; visitantes pagan $3.000 (carro) o $1.500 (moto) por hora o fracción.
- Un carné solo puede tener un vehículo dentro a la vez.
- Ningún vehículo puede permanecer más de 14 horas seguidas.
</reglas>

[FORMATO] Devuelve solo el código, con type hints y docstring. La función retorna una tupla (bool, motivo): motivo explica el rechazo o es "OK".

[RESTRICCIONES] Sin librerías externas. No accedas a bases de datos: recibe los datos como parámetros. Máximo 30 líneas.
```

## Variante
Mismo prompt sin el bloque [RESTRICCIONES].

## Decisiones que el modelo adivinó con el prompt malo

1. Lenguaje: eligió Python sin que se lo pidieran.
2. Datos del vehículo: inventó una clase Vehiculo con placa, marca y modelo (no usa tipo carro/moto ni carné).
3. Dónde se guarda el registro: asumió una lista en memoria como "base de datos".
4. Parámetros y retorno de la función: inventó placa y hora_actual, y que devuelve True/False.
5. Contexto: supuso "un sistema de estacionamiento", sin saber que es ParqueFET.
6. Reglas de negocio: no aplica el carné vigente, la capacidad de 120 carros y 300 motos, ni el límite de 14 horas.
7. Visitantes y tarifas: no distingue estudiantes, personal y visitantes.

## Comparación

## Líneas de cada salida
- Prompt malo: 74 líneas
- Prompt con fórmula (5 bloques + <reglas>): 47 líneas
- Variante (sin [RESTRICCIONES]): 64 líneas

## Prompt malo vs prompt con fórmula
- Reglas que ahora cumple: carné vigente, capacidad 120 carros / 300 motos (cumple a medias), un vehículo por carné, 14 horas, retorno (bool, motivo).
- Lo que sigue fallando: superó las 30 líneas, uso incorrecto de Literal[Motivo], mezcla len(ocupados) con len(vehiculos_dentro) sin separar carros y motos, la regla de 14 horas se aplica al vehículo que entra y no a los que están dentro, y no calcula la tarifa de visitantes ($3.000 carro / $1.500 moto).
- Por qué cambió: al dar [CONTEXTO] con <reglas>, el modelo ya no tuvo que inventar las reglas del negocio, y [FORMATO] fijó el retorno (bool, motivo), por eso la firma coincide con la pedida.

## Variante: se quitó [RESTRICCIONES]
- Qué cambió: la salida pasó de 47 a 64 líneas, y quedó cortada por el límite de 700 tokens (num_predict del Modelfile): termina a mitad de la función, así que 64 líneas no es su tamaño completo. Agregó imports de datetime y timedelta y más código para manejar el tiempo.
- Solo usa la biblioteca estándar (datetime, enum, typing). No usa librerías externas ni base de datos, y no agregó texto explicativo extra.
- Conclusión: quitar [RESTRICCIONES] no rompió la regla de dependencias, pero sí el tamaño: sin el límite de 30 líneas el código creció. Una restricción solo frena lo que el modelo haría por su cuenta; para controlar el tamaño sí es necesaria.
