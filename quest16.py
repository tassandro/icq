import numpy as np

def complex_matrix_operations(matrix):
    """
    Encontra a transposta, conjugada e a adjunta (dagger) de uma matriz complexa.

    Args:
    matrix (numpy.array): Matriz complexa.

    Returns:
    tuple: Uma tupla contendo a transposta, a conjugada e a adjunta (dagger) da matriz.
    """
    transpose = np.transpose(matrix)
    conjugate = np.conj(matrix)
    dagger = np.transpose(conjugate)
    return transpose, conjugate, dagger

# Exemplo de uso:

# Obter entrada do usuário para a matriz complexa
rows = int(input("Digite o número de linhas da matriz: "))
cols = int(input("Digite o número de colunas da matriz: "))

print("Digite os elementos da matriz complexa separados por espaços ou linhas:")
matrix = np.array([[complex(input(f"Elemento ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)])

# Operações com a matriz
transpose, conjugate, dagger = complex_matrix_operations(matrix)

# Imprimir resultados
print("\nMatriz:")
print(matrix)
print("\nTransposta:")
print(transpose)
print("\nConjugada:")
print(conjugate)
print("\nAdjunta (Dagger):")
print(dagger)
