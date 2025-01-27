import itertools
import time

# Função para ler a matriz de adjacência a partir de um arquivo
def read_matrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            matrix.append(list(map(int, line.strip().split())))
    return matrix

# Função para calcular o custo de um caminho
def calcular_custo(caminho, matriz):
    custo = 0
    for i in range(len(caminho) - 1):
        custo += matriz[caminho[i]][caminho[i + 1]]
    custo += matriz[caminho[-1]][caminho[0]]  # Retorno ao ponto inicial
    return custo

# Função do algoritmo de força bruta com tempo limite
def força_bruta_com_tempo_limite(matriz, tempo_limite):
    n = len(matriz)
    vertices = list(range(1, n))  # Exclui o vértice 0 (inicial)
    melhores_custo = float('inf')
    melhor_caminho = []
    melhor_custo_momentaneo = None
    vertices_visitados = 0  # Contador para os vértices visitados
    start_time = time.perf_counter()  # Usar perf_counter para melhor precisão

    for permutacao in itertools.permutations(vertices):
        current_time = time.perf_counter()
        if current_time - start_time > tempo_limite:  # Verifica se o tempo limite foi atingido
            break  # Interrompe a execução se o tempo limite for excedido

        caminho = [0] + list(permutacao)  # Adiciona o vértice inicial (0)
        custo = calcular_custo(caminho, matriz)

        # Se o custo atual for menor, atualiza os valores
        if custo < melhores_custo:
            melhores_custo = custo
            melhor_caminho = caminho

        # Atualiza o melhor custo momentâneo
        melhor_custo_momentaneo = melhores_custo

        # Atualiza o número de vértices visitados
        vertices_visitados += 1

    return melhores_custo, melhor_caminho, vertices_visitados, melhor_custo_momentaneo, time.perf_counter() - start_time

# Função para exibir o tempo de execução
def medir_tempo_execucao(func, *args):
    start_time = time.perf_counter()  # Usar perf_counter para melhor precisão
    resultado = func(*args)   # Chama a função com os parâmetros fornecidos
    end_time = time.perf_counter()    # Armazena o tempo final
    tempo_execucao = end_time - start_time  # Calcula o tempo de execução
    return resultado, tempo_execucao  # Retorna o resultado e o tempo de execução

# Exemplo de uso
if __name__ == "__main__":
    # Caminho para o arquivo a ser lido
    file_path = input("Digite o caminho para o arquivo da matriz: ").strip()

    try:
        # Ler a matriz do arquivo
        matrix = read_matrix(file_path)

        # Definir o tempo limite em segundos
        tempo_limite = float(input("Digite o tempo limite para execução em segundos: ").strip())

        # Executar algoritmo de força bruta com tempo limite
        print("\nExecutando algoritmo de força bruta com tempo limite...")
        custo, caminho, vertices_visitados, melhor_custo_momentaneo, tempo_execucao = força_bruta_com_tempo_limite(matrix, tempo_limite)

        print(f"Caminho ótimo (Força Bruta): {caminho}")
        print(f"Custo ótimo (Força Bruta): {custo}")
        print(f"Melhor custo momentâneo: {melhor_custo_momentaneo}")
        print(f"Número de vértices visitados até o momento: {vertices_visitados}")
        print(f"Tempo de execução (Força Bruta): {tempo_execucao:.8f} segundos")

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

