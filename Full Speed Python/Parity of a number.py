n = int(input("Enter a number: ")) #se pide al usuario que ingrese un numero

def checkParity(n): #funcion que verifica si un numero es par o impar
  result = (n % 2) #si el residuo de la division es 0, el numero es par
  return result #retorna el resultado

if checkParity == 0: #si el numero es par
  print("El numero es par") #se imprime que el numero es par
else:
    print("El numero es impar") #si no, se imprime que el numero es impar
print(checkParity(n)) #llamada a la funcion
