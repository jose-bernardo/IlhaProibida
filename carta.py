class Carta:
    pass

class CartaAlagamento(Carta):
    def __init__(self, terreno):
        self.terreno = terreno

class CartaTesouro(Carta):
    def __init__(self, tesouro):
        self.tesouro = tesouro

    def __repr__(self):
        return self.__class__.__name__ + " " + self.tesouro

class CartaEnchente(Carta):
    def __repr__(self):
        return self.__class__.__name__

class CartaTempestade(Carta):
    def __repr__(self):
        return self.__class__.__name__

class CartaHelicoptero(Carta):
    def __repr__(self):
        return self.__class__.__name__

class CartaSacoAreia(Carta):
    def __repr__(self):
        return self.__class__.__name__
