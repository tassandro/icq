import numpy as np
import matplotlib.pyplot as plt

def plot_complex_power(x):
    n_values = range(1, 11)  # Valores de n de 1 a 10
    results = []  # Lista para armazenar os resultados de x^n para cada valor de n

    for n in n_values:
        result = x ** n
        results.append(result)

    # Plotando os pontos no plano complexo
    plt.figure(figsize=(8, 6))
    for n, result in zip(n_values, results):
        plt.plot(result.real, result.imag, marker='o', label=f'n={n}')

    # Adicionando detalhes ao gráfico
    plt.title('Variação de x^n para n de 1 a 10')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Exemplo de uso
x = complex(input("Informe o número complexo x: "))
plot_complex_power(x)
print('\n\nA cada operação, conforme o módulo do número, ele pode se aproximar ou se afastar mais da origem, além de rotacionar sempre do mesmo ângulo.')
