
import sys
from pathlib import Path
from typing import Optional, Literal
from pydantic import BaseModel

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
from comun import preguntar


class NotaPorteria(BaseModel):
    placa: Optional[str]
    tipo: Optional[Literal["carro", "moto"]]
    evento: Optional[Literal["entrada", "salida"]]
    hora: Optional[str]


NOTAS = [
    "Entró el carro placa ABC123 a las 7:45 de la mañana.",
    "Moto XYZ98A saliendo, son las 5:10 pm.",
    "Ingresó una moto con placa KLM45B a las 14:20.",
    "Salió el carro HJK456 a las 18:05, el visitante pagó en caja.",
    # incompletas / ambiguas
    "Acaba de llegar un carro blanco, no alcancé a ver la placa.",
    "La moto PQR12C pasó por la portería hace un rato.",
]

for texto in NOTAS:
    r = preguntar(
        "Extrae los datos de la nota del vigilante de ParqueFET. "
        "Si un dato no aparece en la nota, déjalo en null; no lo inventes.\n"
        f"<nota>{texto}</nota>",
        formato=NotaPorteria.model_json_schema())
    n = NotaPorteria.model_validate_json(r.message.content)  # falla si no cumple el esquema
    print(f"«{texto}»\n  -> {n.model_dump_json()}\n")
