Aquí tienes la tabla Markdown con los casos de prueba basados estrictamente en los criterios proporcionados. He verificado que cada uno de los 4 criterios tenga al menos un caso cubierto.

| Caso | Entrada | Resultado esperado | Criterio que cubre |
| :--- | :--- | :--- | :--- |
| **CP-01** | Usuario es visitante sin carné vigente; intenta pagar desde celular antes de salir. | El sistema muestra el mensaje: "Los visitantes deben pagar $3.000 (carro) o $1.500 (moto) por hora o fracción" y bloquea la salida sin transacción. | **Criterio 1** |
| **CP-02** | Usuario ha completado el pago desde celular; intenta salir del parqueadero. | El sistema verifica que el vehículo registrado en su carné esté disponible, libera el estacionamiento y confirma la salida exitosa. | **Criterio 2** |
| **CP-03** | Usuario es estudiante o personal de la institución; intenta realizar pago desde celular antes de salir. | El sistema rechaza la operación con el mensaje: "Estudiantes y personal no pagan" e indica que puede salir directamente sin costo. | **Criterio 3** |
| **CP-04** | Usuario ha realizado el pago; intenta liberar su vehículo (verificando un solo vehículo por carné y tiempo <14h). | El sistema verifica que no haya otro vehículo en el mismo carné y permite la salida si el tiempo total es ≤ 14 horas. | **Criterio 4** |

### Verificación de cobertura:
*   **Criterio 1:** Cubierto por el Caso CP-01.
*   **Criterio 2:** Cubierto por el Caso CP-02.
*   **Criterio 3:** Cubierto por el Caso CP-03.
*   **Criterio 4:** Cubierto por el Caso CP-04.

**Nota:** Todos los criterios de aceptación han sido cubiertos con un caso de prueba cada uno. No fue necesario agregar casos adicionales, ya que la lógica de negocio descrita en los 4 puntos se ha mapeado directamente a una prueba por criterio.