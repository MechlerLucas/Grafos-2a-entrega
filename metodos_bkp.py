import numpy as np
import pandas as pd
from grafoGML import*
import igraph as ig
import random
import time
import warnings

#Exibe informações do grafo
def Info(grafo):
    print("\n\n------------Infos------------")
    warnings.filterwarnings("ignore")
    print("Pontes:        ",grafo.bridges())
    print("Componentes:   ",len(grafo.clusters()))
    print("Lista vertices:",grafo.vs.indices)

    listaArestas = []
    for e in grafo.es:
        listaArestas.append(e.tuple)
    print("---------------------------")
    print("Arestas:", *listaArestas, sep = "\n")
    graus = grafo.degree()
    print("Graus: ",graus)
    print("---------------------------")
    print("------------Infos------------\n\n")
#Metodo de Naive para aresta separada
def NaiveAresta(grafo, aresta):
    aux = grafo.copy()
    aux.delete_edges(aresta)

    if (len(aux.clusters()) > len(grafo.clusters())):
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
    #--------------------------------------------------#
    #Verifica se o grafo é eulericano
    graus = grafo.degree()
    for i in graus:
        if graus[i] % 2 or graus[i] == 1 or len(grafo.clusters()) > 1:
            print("Grafo sem caminho euleriano\nGrafo com graus impares ou não conexo")
            quit()
    print("Grafo euleriano")
    listaVertices = grafo.vs.indices

    #Pega lista de arestas e exibe
    listaArestas = []
    for e in grafo.es:
        listaArestas.append(e.tuple)
    #--------------------------------------------------#
    i = len(listaArestas)-1
    Tour = []
    
    aux = grafo.copy()
    v0 = listaVertices[random.randint(0,len(listaVertices)-1)]
    Tour.append(v0)
    vj = v0
    while bool(listaArestas):
        
        vi = vj
        J = 0
        qtdn = aux.neighbors(vi,mode='all')

        if  len(qtdn) > 1:
            for k in qtdn:

                if not NaiveAresta(aux, (vi, k)):
                    arestaRetirada = (vi, k)
                    J = k
                    break

        else:
            J = qtdn[0]
            arestaRetirada = (vi, J)

        aux.delete_edges(arestaRetirada)
        
        listaArestasi = []
        for e in aux.es:
            listaArestasi.append(e.tuple)
        Tour.append(arestaRetirada)
        vj = J
        Tour.append(vj)

        listaArestas.pop(i)
        i -= 1
    return Tour

#Criador aleatorio de grafos
def Aleatorio(nodos):
    random.seed()
    grafoRand = ig.Graph.Erdos_Renyi(n=nodos, p = 0.2, directed=False, loops=True)
    return grafoRand

print("Tour Euleriano", *Fleury(ImportaArq('fleury.gml')), sep = ", ")