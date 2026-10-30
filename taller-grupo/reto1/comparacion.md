# Reto 1 · ParqueFET · Comparación

## Tamaño de cada salida
- Prompt malo: 74 líneas
- Prompt con la fórmula (5 bloques + `<reglas>`): 47 líneas
- Variante (sin el bloque de restricciones): 64 líneas

## Prompt malo contra prompt con la fórmula
**Qué reglas cumple ahora:** el carné vigente, la capacidad de 120 carros y 300 motos (a medias), un vehículo por carné, el límite de 14 horas y que devuelva (bool, motivo).

**Qué sigue fallando:**
- Se pasó de las 30 líneas que pedimos.
- Usó mal `Literal[Motivo]`.
- Mezcla `ocupados` con `vehiculos_dentro` sin separar carros y motos.
- La regla de las 14 horas la aplica al vehículo que está entrando, y debería aplicarla a los que ya están dentro.
- No calcula la tarifa de los visitantes ($3.000 carro y $1.500 moto).

**Por qué cambió:** con el prompt malo el modelo tuvo que inventarse todo. Al darle las reglas dentro de `<reglas>` ya no tuvo que adivinarlas, y al decirle el formato de salida la función quedó con la firma que pedimos.

## Variante: quitamos las restricciones
- **Qué cambió:** la salida pasó de 47 a 64 líneas y quedó cortada a mitad de la función por el límite de 700 tokens, así que en realidad es más larga. Además agregó `datetime` y `timedelta` y más código para manejar el tiempo.
- Siguió usando solo la biblioteca estándar y no agregó texto de más.
- **Conclusión:** sin el bloque de restricciones el código creció, porque ya no tenía el límite de 30 líneas. Las restricciones no le enseñan nada nuevo al modelo, solo le frenan lo que haría por su cuenta, y por eso hacen falta si queremos controlar el tamaño.
