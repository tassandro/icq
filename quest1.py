import math
#a equação dada pode ser reduzida a uma equação do segundo grau usando a substituição x**2=y
def solve_quadratic(a, b, c):

  discriminant = b**2 - 4*a*c
  if discriminant < 0:
    return None
  else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return root1, root2

roots = solve_quadratic(1, 2, 1)

# Print the result
if roots is None:
  print("A equação y^2 + 2y + 1 = 0 não tem solução real.")
else:
  print("A equação y^2 + 2y + 1 = 0 tem solução real:, logo, x^2 - (",roots[0],")=0 e x^2 - (",roots[1],")=0.")

roots1=solve_quadratic(1,0,1)
if roots1 is None:
  print("A equação x^2 + 1 = 0 não tem solução real.")
else:
  print("A equação x^2 + 1 = 0 tem pelo menos uma solução real:", roots1)

