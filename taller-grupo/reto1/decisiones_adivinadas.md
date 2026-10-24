# Decisiones que el modelo tuvo que adivinar (prompt malo)

1. Lenguaje: eligió Python sin que se lo pidieran.
2. Datos del vehículo: inventó una clase Vehiculo con placa, marca y modelo (no usa tipo carro/moto ni carné).
3. Dónde se guarda el registro: asumió una lista en memoria como "base de datos".
4. Parámetros y retorno de la función: inventó placa y hora_actual, y que devuelve True/False.
5. Contexto: supuso "un sistema de estacionamiento", sin saber que es ParqueFET.
6. Reglas de negocio: no aplica el carné vigente, la capacidad de 120 carros y 300 motos, ni el límite de 14 horas (verificar en la salida).
7. Visitantes y tarifas: no distingue estudiantes, personal y visitantes (verificar en la salida).
