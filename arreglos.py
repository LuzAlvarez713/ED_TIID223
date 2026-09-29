

#Declarando un arreglo de nuemeros
numeros=[10,20,30,40,50]

#Imprime la posición 30
print(numeros[2])

#Resigno el vaor de la 3cera posición a 15
numeros[3] = 15
print(numeros)

#Agregamos un valor nuevo al final del arreglo
numeros.append(60)
print(numeros)

#Quitamos un valor del arreglo
numeros.pop(1)
print(numeros)

#Eliminamos por valor, en este caso el valor 30
numeros.remove(30)
print(numeros)

frutas=["Mango", "Manzana", "Uva", "Pera", "Maracuya"]
frutas.remove("Uva")
print(frutas)


frutas.pop(3)
print(frutas)

frutas.append("kiwi")
print(frutas)

frutas[2] = "fresa"
print(frutas)

#Declarando un arreglo vacio y el usuario lo llenaria con los valores que desee
arreglo=[]
n = int(input("ingresa el tamaño del arreglo:"))
arreglo = [0] = [0] *