base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del trinagulo: "))

def area(b: float, h: float) -> float:
    resultado_area = (b*h)/2 
    return resultado_area

def escaleno(lado1: float, lado2: float, lado3: float) -> bool:
    if(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
        return True
    else: 
        return False

def equilatero(lado1: float, lado2: float, lado3: float) -> bool:
    if(lado1 == lado2 and lado2 == lado3):
        return True
    else:
        return False

def isoceles(lado1: float, lado2: float, lado3: float) -> bool:
    if(lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
        return True
    else:
        return False 

resultado = area(base, altura)
print(resultado)