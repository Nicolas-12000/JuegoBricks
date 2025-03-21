import pytest
from src.maquina_cafe import MaquinaCafe

def test_preparar_expresso():
    maquina = MaquinaCafe(agua=100, cafe=50, leche=50)
    assert maquina.preparar("expreso") == "☕ Expreso listo!"
    assert maquina.agua == 50
    assert maquina.cafe == 40

def test_preparar_latte():
    maquina = MaquinaCafe(agua=100, cafe=50, leche=50)
    assert maquina.preparar("latte") == "🥛☕ Latte listo!"
    assert maquina.agua == 50
    assert maquina.cafe == 40
    assert maquina.leche == 30

def test_ingredientes_insuficientes():
    maquina = MaquinaCafe(agua=20, cafe=5, leche=10)
    assert maquina.preparar("expreso") == "❌ Ingredientes insuficientes"
    assert maquina.preparar("latte") == "❌ Ingredientes insuficientes"
