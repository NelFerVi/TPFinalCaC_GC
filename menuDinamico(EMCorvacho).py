import random
continuar = True
	
while (continuar == True):
    print("\n\n############# MENU #############")
    print("[1] Adivina un numero")
    print("[2] Tablas de multiplicar")
    print("[3] PIPATI")
    print("[0] Salir")
    print("################################")
        
    opcionUsuario = input("\nIngrese una opcion: ")
    
    if(opcionUsuario == "1"):
        print("\nOpcion 1: Adivina un numero")
        numeroSecreto = random.randint(1,101)
        numeroAdivinado = -1
        intentos = 0
        
        while (intentos < 5):
            numeroAdivinado = int(input("Ingresa un numero entero: "))
            intentos = intentos + 1

            if (numeroAdivinado < numeroSecreto and intentos < 5):
                print("El numero secreto es mas grande")
            elif (numeroAdivinado > numeroSecreto and intentos < 5):
                print("El numero secreto es mas pequeño")
            elif (numeroAdivinado == numeroSecreto):
                print("\n¡¡Felicitaciones encontraste el numero secreto!!")
                print("Lograste dar con el numero en: ", intentos, " intentos.")
                break
            else:
                print("\n¡¡Que pena no lo lograste!!")
                print("El nro secreto era: ", numeroSecreto)
    
    elif(opcionUsuario == "2"):
        print("\nOpcion 2: Tablas de Multiplicar")
        nro = int(input("Ingrese que tabla desea ver: "))
        print(f"Tabla del: {nro}")
        for i in range(1,11):
            print(f"{i} x {nro} = {nro * i}")
        print()

    elif(opcionUsuario == "3"):
        print("\nOpcion 3: Piedra, Papel o Tijera")
        victUsuario = 0
        victComp = 0
        rondas = 1
        print("Se jugaran 5 rondas")
        while (rondas < 6):
            print ("Ronda nro: ", rondas)
            bandera = True
            while (bandera == True):
                miOpcion = int(input("Elige piedra(1), papel(2) o tijera(3): "))
                if (miOpcion < 1 or miOpcion > 3):
                    print ("Has ingresado una opcion incorrecta. Intenta de nuevo!!")
                else:
                    bandera = False
                    
            compOpcion = random.randint(1,3)
            if miOpcion == compOpcion:
                print("Fue Empate")
                victComp += 1
                victUsuario += 1
            else:
                if (miOpcion == 1):
                    if (compOpcion == 2): # Papel
                        print("Gana Computadora, Papel mata a piedra")
                        victComp += 1
                    else:
                        print("Ganaste, Piedra mata a Tijeras")
                        victUsuario += 1

                elif (miOpcion == 2):
                    if (compOpcion == 3): # Tijeras
                            print("Gana Computadora, Tijeras mata a Papel")
                            victComp += 1
                    else:
                        print("Ganaste, Papel mata a Piedra")
                        victUsuario += 1
                
                elif (miOpcion == 3):
                    if (compOpcion == 1): # Piedra
                        print("Gana Computadora, Piedra mata a Tijeras")
                        victComp += 1
                    else:
                        print("Ganaste, Tijeras mata a Papel")
                        victUsuario += 1
                    
            rondas = rondas + 1

        # Mostrar puntuacion partida
        print("##############################")
        print("########## Resultado #########")
        print("Vos: ", victUsuario, " Computadora: ", victComp)
        print("##############################")
        print()
        if (victUsuario > victComp):
            print("Bravo!! Ganaste!!")
        elif (victUsuario == victComp):
            print("Esto fue un empate!!!")
        else:
            print("Que pena!!! Perdiste!!!")
        print("\nFin del Juego")

    elif(opcionUsuario == "0"):
        print("\nOpcion 0: Salir del Menu")
        break
    else:
        print("Ingresaste una opcion invalida!!! Intenta de nuevo!!!")




