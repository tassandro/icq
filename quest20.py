import numpy as np

def is_unitary(matrix):
    """
    Verifica se uma matriz é unitária.

    Args:
    matrix (numpy.array): Matriz complexa.

    Returns:
    bool: True se a matriz é unitária, False caso contrário.
    """
    # Calcula a adjunta da matriz
    adjoint = np.conj(matrix).T

    # Verifica se a matriz multiplicada pela sua adjunta é a matriz identidade
    identity_matrix = np.eye(matrix.shape[0], dtype=matrix.dtype)
    product = np.dot(matrix, adjoint)
    is_identity = np.allclose(product, identity_matrix)

    # Verifica se a inversa da matriz é igual à sua adjunta
    inverse = np.linalg.inv(matrix)
    is_inverse_equal_adjoint = np.allclose(inverse, adjoint)

    return is_identity and is_inverse_equal_adjoint

# Exemplo de uso:

# Obter entrada do usuário para a matriz complexa
rows = int(input("Digite o número de linhas da matriz: "))
cols = int(input("Digite o número de colunas da matriz: "))

print("Digite os elementos da matriz complexa separados por espaços ou linhas:")
matrix = np.array([[complex(input(f"Elemento ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)])

# Verifica se a matriz é unitária
result = is_unitary(matrix)
if result:
    print("\nA matriz é unitária.")
else:
    print("\nA matriz não é unitária.")
