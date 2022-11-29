import networkx as nx
import numpy as np
import pandas as pd
from grafosArq import *
import igraph as ig


def Naive(grafo):

    if nx.is_weakly_connected(grafo):
        print("é conected")
    else:
        print("não é")
    #print(grafo.nodes())
    #print(list(nx.bridges(grafo)))
    #for i in grafo.number_of_nodes():

    return None

def Tarjan(grafo):


    return None


Naive(EntLista())