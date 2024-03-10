import numpy as np

def complex_vector_addition(vec1, vec2):
    return vec1 + vec2

def complex_vector_inverse(vec):
    return -vec

def complex_scalar_multiplication(vec, scalar):
    return scalar * vec

n = int(input("Digite a dimensão dos vetores complexos: "))

vec1 = np.array([complex(input(f"Digite o elemento {i+1} do primeiro vetor complexo: ")) for i in range(n)])
vec2 = np.array([complex(input(f"Digite o elemento {i+1} do segundo vetor complexo: ")) for i in range(n)])

# Operações com os vetores
addition_result = complex_vector_addition(vec1, vec2)
inverse_result = complex_vector_inverse(vec1)
scalar = complex(input("Digite o escalar complexo para a multiplicação: "))
scalar_multiplication_result = complex_scalar_multiplication(vec1, scalar)

# Imprimir resultados
print("Resultado da adição:", addition_result)
print("Resultado da inversa do primeiro vetor:", inverse_result)
print("Resultado da multiplicação escalar:", scalar_multiplication_result)
