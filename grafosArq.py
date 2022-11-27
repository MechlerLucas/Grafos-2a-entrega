import csv
import numpy
import networkx as nx


####################################Entrada########################################

#Função de entrada por arquivo de matriz de adjacencia
def EntMatriz():
    reader = csv.reader(open("grafoMatrizAdj.csv"), delimiter=";")
    matrizAdj = numpy.array(list(reader))

#    print(matrizAdj)

    grafo = nx.DiGraph()

    # Preenche os vertices do grafo a partir da primeira coluna da matriz de adjacencia
    for k in range(1, len(matrizAdj)):
        grafo.add_node(matrizAdj[k][0])


    # Preenche as arestas do grafo a partir da matriz de adjacencia
    for i in range(0, len(matrizAdj)):
        for j in range(0, len(matrizAdj)):
            if matrizAdj[i][j] == '1':
#                print(i, j)
                grafo.add_edge(matrizAdj[i][0], matrizAdj[0][j])
#    print(grafo.adj)

    return grafo

#Função de entrada por arquivo de lista de adjacencia
def EntLista():

    reader = csv.reader(open("grafoListaAdj.csv"), delimiter=";")
    listaAdJ = numpy.array(list(reader),dtype="object")

    grafo = nx.DiGraph()

    # Preenche os vertices do grafo a partir da lista de arestas
    for k in range(0, len(listaAdJ)):
        for l in range(0, len(listaAdJ[k])):
            grafo.add_node(listaAdJ[k][l])

    # Preenche as arestas do grafo a partir da lista de arestas
    for i in range(0, len(listaAdJ)):
        for j in range(1, len(listaAdJ[i])):
            grafo.add_edge(listaAdJ[i][0], listaAdJ[i][j])
    print("\nVetor de adjacencia\n",grafo.adj)

    return grafo

####################################Saida##########################################

def SaiMatriz(grafo):

    #print(nx.adjacency_matrix(grafo))
    
    #print(nx.to_dict_of_lists(grafo))

#
    print(nx.attr_matrix(grafo,rc_order=['A','B','C','D','E']))
    matrizAdj = nx.attr_matrix(grafo,rc_order=['A','B','C','D','E'])
#    matriz = open('SaiMatriz.csv', 'w', newline='')    
    
#    for line in matrizAdj:
#        matriz.write(line)
#        matriz.write('\n')
    print (matrizAdj)

    return None


def SaiLista(grafo):
    print("\nLista de adjacencia")
    lista = open('SaiLista.csv', 'w', newline='')
    for line in nx.generate_adjlist(grafo, delimiter = ';'):
        print(line)
        lista.write(line)
        lista.write('\n')
    
    return None

#graf = EntLista()
#SaiLista(graf)

graf = EntMatriz()
SaiMatriz(graf)