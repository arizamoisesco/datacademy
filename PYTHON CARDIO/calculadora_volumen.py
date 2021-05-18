import math

def volumen_cilindro(radio, altura):
    resultado = math.pi*(radio**2)*altura
    return resultado


if __name__ == "__main__":
    radio = int(input("Ingrese el radio de la base: "))
    altura = int(input("Ingrese la altura del cilindro: "))
    resultado_volumen = volumen_cilindro(radio, altura)
    print(f"El volumen del cilindro es: {resultado_volumen}")
