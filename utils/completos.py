def grafos_completos(loaded_graphs):
    completos = [] 

    for i, graph in enumerate(loaded_graphs):
        num_vertices = graph.vertices
        num_arestas = graph.num_arestas

        if num_arestas == num_vertices * (num_vertices - 1) // 2:
            completos.append(str(i + 1))

    if completos:
        print(f"Os grafos {', '.join(completos)} são completos.")
    else:
        print("Nenhum grafo completo encontrado.")