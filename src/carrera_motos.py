import random

class Moto:
    def __init__(self, nombre, velocidad_max):
        """Inicializa la moto con un nombre y una velocidad máxima."""
        self.nombre = nombre
        self.velocidad_max = velocidad_max

    def correr(self):
        """Simula la velocidad alcanzada en la carrera (aleatoria hasta el máximo)."""
        return random.randint(1, self.velocidad_max)

def determinar_ganador(moto1, moto2):
    """Determina qué moto gana en una carrera."""
    velocidad1 = moto1.correr()
    velocidad2 = moto2.correr()

    if velocidad1 > velocidad2:
        return f"¡{moto1.nombre} gana con {velocidad1} km/h!"
    elif velocidad2 > velocidad1:
        return f"¡{moto2.nombre} gana con {velocidad2} km/h!"
    else:
        return "¡Empate!"
