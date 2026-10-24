import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from comun import preguntar
modelo, entrada, salida = sys.argv[1:4]
r = preguntar(Path(entrada).read_text(encoding="utf-8"), modelo=modelo)
Path(salida).write_text(r.message.content, encoding="utf-8")
print("Listo:", salida)
