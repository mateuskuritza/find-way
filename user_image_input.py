import matplotlib.pyplot as plt

# Função para capturar os cliques do mouse e retornar as coordenadas na imagem
def capturar_cliques(eventos, ax):
    cliques = []
    for evento in eventos:
        # Calcular as coordenadas na imagem
        x, y = int(evento[0]), int(evento[1])
        cliques.append((x, -y))
        ax.plot(x, y, 'ro')  # Marcar o ponto selecionado com um círculo vermelho
        plt.draw()  # Atualizar a imagem com os pontos marcados
    return cliques

def handle(matriz):
    # Exibir a imagem cortada
    test = plt.imshow(matriz, cmap='gray')
    plt.title('Clique para escolher a origem e o destino')
    plt.axis('on')  # Mantém os eixos para referência

    # Esperar o usuário clicar duas vezes para selecionar origem e destino
    eventos = plt.ginput(2, timeout=-1)  # timeout=-1 significa que vai esperar até que o usuário termine de clicar
    cliques = capturar_cliques(eventos, plt.gca())

    # Extrair origem e destino das coordenadas clicadas
    if len(cliques) == 2:
        origem_clique, destino_clique = cliques
    else:
        print("Dois pontos não foram selecionados.")

    plt.close()        
    return origem_clique, destino_clique
