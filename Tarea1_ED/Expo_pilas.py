# 1.crear pila vacia
historial = []

# 2. Aplicar / Push (Agregar Elementos)
historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")


print("Historial:", historial)

# 3. ver el elemento superior (Peek / Cima)
pagina_actual = historial[2]
print("Página actual:", pagina_actual)

# 4. Desapilar / Pop (Eliminar el ultimo ingresado)
pagina_salida = historial.pop()
print("Saliendo de:", pagina_salida)

print("Historial actualizando:", historial)