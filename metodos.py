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
def Naive(grafo, aresta):
    aux = grafo.copy()
    aux.delete_edges(aresta)

    if (len(aux.clusters()) > len(grafo.clusters())):
        return True
    else:
        return False

#Metodo de Tarjan
def Tarjan(grafo, aresta):
    
    aux = grafo.copy() #Faz uma copia do grafo para evitar erros

    pilha = []
    i = 0 #Variável "i" que será utilizada para a inicialização
    for e in aux.es:
        if i == 0: #Na primeira "passada" do for, para a inicialização do primeiro vértice, raiz da busca
            aux.delete_edges(e) #deleta o vértice do grafo aux
        for x in aux.vs:
            testa = len(aux.neighbors(x)) #olha quantos vizinhos o vértice tem
            if testa > 1: #caso tenha mais de um, deleta a aresta atual
                aux.delete_edges(e)                                                                    
        i = i + 1
    for e in aux.es:
        pilha.append(e.tuple) #faz o empilhamento


    if(len(pilha)>0):
        if(pilha[len(pilha)-1] == aresta):
            return True
        else:
            return False
    
    return None

#Metodo de Fleury
#op = qual metodo será usado para identificar ponte, 0 = tarjan e 1 = naive
def Fleury(grafo, op):
    warnings.filterwarnings("ignore")
    #--------------------------------------------------#
    #Verifica se o grafo é eulericano

    graus = grafo.degree()
    listaVertices = grafo.vs.indices

    #Pega lista de arestas
    listaArestas = []
    for e in grafo.es:
        listaArestas.append(e.tuple)
    
    for i in graus:
        if not ((i % 2 == 0) and (len(grafo.clusters()) == 1)):
            print("Grafo sem caminho euleriano (graus impares ou não conexo)")
            return 0
    print("Grafo euleriano")
    Info(grafo)
    if op == 0:
        print("Identificando pontes por Tarjan")
    if op == 1:
        print("Identificando pontes por Naive")
    #--------------------------------------------------#
    inicio = time.time() #Inicio da variável de tempo, para comparação
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
        arestaRetirada = []

        if  len(qtdn) > 1:
            for k in qtdn:

                if op == 0:
                    if not Tarjan(aux, (vi, k)):
                        arestaRetirada = (vi, k)
                        J = k
                        break

                if op == 1:
                    if not Naive(aux, (vi, k)):
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

    fim = time.time()
    print("%10.3f segundos gastos"%(fim-inicio))
    return Tour

#Criador aleatorio de grafos
def Aleatorio(nodos):
    random.seed()
    grafoRand = ig.Graph.Erdos_Renyi(n=nodos, p = 0.9, directed=False, loops=False)
    return grafoRand


def TestesRand(tipoPonte):

    grafo =  Aleatorio(10)
    op = 0
    inicio = time.time() #Inicio da variável de tempo, para comparação
    while op != 1:
        while True:
            try:
                aux = Fleury(grafo, tipoPonte)
                if aux == 0:
                    grafo =  Aleatorio(10)
                    op = 0
                else:
                    Info(grafo)
                    print("Tour euleriano", *aux, sep=";")
                    op = 1
                    fim = time.time()
                    print("%10.3f segundos gastos para procura"%(fim-inicio))
                    break
            except KeyboardInterrupt:
                fim = time.time()
                print ("%10.3f de busca sem sucesso"%(fim-inicio))
                op = 0
                return
            
        
        
        
        
        
        


#print("Tour Euleriano", *Fleury(ImportaArq('fleuryN.gml'),1), sep = ", ")


TestesRand(0)