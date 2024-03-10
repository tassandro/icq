import numpy as np

def is_hermitian(matrix):
    """
    Verifica se uma matriz é hermitiana.

    Args:
    matrix (numpy.array): Matriz complexa.

    Returns:
    bool: True se a matriz é hermitiana, False caso contrário.
    """
    # Calcula a adjunta da matriz
    adjoint = np.conj(matrix).T

    # Verifica se a matriz é igual à sua adjunta
    return np.allclose(matrix, adjoint)

# Exemplo de uso:

# Obter entrada do usuário para a matriz complexa
rows = int(input("Digite o número de linhas da matriz: "))
cols = int(input("Digite o número de colunas da matriz: "))

print("Digite os elementos da matriz complexa separados por espaços ou linhas:")
matrix = np.array([[complex(input(f"Elemento ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)])

# Verifica se a matriz é hermitiana
result = is_hermitian(matrix)
if result:
    print("\nA matriz é hermitiana.")
else:
    print("\nA matriz não é hermitiana.")
