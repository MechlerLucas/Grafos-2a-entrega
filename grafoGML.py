import igraph as ig
import matplotlib.pyplot as plt

#import de grafo em arquivo GML para objeto grafo
def ImportaArq():
    grafo = ig.Graph()
    grafo = ig.load("entrada.gml")
    
    print("Grafo importado com sucesso")
    print(grafo.vcount(), "vertices")
    print(grafo.ecount(), "arestas")
    
    return grafo

#export de grafo em objeto para arquivo GML
def ExportaArq(grafo):
    grafo.save("saida.gml")

    print("Grafo exportado com sucesso")
    print(grafo.vcount(), "vertices")
    print(grafo.ecount(), "arestas")

    return None