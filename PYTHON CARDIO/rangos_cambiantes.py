def organizar_numeros(num1: int, num2: int) -> tuple:
    if num1 > num2: 
       numero_mayor, numero_menor = num1, num2
    else:
        numero_mayor, numero_menor = num2, num1

    return numero_mayor, numero_menor

if __name__ == "__main__":
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    comparacion = int(input("Ingrese el número a comparar: "))

    limite_superior, limite_inferior = organizar_numeros(num1, num2)
    print("*"*30)
    print(f"Rango superior: {limite_superior}\nRango inferior: {limite_inferior}\nNúmero a comparar: {comparacion}")
    print("*"*30)
    if comparacion > limite_inferior and comparacion < limite_superior:
        print(f"El número {comparacion} esta dentro del rango")
    else:
        print(f"El número {comparacion} esta fuera del rango")
    print("*"*30)