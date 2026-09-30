from grafo.base import Grafo


class GrafoLista(Grafo):
    def __init__(self, n):
        self.n = n
        self.m = 0
        self.adj = [set() for _ in range(n)]

    def ordem(self):
        return self.n

    def tamanho(self):
        return self.m

    def vizinhos(self, v):
        return self.adj[v]

    def tem_aresta(self, u, v):
        return v in self.adj[u]

    def inserir_aresta(self, u, v):
        if u == v:
            raise ValueError("laço não é permitido")
        if v in self.adj[u]:
            return
        self.adj[u].add(v)
        self.adj[v].add(u)
        self.m += 1

    def grau(self, v):
        return len(self.adj[v])  # O(1)
