import numpy as np
import pandas as pd
from grafoGML import*
import igraph as ig
import random
import time

#Exibe informações do grafo
def Info(grafo):
    print("Pontes:        ",grafo.bridges())
    print("Componentes:   ",len(grafo.connected_components()))
    print("Lista vertices:",grafo.vs.indices)
    listaArestas = []
    for e in grafo.es:
        listaArestas.append(e.tuple)
    print("---------------------------")
    print(*listaArestas, sep = "\n")
    print("---------------------------")

#Metodo de Naive
def Naive(grafo):
    inicio = time.time()
    aux = grafo
    Info(grafo)

    listaArestas = []
    for e in grafo.es:
        listaArestas.append(e.tuple)

    inicial_componentes = grafo.clusters()
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
    
    fim = time.time()

    print("%10.3f segundos gastos"%(fim-inicio))
    return None

#Metodo de Tarjan
def Tarjan(grafo):
    inicio = time.time()


    fim = time.time()

    print("%10.3f segundos gastos"%(fim-inicio))
    return None

#Criador aleatorio de grafos
def Aleatorio(nodos):
    random.seed()
    grafoRand = ig.Graph.Erdos_Renyi(n=nodos, p = 0.2, directed=False, loops=True)
    return grafoRand

#Info(Aleatorio(10))
Naive(ImportaArq('entrada.gml'))