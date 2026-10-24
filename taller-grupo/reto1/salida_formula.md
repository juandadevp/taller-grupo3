```python
from enum import Enum
from typing import Tuple, Literal

class Motivo(str):
    OK = "OK"
    CARNE_EXPIRADO = "Carné expirado o no registrado"
    CAPACIDAD_SUPERADA = "Parqueadero lleno (120 carros / 300 motos)"
    VEHICULO_DENTRO = "Vehículo ya registrado en este carné"
    TIEMPO_EXCESIVO = "Vehículo permaneciendo más de 14 horas seguidas"

class TipoVehiculo(str):
    CARRO = "Carro"
    MOTO = "Moto"

def puede_ingresar(vehiculo: dict, ocupados: list, vehiculos_dentro: set) -> Tuple[bool, Literal[Motivo]]:
    """
    Decide si un vehículo puede ingresar al parqueadero de ParqueFET.
    
    Args:
        vehiculo: Diccionario con claves 'tipo' (TipoVehiculo), 'hora_entrada' (int) y 'carnes' (set).
        ocupados: Lista de vehículos actualmente en el parqueadero.
        vehiculos_dentro: Conjunto de IDs de carnés que ya tienen un vehículo dentro.
    
    Returns:
        Tupla (bool, motivo): True si puede entrar, False con la razón del rechazo.
    """
    if not vehiculo.get('carnes'):
        return False, Motivo.CARNE_EXPIRADO
    
    carnet_id = list(vehiculo['carnes'])[0]
    tipo = vehiculo['tipo']
    horas_actuales = vehiculo['hora_entrada']  # Asumimos que es hora actual o tiempo transcurrido
    if not isinstance(horas_actuales, int) or horas_actuales < 0:
        return False, Motivo.CARNE_EXPIRADO
    
    tipo_maximo = {TipoVehiculo.MOTO: 300, TipoVehiculo.CARRO: 120}
    if len(ocupados) >= tipo_maximo[tipo] or len(vehiculos_dentro) >= tipo_maximo[tipo]:
        return False, Motivo.CAPACIDAD_SUPERADA
    
    if carnet_id in vehiculos_dentro:
        return False, Motivo.VEHICULO_DENTRO
    
    if horas_actuales > 14:
        return False, Motivo.TIEMPO_EXCESIVO
    
    return True, Motivo.OK
```