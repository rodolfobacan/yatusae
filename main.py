import math
def angulo(a, b):
  if a<=0 or b<=0:
    print("error, ingrese valor positivo")
    bac=0
  else:
    c= math.sqrt(a**2 + b**2)
    bac= math.asin(a/c)

  return bac    
#es equivalente a la funcion main
if __name__ == "__main__":
  print("ingrese el valor de cateto a: ")
  cateto_a = float(input())
  print("ingrese el valor de cateto b: ")
  cateto_b = float(input())

  BAC= angulo(cateto_a, cateto_b)

  print("el valor del angulo del triangulo es: " + str(BAC))
  
