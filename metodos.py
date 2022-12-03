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
def Tarjan(grafo, aresta):
    inicio = time.time() #Inicio da variável de tempo, para comparação
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

    fim = time.time()
    if(len(pilha)>0):
        if(pilha[len(pilha)-1] == aresta):
            print(aresta, "e uma ponte")
            #print("%10.3f segundos gastos"%(fim-inicio))
            return True
        else:
            print(aresta, "NAO e uma ponte")
            #print("%10.3f segundos gastos"%(fim-inicio))
            return False
    #print("%10.3f segundos gastos"%(fim-inicio))
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


''' Teste ainda não funcional, tendo problemas com mais de 1000 
vértices, não sei se a lógica que eu implementei é a mesma esperada
desde o inicio!!!'''
def TestaRandomico():
    print("-------------------------------------------------")
    aux = Aleatorio(100)
    listaArestasRandom = []
    listaArestasAux = []
    inicio = time.time()
    i = 0
    aux1 = False
    for e in aux.es:
        listaArestasRandom.append(e.tuple)
        listaArestasAux.append(False)
        print(e.tuple)


    print("------------------teste-------------------------------")
    for e in aux.es:
        if aux1 == False:
            v1 = random.randrange(0,99)
            try:
                if Tarjan(aux,(listaArestasRandom[v1])) == True:
                    aux1 = True
            except:
                v1 = random.randrange(0,99)
                if Tarjan(aux,(listaArestasRandom[v1])) == True:
                    aux1 = True
        i = i+1
                
    fim = time.time()
    print("%10.3f segundos gastos"%(fim-inicio))



