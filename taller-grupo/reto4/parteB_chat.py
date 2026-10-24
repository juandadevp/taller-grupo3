"""Reproduce la Parte B como lo hace `ollama run`: en cada turno reenvía TODO el historial.

    uv run taller-grupo/reto4/parteB_chat.py                    # como dice el reto: 512 y 400 palabras
    uv run taller-grupo/reto4/parteB_chat.py --escalado         # 2048 y 1500 palabras

Ollama 0.40 con el motor MLX (Mac) sube num_ctx a un mínimo de 2048, así que con 512 no recorta nada.
--escalado mantiene la proporción de la guía: una respuesta larga + la pregunta siguiente no caben en la ventana.

Imprime cuántos tokens leyó el modelo en cada turno (prompt_eval_count) para ver el recorte.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import argparse
from comun import preguntar

ap = argparse.ArgumentParser()
ap.add_argument("--escalado", action="store_true")
a = ap.parse_args()
NUM_CTX, NUM_PREDICT, PALABRAS, SUF = (2048, 1900, 1500, "_escalado") if a.escalado else (512, None, 400, "")

AQUI = Path(__file__).resolve().parent
REGLA = "Empieza SIEMPRE tu respuesta con «Veredicto ParqueFET:»."
P1 = (f"Explica en al menos {PALABRAS} palabras cómo funciona el ingreso de un vehículo al parqueadero ParqueFET "
      "de la FET: carné vigente, capacidad de 120 carros y 300 motos, y un vehículo por carné.")
P2 = (f"Explica en al menos {PALABRAS} palabras cómo se cobra en ParqueFET: estudiantes y personal no pagan; "
      "visitantes pagan $3.000 (carro) o $1.500 (moto) por hora o fracción, con un máximo de 14 horas.")


def conversar(nombre, historial, preguntas):
    salida = [f"# Parte B · {nombre} · num_ctx={NUM_CTX} (efectivo en Ollama 0.40: mínimo 2048)\n"]
    for p in preguntas:
        historial.append({"role": "user", "content": p})
        r = preguntar(None, modelo="qwen-demo", num_ctx=NUM_CTX, num_predict=NUM_PREDICT, mensajes=historial)
        texto = r.message.content.strip()
        historial.append({"role": "assistant", "content": texto})
        empieza = texto.startswith("Veredicto ParqueFET:")
        salida += [f"## >>> {p}\n", f"_tokens leídos: {r.prompt_eval_count} · tokens generados: {r.eval_count} · "
                   f"¿empieza con la regla?: {'Sí' if empieza else 'No'}_\n", texto, "\n"]
        print(nombre, "|", p[:40], "| leídos", r.prompt_eval_count, "| regla:", empieza)
    (AQUI / f"salida_B_{nombre}{SUF}.md").write_text("\n".join(salida), encoding="utf-8")


conversar("A_regla_en_chat", [], [f"Regla: {REGLA[0].lower()}{REGLA[1:-1]}. ¿Entendido?", P1, P2])
conversar("B_regla_en_system", [{"role": "system", "content": REGLA}], [P1, P2])
