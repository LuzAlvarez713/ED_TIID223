
# Practica: Pilas y Colas
# Estructura de Datos

def menu_principal():
    print("-------- PILAS Y COLAS ----------")
    print("1. Trabajar con Colas")
    print("2. Trabajar con Pilas")
    print("3. Salir")
    print("-----------------------------------")


def menu_cola():
    cola = []

    while True:
        print("---------- MENU DE COLAS ---------")
        print("1. Insertar en cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Regresar al menu principal")
        print("-----------------------------------")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            try:
                numero = int(input("Ingresa un numero: "))
                cola.append(numero)
                print("Numero insertado correctamente.")
            except ValueError:
                print("Error: debes ingresar un numero entero.")

        elif opcion == "2":
            if len(cola) > 0:
                eliminado = cola.pop(0)
                print("Elemento eliminado:", eliminado)
            else:
                print("La cola esta vacia.")

        elif opcion == "3":
            if len(cola) > 0:
                print("Elementos de la cola:", cola)
            else:
                print("La cola esta vacia.")

        elif opcion == "4":
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")


def menu_pila():
    pila = []

    while True:
        print("---------- MENU DE PILAS ----------")
        print("1. Insertar en pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Regresar al menu principal")
        print("-----------------------------------")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            try:
                numero = int(input("Ingresa un numero: "))
                pila.append(numero)
                print("Numero insertado correctamente.")
            except ValueError:
                print("Error: debes ingresar un numero entero.")

        elif opcion == "2":
            if len(pila) > 0:
                eliminado = pila.pop()
                print("Elemento eliminado:", eliminado)
            else:
                print("La pila esta vacia.")

        elif opcion == "3":
            if len(pila) > 0:
                print("Elementos de la pila:", pila)
                print("Tope de la pila:", pila[-1])
            else:
                print("La pila esta vacia.")

        elif opcion == "4":
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")


# Programa principal
while True:
    menu_principal()
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        menu_cola()

    elif opcion == "2":
        menu_pila()

    elif opcion == "3":
        print("\nHas seleccionado salir.")
        repetir = input(
            "Deseas ejecutar nuevamente el programa? (s/n): "
        ).lower().strip()

        if repetir == "s":
            print("Reiniciando programa...")
        else:
            print("Programa finalizado. Hasta pronto!")
            break

    else:
        print("Opcion no valida. Intenta nuevamente.")
