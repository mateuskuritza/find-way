import cv2
import matplotlib.pyplot as plt
import numpy as np

def to_binary_matrix(image_path, fator_reducao = 10, invert_color_path = True):
    # Carregar a imagem
    imagem = cv2.imread(image_path)

    # Converter para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar binarização (thresholding)
    type = cv2.THRESH_BINARY_INV if invert_color_path else cv2.THRESH_BINARY
    _, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, type)

    # Converter a imagem binária para uma matriz binária
    matriz_binaria = imagem_binaria // 255

    matriz_reduzida = cv2.resize(matriz_binaria, (matriz_binaria.shape[1] // fator_reducao, matriz_binaria.shape[0] // fator_reducao), interpolation=cv2.INTER_AREA)

    return 1 - matriz_reduzida # Inverter os valores para que 0 represente caminho e 1 represente parede

def show_binary_matrix(matriz_binaria):
    # Visualizar a matriz binária
    plt.imshow(matriz_binaria, cmap='gray')  # 'gray' mapeia os valores 0 para preto e 1 para branco
    plt.title('Visualização do Labirinto')
    plt.axis('off')  # Desativa os eixos para uma visualização mais limpa
    plt.show()



    # Definir a função para cortar o espaço em branco ao redor da imagem
def cortar_espacos_brancos(matriz):
    # Encontrar as linhas onde o primeiro e o último caminho ocorrem
    linhas_com_caminho = np.where(matriz == 0)[0]
    primeira_linha, ultima_linha = linhas_com_caminho[0], linhas_com_caminho[-1]

    # Encontrar as colunas onde o primeiro e o último caminho ocorrem
    colunas_com_caminho = np.where(matriz == 0)[1]
    primeira_coluna, ultima_coluna = colunas_com_caminho[0], colunas_com_caminho[-1]

    # Cortar a matriz para remover o espaço em branco
    matriz_cortada = matriz[primeira_linha:ultima_linha+1, primeira_coluna:ultima_coluna+1]
    
    return matriz_cortada