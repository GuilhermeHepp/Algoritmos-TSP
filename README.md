# Algoritmos-TSP
# Problema do Caixeiro Viajante (TSP)

O **Problema do Caixeiro Viajante** (TSP - Travelling Salesman Problem) é um dos problemas mais estudados nas áreas de Otimização Combinatória e Teoria dos Grafos, devido à sua relevância teórica e prática. O objetivo do TSP é encontrar o menor caminho que percorre um conjunto de cidades exatamente uma vez, retornando ao ponto de origem. Este é um problema NP-difícil, o que significa que, até o momento, não existe um algoritmo eficiente capaz de resolvê-lo em tempo polinomial.

Este projeto explora dois tipos de abordagens para resolver o TSP: **algoritmos exatos** e **algoritmos aproximativos**.

## Algoritmos Exatos

### Algoritmo de Força Bruta
O algoritmo de força bruta resolve o TSP enumerando todas as possíveis permutações dos vértices de um grafo, calculando o custo de cada percurso e selecionando o menor. Para um grafo com \(n\) vértices, o número de permutações é dado por \((n-1)!\), o que gera uma complexidade de \(O(n!)\). Embora simples, este método se torna impraticável para instâncias maiores devido à explosão combinatória.

#### Execuções
- O projeto inclui execuções do algoritmo de força bruta, apresentando dados coletados sobre o desempenho com diferentes configurações de caches.
  
## Algoritmos Aproximativos

Dada a complexidade do TSP, a resolução exata pode ser inviável para instâncias grandes, já que o tempo de execução pode se estender por longos períodos. Por isso, algoritmos aproximativos são utilizados para encontrar soluções que sejam próximas do ótimo, mas com um tempo de execução polinomial.

### Algoritmo de Christofides
O Algoritmo de Christofides é uma solução aproximativa que garante uma solução no máximo 1,5 vezes o custo da solução ótima, sendo amplamente utilizado em grafos completos e ponderados. O algoritmo é composto por seis etapas principais:
1. Criação de uma árvore geradora mínima.
2. Identificação de vértices com grau ímpar.
3. Cálculo da mínima combinação perfeita.
4. Formação de um multigrafo.
5. Geração de um circuito Euleriano.
6. Conversão do circuito Euleriano em um circuito Hamiltoniano.

## Objetivo do Projeto
Este projeto visa implementar e analisar diferentes abordagens para o TSP, comparando a eficácia dos algoritmos exatos e aproximativos, e avaliando o desempenho em termos de tempo de execução e qualidade das soluções obtidas.
