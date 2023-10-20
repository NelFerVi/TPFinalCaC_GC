
import random
continuar = True

while (continuar == True):
    print("\n\n############## MENU #############")
    print("[1] Adivinaste el numero1")
    print("[2] tabla de multiplicacion")
    print("[3] pipa ")
    print("[0] salir")
    print("#######################################")
    
    opcionUsuario =  input("\nIngrese una opcion:")

opcion = int( input("Menu\n1. opcion [1]\n2. Opcion [2]\nFvor ingresar opcion [1_2]:"))

if(opcion == 1):
    print("\nAccedio al menu principal 1\n")
    opcion = int( input("SubMenu \n1.1 opcion [1] \n1.2 Opcion [2] \nFavor ingresar opcion [1_2]: ") )
    if(opcion == 1):
    #InvocarFuncion1_1()
     print("\nAccedio al submenu 1.2\n")
    else:
        print("\nError de menu\n")
        
elif( opcion == 2):
    print("\nAccedio al menu principal 2\n")
    opcion = int( input("SubMenu \n2.1 Opcion [1] \n2.2 Opcion [2] \nFavor ingresar opcion [1_2]: ") )
    if( opcion == 1):
        #InvocarFuncion2_2()
        print("\nAccedio al submenu 2.1\n")
    elif( opcion == 2):
        #InvocarFuncion2_2()
        print("\nAccedio al submenu 2.2\n")
    else:
        print("\nError de menu\n")
else:
        print("\nAccedio al menu principal 3\n")
        print("\Menu sin submenu")


