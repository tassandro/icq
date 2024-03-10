import numpy as np
import matplotlib.pyplot as plt

def plot_complex_addition(c):
    # Definindo os valores de v como números complexos
    v_values = [complex(i, j) for i in range(-1, 1) for j in range(-1, 1)]

    # Calcular o vetor do número complexo c
    c_vector = np.array([0, c.real]), np.array([0, c.imag])

    # Calculando os limites dos eixos x e y
    x_min = min(c.real, min(v.real for v in v_values))
    x_max = max(c.real, max(v.real for v in v_values))
    y_min = min(c.imag, min(v.imag for v in v_values))
    y_max = max(c.imag, max(v.imag for v in v_values))

    # Plotar a soma c + v para cada valor de v
    for v in v_values:
        result = c + v
        plt.plot(result.real, result.imag, marker='o', label=f'v={v}')

    # Plotar o vetor de c
    plt.quiver(*c_vector, color='red', angles='xy', scale_units='xy', scale=1, label='c')

    # Adicionando detalhes ao gráfico
    plt.title('Soma c + v para diferentes valores de v')
    plt.xlabel('Real')
    plt.ylabel('Imaginário')
    plt.legend()
    plt.grid(True)
    plt.xlim(x_min - 1, x_max + 1)
    plt.ylim(y_min - 1, y_max + 1)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Exemplo de uso
c = complex(input("Informe o número complexo c: "))
plot_complex_addition(c)
