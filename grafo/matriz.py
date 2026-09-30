from grafo.base import Grafo


class GrafoMatriz(Grafo):
    def __init__(self, n):
        self.n = n
        self.m = 0
        self.a = [[0] * n for _ in range(n)]

    def ordem(self):
        return self.n

    def tamanho(self):
        return self.m

    def vizinhos(self, v):
        # varre a linha inteira: Θ(n)
        return [w for w in range(self.n) if self.a[v][w]]

    def tem_aresta(self, u, v):
        return self.a[u][v] == 1

    def inserir_aresta(self, u, v):
        if u == v:
            raise ValueError("laço não é permitido")
        if self.a[u][v]:
            return
        self.a[u][v] = self.a[v][u] = 1
        self.m += 1
