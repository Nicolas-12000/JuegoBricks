import pytest
import random
from src.batalla_pokemon import Pokemon, batalla

def test_pokemon():
    """Verifica que los Pokémon se inicializan correctamente."""
    mudkip = Pokemon("Mudkip", 50, 30, 100)
    assert mudkip.nombre == "Mudkip"
    assert mudkip.ataque == 50
    assert mudkip.defensa == 30
    assert mudkip.vida == 100

def test_ataque(monkeypatch):
    """Simula un ataque y verifica que el daño se aplica correctamente."""
    mudkip = Pokemon("Mudkip", 50, 30, 100)
    charmander = Pokemon("Charmander", 40, 20, 100)

    monkeypatch.setattr(random, "randint", lambda a, b: 0)  # No variación de daño

    mudkip.atacar(charmander)
    assert charmander.vida == 70  # (50 ataque - 20 defensa = 30 daño)

def test_batalla(monkeypatch):
    """Simula una batalla y verifica el ganador."""
    mudkip = Pokemon("Mudkip", 50, 30, 100)
    charmander = Pokemon("Charmander", 40, 20, 100)

    secuencia = [0, 0, 0, 0, 0, 0]  # Simula ataque constante sin variaciones

    def mock_randint(a, b):
        return secuencia.pop(0)

    monkeypatch.setattr(random, "randint", mock_randint)

    assert batalla(mudkip, charmander) == "¡Mudkip gana la batalla!"
