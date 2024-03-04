class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)
    
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

def get_complex_number():
    real = float(input("Digite a parte real do número complexo: "))
    imaginary = float(input("Digite a parte imaginária do número complexo: "))
    return ComplexNumber(real, imaginary)

# Obter os números complexos do usuário
print("Digite o primeiro número complexo:")
c1 = get_complex_number()

print("\nDigite o segundo número complexo:")
c2 = get_complex_number()

print("\nDigite o terceiro número complexo:")
c3 = get_complex_number()

# a) Comutatividade na soma
# c1 + c2 = c2 + c1
print("\nComutatividade na soma:")
print(c1 + c2 == c2 + c1)

# a) Comutatividade na multiplicação
# c1 × c2 = c2 × c1
print("\nComutatividade na multiplicação:")
print(c1 * c2 == c2 * c1)

# b) Associatividade na soma
# (c1 + c2) + c3 = c1 + (c2 + c3)
print("\nAssociatividade na soma:")
print((c1 + c2) + c3 == c1 + (c2 + c3))

# b) Associatividade na multiplicação
# (c1 × c2) × c3 = c1 × (c2 × c3)
print("\nAssociatividade na multiplicação:")
print((c1 * c2) * c3 == c1 * (c2 * c3))

# c) Distributividade
# c1 × (c2 + c3) = (c1 × c2) + (c1 × c3)
print("\nDistributividade:")
print(c1 * (c2 + c3) == (c1 * c2) + (c1 * c3))
