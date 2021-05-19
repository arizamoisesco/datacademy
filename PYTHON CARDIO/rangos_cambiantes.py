
if __name__ == "__main__":
    limite_superior = int(input("Ingrese un número: "))
    limite_inferior = int(input("Ingrese otro número: "))
    comparacion = int(input("Ingrese el número a comparar: "))

    if comparacion > limite_inferior and comparacion < limite_superior:
        print(f"El número {comparacion} esta dentro del rango")
    else:
        print(f"El número {comparacion} esta fuera del rango")