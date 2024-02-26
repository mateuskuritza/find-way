import dijkstra
import process_image
import image_to_graph
import networkx as nx
import matplotlib.pyplot as plt
import math
import cv2
import user_image_input

FATOR_REDUCAO = 10
IMAGE = "cidade.png"
# LABIRINTO = "labirinto.webp"
# LABIRINTO = "cars.png"
# LABIRINTO = "grande_labirinto.png"
LABIRINTO = f"images/{IMAGE}"

INVERT_COLOR_PATH = False # Boolean

graph, matriz = image_to_graph.handle(image_path=LABIRINTO, fator_reducao=FATOR_REDUCAO, invert_color_path=INVERT_COLOR_PATH)

origin, destiny = user_image_input.handle(matriz)
# image_to_graph.show(graph, graph.nodes) 

# coordenadas_origem = (origin[0] // FATOR_REDUCAO, origin[1] // FATOR_REDUCAO)
# coordenadas_destino = (destiny[0] // FATOR_REDUCAO, destiny[1] // FATOR_REDUCAO)

# Encontrar nós mais próximos para as coordenadas de origem e destino
posicoes = {no: (no[1], -no[0]) for no in graph.nodes}
# posicoes = {no: (no[0], no[1]) for no in graph.nodes}
no_origem = dijkstra.encontrar_no_mais_proximo(posicoes, *origin)
no_destino = dijkstra.encontrar_no_mais_proximo(posicoes, *destiny)

caminho = dijkstra.calculate(graph, no_origem, no_destino)

# Desenhar o grafo
plt.figure(figsize=(8, 8))
nx.draw(graph, pos=posicoes, node_size=10, with_labels=False, node_color='lightblue')

# Desenhar o caminho do Dijkstra
caminho_posicoes = [posicoes[no] for no in caminho]
nx.draw_networkx_nodes(graph, pos=posicoes, nodelist=caminho, node_size=30, node_color='red')
nx.draw_networkx_edges(graph, pos=posicoes, edgelist=list(zip(caminho, caminho[1:])), edge_color='red', width=1)

plt.savefig(f"./out/dijkstra_{IMAGE}")
plt.show()

# TODO: Dar a opcao de além de selecionar ponto de origem, destino e pontos intermediarios?