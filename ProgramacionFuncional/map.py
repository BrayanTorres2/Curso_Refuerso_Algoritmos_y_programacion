#Funciones de orden Superior
#funcion Map (funcion,lista)
def mitad(n):
  return n/2
lista=[1,2,3,4,5,6,7,8,9]
print(list(map(mitad,lista)))
print(list(map(lambda n:n*3,lista)))
