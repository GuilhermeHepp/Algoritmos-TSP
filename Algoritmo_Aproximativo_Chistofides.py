import time
from itertools import combinations
import heapq

def read_matrix(file_path):
    """Lê a matriz de adjacência de um arquivo."""
    try:
        with open(file_path, 'r') as file:
            matrix = []
            for line in file:
                matrix.append(list(map(int, line.split())))
            return matrix
    except Exception as e:
        raise ValueError(f"Erro ao ler o arquivo: {e}")

def christofides(matrix, time_limit, result_holder):
    n = len(matrix)
    best_cost = float('inf')
    best_path = []
    start_time = time.perf_counter()  # Use perf_counter para melhor precisão

    # 1. Cria a árvore geradora mínima usando o algoritmo de Prim
    mst = prim_mst(matrix)

    # 2. Encontre os vértices com grau ímpar no MST
    odd_vertices = find_odd_degree_vertices(mst)

    # 3. Encontre a combinação perfeita mínima (emparelhamento mínimo)
    min_weight_perfect_matching = find_minimum_weight_perfect_matching(odd_vertices, matrix)

    # 4. Crie o multigrafo
    multigraph = create_multigraph(mst, min_weight_perfect_matching)

    # 5. Encontre o circuito euleriano no multigrafo
    eulerian_circuit = find_eulerian_circuit(multigraph)

    # 6. Converta o circuito euleriano em um caminho hamiltoniano
    hamiltonian_path = convert_to_hamiltonian(eulerian_circuit)

    # Calcule o custo do caminho hamiltoniano
    cost = sum(matrix[hamiltonian_path[i]][hamiltonian_path[i+1]] for i in range(n-1))

    # Verifique o tempo limite
    elapsed_time = time.perf_counter() - start_time  # Tempo de execução
    if elapsed_time > time_limit:
        result_holder["cost"], result_holder["path"], result_holder["time"] = best_cost, best_path, elapsed_time
        return  # Interrompe se o tempo limite for atingido

    result_holder["cost"], result_holder["path"], result_holder["time"] = cost, hamiltonian_path, elapsed_time

def run_christofides(matrix, time_limit):
    result_holder = {"cost": None, "path": None, "time": None}
    christofides(matrix, time_limit, result_holder)
    return result_holder

def prim_mst(matrix):
    """Implementação do algoritmo de Prim para encontrar a Árvore Geradora Mínima (MST)."""
    n = len(matrix)
    mst = {i: [] for i in range(n)}
    visited = [False] * n
    min_heap = [(0, 0, -1)]  # (custo, vértice, pai)

    while min_heap:
        cost, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            mst[parent].append(u)
            mst[u].append(parent)

        for v in range(n):
            if not visited[v]:
                heapq.heappush(min_heap, (matrix[u][v], v, u))

    return mst

def find_odd_degree_vertices(mst):
    """Encontre os vértices com grau ímpar na árvore geradora mínima."""
    return [v for v in mst if len(mst[v]) % 2 == 1]

def find_minimum_weight_perfect_matching(odd_vertices, matrix):
    """Encontre a combinação perfeita mínima usando um algoritmo de emparelhamento mínimo."""
    # Aqui, utilizamos uma abordagem simplificada para encontrar o emparelhamento perfeito
    matching = []
    for i in range(0, len(odd_vertices), 2):
        matching.append((odd_vertices[i], odd_vertices[i + 1]))
    return matching

def create_multigraph(mst, matching):
    """Crie um multigrafo a partir da árvore geradora mínima e do emparelhamento perfeito."""
    multigraph = {v: set() for v in mst}
    for u in mst:
        for v in mst[u]:
            multigraph[u].add(v)
            multigraph[v].add(u)

    for u, v in matching:
        multigraph[u].add(v)
        multigraph[v].add(u)
    
    return multigraph

def find_eulerian_circuit(multigraph):
    """Encontre o circuito euleriano em um multigrafo usando o algoritmo de Hierholzer."""
    circuit = []
    stack = [list(multigraph.keys())[0]]

    while stack:
        u = stack[-1]
        if multigraph[u]:
            v = multigraph[u].pop()
            stack.append(v)
            multigraph[v].remove(u)
        else:
            circuit.append(u)
            stack.pop()

    return circuit

def convert_to_hamiltonian(circuit):
    """Converte um circuito euleriano em um caminho hamiltoniano removendo os vértices repetidos."""
    visited = set()
    hamiltonian_path = []

    for v in circuit:
        if v not in visited:
            visited.add(v)
            hamiltonian_path.append(v)

    return hamiltonian_path

if __name__ == "__main__":
    # Caminho para o arquivo a ser lido
    file_path = input("Digite o caminho para o arquivo da matriz: ").strip()
    time_limit = float(input("Digite o tempo limite em segundos: ").strip())

    try:
        # Ler a matriz do arquivo
        matrix = read_matrix(file_path)
        print("Matriz de adjacência lida:")
        for row in matrix:
            print(row)

        # Executar o algoritmo de Christofides
        print("\nExecutando algoritmo de Christofides...")
        christofides_result = run_christofides(matrix, time_limit)
        print(f"Caminho aproximado (Christofides): {christofides_result['path']}")
        print(f"Custo aproximado (Christofides): {christofides_result['cost']}")
        print(f"Tempo de execução (Christofides): {christofides_result['time']:.8f} segundos")

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
