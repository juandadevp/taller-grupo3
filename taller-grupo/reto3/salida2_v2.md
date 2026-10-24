Aquí tienes 4 criterios de aceptación en formato Dado / Cuando / Entonces, basados estrictamente en las reglas de negocio proporcionadas:

1.  **Dado** que el usuario es un visitante y no posee carné vigente, **cuando** intente realizar el pago desde su celular antes de salir, **entonces** el sistema le mostrará el mensaje de error "Los visitantes deben pagar $3.000 (carro) o $1.500 (moto) por hora o fracción" y no permitirá la salida sin transacción.

2.  **Dado** que el usuario ha completado el pago desde su celular, **cuando** intente salir del parqueadero, **entonces** el sistema verificará que el vehículo registrado en su carné (si aplica) esté disponible para liberar y confirmará la salida exitosa.

3.  **Dado** que el usuario es un estudiante o personal de la institución, **cuando** intente realizar el pago desde su celular antes de salir, **entonces** el sistema rechazará la operación con el mensaje "Estudiantes y personal no pagan" y le indicará que puede salir directamente sin costo.

4.  **Dado** que el usuario ha realizado el pago y está a punto de salir, **cuando** intente liberar su vehículo, **entonces** el sistema verificará que no haya otro vehículo registrado en el mismo carné (para cumplir la regla de un solo vehículo por carné) y permitirá la salida si el tiempo de permanencia total es menor o igual a 14 horas.