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
    
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

def get_complex_number():
    real = float(input("Digite a parte real do número complexo: "))
    imaginary = float(input("Digite a parte imaginária do número complexo: "))
    return ComplexNumber(real, imaginary)

# Obter os números complexos do usuário
print("Digite o primeiro número complexo:")
c1 = get_complex_number()

print("Digite o segundo número complexo:")
c2 = get_complex_number()


print(c1.conjugate()+c2.conjugate())
print((c1+c2).conjugate())
print(c1.conjugate()+c2.conjugate()==(c1+c2).conjugate())

print(c1.conjugate()*c2.conjugate())
print((c1*c2).conjugate())
print(c1.conjugate()*c2.conjugate()==(c1*c2).conjugate())


