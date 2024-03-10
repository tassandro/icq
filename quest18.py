import numpy as np

def trace(matrix):
    """
    Calcula o traço de uma matriz complexa.

    Args:
    matrix (numpy.array): Matriz complexa.

    Returns:
    complex: Traço da matriz.
    """
    return np.trace(matrix)

# Exemplo de uso:

# Obter entrada do usuário para a matriz complexa
rows = int(input("Digite o número de linhas da matriz: "))
cols = int(input("Digite o número de colunas da matriz: "))

print("Digite os elementos da matriz complexa separados por espaços ou linhas:")
matrix = np.array([[complex(input(f"Elemento ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)])

# Verifica se a matriz é quadrada (número de linhas igual ao número de colunas)
if rows != cols:
    print("Erro: O traço só pode ser calculado para uma matriz quadrada.")
else:
    # Calcula o traço
    result = trace(matrix)
    print("\nTraço da matriz:", result)
