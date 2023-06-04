import json

from grafo.grafo import Grafo

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

