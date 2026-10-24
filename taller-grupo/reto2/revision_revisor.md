CAMBIOS REQUERIDOS

**Hallazgos:**
- Línea 3: Falta verificar si el tipo de vehículo es "moto" antes de permitir ingreso, ignorando 
la capacidad de 300 motos.
- Línea 5: No se valida el límite de 14 horas de permanencia para ningún vehículo.
- Línea 6: Se retorna `True` sin considerar que un carné solo puede tener un vehículo a la vez 
(falta verificar `ocupados`).
- Línea 7: Falta manejar casos borde donde el tiempo exacto sea 14 horas o menos de 14 horas.

Envíe el código que desea revisar.