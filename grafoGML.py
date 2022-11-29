import igraph as ig
import matplotlib.pyplot as plt

def EntMatriz():
    grafo = ig.Graph()
    grafo = ig.load("entrada.gml")
    
    print("Grafo importado com sucesso")

    print(grafo.vcount(), "vertices")
    print(grafo.ecount(), "arestas")
    
    return grafo

def SaiMatriz(grafo):
    grafo.save("saida.gml")

    print("Grafo exportado com sucesso")
    print(grafo.vcount(), "vertices")
    print(grafo.ecount(), "arestas")

    return None

SaiMatriz(EntMatriz())