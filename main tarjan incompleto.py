import numpy as np
import pandas as pd
from grafoGML import*
import igraph as ig
import matplotlib.pyplot as plt

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

'''def Tarjan(grafo):
    aux = grafo
    aux_v = -345
    aux_v1 = -345
    aux_v2 = -1
    contador = 0 
    z = 0
    #print(aux.es.select)
    pilha = []
    i = 0
    teste = True
    for e in aux.es:
        #print(str(aux_v1))
        if i == 0:
            aux_v1 = e.tuple[1] 
            print(e.tuple)
            contador = contador + 1
            
        for x in aux.es:
            anterior = x.tuple[0]
            if  x.tuple[0] == aux_v1:
                #pilha.append(x.tuple)
                print(x.tuple)
                contador = contador + 1
                aux_v2 = x.tuple[0]
                aux_v1 = x.tuple[1]
                teste = False

            
        aux_v1 = 1
        i = i+1


    return None'''


def Tarjan(grafo,vertice):
    aux = grafo
    contador = 0
    pilha = []
    aux_contador = -1
    pilha.append(vertice)
    raiz = vertice
    rodou_aqui = False
    tamanho = 0
    aux_tamanho = 0
    for e in aux.es:
        aux_contador = contador
        rodou_aqui = False
        aux_tamanho = tamanho
        if (e.tuple[0] == vertice) and (e.tuple[1] == pilha[len(pilha)-2] or raiz in pilha ):
            print(str(e.tuple))
            vertice = e.tuple[1]
            if(vertice not in pilha):
                pilha.append(vertice)
            contador = contador + 1
            rodou_aqui = True
            tamanho = len(pilha)
        elif (aux_contador == contador and aux_tamanho == tamanho):
            #print("testa "+ str(vertice))
            vertice = pilha[len(pilha)-2]
            #print("uepa: "+str(pilha[len(pilha)-2]))
            aux_tamanho = tamanho
        #vertice = 1
    

    print("-----------------PILHA---------------------")
    for j in pilha:
        print(j)
            
            
   
        testa = -1
        





'''
    aux = grafo
    contador = 0 
    z = 0
    pilha = []
    i = 0
    teste = True
    auxv = node
    for e in aux.es:
        #print(e.tuple[1])
        if e.tuple[0] == auxv:
            auxv = e.tuple[1]
            #print(e.tuple)
            #print(auxv)
            pilha.append(auxv)
    for j in pilha:
        print(j)

            #print("Achou disgraça" + str(e.tuple))'''


#Naive(ImportaArq())
print(Tarjan(ImportaArq(),0))
