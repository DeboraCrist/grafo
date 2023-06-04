
from entrada.carregar_grafos import carregar_grafos
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
