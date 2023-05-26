class Grafo:
    def __init__(self, vertices, direcionado=True):
        self.vertices = vertices
        self.direcionado = direcionado
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u - 1][v - 1] += 1
        if not self.direcionado:
            self.grafo[v - 1][u - 1] += 1

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])


vertices = int(input("Digite o número de vértices do grafo: "))
g = Grafo(vertices)

arestas = int(input("Digite o número de arestas: "))
for i in range(arestas):
    print(f"Digite as informações da aresta {i + 1}:")
    u = int(input("Vértice de origem: "))
    v = int(input("Vértice de destino: "))
    g.adiciona_aresta(u, v)

g.mostra_matriz()

# vertice = 5

# [0, 1, 0, 0, 0]
# [0, 0, 1, 1, 0]
# [0, 0, 0, 1, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]