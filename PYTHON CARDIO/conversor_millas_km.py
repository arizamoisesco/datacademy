#Recibimos los datos del usuario convertidos a números
print("Bienvenido señor usuario")
operacion_deseada = input("¿Qué conversión desea realizar?\n(a)km -> millas\n(b)millas -> km\nIngrese la letra de la opción deseada: ").lower()
if(operacion_deseada == "a"):
    distancia = float(input("Ingrese la distancia en km que desea convertir: "))
    kilometros = distancia / 1.609344 
    print(f"El resultado de su conversión es: {kilometros} millas")
elif(operacion_deseada == "b"):
    distancia = float(input("Ingrese la distancia en millas que desea convertir: "))
    kilometros = distancia * 1.609344 
    print(f"El resultado de su conversión es: {kilometros} km")
#Ejecuto la conversión

#Genero el resultado en pantalla

