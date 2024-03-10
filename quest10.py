import math

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    theta_deg = math.degrees(theta)
    return r, theta_deg

def main():
    # Solicita ao usuário as coordenadas cartesianas
    x = float(input("Digite o valor de x (coordenada x): "))
    y = float(input("Digite o valor de y (coordenada y): "))

    # Converte as coordenadas cartesianas para polares
    r, theta_deg = cartesian_to_polar(x, y)

    # Exibe as coordenadas polares correspondentes
    print(f"As coordenadas cartesianas ({x}, {y}) correspondem a coordenadas polares: (r = {r}, theta = {theta_deg}°)")

if __name__ == "__main__":
    main()
