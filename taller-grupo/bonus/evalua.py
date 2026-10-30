
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
from comun import preguntar

# (texto, etiqueta, ambiguo)
CASOS = [
    ("Soy estudiante con carné vigente y quiero entrar con mi carro.", "PERMITIDO", False),
    ("Un visitante en moto sin carné pide entrar.", "NEGADO", False),
    ("Un docente intenta entrar con carné vencido.", "NEGADO", False),
    ("Visitante en carro sale tras 2 horas y 10 minutos, ¿cuánto paga?", "COBRO", False),
    ("Una moto lleva 15 horas dentro del parqueadero.", "INCIDENTE", False),
    ("Encontré un carro con el vidrio roto en el nivel 2.", "INCIDENTE", False),
    # ambiguos
    ("Mi carné ya tiene otro vehículo adentro, ¿puedo entrar con el carro de mi papá?", "NEGADO", True),
    ("Entré con mi carro hace 3 horas siendo visitante, ¿me toca pagar?", "COBRO", True),
    ("El parqueadero de carros está lleno y llegó un estudiante.", "NEGADO", True),
    ("Un empleado salió y la barrera no levantó.", "INCIDENTE", True),
]

V1 = """Clasifica el mensaje de ParqueFET en UNA categoría: PERMITIDO, NEGADO, COBRO o INCIDENTE.
Responde solo con la categoría.
Mensaje: "{mensaje}\""""

V2 = """Clasifica el mensaje del parqueadero de ParqueFET en UNA categoría, según estas reglas:
- PERMITIDO: el vehículo cumple las reglas y puede ingresar (carné vigente, hay cupo, el carné no tiene otro vehículo adentro).
- NEGADO: el ingreso no procede (sin carné o vencido, sin cupo: 120 carros / 300 motos, o el carné ya tiene un vehículo adentro).
- COBRO: pregunta o trámite de pago; solo visitantes pagan ($3.000 carro, $1.500 moto por hora o fracción).
- INCIDENTE: algo anormal: daños, falla de equipos o permanencia de más de 14 horas.

Ejemplos:
"Entró un estudiante con carné vigente y hay cupo." -> PERMITIDO
"Una moto de visitante sale tras 40 minutos, ¿cuánto debe?" -> COBRO
"La talanquera quedó trabada y no abre." -> INCIDENTE
"Un estudiante sin carné quiere entrar." -> NEGADO

Responde solo con PERMITIDO, NEGADO, COBRO o INCIDENTE.
Mensaje: "{mensaje}\""""


def clasificar(plantilla, mensaje, modelo):
    r = preguntar(plantilla.format(mensaje=mensaje), modelo=modelo, num_predict=10)
    m = re.search(r"PERMITIDO|NEGADO|COBRO|INCIDENTE", r.message.content.upper())
    return m.group(0) if m else r.message.content.strip()


ap = argparse.ArgumentParser()
ap.add_argument("--modelo", default="qwen3.5:4b")
a = ap.parse_args()

print(f"Modelo: {a.modelo}\n")
for nombre, plantilla in [("v1", V1), ("v2", V2)]:
    ok = 0
    for msg, esperado, amb in CASOS:
        obtenido = clasificar(plantilla, msg, a.modelo)
        if obtenido == esperado:
            ok += 1
        else:
            print(f"  [{nombre}] falló{' (ambiguo)' if amb else ''}: «{msg}» -> {obtenido} (esperado {esperado})")
    print(f"{nombre}: {ok}/{len(CASOS)}\n")
