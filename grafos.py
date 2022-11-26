import csv
import numpy
import networkx as nx

def Matrix():
    reader = csv.reader(open("grafo.csv"), delimiter=";")
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

def EdgeList():

    reader = csv.reader(open("grafoEdgeList.csv"), delimiter=";")
    matrizEdge = numpy.array(list(reader))

    print(matrizEdge)

    grafo = nx.DiGraph()

    # Preenche os vertices do grafo a partir da lista de arestas
    for k in range(0, len(matrizEdge)):
        grafo.add_node(matrizEdge[k][0])

    # Preenche as arestas do grafo a partir da matriz de adjacencia
    for i in range(0, len(matrizEdge)):
                print(matrizEdge[i][0], matrizEdge[i][1])
                grafo.add_edge(matrizEdge[i][0], matrizEdge[i][1])
    print(grafo.adj)

    return grafo


graf = EdgeList()