import sys
from pathlib import Path

from grafo.construcao import construir
from grafo.conferencia import conferir
from grafo.leitura import indexar, ler_pares
from grafo.lista import GrafoLista

# uso: python -m grafo.pipeline [arquivo]   (padrão: dados/exemplo.edges)
caminho = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("dados/exemplo.edges")

pares, relatorio = ler_pares(caminho)
indice = indexar(pares)
g, repetidas = construir(pares, indice, GrafoLista)

# separa as repetições: mesmo arco u->v de novo (duplicata) ou v->u depois de u->v (recíproco)
vistos = set()
duplicatas = reciprocos = 0
for u, v in pares:
    if (u, v) in vistos:
        duplicatas += 1
    elif (v, u) in vistos:
        reciprocos += 1
    vistos.add((u, v))

print(relatorio)
print({"repetidas": repetidas, "duplicatas": duplicatas, "reciprocos": reciprocos})
print(conferir(g))
