numeros = [10, 20, 30, 40, 50]

#1
numeros = [10, 20, 30, 40, 50]

print(numeros[2])

#2
numeros = [10, 20, 30, 40, 50]

numeros[2] = 100

print(numeros)

#3
numeros = [10, 20, 30, 40, 50]

numeros.append(60)

print(numeros)

#4
numeros.append([60, 70])
print(numeros)

#5
numeros.append(60)
numeros.append(70)
print(numeros)

#6
numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print(numeros[5][0])

#Insert (1)
numeros = [10, 20, 30, 40]

numeros.insert(2, 25)

print(numeros)

#2
numeros = [10, 20, 30, 40]

numeros = numeros + [50]

print(numeros)

#3
numeros = [10, 20, 30, 40]

numeros = numeros + [50,60,70]

print(numeros)

#Extend() 1.
numeros = [10, 20, 30]

otros_numeros = [40, 50, 60]

numeros.extend(otros_numeros)

# len
numeros = [10, 20, 30]

numeros[len(numeros):] = [40]

print(numeros)

#Calificaciones 

calificaciones = [70, 85, 90, 65]

calificaciones = [70, 85, 90, 65]

calificaciones.append(95)

calificaciones.insert(2, 80)

print(calificaciones)

#Colores
colores = ["Azul", "Negro", "Rosa"]

colores.extend(["Verde", "Morado", "Rojo"])

print(colores)

print(colores[1])


#2
Colores = ["Negro"]
print(Colores)

#Posiciones
numeros = [10, 20, 30, 40]

numeros.insert(2, 95)
numeros.insert(5, 50)
numeros.append(67)

print(numeros)

print("El número 95 está en el índice:", numeros.index(95))
print("El número 67 está en el índice:", numeros.index(67))

for i in range(len(numeros)):
    print("Índice", i, ":", numeros[i])