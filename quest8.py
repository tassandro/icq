import matplotlib.pyplot as plt

def plot_vector(vectors, colors, labels):
    plt.axvline(x=0, color='gray', lw=0.5)
    plt.axhline(y=0, color='gray', lw=0.5)
    for i in range(len(vectors)):
        plt.quiver(0, 0, vectors[i][0], vectors[i][1], angles='xy', scale_units='xy', scale=1, color=colors[i], label=labels[i])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-2, 4)  # Definindo limites do eixo x
    plt.ylim(-3, 3)  # Definindo limites do eixo y
    plt.grid()
    plt.legend()
    plt.show()

# Vetores
vector_a = (2, -1)
vector_b = (1, 1)

# Soma dos vetores
result_sum = (vector_a[0] + vector_b[0], vector_a[1] + vector_b[1])

# Subtração dos vetores
result_diff = (vector_a[0] - vector_b[0], vector_a[1] - vector_b[1])

# Plotagem dos vetores
plot_vector([vector_a, vector_b, result_sum], ['r', 'b', 'g'], ['Vetor (2,-1)', 'Vetor (1,1)', 'Soma'])
plot_vector([vector_a, vector_b, result_diff], ['r', 'b', 'g'], ['Vetor (2,-1)', 'Vetor (1,1)', 'Diferença'])
