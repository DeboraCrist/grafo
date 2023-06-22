class Grafo:
    def __init__(self, vertices, direcionado=True):
        self.vertices = vertices
        self.direcionado = direcionado
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]
        self.num_arestas = 0
        self.letras = []

    def adiciona_aresta(self, u, v):
        self.grafo[u - 1][v - 1] += 1
        if not self.direcionado:
            self.grafo[v - 1][u - 1] += 1
        self.num_arestas += 1

    def grau_vertice(self, vertice):
        vertice_idx = vertice - 1
        grau = 0

        for i in range(self.vertices):
            if self.grafo[vertice_idx][i] > 0:
                grau += self.grafo[vertice_idx][i]  # Outgoing edges
            if self.grafo[i][vertice_idx] > 0 and i != vertice_idx:
                grau += self.grafo[i][vertice_idx]  # Incoming edges

        return grau
