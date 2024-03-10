import numpy as np

def inner_product(matrix_a, matrix_b):
    """
    Calcula o produto interno de duas matrizes complexas.

    Args:
    matrix_a (numpy.array): Primeira matriz complexa.
    matrix_b (numpy.array): Segunda matriz complexa.

    Returns:
    complex: Produto interno das matrizes.
    """
    # Calcula a adjunta de matrix_a
    adjoint_a = np.conj(matrix_a).T

    # Calcula o produto interno como o traço da multiplicação da adjunta de matrix_a por matrix_b
    result = np.trace(np.dot(adjoint_a, matrix_b))
    return result

# Exemplo de uso:

# Obter entrada do usuário para as matrizes complexas
rows_a = int(input("Digite o número de linhas da matriz A: "))
cols_a = int(input("Digite o número de colunas da matriz A: "))
rows_b = int(input("Digite o número de linhas da matriz B: "))
cols_b = int(input("Digite o número de colunas da matriz B: "))

print("Digite os elementos da matriz A complexa separados por espaços ou linhas:")
matrix_a = np.array([[complex(input(f"Elemento A({i+1},{j+1}): ")) for j in range(cols_a)] for i in range(rows_a)])
print("Digite os elementos da matriz B complexa separados por espaços ou linhas:")
matrix_b = np.array([[complex(input(f"Elemento B({i+1},{j+1}): ")) for j in range(cols_b)] for i in range(rows_b)])

# Verifica se as dimensões das matrizes são compatíveis para o produto interno
if cols_a != rows_b:
    print("Erro: O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.")
else:
    # Calcula o produto interno
    result = inner_product(matrix_a, matrix_b)
    print("\nProduto interno das matrizes A e B:", result)
