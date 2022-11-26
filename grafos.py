import csv
import numpy
import networkx as nx

def EntMatriz():
    reader = csv.reader(open("grafoMatrizAdj.csv"), delimiter=";")
    matrizAdj = numpy.array(list(reader))

    print(matrizAdj)

    grafo = nx.DiGraph()

    # Preenche os vertices do grafo a partir da primeira coluna da matriz de adjacencia
    for k in range(1, len(matrizAdj)):
        grafo.add_node(matrizAdj[k][0])


    # Preenche as arestas do grafo a partir da matriz de adjacencia
    for i in range(0, len(matrizAdj)):
        for j in range(0, len(matrizAdj)):
            if matrizAdj[i][j] == '1':
                print(i, j)
                grafo.add_edge(matrizAdj[i][0], matrizAdj[0][j])
    print(grafo.adj)

    return grafo

def EntLista():

    reader = csv.reader(open("grafoListaAdj.csv"), delimiter=";")
    listaAdJ = numpy.array(list(reader))

    print(listaAdJ)

    grafo = nx.DiGraph()

    # Preenche os vertices do grafo a partir da lista de arestas
    for k in range(0, (listaAdJ)):
        grafo.add_node(listaAdJ[k][0])

    # Preenche as arestas do grafo a partir da lista de arestas
    for i in range(0, len(listaAdJ)):
                print(listaAdJ[i][0], listaAdJ[i][1])
                grafo.add_edge(listaAdJ[i][0], listaAdJ[i][1])
    print(grafo.adj)

    return grafo




graf = EntEdgeList()