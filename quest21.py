import numpy as np

def tensor_product(matrix1, matrix2):
    """
    Calcula o produto tensorial de duas matrizes complexas.

    Args:
    matrix1 (numpy.array): Primeira matriz complexa.
    matrix2 (numpy.array): Segunda matriz complexa.

    Returns:
    numpy.array: Matriz resultante do produto tensorial.
    """
    return np.kron(matrix1, matrix2)

# Exemplo de uso:

# Obter entrada do usuário para as matrizes complexas
rows1 = int(input("Digite o número de linhas da primeira matriz: "))
cols1 = int(input("Digite o número de colunas da primeira matriz: "))
rows2 = int(input("Digite o número de linhas da segunda matriz: "))
cols2 = int(input("Digite o número de colunas da segunda matriz: "))

print("Digite os elementos da primeira matriz complexa separados por espaços ou linhas:")
matrix1 = np.array([[complex(input(f"Elemento 1({i+1},{j+1}): ")) for j in range(cols1)] for i in range(rows1)])
print("Digite os elementos da segunda matriz complexa separados por espaços ou linhas:")
matrix2 = np.array([[complex(input(f"Elemento 2({i+1},{j+1}): ")) for j in range(cols2)] for i in range(rows2)])

# Calcula o produto tensorial
result = tensor_product(matrix1, matrix2)

# Imprime o resultado
print("\nProduto Tensorial:")
print(result)
