
def encontrar_vertices_inalcancaveis(partida, loaded_graphs):
    vertices_inalcancaveis_total = []

    for i, graph in enumerate(loaded_graphs):
        if partida in graph.letras:
            vertice_idx = graph.letras.index(partida) + 1
            visitados = set()
    
            def dfs(v):
                visitados.add(v)
                for vizinho in range(1, graph.vertices + 1):
                    if graph.grafo[v - 1][vizinho - 1] > 0 and vizinho not in visitados:
                        dfs(vizinho)
                    if graph.grafo[vizinho - 1][v - 1] > 0 and vizinho not in visitados:
                        dfs(vizinho)

            dfs(vertice_idx)
            
            vertices_inalcancaveis = [graph.letras[v - 1] for v in range(1, graph.vertices + 1) if v not in visitados]
            print(f"Vértices inalcancaveis a partir do vértice {partida} no grafo de ID={i + 1}:")
            print(vertices_inalcancaveis)
            vertices_inalcancaveis_total.extend(vertices_inalcancaveis)

    return  vertices_inalcancaveis_total