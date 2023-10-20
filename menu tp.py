continuar = True
while continuar == True :

    print("""##### MENU #####
    [1] Adivina el numero
    [2] Tablas de multiplicar
    [3] PiPaTi
    [0] Salir
    """)

    opcionElegida = int(input("Ingrese una opcion"))

    if opcionElegida == 1 :
        print("### Adivina el numero ###")
        from random import randint
        numeroSecreto = randint(1,100)
        numeroAdivinado = -1
        intentos = 0
        print("Tenes cinco intentos para encontrar el numero secreto")
        while intentos < 5:
            intentos = intentos + 1
            numeroAdivinado = int(input("Ingresa un numero"))
            if numeroAdivinado < numeroSecreto:
                print("El numero secreto es mas grande")
            else:
                if numeroAdivinado > numeroSecreto:
                    print("El numero es mas pequeño")
                else:
                    print("Felicitaciones encontraste el numero secreto")
                    break
        if numeroAdivinado == numeroSecreto:    
            print(f"Lograste el numero en {intentos} intento/s")
        else: 
            print("Perdiste, no has encontrado el numero secreto")   
            
    elif opcionElegida == 2 :
        print("### Tablas de multiplicar ###")
        numero = int(input("Ingresa el numero a multiplicar"))
        print(f"Tabla del {numero}")
        for i in range(1,11):
            print(f"{numero} x {i} = {numero*i}")

    elif opcionElegida == 3 :
        print("### PiPaTi ###")  
        print("Vamos a jugar al piedra, papel o tijera al mejor de 3")

        victoriasUsuario = 0
        victoriasComputadora = 0
        empates = 0
        partidas = 1
        while partidas <= 3:
            print(f"Enfrentamiento numero: {partidas}")
            opcionUsuario = int(input("Elegi: piedra (1), papel (2), tijera (3)"))
            opcionComputadora = randint(1,3)
            if opcionUsuario == opcionComputadora:
                print("Empate")
                empates = empates + 1
            else: 
                if opcionUsuario == 1 and opcionComputadora == 2: #Usuario elige piedra
                    print("Perdiste, papel mata piedra")   
                    victoriasComputadora = victoriasComputadora + 1
                elif opcionUsuario == 1 and opcionComputadora == 3: 
                    print("Ganaste, piedra mata tijera")
                    victoriasUsuario = victoriasUsuario + 1
                elif opcionUsuario == 2 and opcionComputadora == 1: #Usuario elige papel
                    print("Ganaste, papel mata piedra")
                    victoriasUsuario = victoriasUsuario + 1
                elif opcionUsuario == 2 and opcionComputadora == 3:
                    print("Perdiste, tijera mata papel")
                    victoriasComputadora = victoriasComputadora + 1
                elif opcionUsuario == 3 and opcionComputadora == 1: #Usuario elige tijeras
                    print("Perdiste, piedra mata tijera")
                    victoriasComputadora = victoriasComputadora + 1
                else:
                    print("Ganaste, tijera mata papel")
                    victoriasUsuario = victoriasUsuario + 1   
            
            partidas = partidas + 1

        print("Resultados:")    
        print(f"Vos: {victoriasUsuario}, Computadora: {victoriasComputadora}, Empates: {empates} ")

    elif opcionElegida == 0 :
        print("Saliendo...")
        continuar = False   
    else: 
        print("Opcion incorrecta. Ingrese una opcion valida")      
