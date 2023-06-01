import json

class Grafo:
    def __init__(self, vertices, direcionado=True):
        self.vertices = vertices
        self.direcionado = direcionado
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u - 1][v - 1] += 1
        if not self.direcionado:
            self.grafo[v - 1][u - 1] += 1
"""
    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])
"""    
def tipo_de_grafo(grafo):
    vertices = set()
    multiarestas = set()
    lacos = set()

    for u in range(grafo.vertices):
        for v in range(grafo.vertices):
            if grafo.grafo[u][v] > 0:
                aresta = (u+1, v+1)
                vertices.add(u+1)
                vertices.add(v+1)

                if u == v:
                    lacos.add(u+1)

                if grafo.direcionado:
                    if grafo.grafo[v][u] > 0 or grafo.grafo[u][v] > 1:
                        multiarestas.add(aresta)
                else:
                    if grafo.grafo[v][u] > 1 or grafo.grafo[u][v] > 1:
                        multiarestas.add(aresta)

    if multiarestas and lacos:
        print("O grafo é um pseudografo.")
    elif multiarestas and not lacos:
        print("O grafo é um multigrafo.")
    elif not multiarestas and not lacos:
        print("O grafo é um grafo simples.")
    else:
        print("Não foi possível determinar o tipo do grafo.")

def carregar_grafos(arquivo):
    with open(arquivo, 'r') as f:
        try:
            data = json.load(f)
            graphs = data["graphs"]

            for graph in graphs:
                print(f"\nAnalisando Grafo {graph['id']}")

                vertices = len(graph["vertices"])
                g = Grafo(vertices)

                for edge in graph["edges"]:
                    u = graph["vertices"].index(edge[0]) + 1
                    v = graph["vertices"].index(edge[1]) + 1
                    g.adiciona_aresta(u, v)
                
                #g.mostra_matriz()
                tipo_de_grafo(g)
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar o arquivo JSON: {str(e)}")

def main():
    entrada = input("Digite o comando 'grafos carregar arquivo.json': ")
    partes = entrada.split(" ")
    
    if len(partes) != 3 or partes[0] != "grafos" or partes[1] != "carregar":
        print("Comando inválido.")
        return

    arquivo = partes[2]
    carregar_grafos(arquivo)

if __name__ == '__main__':
    main()
