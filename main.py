from entrada.carregar_grafos import carregar_grafos
from utils.completos import grafos_completos
from utils.desconexo import is_desconexo
from utils.tipo_de_grafo import tipo_de_grafo

def main():
    entrada = input("Digite o comando: ")
    partes = entrada.split(" ")

    if len(partes) == 3 and partes[0] == "grafos" and partes[1] == "carregar":
        arquivo = partes[2]
        loaded_graphs = carregar_grafos(arquivo)

        if loaded_graphs is not None:
            print("Grafos carregados com sucesso!")
            pseudografos = []
            disconnected_graphs = []

            for i, graph in enumerate(loaded_graphs):
                if is_desconexo(graph):
                    disconnected_graphs.append(str(i + 1))

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
                elif comando == "grafos desconexos":
                    if disconnected_graphs:
                        print(f"Os grafos {', '.join(disconnected_graphs)} são desconexos.")
                    else:
                        print("Nenhum grafo desconexo encontrado.")
                elif comando == "grafos completos":
                    grafos_completos(loaded_graphs)
                elif comando.startswith("grafos graus id="):
                    partes_comando = comando.split("=")
                    if len(partes_comando) == 2:
                        graph_id = int(partes_comando[1])
                        if 1 <= graph_id <= len(loaded_graphs):
                            graph = loaded_graphs[graph_id - 1]
                            print(f"Graus dos vértices do grafo de ID={graph_id}:")
                            for vertice in range(1, graph.vertices + 1):
                                grau = graph.grau_vertice(vertice)
                                letra = graph.letras[vertice - 1]
                                print(f"Vértice {letra}: Grau {grau}")
                        else:
                            print("ID do grafo inválido.")
                    else:
                        print("Comando inválido.")
                elif comando.startswith("grafos grau id="):
                    partes_comando = comando.split()
                    if len(partes_comando) == 4:
                        try:
                            graph_id = int(partes_comando[2][3:])
                            vertice = partes_comando[3].split("=")[1].strip('\"')
                            if 1 <= graph_id <= len(loaded_graphs):
                                graph = loaded_graphs[graph_id - 1]
                                try:
                                    vertice_idx = graph.letras.index(vertice) + 1
                                    grau = graph.grau_vertice(vertice_idx)
                                    letra = graph.letras[vertice_idx - 1]
                                    print(f"Vértice {letra} do grafo de ID={graph_id}: Grau {grau}")
                                except ValueError:
                                    print("Vértice não encontrado.")
                            else:
                                print("ID do grafo inválido.")
                        except ValueError:
                            print("ID do grafo inválido.")
                    else:
                        print("Comando inválido.")

                elif comando.startswith("grafos alcancaveis partida="):
                    partes_comando = comando.split("=")
                    if len(partes_comando) == 2:
                        partida = partes_comando[1].strip('\"')
                        vertices_alcancaveis_total = []

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

                                vertices_alcancaveis = [graph.letras[v - 1] for v in visitados]
                                print(f"Vértices alcançáveis a partir do vértice {partida} no grafo de ID={i + 1}:")
                                print(vertices_alcancaveis)
                                vertices_alcancaveis_total.extend(vertices_alcancaveis)
                        
                    else:
                        print("Comando inválido.")

                elif comando == "grafos sair":
                    print("Encerrando o programa...")
                    break
                else:
                    print("Comando inválido.")

    else:
        print("Comando inválido.")

if __name__ == "__main__":
    main()