import numpy as np
import pandas as pd
from grafoGML import*
import igraph as ig


def Naive(grafo):

    aux = grafo
    #print(grafo.connected_components(mode='weak'))
    print("Pontes:        ",grafo.bridges())
    print("Componentes:   ",len(aux.clusters()))
    print("Lista vertices:",grafo.vs.indices)
    print("Lista arestas: ",grafo.es.indices)
    print("Lista conexões:",grafo.es.tuples)
    vertex_indices = range(grafo.ecount())
    for e in grafo.es:
        print(e.tuple)
    arestas = grafo.es.indices
    inicial_componentes = grafo.clusters()
    print("---------------------------")
    for i in range (grafo.ecount()):
        #print(arestas[i])
        #aux.delete_edges(arestas[i])
        print(aux.es.indices)
        print(vertex_indices[i])
#        if (len(aux.clusters()) < type(int(inicial_componentes))):
#            print(arestas[i], "é uma ponte")
#        else:
#            aux = grafo
    

    return None

def Tarjan(grafo):


    return None


Naive(ImportaArq())