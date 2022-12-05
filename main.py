attempts = 0
import random
options = ('piedra', 'tijera', 'papel') # las opciones representadas en una tupla

global cpu_wins
global user_wins
cpu_wins = 0
user_wins = 0
while attempts < 3: # while tres intentos
    attempts += 1 #suma un intento
    user_input = input("Piedra, papel o tijera: ") #input del usuario   
    cpu_option = random.randint(0, 2) # se genera un numero del 0 al 2 
  
    if user_input.lower() in options: # si existe el valor introducido por el usuario en la tupla ejecutar lo demas
      
        user_option = options.index(user_input.lower()) # el input del usuario se convierte en un la posicion correspondiente de la tupla
        
        print("***********")
        print("ROUND", attempts)
        print("***********")
        
        print("Usuario: ",user_input.lower()) # se muestra al usuario el string elegido
        print("CPU: ", options[cpu_option]) # se muestra el usuario la opcion de la cpu en forma de string

        # Condicionales de piedra, papel, tijera
        if user_option == cpu_option:
            print("Es un empate, intenta de nuevo")
        
        elif user_option == 0 and cpu_option == 1 :
            user_wins += 1
            print(user_input.upper(),"le gana a", options[cpu_option].upper() + ". Has ganado!")
        
        elif user_option == 1 and cpu_option == 2:
            user_wins += 1
            print(user_input.upper(),"le gana a", options[cpu_option].upper() + ". Has ganado!")
        
        elif user_option == 2 and cpu_option == 0:
            user_wins += 1
            print(user_input.upper(),"le gana a", options[cpu_option].upper() + ". Has ganado!")
        
        else:
            cpu_wins += 1
            print(options[cpu_option].upper(), "gana a", user_input.upper() + ". La CPU gana :(")

    
    
    else: # si el valor no se encuentra dentro de la tupla, no es valido
        print("La opcion ingresada no es valida, intenta con: piedra, papel o tijera")
        quit()
    
    print("-----------------")
    print("Usuario:",user_wins, "CPU:", cpu_wins)
    print("-----------------")
    
if user_wins == cpu_wins:
    print("Es un empate, comienza el juego de nuevo")
elif user_wins > cpu_wins:
    print("Le has ganado a la Computadora!!!!!!")
else:
    print("La computadora siempre gana ;)")
