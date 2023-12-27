#!/usr/bin/env python3

import random
from jogador import Explorador, Navegador, Piloto, Engenheiro, Mensageiro, Mergulhador
from carta import CartaTesouro, CartaEnchente, CartaSacoAreia, CartaAlagamento, CartaHelicoptero, CartaTempestade
from terreno import Terreno, TerrenoTesouro, TerrenoTesouroFogo, TerrenoTesouroOceano, TerrenoTesouroTerra, TerrenoTesouroVento, PortoDosTolos
from tabuleiro import Tabuleiro
#from recebeInput import RecebeInput
from mostrador import Mostrador

from browser import document

dificuldades = ["normal", "elite", "lendario"]

terrenos_neutros = [
        ('PORTAO_COBRE', '45aU3nf'),
        ('PORTAO_BRONZE', 'BL6lB7H'),
        ('VALE_TENEBROSO', 'OZE1myn'),
        ('PORTAO_OURO', 'J6ow4jR'),
        ('PORTAO_PRATA', 'v0g7eGm'),
        ('PORTAO_FERRO', 'yKU6ngz'),
        ('ATALAIA', 'sdJ4W5O'),
        ('OBSERVATORIO', 'E9MflTP'),
        ('PANTANO_BRUMAS', 'NDioDZg'),
        ('ROCHA_FANTASMA', 'TCmLjeT'),
        ('PENEDO_BALDIO', 'MvN7kTU'),
        ('BOSQUE_CARMESIM', 'Uni02EK'),
        ('DUNAS_ENGANO', 'cG5UYCf'),
        ('PONTE_SUSPENSA', 'GC8V8CQ'),
        ('LAGOA_PERDIDA', '7o1qq10')
        ]

terrenos_terra = [('TEMPLO_LUA', 'J160xpm'), ('TEMPLO_SOL', 'O0OSVFt')]
terrenos_vento = [('JARDIM_SUSSUROS', 'pjVcyoy'), ('JARDIM_UIVOS', 'ZNuPWqZ')]
terrenos_fogo = [('CAVERNA_LAVA', '2j1IAyf'), ('CAVERNA_SOMBRAS', 'b4xtltc')]
terrenos_oceano = [('PALACIO_CORAL', 'tLDbzd2'), ('PALACIO_MARES', 'rYxQaTa')]

aventureiros = ['explorador',
                'mergulhador',
                'piloto',
                'navegador',
                'engenheiro',
                'mensageiro'
                ]

tesouros = ['terra', 'fogo', 'vento', 'oceano']

class Ilha:
    def __init__(self, dificuldade, numero_jogadores):
        self.mostrador = Mostrador()
        # 24 cartas terreno
        self.terrenos_neutros = [Terreno(nome, url) for nome, url in terrenos_neutros]

        self.porto = PortoDosTolos('CU3TLYh')
        self.terrenos_terra = [TerrenoTesouro(nome, url, 'terra') for nome, url in terrenos_terra]
        self.terrenos_vento = [TerrenoTesouro(nome, url, 'vento') for nome, url in terrenos_vento]
        self.terrenos_fogo = [TerrenoTesouro(nome, url, 'fogo') for nome, url in terrenos_fogo]
        self.terrenos_oceano = [TerrenoTesouro(nome, url, 'oceano') for nome, url in terrenos_oceano]
        self.terrenos = self.terrenos_fogo + \
                self.terrenos_terra + \
                self.terrenos_oceano + \
                self.terrenos_vento + \
                self.terrenos_neutros + \
                [self.porto]

        # 24 cartas alagamento, uma para cada terreno e baralhar
        self.cartas_alagamento = [CartaAlagamento(terreno) for terreno in self.terrenos]
        # 28 cartas tesouro
        self.cartas_tesouro = []
        self.numero_jogadores = numero_jogadores
        # 5 cartas de cada tesouro
        for tesouro in tesouros:
            for _ in range(5):
                self.cartas_tesouro.append(CartaTesouro(tesouro))
        # 3 fuga de helicoptero
        for _ in range(3):
            self.cartas_tesouro.append(CartaHelicoptero())
        # 2 cartas saco de areia
        for _ in range(2):
            self.cartas_tesouro.append(CartaSacoAreia())
        # gerar aleatoriamente os aventureiros dependendo no numero de jogadores
        self.aventureiros = []

        random.shuffle(self.terrenos)
        random.shuffle(self.cartas_alagamento)
        random.shuffle(self.cartas_tesouro)
        self.tabuleiro = Tabuleiro(self.terrenos)

        # mostra tabuleiro no browser
        self.mostrador.desenha_tabuleiro(self.terrenos)

        #self.recebeInput = RecebeInput(self.tabuleiro, self.aventureiros)

        # não tem tempestade no início
        self.tem_tempestade = False
        self.tesouros = []

        # definir nível de enchente
        if dificuldade == "normal":
            self.nivel_enchente = 2
        elif dificuldade == "elite":
            self.nivel_enchente = 3
        elif dificuldade == "lendario":
            self.nivel_enchente = 4
        else:
            self.nivel_enchente = 1

    def setup(self):
        for tipo_aventureiro in random.sample(aventureiros, self.numero_jogadores):
            if tipo_aventureiro == 'explorador':
                self.aventureiros.append(Explorador(self))
            elif tipo_aventureiro == 'mergulhador':
                self.aventureiros.append(Mergulhador(self))
            elif tipo_aventureiro == 'navegador':
                self.aventureiros.append(Navegador(self))
            elif tipo_aventureiro == 'piloto':
                self.aventureiros.append(Piloto(self))
            elif tipo_aventureiro == 'engenheiro':
                self.aventureiros.append(Engenheiro(self))
            elif tipo_aventureiro == 'mensageiro':
                self.aventureiros.append(Mensageiro(self))
            else:
                raise ValueError('Aventureiro sinistro')

        self.mostrador.desenha_jogadores(self.aventureiros)

        #print("Aventureiros:", self.aventureiros)
        # distribuir 2 cartas tesouro a cada Jogador
        for aventureiro in self.aventureiros:
            while aventureiro.numero_mao() < 2:
                # compra carta do baralho de tesouros
                carta_tesouro = self.cartas_tesouro.pop()
                aventureiro.comprar_carta(carta_tesouro)
                #print(aventureiro.__class__.__name__ + " comprou " + str(carta_tesouro))
        # adiciona enchente agora apenas
        for _ in range(3):
            self.cartas_tesouro.append(CartaEnchente())
            self.cartas_tesouro.append(CartaTempestade())
        # baralha outra vez mas com as cartas de enchente
        random.shuffle(self.cartas_tesouro)

        self.tesouros_coletados = 0


    def start(self):

        while True:
            break
            for aventureiro in self.aventureiros:
                numero_de_jogadas = 2 if self.tem_tempestade else 3
                for _ in range(numero_de_jogadas):
                    self.recebeInput.jogada(aventureiro)
                    pass

                # comprar carta de tesouro
                for _ in range(2):
                    carta = self.cartas_tesouro.pop()
                    if isinstance(carta, CartaEnchente):
                        self.nivel_enchente += 1
                        print("Enchente!")
                    elif isinstance(carta, CartaTempestade):
                        self.tempestade = True
                        print("Tempestade!")
                    else:
                        aventureiro.comprar_carta(carta)

                # define o número de cartas de alagamento compradas nesta ronda
                numero_de_alagamento = self.nivel_enchente + 1 if self.tem_tempestade else self.nivel_enchente
                print(self.cartas_alagamento)
                for _ in range(numero_de_alagamento):
                    self.cartas_alagamento.pop().terreno.alagar()

    def termina_tempestade(self):
        self.tem_tempestade = False
        print("Tempestade terminou!")

    def simulate(self):
        self.tabuleiro.printer()
        a = self.aventureiros[0]
        #import numpy as np
        #print(np.array(self.tabuleiro.disposicao))
        #print(a.posicao)
        #a.mover("right")
        #a.obter_tesouro()
        #print(a.posicao)
        #a.mover("right")
        #print(a.posicao)
        #terreno = self.tabuleiro.disposicao[a.posicao[0]][a.posicao[1]]
        #print(terreno, terreno.estado)
        #a.obter_tesouro()
        #a.mao = []
        #print(a.mao)
        #a.mao = [CartaTesouro("vento") for _ in range(5)]
        #print(a.mao)
        #a.obter_tesouro()
        #print(a.mao)
        #a.obter_tesouro()
        #a.mover("right")
        #print(a.posicao)
        #a.mover("right")
        #print(a.posicao)
        #terreno = self.tabuleiro.disposicao[a.posicao[0] + 1][a.posicao[1]]
        #print(terreno, terreno.estado)
        #terreno.alagar()
        #print(terreno, terreno.estado)
        #a.drenar("down")
        #print(terreno, terreno.estado)
        #terreno.alagar()
        #print(terreno, terreno.estado)
        #a.mover("down")
        #print(a.posicao)
        #a.mover("up")
        #print(a.posicao)
        #terreno.alagar()
        #print(terreno, terreno.estado)
        #a.mover("down")

"""
class TestJogo(unittest.TestCase):
    def test_jogo_setup(self):
        jogo = Jogo("normal", 4)
        jogo.setup()

        self.assertEqual(len(jogo.aventureiros), 4)
        for aventureiro in jogo.aventureiros:
            self.assertTrue(
                isinstance(
                    aventureiro,
                    (Explorador, Navegador, Piloto, Engenheiro, Mensageiro, Mergulhador),
                )
            )
            self.assertEqual(aventureiro.numero_mao(2), 2)

        for aventureiro in jogo.aventureiros:
            self.assertEqual(aventureiro.numero_mao(), 2)

        expected_treasure_cards = 28 - 2 * 4 # 28 cartas menos 2 de cada jogador
        self.assertEqual(len(jogo.cartas_tesouro), expected_treasure_cards)

        enchente_count = sum(1 for card in jogo.cartas_tesouro if isinstance(card, CartaEnchente))
        self.assertGreaterEqual(enchente_count, 3)
"""

if __name__ == '__main__':
    jogo = Jogo("normal", 4)
    jogo.setup()
    jogo.start()
