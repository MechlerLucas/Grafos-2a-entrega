import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ManipulacaoGrafo():
    def __init__(self,tipoGrafo):
        self.tipoGrafo = tipoGrafo
        if(tipoGrafo == 1):
            self.G = nx.DiGraph()
        else:
            self.G = nx.MultiGraph() 

    def add_vertice(self,v):
        self.G.add_node(v)

    def add_aresta(self,v1,v2):
        self.G.add_edge(v1,v2)
    
    def remove_aresta(self, v1, v2):
        self.G.remove_edge(v1,v2)

    def add_ponderacao_aresta(self,v1,v2,weight):
        if(self.tipoGrafo == 1):
            self.G[v1][v2]["weight"]= weight
        else:
            self.G[v1][v2][0]["weight"]= weight

    def add_rotulacao_aresta(self,v1,v2,label):
        if(self.tipoGrafo == 1):
            self.G[v1][v2]["label"] = label
        else:
            self.G[v1][v2][0]["label"] = label
    
    def add_ponderacao_vertice(self,v,weight):
        self.G.nodes[v]["weight"] = weight
    
    def verifica_existencia_vertice(self,v):
        return self.G.has_node(v)
    
    def verifica_existencia_aresta(self,v1,v2):
        return self.G.has_edge(v1,v2)
    
    def verifica_adjacencia_vertices(self,v1, v2):
        if(self.tipoGrafo == 1):
            return True if v1 in list(self.G.successors(v2)) else False
        else:
            return True if v1 in list(self.G.neighbors(v2)) else False
    
    def verifica_adjacencia_arestas(self,a1,a2):
        if(a1 != a2 and self.verifica_existencia_aresta(a1[0],a1[1]) and self.verifica_existencia_aresta(a2[0],a2[1])):
            if(self.tipoGrafo == 1):
                return a1[0] == a2[0]
            else:
                return a1[0] == a2[0] or a1[1] == a2[1] or a1[0] == a2[1] or a2[0] == a1[1]
        else:
            return False
        
    def quantidade_aresta(self):
        return self.G.number_of_edges()

    def quantidade_vertices(self):
        return self.G.number_of_nodes()

    def verifica_grafo_completo(self):
        return nx.is_connected(self.G)
    
    def verifica_grafo_vazio(self):
        return nx.is_empty(self.G)
    
    def print_matriz_adjacencia(self):
        print(pd.DataFrame(nx.adjacency_matrix(self.G).toarray(), columns=self.G.nodes(), index=self.G.nodes()))
    
    def print_lista_adjacencia(self):
        if(self.tipoGrafo == 1):
            for v in self.G.nodes():
                print(f'{v} - {list(self.G.successors(v))}')
        else:
            for v in self.G.nodes():
                print(f'{v} - {list(self.G.neighbors(v))}')

    def exportar_grafo(self,nomeArq):
        nx.write_gml(self.G, nomeArq)

    def importar_grafo(self):
        self.G = nx.read_gml("entrada.gml", label = 'id')

    def draw(self):
        nx.draw_networkx(self.G)
        plt.show()