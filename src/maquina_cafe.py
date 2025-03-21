class MaquinaCafe:
    def __init__(self, agua, cafe, leche):
        """Inicializa la máquina con la cantidad de ingredientes disponibles."""
        self.agua = agua
        self.cafe = cafe
        self.leche = leche

    def preparar(self, tipo):
        """Prepara café según el tipo solicitado y los ingredientes disponibles."""
        if tipo == "expreso" and self.agua >= 50 and self.cafe >= 10:
            self.agua -= 50
            self.cafe -= 10
            return "☕ Expreso listo!"
        elif tipo == "latte" and self.agua >= 50 and self.cafe >= 10 and self.leche >= 20:
            self.agua -= 50
            self.cafe -= 10
            self.leche -= 20
            return "🥛☕ Latte listo!"
        else:
            return "❌ Ingredientes insuficientes"
