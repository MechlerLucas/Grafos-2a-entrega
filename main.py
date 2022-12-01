import numpy as np
import pandas as pd
from grafoGML import*
import igraph as ig

def Info(grafo):
    print("Pontes:        ",grafo.bridges())
    print("Componentes:   ",len(grafo.clusters()))
    print("Lista vertices:",grafo.vs.indices)
    print("Lista arestas: ",grafo.es.indices)

def Naive(grafo):

    aux = grafo
    Info(grafo)
    listaArestas = []
    for e in grafo.es:
        listaArestas.append(e.tuple)
    
    inicial_componentes = grafo.clusters()
    print("---------------------------")
    print(*listaArestas, sep = "; ")
    print("---------------------------")
    
    i = 0
    for j in listaArestas:
        print("Deletando: ",j)
        aux.delete_edges(j)
        print("Qtd nova:    ",len(aux.clusters()))
        print("Qtd inicial: ",len(inicial_componentes))
        if (len(aux.clusters()) > len(inicial_componentes)):
            print(listaArestas[i], "é uma ponte")
            print("...")
        else:
            print("...")
        aux = grafo.copy()
        i += 1
    

    return None

def Tarjan(grafo):


    return None


Naive(ImportaArq('entrada.gml'))