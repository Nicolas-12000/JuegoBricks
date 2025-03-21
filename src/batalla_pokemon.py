import random

class Pokemon:
    def __init__(self, nombre, ataque, defensa, vida):
        """Inicializa un Pokémon con atributos de batalla."""
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida

    def atacar(self, enemigo):
        """Calcula el daño hecho al enemigo considerando su defensa."""
        daño = max(1, self.ataque - enemigo.defensa + random.randint(-3, 3))
        enemigo.vida -= daño
        return f"{self.nombre} ataca a {enemigo.nombre} y le causa {daño} de daño!"

def batalla(pokemon1, pokemon2):
    """Simula una batalla por turnos entre dos Pokémon."""
    while pokemon1.vida > 0 and pokemon2.vida > 0:
        pokemon1.atacar(pokemon2)
        if pokemon2.vida <= 0:
            return f"¡{pokemon1.nombre} gana la batalla!"
        pokemon2.atacar(pokemon1)
        if pokemon1.vida <= 0:
            return f"¡{pokemon2.nombre} gana la batalla!"
