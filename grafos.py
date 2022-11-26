import csv
import numpy
import networkx as nx

reader = csv.reader(open("grafo.csv"), delimiter=";")
matrizAdj = numpy.array(list(reader))

print(matrizAdj)

grafo = nx.MultiGraph()

# Preenche os vertices do grafo a partir da primeira coluna da matriz de adjacencia
for k in range(1, len(matrizAdj)):
    grafo.add_node(matrizAdj[k][0])


# Preenche as arestas do grafo a partir da matriz de adjacencia
for i in range(1, len(matrizAdj)):
    for j in range(1, len(matrizAdj)):
        if matrizAdj[i][j] == '1':
            print(i, j)
            grafo.add_edge(matrizAdj[i][0], matrizAdj[0][j])
print(grafo.adj)
