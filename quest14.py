def mobius_transform(z):
    if z == 0:
        return float('inf')
    else:
        return 1 / z

# Obter entrada do usuário
real = float(input("Digite a parte real do número complexo: "))
imaginary = float(input("Digite a parte imaginária do número complexo: "))
z = complex(real, imaginary)

# Aplicar a transformação de Möbius
resultado = mobius_transform(z)
print("R(x) =", resultado)
