class Terreno:
    def __init__(self, nome, url):
        self.nome = nome
        self.url = url
        self.estado = "seco"

    def alagar(self):
        if self.estado == "seco":
            self.estado = "alagado"
        else:
            self.estado = "afundado"

    def drenar(self):
        self.estado = "seco"

    def esta_alagado(self):
        return self.estado == "alagado"

    def esta_afundado(self):
        return self.estado == "afundado"

    def __repr__(self):
        return f"{self.nome}".ljust(20)

class TerrenoTesouro(Terreno):
    def __init__(self, nome, url, tesouro):
        super().__init__(nome, url)
        self.tesouro = tesouro
        self.tem_tesouro = True

    def obter_tesouro(self):
        self.tem_tesouro = False
        return self.tesouro

class TerrenoTesouroFogo(TerrenoTesouro):
    def __init__(self, nome, tesouro):
        super().__init__(nome, tesouro)

class TerrenoTesouroVento(TerrenoTesouro):
    def __init__(self, nome, tesouro):
        super().__init__(nome, tesouro)

class TerrenoTesouroOceano(TerrenoTesouro):
    def __init__(self, nome, tesouro):
        super().__init__(nome, tesouro)

class TerrenoTesouroTerra(TerrenoTesouro):
    def __init__(self, nome, tesouro):
        super().__init__(nome, tesouro)

class PortoDosTolos(Terreno):
    def __init__(self, url):
        super().__init__('PISTA_POUSO', url)
