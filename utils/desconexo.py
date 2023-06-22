def is_desconexo(grafo):
    visitados = set()

    def dfs(v):
        visitados.add(v)
        for vizinho in range(1, grafo.vertices + 1):
            if grafo.grafo[v - 1][vizinho - 1] > 0 and vizinho not in visitados:
                dfs(vizinho)

    componentes_conexas = 0

    for vertice in range(1, grafo.vertices + 1):
        if vertice not in visitados:
            componentes_conexas += 1
            dfs(vertice)

    return componentes_conexas > 1
