import random


def gerar(n, densidade, fabrica):
    # semente fixa (42) para matriz e lista receberem as mesmas arestas
    random.seed(42)
    g = fabrica(n)
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < densidade:
                g.inserir_aresta(u, v)
    return g
