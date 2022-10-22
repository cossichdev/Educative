x = int(input("Enter a number (X): "))  # se pide al usuario que ingrese un numero

y = int(input("Enter a number (Y): "))  # se pide al usuario que ingrese un numero

def inRange(x, y): # funcion que verifica si un numero esta en un rango
  
  result = (x < 1/3 < y) # si el numero esta entre 1/3 y y, retorna True
  
  return result # retorna el resultado

print(inRange(x, y)) # llamada a la funcion

