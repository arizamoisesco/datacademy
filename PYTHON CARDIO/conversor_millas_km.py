#Recibimos los datos del usuario convertidos a números
print("Bienvenido señor usuario")
distancia = float(input("Ingrese la distancia que desea convertir: "))
#Ejecuto la conversión
kilometros = distancia * 1.609344 
#Genero el resultado en pantalla
print(f"El resultado de su conversión es: {kilometros} km")
