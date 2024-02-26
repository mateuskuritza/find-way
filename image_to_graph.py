import process_image
import matplotlib.pyplot as plt

# Reimportar a biblioteca networkx
import networkx as nx

def detectar_vizinhos(matriz, x, y):
    # Movimentos possíveis: cima, baixo, esquerda, direita
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    vizinhos = []
    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        # Verificar se a nova posição está dentro dos limites da matriz e é um caminho (1)
        if 0 <= nx < matriz.shape[0] and 0 <= ny < matriz.shape[1] and matriz[nx, ny] == 1:
            vizinhos.append((nx, ny))
    return vizinhos

def eh_intersecao_ou_extremidade(matriz, x, y):
    vizinhos = detectar_vizinhos(matriz, x, y)
    # Uma interseção tem mais de dois vizinhos, uma extremidade tem apenas um
    return len(vizinhos) != 2

def encontrar_nos(matriz):
    nos = set()
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i, j] == 1:
                if eh_intersecao_ou_extremidade(matriz, i, j):
                    nos.add((i, j))
    return nos

def handle(image_path, fator_reducao = 2, invert_color_path = True):
    matriz_reduzida = process_image.to_binary_matrix(image_path, fator_reducao, invert_color_path)
    matriz_cortada = process_image.cortar_espacos_brancos(matriz_reduzida)
    # process_image.show_binary_matrix(matriz_reduzida)

    # Encontrar nós na matriz binária reduzida do labirinto
    nos = encontrar_nos(matriz_cortada)

    # Agora vamos criar o grafo com base nos nós encontrados
    G = nx.Graph()
    G.add_nodes_from(nos)

    # Adicionando arestas
    for no in nos:
        vizinhos = detectar_vizinhos(matriz_cortada, *no)
        for vizinho in vizinhos:
            if vizinho in nos:
                G.add_edge(no, vizinho)

    return G, matriz_cortada



def show(graph, nos):
    # Agora temos o grafo com nós e arestas. Vamos verificar quantos nós e arestas temos.
    num_nos = graph.number_of_nodes()
    num_arestas = graph.number_of_edges()
    num_nos, num_arestas
    posicoes = {no: (no[1], -no[0]) for no in nos}  # Inverter o eixo y para corresponder à orientação da imagem
    # posicoes = {no: (no[0], no[1]) for no in nos}  # Inverter o eixo y para corresponder à orientação da imagem
    # Desenhar o grafo
    plt.figure(figsize=(8, 8))  # Tamanho da figura
    nx.draw(graph, posicoes, node_size=10, with_labels=False)
    plt.title('Grafo do Labirinto')
    plt.show()

    print(f"O grafo tem {num_nos} nós e {num_arestas} arestas.")


