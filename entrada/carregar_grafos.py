import json

from grafo.grafo import Grafo

def carregar_grafos(arquivo):
    with open(arquivo, "r") as f:
        try:
            data = json.load(f)
            graphs = data["graphs"]
            loaded_graphs = []

            for graph in graphs:
                vertices = graph["vertices"]
                vertices_indices = {v: i + 1 for i, v in enumerate(vertices)}
                g = Grafo(len(vertices))

                for edge in graph["edges"]:
                    u = vertices_indices[edge[0]]
                    v = vertices_indices[edge[1]]
                    g.adiciona_aresta(u, v)

                g.letras = vertices
                loaded_graphs.append(g)

            return loaded_graphs

        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar o arquivo JSON: {str(e)}")
            