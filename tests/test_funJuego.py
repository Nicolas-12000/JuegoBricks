import pytest
from src.funJuego import iniciar_juego, mover_personaje, finalizar_juego

# ==============================
# Prueba 1: Iniciar Juego
# ==============================
def test_iniciar_juego(capsys):
    iniciar_juego()
    captured = capsys.readouterr()
    assert "¡Iniciando juego!!!" in captured.out

# ==============================
# Prueba 2: Mover Personaje
# ==============================
@pytest.mark.parametrize("direccion", ["izquierda", "derecha", "arriba", "abajo"])
def test_mover_personaje(capsys, direccion):
    mover_personaje(direccion)
    captured = capsys.readouterr()
    assert f"Moviendo personaje hacia {direccion}" in captured.out

# ==============================
# Prueba 3: Finalizar Juego
# ==============================
def test_finalizar_juego(capsys):
    finalizar_juego()
    captured = capsys.readouterr()
    assert "¡Fin del juego!!" in captured.out
