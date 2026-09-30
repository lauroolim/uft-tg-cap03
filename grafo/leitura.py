def ler_pares(caminho):
    """Lê "u v" por linha (colunas extras, como timestamp, são ignoradas)."""
    pares = []
    relatorio = {"linhas": 0, "ignoradas": 0, "lacos": 0}
    with open(caminho, encoding="utf-8") as arq:
        for linha in arq:
            relatorio["linhas"] += 1
            campos = linha.split()
            if len(campos) < 2 or campos[0].startswith("#"):
                relatorio["ignoradas"] += 1
                continue
            u, v = campos[0], campos[1]
            if u == v:
                relatorio["lacos"] += 1
                continue
            pares.append((u, v))
    return pares, relatorio


def indexar(pares):
    indice = {}
    for u, v in pares:
        for r in (u, v):
            if r not in indice:
                indice[r] = len(indice)
    return indice
