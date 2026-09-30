def construir(pares, indice, criar):
    g = criar(len(indice))
    repetidas = 0
    for u, v in pares:
        antes = g.tamanho()
        g.inserir_aresta(indice[u], indice[v])
        if g.tamanho() == antes:
            repetidas += 1
    return g, repetidas
