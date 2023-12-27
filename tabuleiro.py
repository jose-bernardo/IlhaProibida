SPACES = " " * 20

class Tabuleiro:
    def __init__(self, terrenos):
        self.terrenos = terrenos

        #for i, linha in enumerate(self.disposicao):
        #    for j, entrada in enumerate(linha):
        #        if entrada == 1:
        #            self.disposicao[i][j] = self.terrenos.pop()

    def terreno_valido(self, posicao):
        if posicao[0] >= 0 and posicao[1] <= 5:
            terreno = self.disposicao[posicao[0]][posicao[1]]
            if terreno != 0 and not terreno.esta_afundado():
                return True
        return False

    def printer(self):
        impressao = [[SPACES if e == 0 else str(e) for e in linha] for linha in self.disposicao]
        for linha in impressao:
            print(''.join(linha))
