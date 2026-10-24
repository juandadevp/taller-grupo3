Aquí tienes la tabla de casos de prueba basada en los criterios de aceptación proporcionados para **ParqueFET**.

He analizado cada criterio y he diseñado un caso de prueba por uno, asegurando que cubra la lógica positiva (éxito) y negativa (error) descrita en cada regla.

| Caso | Entrada | Resultado esperado | Criterio que cubre |
| :--- | :--- | :--- | :--- |
| **CP-01** | Usuario intenta ingresar con un vehículo no registrado en carné vigente o con >14 horas de permanencia. | El sistema permite la entrada y registra la hora de inicio. | **Criterio 1**: Permite ingreso si el vehículo no está en carné vigente ni excede 14 horas. |
| **CP-02** | Usuario (visitante) selecciona pagar por hora/fracción; Sistema calcula $3.000 (carro) o $1.500 (moto). | Transacción exitosa y pago realizado. | **Criterio 2**: Calcula automáticamente el monto correcto para visitantes ($3.000/$1.500) y permite la transacción. |
| **CP-03** | Usuario intenta ingresar con un vehículo ya registrado en otro carné activo simultáneamente. | El sistema muestra error de "Vehículo ocupado" y bloquea la entrada. | **Criterio 3**: Bloquea la entrada y muestra error si el usuario tiene otro vehículo dentro a la vez. |
| **CP-04** | Usuario ha completado el pago exitosamente desde su móvil; Sistema verifica que la capacidad (120 carros / 300 motos) esté disponible. | El sistema valida la capacidad y otorga acceso inmediato al parqueadero. | **Criterio 4**: Valida la saturación de capacidad y permite el ingreso solo si hay espacio disponible tras un pago exitoso. |

### Resumen de cobertura
*   **Criterio 1:** Cubierto por el **CP-01**.
*   **Criterio 2:** Cubierto por el **CP-02**.
*   **Criterio 3:** Cubierto por el **CP-03**.
*   **Criterio 4:** Cubierto por el **CP-04**.

**Nota sobre agregados:** No fue necesario agregar casos adicionales, ya que se ha diseñado un caso de prueba específico para cada uno de los cuatro criterios proporcionados, cubriendo tanto la lógica de éxito como la de error descrita en cada regla.