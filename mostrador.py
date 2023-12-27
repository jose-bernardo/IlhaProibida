from browser import document

class Mostrador:
    def __init__(self):
        document.body.style.backgroundImage = "url('https://i.imgur.com/gVHmY2v.jpg')"
        document.body.style.backgroundSize = "cover"

    def desenha_tabuleiro(self, terrenos):
        disposicao = (0, 2, 6, 12, 18, 22, 24)
        container = document.getElementById("jogo")
        for i in range(len(disposicao) - 1):
            container_div = document.createElement('div')
            container_div.style.display = 'flex'
            container_div.style.justifyContent = 'center'
            container_div.style.alignItems = 'center'
            for terreno in terrenos[disposicao[i]:disposicao[i+1]]:
                img = document.createElement("img")
                img.src = "https://i.imgur.com/" + terreno.url + ".png"
                img.title = f"{terreno}"
                img.style.width = "120px"  # Adjust the width as needed
                img.style.height = "120px"  # Adjust the height as needed
                img.style.padding = '4px'
                container_div.appendChild(img)
            container.appendChild(container_div)
        document.body.appendChild(container_div)

    def desenha_jogadores(self, jogadores):
        container = document.getElementById("jogo")
        for i, jogador in enumerate(jogadores):
            img = document.createElement("img")

            # Set the absolute position of the image
            img.src = "https://i.imgur.com/" + jogador.url + ".png"
            img.id = f"{jogador}"
            img.title = f"{jogador}"
            img.style.width = "50px"
            img.style.height = "50px"
            img.style.position = 'absolute'
            img.style.left = f'{458 + i*30}px' 
            img.style.top = '140px'
            container.appendChild(img)
