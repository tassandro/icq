k = 1j

print(k**2)
print(k**3)
print(k**4)
print(k**5)

def calcular_potencias_i(n):
        if n % 4 == 1:
            print(f'i^{n} = i')
        elif n % 4 == 2:
            print(f'i^{n} = -1')
        elif n % 4 == 3:
            print(f'i^{n} = -i')
        else:
            print(f'i^{n} = 1')

calcular_potencias_i(15)
