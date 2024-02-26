import sys
import networkx as nx
import numpy as np

# Função do algoritmo de Dijkstra
def calculate(graph, source, target):
    return nx.dijkstra_path(graph, source, target)
    
    

def encontrar_no_mais_proximo(posicoes, ponto_x, ponto_y):
    # Inverter o ponto_y devido à inversão do eixo y para correspondência com a matriz binária
    ponto = (ponto_x, ponto_y)
    no_mais_proximo = None
    distancia_minima = float('inf')
    for no, pos in posicoes.items():
        distancia = np.sqrt((pos[0] - ponto[0]) ** 2 + (pos[1] - ponto[1]) ** 2)
        if distancia < distancia_minima:
            no_mais_proximo = no
            distancia_minima = distancia
    return no_mais_proximo
