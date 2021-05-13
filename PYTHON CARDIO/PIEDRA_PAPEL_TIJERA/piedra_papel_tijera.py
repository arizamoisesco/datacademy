import random

piedra = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijeras = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def juego(jugador: int, computadora: int) -> str:
    intentos = 0
    puntos_computadora = 0 
    puntos_usuario = 0 
    while intentos < 3:
        opciones = f"Piedra {piedra}", f"Papel{papel}", f"Tijera {tijeras}"
        print(f"Tu escogiste {opciones[mano_usuario]} y el computador {opciones[mano_cpu]}")

        if(mano_usuario == 0 and mano_cpu == 0):
            print("Quedaron empatados")
        elif(mano_usuario == 0 and mano_cpu == 1):
            print("Perdiste punto para la computadora")
        elif(mano_usuario == 0 and mano_cpu == 2):
            print("Ganaste punto para ti")
        elif(mano_usuario == 1 and mano_cpu == 0):
            print("Ganaste punto para ti")
        elif(mano_usuario == 1 and mano_cpu == 1):
            print("Quedaron empatados")
        elif(mano_usuario == 1 and mano_cpu == 2):
            print("Perdiste: tijera corta papel")
        elif(mano_usuario == 2 and mano_cpu == 0):
            print("Perdiste: La roca destruye la tijera")
        elif(mano_usuario == 2 and mano_cpu == 1):
            print("Ganaste")
        elif(mano_usuario == 2 and mano_cpu == 2):
            print("Quedaron empatados")
        else: 
            print("Seleccionaste una opción incorrecta")
    
if __name__ == "__main__":
    print("Bienvenido al juego de piedra, papel y tijera")
    mano_usuario = int(input("¿Cuál opción deseas? Escribe piedra(0), papel(1), tijeras(2)"))
    mano_cpu = random.randint(0, 2)
    juego(mano_usuario, mano_cpu)