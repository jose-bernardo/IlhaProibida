from terreno import TerrenoTesouro
from carta import CartaTesouro

class Jogador:
    def __init__(self, jogo):
        self.mao = []
        self.jogo = jogo
        self.posicao = (2, 2) # por enquanto começa sempre no terreno (2,2)
        self.url = "6FVP1bF"

    def comprar_carta(self, carta):
        self.mao.append(carta)

    def numero_mao(self):
        return len(self.mao)

    def mover(self, direcao):
        if direcao == "up":
            nova_posicao = (self.posicao[0] - 1, self.posicao[1])
        elif direcao == "down":
            nova_posicao = (self.posicao[0] + 1, self.posicao[1])
        elif direcao == "left":
            nova_posicao = (self.posicao[0], self.posicao[1] - 1)
        elif direcao == "right": 
            nova_posicao = (self.posicao[0], self.posicao[1] + 1)
        else:
            return False

        if self.jogo.tabuleiro.terreno_valido(nova_posicao):
            self.posicao = nova_posicao
            return True
        else:
            print("não dá")
            return False

    def drenar(self, direcao):
        if direcao == "up":
            terreno_pos = (self.posicao[0] - 1, self.posicao[1])
        elif direcao == "down":
            terreno_pos = (self.posicao[0] + 1, self.posicao[1])
        elif direcao == "left":
            terreno_pos = (self.posicao[0], self.posicao[1] - 1)
        elif direcao == "right": 
            terreno_pos = (self.posicao[0], self.posicao[1] + 1)
        elif direcao == "atual":
            terreno_pos = self.posicao
        else:
            return False

        self.jogo.tabuleiro.disposicao[terreno_pos[0]][terreno_pos[1]].drenar()

    def doar_carta(self, index, jogador):
        jogador.receber_carta(self.mao[index])

    def receber_carta(self, carta):
        self.mao.append(carta)

    def obter_tesouro(self):
        terreno = self.jogo.tabuleiro.disposicao[self.posicao[0]][self.posicao[1]]
        if isinstance(terreno, TerrenoTesouro) and terreno.tem_tesouro:
            # obtem o tesouro se tiver pelo menos 4 cartas do tesouro nesse terreno
            cartas_tesouro = list(filter(lambda carta: isinstance(carta, CartaTesouro) and carta.tesouro == terreno.tesouro, self.mao))
            if len(cartas_tesouro) > 3:
                # remove as cartas da mão
                self.mao = list(set(self.mao) - set(cartas_tesouro[:4]))
                self.jogo.tesouros.append(terreno.obter_tesouro())
                self.jogo.termina_tempestade()
            else:
                print("meu arranja as cartas")
        else:
            print("isto nao tem tesouro")

    def especial(self):
        pass

class Explorador(Jogador):
    def __init__(self, jogo):
        super().__init__(jogo)

    def especial(self):
        pass

    def __repr__(self):
        return "Explorador"

class Mergulhador(Jogador):
    def __init__(self, jogo):
        super().__init__(jogo)

    def especial(self):
        pass

    def __repr__(self):
        return "Mergulhador"

class Navegador(Jogador):
    def __init__(self, jogo):
        super().__init__(jogo)

    def especial(self):
        pass

    def __repr__(self):
        return "Navegador"

class Piloto(Jogador):
    def __init__(self, jogo):
        super().__init__(jogo)

    def especial(self):
        pass

    def __repr__(self):
        return "Piloto"

class Engenheiro(Jogador):
    def __init__(self, jogo):
        super().__init__(jogo)

    def especial(self):
        pass

    def __repr__(self):
        return "Engenheiro"

class Mensageiro(Jogador):
    def __init__(self, jogo):
        super().__init__(jogo)

    def especial(self):
        pass

    def __repr__(self):
        return "Mensageiro"


