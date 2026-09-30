import statistics
import time

from grafo.gerar_aleatorio import gerar
from grafo.lista import GrafoLista
from grafo.matriz import GrafoMatriz
from grafo.triangulos import contar_triangulos

N = 2000
DENSIDADES = [0.001, 0.05, 0.5]

print("| densidade | implementação | tempo mediano (s) | espaço (posições) | m |")
print("|---|---|---|---|---|")
for rho in DENSIDADES:
    for nome, fabrica in [("matriz", GrafoMatriz), ("lista", GrafoLista)]:
        g = gerar(N, rho, fabrica)
        m = g.tamanho()
        tempos = []
        for _ in range(3):
            t0 = time.perf_counter()
            contar_triangulos(g)
            tempos.append(time.perf_counter() - t0)
        espaco = N * N if nome == "matriz" else N + 2 * m
        print(f"| {rho} | {nome} | {statistics.median(tempos):.4f} | {espaco} | {m} |", flush=True)
