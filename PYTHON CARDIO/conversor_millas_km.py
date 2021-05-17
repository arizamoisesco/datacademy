#Recibimos los datos del usuario convertidos a números

def conversion(opcion: str) -> str:
    if(opcion == "a"):
        distancia = float(input("Ingrese la distancia en km que desea convertir: "))
        kilometros = distancia / 1.609344 
        return f"El resultado de su conversión es: {kilometros} millas"
    elif(opcion == "b"):
        distancia = float(input("Ingrese la distancia en millas que desea convertir: "))
        kilometros = distancia * 1.609344 
        return f"El resultado de su conversión es: {kilometros} km"

if __name__ == "__main__":
    print("Bienvenido señor usuario")
    operacion_deseada = input("¿Qué conversión desea realizar?\n(a)km -> millas\n(b)millas -> km\nIngrese la letra de la opción deseada: ").lower()
    respuesta = conversion(operacion_deseada)
    print(respuesta)

