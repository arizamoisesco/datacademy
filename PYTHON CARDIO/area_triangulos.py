base = float(input("Ingrese la base del triangulo en cm: "))
altura = float(input("Ingrese la altura del trinagulo en cm: "))


def area(b: float, h: float) -> float:
    resultado_area = (b * h) / 2
    return resultado_area


def escaleno(lado1: float, lado2: float, lado3: float) -> bool:
    if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        return True
    else:
        return False


def equilatero(lado1: float, lado2: float, lado3: float) -> bool:
    if lado1 == lado2 and lado2 == lado3:
        return True
    else:
        return False


def isoceles(lado1: float, lado2: float, lado3: float) -> bool:
    if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return True
    else:
        return False


if __name__ == "__main__":
    resultado = area(base, altura)
    print(f"El area de su triángulo es: {resultado} cm")
    opcion_tipo_triangulo = input(
        "¿Desea averiguar que tipo de triangulo tiene S/N?"
    ).upper()
    if opcion_tipo_triangulo == "S":
        print("Ingrese a continuación los otros lados restantes\n")
        lado1 = float(input("lado 1: "))
        lado2 = float(input("Lado 2: "))
        if escaleno(base, lado1, lado2):
            print("Su triangulo es escaleno")
        elif equilatero(base, lado1, lado2):
            print("Su triangulo es equilatero")
        elif isoceles(base, lado1, lado2):
            print("Su triángulo es isoceles")
    else:
        print("Gracias por usuarme")
