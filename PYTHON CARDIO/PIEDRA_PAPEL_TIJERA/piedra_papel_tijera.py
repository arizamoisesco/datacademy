import random
import ascii_manos as manos

def definir_ganador(puntos_computadora: int, puntos_usuario: int)-> str:
    if puntos_usuario > puntos_computadora:
        return " 🥳El ganador es el usuario 😛"
    elif puntos_usuario < puntos_computadora:
        return "🤕La Computadora ha ganado 💻"
    else:
        return "Quedaron empatados🤝"


def juego(jugador: int, computadora: int) -> int:
    opciones = f"Piedra {manos.piedra}", f"Papel{manos.papel}", f"Tijera {manos.tijera}"
    print(f"Tu escogiste {opciones[mano_usuario]} y el computador {opciones[mano_cpu]}")

    if(mano_usuario == 0 and mano_cpu == 0) or (mano_usuario == 1 and mano_cpu == 1) or (mano_usuario == 2 and mano_cpu == 2):
        return 0 #Empatados
    elif (mano_usuario == 0 and mano_cpu == 1) or (mano_usuario == 1 and mano_cpu == 2) or (mano_usuario == 2 and mano_cpu == 0):
        return 1 #Gano un punto la computadora
    elif (mano_usuario == 0 and mano_cpu == 2) or (mano_usuario == 1 and mano_cpu == 0) or (mano_usuario == 2 and mano_cpu == 1):
        return 2 #Ganaste un punto
    else:
        print("Seleccionaste una opción incorrecta")


if __name__ == "__main__":
    print("Bienvenido al juego de piedra, papel y tijera")

    punto_computadora = 0
    punto_usuario = 0
    numero_ronda = 1
    while numero_ronda < 4:
        print("*"*20)
        mano_usuario = int(input("¿Cuál opción deseas? Escribe piedra(0), papel(1), tijeras(2): "))
        mano_cpu = random.randint(0, 2)

        punto = juego(mano_usuario, mano_cpu)
        if punto == 1: 
            punto_computadora += 1
            print(f"Ronda {numero_ronda} gana computadora")
        elif punto == 2:
            punto_usuario += 1
            print(f"Ronda {numero_ronda} ganaste")
        else:
            print(f"Ronda {numero_ronda} quedaron empatados")

        numero_ronda += 1

    print(definir_ganador(punto_computadora, punto_usuario))
    
    


