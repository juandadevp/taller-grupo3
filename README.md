# Taller · Ingeniería de prompts y de contexto

Diplomado en Ingeniería de Software con IA y Sistemas Agénticos · FET · Sesión 03

- **Integrantes:** juan david plata polania, jorge alejandro arias, cristian alirio ruiz
- **Caso:** Caso 1 · ParqueFET
- **Modelos:** qwen-demo (qwen3.5:4b) y phi-demo (phi4-mini)
- **Equipo:** Mac (macOS), Ollama 0.40.10

## Estructura de la entrega
- [taller-grupo/reto1/](taller-grupo/reto1/) · Rescatar un prompt malo
- [taller-grupo/reto2/](taller-grupo/reto2/) · System prompt del revisor y prompt injection
- [taller-grupo/reto3/](taller-grupo/reto3/) · Del requisito a los casos de prueba
- [taller-grupo/reto4/](taller-grupo/reto4/) · Razonar y manejar el contexto

## Nota sobre cómo se ejecutó
- En los retos 1 y 3, y en la parte A del reto 4, se usó el script `taller-grupo/correr.py` para guardar las salidas de los prompts sin códigos de terminal.
- En el reto 4, con la versión de Ollama usada (0.40.10), ollama ps mostró 2048 aunque se pidió 512, y ni siquiera con 2103 tokens leídos se recortó el historial; se explica en `taller-grupo/reto4/explicacion.md`.

## Reflexión del grupo
La técnica con más efecto fue dar el contexto con las reglas de negocio dentro de `<reglas>` (reto 1): el modelo dejó de inventar y mejoró mucho, aunque con errores. También vimos que un error en un paso de una cadena se arrastra a los siguientes (reto 3), que pedir razonamiento paso a paso no garantiza razonar bien (reto 4) y que un system prompt más largo no asegura mejor comportamiento (reto 2).

Si mañana le pedimos a una IA que programe una funcionalidad, daremos las reglas y restricciones desde el inicio, dividiremos la tarea en pasos pequeños y revisaremos cada salida antes de usarla.

---
El kit original de la clase está en [README_KIT.md](README_KIT.md).
