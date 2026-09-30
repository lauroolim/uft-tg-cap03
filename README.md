# Atividade 3.16 — Medir o efeito da representação

**Pergunta:** em `contar_triangulos`, a representação (matriz × lista de adjacência) muda o tempo gasto, e isso depende da densidade do grafo?

**Itens 1 e 2.** `GrafoMatriz` e `GrafoLista` foram implementadas do zero a partir da interface `Grafo`. O teste (`python -m pytest testes/`) monta o grafo da Figura 3.1 nas duas classes e confere n = 6, m = 8, graus (4,3,3,3,2,1) e soma dos graus 16 = 2m. Resultado: os 2 testes passaram.

**Item 3 (matriz de incidência de G − ce).** _A fazer à mão._

**Itens 4 e 5.** Os grafos aleatórios têm n = 2000 e semente 42, então as duas classes recebem as mesmas arestas. O tempo é a mediana de 3 execuções com `time.perf_counter`. O espaço é contado em posições: n² na matriz e n + 2m na lista.

| ρ | implementação | tempo mediano (s) | espaço (posições) | m |
|---|---|---|---|---|
| 0.001 | matriz | 0.2124 | 4000000 | 1910 |
| 0.001 | lista | 0.0008 | 5820 | 1910 |
| 0.05 | matriz | 6.5486 | 4000000 | 99819 |
| 0.05 | lista | 0.5916 | 201638 | 99819 |
| 0.5 | matriz | 123.8871 | 4000000 | 999109 |
| 0.5 | lista | 58.0456 | 2000218 | 999109 |

**Item 6 — análise.** A lista foi mais rápida nas três densidades: cerca de 265× em ρ = 0,001, 11× em ρ = 0,05 e 2× em ρ = 0,5. Pela Tabela 3.3, a matriz só leva vantagem em "u,v adjacentes?" (Θ(1)), e `contar_triangulos` usa essa operação uma vez por trio. O custo dominante é percorrer N(v), que custa Θ(n) na matriz e Θ(d(v)) na lista. Por isso o custo composto é Θ(n(n+m)) na matriz e O(n + Σd(v)²) na lista.

A ordem entre as duas não se inverteu, mas a vantagem da lista cai conforme a densidade cresce. Quando ρ → 1, d(v) → n, e as duas expressões tendem a n³. Em ρ = 0,05 a teoria prevê cerca de 10× (2·10⁸ contra 2·10⁷), o que bate com os 11× medidos. Houve duas diferenças:

- Em ρ = 0,5 a teoria prevê cerca de 1× e medimos 2×. A notação Θ esconde a constante: a matriz varre as 2000 posições da linha e depois percorre os cerca de 1000 vizinhos, enquanto a lista percorre só os cerca de 1000. Para testar, bastaria rodar com ρ próximo de 1 e ver se a razão cai.
- Em ρ = 0,001 a teoria prevê cerca de 700× e medimos 265×. O tempo da lista é tão pequeno que o custo fixo do laço em Python pesa mais. Para testar, bastaria variar n mantendo o grau médio fixo.

**Item 7 — dataset CollegeMsg (SNAP).** O arquivo é orientado (`origem destino timestamp`) e cada linha é uma mensagem. Carregamos com `python -m grafo.pipeline dados/CollegeMsg.txt`:

- 59835 linhas, 0 ignoradas e 0 laços.
- 45997 arestas repetidas:
  - 39539 são duplicatas verdadeiras (a mesma pessoa manda outra mensagem à mesma pessoa);
  - 6458 são arcos recíprocos (v→u depois de u→v).
- n = 1899, igual ao número de rótulos distintos do arquivo (não houve laços nem isolados).
- m = 13838 e ρ(G) ≈ 0,0077.

Com essa densidade, usaríamos a **lista de adjacência**. A matriz ocuparia cerca de 3,6 milhões de posições, contra 29575 da lista, e o grafo está na faixa em que a lista foi de 11× a 265× mais rápida.
