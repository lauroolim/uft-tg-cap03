def conferir(g):
    n, m = g.ordem(), g.tamanho()
    graus = [g.grau(v) for v in g.vertices()]
    return {
        "n": n,
        "m": m,
        "soma_graus": sum(graus),
        "aperto_de_mao": sum(graus) == 2 * m,
        "isolados": graus.count(0),
        "densidade": 2 * m / (n * (n - 1)) if n > 1 else 0.0,
    }
