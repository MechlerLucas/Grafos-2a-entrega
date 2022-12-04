import ManipulacaoGrafo as m
import igraph as ig
from metodos import Fleury
import os

def main():
    clear = lambda: os.system('cls')
    grafo = criarGrafo()
    opcao = -1
    clear()

    while opcao != 0:
        opcao = menu()
        if opcao == 1:
            v = input("Digite o rótulo do vértice: ")
            grafo.add_vertice(v)
        elif opcao == 2:
            v1 = input("Digite o vértice 1: ")
            v2 = input("Digite o vértice 2: ")
            grafo.add_aresta(v1,v2)
        elif opcao == 3:
            v1 = input("Digite o vértice 1: ")
            v2 = input("Digite o vértice 2: ")
            grafo.remove_aresta(v1,v2)
        elif opcao == 4:
            v1 = input("Digite o vértice 1: ")
            v2 = input("Digite o vértice 2: ")
            peso = input("Digite o peso:")
            grafo.add_ponderacao_aresta(v1,v2,peso)
        elif opcao == 5:
            v1 = input("Digite o vértice 1: ")
            v2 = input("Digite o vértice 2: ")
            label = input("Digite o rótulo: ")
            grafo.add_rotulacao_aresta(v1,v2,label)
        elif opcao == 6:
            v = input("Digite o vértice: ")
            peso = input("Digite o peso: ")
            grafo.add_ponderacao_vertice(v,peso)
        elif opcao == 7:
            v = input("Digite o vértice: ")
            if(grafo.verifica_existencia_vertice(v)):
                print(f'O vértice {v} existe.')
            else:
                print(f'O vértice {v} não existe.')
        elif opcao == 8:
            v1 = input("Digite o vértice 1: ")
            v2 = input("Digite o vértice 2: ")
            if(grafo.verifica_existencia_aresta(v1,v2)):
                print(f'A aresta ({v1},{v2}) existe.')
            else:
                print(f'A aresta ({v1},{v2}) não existe.')
        elif opcao == 9:
            v1 = input("Digite o vértice 1: ")
            v2 = input("Digite o vértice 2: ")
            if(grafo.verifica_adjacencia_vertices(v1,v2)):
                print(f'O vértice {v1} é adjacente ao vértice {v2}.')
            else:
                print(f'O vértice {v1} não é adjacente ao vértice {v2}.')
        elif opcao == 10:
            print("Aresta 1:")
            a1 = input("Digite os vértices da aresta 1: Ex: a,b ").split(",")
            print()
            print("Aresta 2:")
            a2 = input("Digite os vértices da aresta 2: Ex: a,b ").split(",")
            if(grafo.verifica_adjacencia_arestas(a1,a2)):
                print(f'A aresta ({a1[0]},{a1[1]}) é adjacente à aresta ({a2[0]},{a2[1]}).')
            else:
                print(f'A aresta ({a1[0]},{a1[1]}) não é adjacente à aresta ({a2[0]},{a2[1]}).')
        elif opcao == 11:
            qtdAresta = grafo.quantidade_aresta()
            print(f'O grafo possui {qtdAresta} arestas.')
        elif opcao == 12:
            qtdVertices = grafo.quantidade_vertices()
            print(f'O grafo possui {qtdVertices} vértices.')
        elif opcao == 13:
            if(grafo.verifica_grafo_completo()):
                print(f'O grafo é completo.')
            else:
                print(f'O grafo não é completo.')
        elif opcao == 14:
            if(grafo.verifica_grafo_vazio()):
                print(f'O grafo é vazio.')
            else:
                print(f'O grafo não é vazio.')
        elif opcao == 15:
            grafo.print_matriz_adjacencia()
        elif opcao == 16:
            grafo.print_lista_adjacencia()
        elif opcao == 17:
            grafo.draw()
        elif opcao == 18:
            nomeArq = input("Digite o nome do arquivo: Ex: saida.gml: ")
            grafo.exportar_grafo(nomeArq)
        elif opcao == 19:
            metodo = input("Escolha o método:\n0:Naive\n1:Tarjan\n\n")
            Fleury(ig.Graph.from_networkx(grafo.G),metodo)
        os.system("pause")
        clear()



def menu():
    print("************MENU**************")
    opcao = input("""
                      1: Adicionar Vértice
                      2: Adicionar Aresta
                      3: Remover Aresta
                      4: Ponderar Aresta
                      5: Rotular Aresta
                      6: Ponderar Vértice
                      7: Verificar Existência Vértice
                      8: Verificar Existência Aresta
                      9: Verificar Adjacência Vertices
                     10: Verificar Adjacência Arestas 
                     11: Quantidade de Arestas
                     12: Quantidade de Vertices
                     13: Verificar se Grafo é completo
                     14: Verificar se Grafo é vazio
                     15: Representação da Matriz de Adjacência
                     16: Representação da Lista de Adjacência
                     17: Representação Gráfica do Grafo
                     18: Exportar Grafo (.gml)
                     19: Encontrar Caminho Euleriano
                      0: Sair

                      Escolha uma opção: """)

    return int(opcao)


def criarGrafo():
    print("Selecione uma opção para gerar o grafo:")
    tipoGrafo = input("0: Direcionado\n1: Não Direcionado\n\n")
    grafo = m.ManipulacaoGrafo(tipoGrafo)

    importarGrafo = int(input("Deseja importar grafo?\n1:Sim\n2:Não\n\n"))

    if(importarGrafo==1):
        nomeArquivo = input("Digite o nome do arquivo: Ex: entrada.gml: ")
        grafo.importar_grafo()

    return grafo
 

if __name__ == "__main__":
    main()