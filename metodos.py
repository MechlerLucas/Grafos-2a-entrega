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
    print("\n\n------------Naive------------")
    aux = grafo.copy()
    print("Deletando: ",aresta)
    aux.delete_edges(aresta)

    print("Qtd nova:    ",len(aux.clusters()))
    print("Qtd inicial: ",len(grafo.clusters()))

    if (len(aux.clusters()) > len(grafo.clusters())):
        print(aresta, "é uma ponte")
        print("------------Naive------------")
        return True
    else:
        print(aresta, " não é uma ponte")
        print("------------Naive------------\n\n")
        return False



#Metodo de Tarjan
def Tarjan(grafo):
    inicio = time.time()


    fim = time.time()

    print("%10.3f segundos gastos"%(fim-inicio))
    return None

#Metodo de Fleury
def Fleury(grafo):
    #Info(grafo)
    print("\n\n------------Fleury-----------")
    #--------------------------------------------------#
    #Verifica se o grafo é eulericano
    graus = grafo.degree()
    for i in graus:
        if graus[i] % 2 or graus[i] == 1:
            print("Grafo sem caminho euleriano")
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

        print("Loop ",i)
        print("Tour =",*Tour, sep="")
        
        vi = vj
        J = 0

        print("vi =",vi )
        print("Vertice selecionado: ", vi)
        qtdn = aux.neighbors(vi,mode='all')
        print("Quantidade neib = ",len(qtdn))

        if  len(qtdn) > 1:
            print("\n\nAdjacentes:", *aux.neighbors(vi, mode='all'), sep=';')
            for k in qtdn:

                if not NaiveAresta(aux, (vi, k)):
                    arestaRetirada = (vi, k)
                    J = k
                    break

        else:
            J = qtdn[0]
            arestaRetirada = (vi, J)

        print("Deletando: ",arestaRetirada)

        aux.delete_edges(arestaRetirada)
        
        listaArestasi = []
        for e in aux.es:
            listaArestasi.append(e.tuple)
        print("---------------------------")
        print("Arestas:", *listaArestasi, sep = "; ")
        Tour.append(arestaRetirada)
        vj = J
        Tour.append(vj)
        print("VJ = ",vj,"\n---")

        listaArestas.pop(i)
        i -= 1
    print("------------Fleury-----------\n\n")
    return Tour

#Criador aleatorio de grafos
def Aleatorio(nodos):
    random.seed()
    grafoRand = ig.Graph.Erdos_Renyi(n=nodos, p = 0.2, directed=False, loops=True)
    return grafoRand


print("Tour de saida", *Fleury(ImportaArq('fleury.gml')), sep = ", ")


#Info(ImportaArq('entrada.gml'))

#NaiveAresta(ImportaArq('entrada.gml'),(4, 5))

#Fleury(ImportaArq('entrada.gml'))
#Naive(ImportaArq('entrada.gml'))
#Info(Aleatorio(1000))