
import numpy as np
import matplotlib.pyplot as plt

def plot_complex_multiplication(a, b_real, c_imaginary):
    # Multiplicação a x b
    ab = a * b_real

    # Multiplicação a x c
    ac = a * (1j * c_imaginary)

    # Plotando os pontos no plano complexo
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Gráfico a x b
    ax[0].plot([0, ab.real], [0, ab.imag], 'r-o')
    ax[0].plot(ab.real, ab.imag, 'ro')
    ax[0].annotate(f"{ab}", (ab.real, ab.imag), textcoords="offset points", xytext=(10, 10), ha='center')
    ax[0].annotate('a * r', (ab.real/2, ab.imag/2), textcoords="offset points", xytext=(10, 10), ha='center')
    ax[0].grid(True)
    ax[0].set_title('a x r')
    ax[0].set_xlabel('Real')
    ax[0].set_ylabel('Imaginary')

    # Gráfico a x c
    ax[1].plot([0, ac.real], [0, ac.imag], 'b-o')
    ax[1].plot(ac.real, ac.imag, 'bo')
    ax[1].annotate(f"{ac}", (ac.real, ac.imag), textcoords="offset points", xytext=(10, 10), ha='center')
    ax[1].annotate('a * n', (ac.real/2, ac.imag/2), textcoords="offset points", xytext=(10, 10), ha='center')
    ax[1].grid(True)
    ax[1].set_title('a x n')
    ax[1].set_xlabel('Real')
    ax[1].set_ylabel('Imaginary')

    plt.tight_layout()
    plt.show()

# Exemplo de uso
c = complex(input("Informe o número complexo c: "))
b_real = float(input("Informe o número real r: "))
c_imaginary = float(input("Informe o número imaginário n (sem a unidade imaginária): "))

plot_complex_multiplication(a, b_real, c_imaginary)
