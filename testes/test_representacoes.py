import pytest

from grafo.lista import GrafoLista
from grafo.matriz import GrafoMatriz

# Figura 3.1: a..f -> 0..5
ARESTAS = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]


@pytest.mark.parametrize("Classe", [GrafoMatriz, GrafoLista])
def test_grafo_exemplo(Classe):
    g = Classe(6)
    for u, v in ARESTAS:
        g.inserir_aresta(u, v)

    graus = [g.grau(v) for v in g.vertices()]
    assert g.ordem() == 6
    assert g.tamanho() == 8
    assert sorted(graus, reverse=True) == [4, 3, 3, 3, 2, 1]
    assert sum(graus) == 16 == 2 * g.tamanho()
