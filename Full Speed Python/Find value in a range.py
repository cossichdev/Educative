x = int(input("Enter a number (X): "))  # se pide al usuario que ingrese un numero

y = int(input("Enter a number (Y): "))  # se pide al usuario que ingrese un numero

def inRange(x, y): # funcion que verifica si un numero esta en un rango
  return (x < 1/3 < y)  # si el numero esta en el rango, retorna True

print(inRange(x, y)) # llamada a la funcion

