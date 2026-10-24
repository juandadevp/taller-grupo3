```python
from datetime import datetime, timedelta
from enum import Enum
from typing import Tuple, Literal

class MotivoRechazo(Enum):
    CARNE_VALIDO = "Carné no vigente"
    CAPACIDAD_SUPERADA = "Parqueadero lleno"
    VEHICULO_DENTRO_OCCUPADO = "Vehículo ya registrado en este carné"
    TIEMPO_MAXIMO_EXCEDIDO = "Excede el límite de 14 horas continuas"

class TipoVehiculo(Enum):
    CARRO = "Carro"
    MOTO = "Moto"

class EstadoCarnes:
    def __init__(self, total_carros: int, total_motos: int) -> None:
        self.total_capacidad_carros = total_carros
        self.total_capacidad_motos = total_motos
        self.ocupados_carros = 0
        self.ocupados_motos = 0

    def verificar_capacidad(self, tipo: TipoVehiculo) -> bool:
        if tipo == TipoVehiculo.CARRO:
            return self.ocupados_carros < self.total_capacidad_carros
        return self.ocupados_motos < self.total_capacidad_motos

class Carne:
    def __init__(self, es_vigente: bool) -> None:
        self.es_vigente = es_vigente
        self.vehiculo_actual: Optional[TipoVehiculo] = None
        self.ingreso_hora: Optional[datetime] = None

    def verificar_unico_vehiculo(self, tipo: TipoVehiculo) -> bool:
        if self.vehiculo_actual is not None and self.vehiculo_actual != tipo:
            return False
        return True

    def verificar_tiempo_maximo(self, hora_actual: datetime) -> bool:
        if self.ingreso_hora is None:
            return True
        duracion = (hora_actual - self.ingreso_hora).total_seconds() / 3600
        return duracion <= 14

def puede_ingresar(vehiculo: Carne, ocupados: EstadoCarnes, vehiculos_dentro: dict) -> Tuple[bool, Literal["OK", str]]:
    """
    Determina si un vehículo puede ingresar al parqueadero de ParqueFET.

    Args:
        vehiculo (Carne): Objeto que representa el carné del usuario.
        ocupados (EstadoCarnes): Estado actual de la capacidad y ocupación del parqueadero.
        vehiculos_dentro (dict): Diccionario mapeando IDs de vehículos a sus tipos actuales dentro del parqueadero.

    Returns:
        Tuple[bool, str]: Retorna una tupla con el estado de entrada y el motivo.
            Si es True, el segundo elemento es "OK".
            Si es False, el segundo elemento explica por qué fue rechazado.
    """
    
    # Verificación 1: Carné vigente
    if not vehiculo.es_vigente:
        return (False, MotivoRechazo.CARNE_VALIDO.value)

    # Verificación 2: Capacidad del parqueadero
    tipo_vehiculo = None