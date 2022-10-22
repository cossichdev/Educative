x = 9
y = 4

def MathOp(): # Funcion que realiza las operaciones matematicas
  classic_division = x/y  #division clasica con decimales
  floor_division = x//y  #division entera sin decimales
  modulus = x % y  #modulo significa el residuo de la division
  power = x**y  #potencia significa elevar un numero a otro
  
  return [classic_division, floor_division, modulus, power] #retorna los resultados de las operaciones

[classic_division, floor_division, modulus, power] = MathOp() #llaamada a la funcion
print(classic_division)
print(floor_division)
print(modulus)
print(power)
