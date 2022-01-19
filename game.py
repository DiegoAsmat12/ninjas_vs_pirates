from classes.Ninja import Ninja
from classes.Pirate import Pirate
from classes.NinjaSombra import NinjaSombra
jugador1 = NinjaSombra("")
jugador2 = Pirate("")



print(" ******** Inicializando Juego ******** ")
ready=False
while(not ready):
    print(" ******* Opciones de juego ******* ")
    print("1. Crear Personaje")
    print("2. Modificar Inventarios")
    print("3. Ready")
    opcion = input("Elija la opcion: ")
    if(opcion==1):
        tipo=0
        print("1. Ninja")
        print("2. Pirata")
        tipo= input("Escoja el tipo: ")
        if(tipo==1):
            nombre = input("Nombre: ")
            print("1. Ninja")
            print("2. Ninja Sombra")
            print("Cualquier otro input retornará al origen")
            subtipo= input("Sub tipo: ")
            if subtipo==1: 
                jugador1 = Ninja(nombre)
            elif subtipo==2:
                jugador1=NinjaSombra(nombre)
            else:
                print("Volviendo a origen")
        elif tipo==2:
            nombre = input("Nombre: ")
            jugador2= Pirate(nombre)


    elif(opcion==2):
        inventario=0
        print("1. Ninja")
        print("2. Pirata")
        inventario= input("Escoja el inventario: ")
        nombre = input("Nombre: ")
        poder = input("Poder: ")
        cantidad = input("Cantidad")
        if(tipo==1):
            Ninja.addToInventory(nombre,poder,cantidad)
        elif tipo==2:
            Pirate.addToInventory(nombre,poder,cantidad)
    elif(opcion==3):
        if(jugador1.name!="" and jugador2.name!=""):
            print(" ***** Inicializando Juego ***** ")
            ready=True
        else:
            print
    else: print("Por favor escoja una opción de las mostradas")

print("Empezando Batalla")
turno = 1
while(jugador1.health>0 or jugador2.health>0):
    print(f"********Turno {turno}********")
    print("Ninja -> Que hago?")
    print("1. Atacar")
    print("2. Usar Inventario")
    accionNinjaDecidida = False
    while(not accionNinjaDecidida):
        accion=input("Accion: ")
        if(accion==1):
            jugador1.attack(jugador2)
            accionNinjaDecidida=True
        elif(accion==2):
            print("Usando Objeto")
            accionNinjaDecidida=True
        else:
            print("Escoger una acción valida")

    print("Pirata -> Que hago?")
    print("1. Atacar")
    print("2. Usar Inventario")
    accionPirataDecidida = False
    while(not accionPirataDecidida):
        accion=input("Accion: ")
        if(accion==1):
            jugador2.attack(jugador1)
            accionPirataDecidida=True
        elif(accion==2):
            print("Usando Objeto")
            accionPirataDecidida=True
        else:
            print("Escoger una acción valida")

