
import math

def solve_quadratic(a, b, c):

  discriminant = b**2 - 4*a*c
  if discriminant < 0:
    return None
  else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return root1, root2

roots = solve_quadratic(1, 0, 1)

# Print the result
if roots is None:
  print("A equação x^2 + 1 = 0 não tem solução real.")
else:
  print("A equação x^2 + 1 = 0 tem pelo menos uma solução real.", roots)
