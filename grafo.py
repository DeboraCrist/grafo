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
        return "pseudografo"
    elif multiarestas and not lacos:
        return "multigrafo"
    elif not multiarestas and not lacos:
        return "grafo simples"
    else:
        return "indefinido"

def carregar_grafos(arquivo):
    with open(arquivo, 'r') as f:
        try:
            data = json.load(f)
            graphs = data["graphs"]
            loaded_graphs = []

            for graph in graphs:
                vertices = len(graph["vertices"])
                g = Grafo(vertices)

                for edge in graph["edges"]:
                    u = graph["vertices"].index(edge[0]) + 1
                    v = graph["vertices"].index(edge[1]) + 1
                    g.adiciona_aresta(u, v)

                loaded_graphs.append(g)

            return loaded_graphs

        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar o arquivo JSON: {str(e)}")

def main():
    entrada = input("Digite o comando: ")
    partes = entrada.split(" ")

    if len(partes) == 3 and partes[0] == "grafos" and partes[1] == "carregar":
        arquivo = partes[2]
        loaded_graphs = carregar_grafos(arquivo)

        if loaded_graphs is not None:
            print("Grafos carregados com sucesso!")
            pseudografos = []  

            while True:
                comando = input("Digite o comando: ")
                if comando == "grafos multigrafos":
                    for i, graph in enumerate(loaded_graphs):
                        tipo = tipo_de_grafo(graph)
                        if tipo == "multigrafo":
                            print(f"Grafo {i + 1} é um multigrafo.")
                elif comando == "grafos pseudografos":
                    for i, graph in enumerate(loaded_graphs):
                        tipo = tipo_de_grafo(graph)
                        if tipo == "pseudografo":
                            pseudografos.append(str(i + 1))
                    if pseudografos:
                        print(f"Os grafos {', '.join(pseudografos)} são pseudografos.")
                    else:
                        print("Nenhum pseudografo encontrado.")
                elif comando == "grafos sair":
                    break 
                else:
                    print("Comando inválido.")
    else:
        print("Comando inválido.")

if __name__ == '__main__':
    main()
