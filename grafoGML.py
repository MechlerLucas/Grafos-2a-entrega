import igraph as ig
import warnings
import networkx as nx

#import de grafo em arquivo GML para objeto grafo
def ImportaArq(nomeArq):
    warnings.filterwarnings("ignore")
    grafo = ig.Graph()
    grafo = ig.load(nomeArq)
    
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