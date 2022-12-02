import numpy as np
import pandas as pd
from grafoGML import*
import igraph as ig
import random
import time
import warnings

#Exibe informações do grafo
def Info(grafo):
    warnings.filterwarnings("ignore")
    print("Pontes:        ",grafo.bridges())
    print("Componentes:   ",len(grafo.clusters()))
    print("Lista vertices:",grafo.vs.indices)
    listaArestas = []
    for e in grafo.es:
        listaArestas.append(e.tuple)
    print("---------------------------")
    print(*listaArestas, sep = "\n")
    print("---------------------------")

#Metodo de Naive para aresta separada
def NaiveAresta(grafo, aresta):
    
    aux = grafo.copy()

    Info(grafo)

    print("Deletando: ",aresta)
    aux.delete_edges(aresta)

    print("Qtd nova:    ",len(aux.clusters()))
    print("Qtd inicial: ",len(grafo.clusters()))

    if (len(aux.clusters()) > len(grafo.clusters())):
        print(aresta, "é uma ponte")
        return True
    else:
        return False



#Metodo de Tarjan
def Tarjan(grafo):
    inicio = time.time()


    fim = time.time()

    print("%10.3f segundos gastos"%(fim-inicio))
    return None

#Metodo de Fleury
def Fleury(grafo):
    Info(grafo)
    listaAdjacentes = grafo.get_adjlist(mode = "all")
    print(*listaAdjacentes, sep = "\n")
    graus = grafo.degree()
    print(graus)
    for i in graus:
        if graus[i] % 2 or graus[i] == 1:
            print("Grafo sem caminho euleriano")
            quit()
    
    listaVertices = []
    for e in grafo.vs:
        listaVertices.append(e.tuple)

    listaArestas = []
    for e in grafo.es:
        listaArestas.append(e.tuple)

    #--------------------------------------------------#
    i = 0
    Tour = []

    aux = grafo.copy()
    v0 = listaVertices[0]
    Tour.append[v0]
    
    while not bool(listaArestas):
        vi = Tour[i]

        if len(aux.neighbors(vi)) > 1:
            for j in aux.neighbors(vi):
                if NaiveAresta(aux, (vi, j)):
                    arestaRetirada = (vi, j)
                    J = j
                    break
        else:
            J = aux.neighbors(vi)
            arestaRetirada = (vi, J)

        aux.delete_edges(arestaRetirada)
        Tour.append(arestaRetirada)
        vj = J
        Tour.append(vj)

        aresta = "("+vi+", "+vj+")"
        listaArestas.remove(aresta)
    return Tour


#Criador aleatorio de grafos
def Aleatorio(nodos):
    random.seed()
    grafoRand = ig.Graph.Erdos_Renyi(n=nodos, p = 0.2, directed=False, loops=True)
    return grafoRand

Info(ImportaArq('entrada.gml'))

NaiveAresta(ImportaArq('entrada.gml'),(4, 5))

#Fleury(ImportaArq('entrada.gml'))
#Naive(ImportaArq('entrada.gml'))
#Info(Aleatorio(1000))