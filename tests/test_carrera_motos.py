import pytest
import random
from src.carrera_motos import Moto, determinar_ganador

def test_moto():
    """Verifica que la moto se inicializa correctamente."""
    moto = Moto("Ducati", 300)
    assert moto.nombre == "Ducati"
    assert moto.velocidad_max == 300

def test_correr(monkeypatch):
    """Simula la velocidad alcanzada por una moto."""
    moto = Moto("Yamaha", 200)

    monkeypatch.setattr(random, "randint", lambda a, b: 150)
    assert moto.correr() == 150

def test_determinar_ganador(monkeypatch):
    """Simula una carrera y verifica el resultado."""
    moto1 = Moto("Honda", 250)
    moto2 = Moto("Suzuki", 250)

    resultados = [220, 180]  # Honda corre 220, Suzuki 180

    def mock_randint(a, b):
        return resultados.pop(0)

    monkeypatch.setattr(random, "randint", mock_randint)

    assert determinar_ganador(moto1, moto2) == "¡Honda gana con 220 km/h!"
