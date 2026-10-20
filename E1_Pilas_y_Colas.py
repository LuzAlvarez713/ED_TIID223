
from collections import deque

def menu_cola():
    cola = deque()

    while True:
        print("------ MENU DE COLAS ------")
        print("1. Insertar en cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Regresar al menu principal")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            try:
                numero = int(input("Ingresa un numero: "))
                cola.append(numero)
                print("Numero insertado correctamente.")
            except ValueError:
                print("Error: ingresa un numero entero.")

        elif opcion == "2":
            if cola:
                eliminado = cola.popleft()
                print("Elemento eliminado:", eliminado)
            else:
                print("La cola esta vacia.")

        elif opcion == "3":
            if cola:
                print("Elementos de la cola:", list(cola))
            else:
                print("La cola esta vacia.")

        elif opcion == "4":
            break

        else:
            print("Opcion no valida.")


def menu_pila():
    pila = deque()

    while True:
        print("------ MENU DE PILAS ------")
        print("1. Insertar en pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Regresar al menu principal")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            try:
                numero = int(input("Ingresa un numero: "))
                pila.append(numero)
                print("Numero insertado correctamente.")
            except ValueError:
                print("Error: ingresa un numero entero.")

        elif opcion == "2":
            if pila:
                eliminado = pila.pop()
                print("Elemento eliminado:", eliminado)
            else:
                print("La pila esta vacia.")

        elif opcion == "3":
            if pila:
                print("Elementos de la pila (base a tope):",
                      list(pila))
            else:
                print("La pila esta vacia.")

        elif opcion == "4":
            break

        else:
            print("Opcion no valida.")


# Menu principal
while True:
    print("------ PILAS Y COLAS ------")
    print("1. Trabajar con colas")
    print("2. Trabajar con pilas")
    print("3. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        menu_cola()

    elif opcion == "2":
        menu_pila()

    elif opcion == "3":
        repetir = input(
            "Deseas ejecutar nuevamente el programa? (s/n): "
        ).lower().strip()

        if repetir == "s":
            print("Volviendo al menu principal...")
        else:
            print("Programa finalizado.")
            break

    else:
        print("Opcion no valida.")
