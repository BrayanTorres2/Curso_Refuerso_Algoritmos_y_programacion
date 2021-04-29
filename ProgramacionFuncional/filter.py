#Funciones de orden Superior
#funcion filter (funcion,lista)
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
def es_par(n):
  if(n%2==0):
    return True
  else:
    return False
print(list(filter( es_par, lista)))
print(list(filter(lambda n:n%2==0, lista)))
