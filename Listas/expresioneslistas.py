""""
# [expresion for var in list if cond]
potencias = []
for i in range(0, 11):
    potencias.append(2**i)
print(potencias)

potencias = [2 ** i for i in range(0, 11)]
print(potencias)

palabra = 'supuestamentico'
cerradas = [vocal for vocal in palabra if (vocal == 'i' or vocal == 'u')]
print(cerradas)

# Guardar los números en entre 0 y 100 
# que sean múltiplos de 2 y de 5 al mismo tiempo
lista=[numero for numero in range(0,101) if(numero%2==0 and numero%5==0)]
print(lista)

# Función que reciba un número y retorne una lista
# con los divisores de ese número entre 1 y 100
def divisores(n: int) -> [int]:
    return [numero for numero in range(1,101) if(n%numero==0)]

# Obtener la lista de primos que hay entre 2 y 100
lista1=[numero for numero in range(2,101) if(len(divisores(numero))==2)]
print(lista1)

conjunto = set(palabra)
print(conjunto)

c1 = {9, 6, 1, 4, 9, 1}
c2 = set([i for i in range(10) if i % 2 == 0])
print("c1=", c1)
print("c2=", c2)
u = c1 | c2
print(u)
inter = c1 & c2
print(inter)
difer = c1 - c2
print(difer)
x = list(c1)[0]
print("x=", x)
# Contar las veces que aparece una letra
# en una palabra
def contar_letra(pal: str, letra: str) -> int:
    return pal.count(letra)

print(contar_letra(palabra, 'u'))  
conjunto3={}
res = [(letra, contar_letra(palabra, letra)) 
          for letra in palabra]
print(set(res)) 
"""
caps = dict()
caps['LA GUAJIRA'] = 'RIOHACHA'
caps['MAGDALENA'] = 'SANTA MARTA'
caps['NARIÑO'] = 'PASTO'
caps['META'] = 'VILLAVICENCIO'
print(caps.keys())
print(caps.values())
print(list(enumerate(caps)))

dpto = input("Entra un departamento: ").upper()

if not(dpto in caps.keys()):
    print("El depto", dpto, "no existe")
else:
    capital = caps[dpto]
    print(f"La capital de {dpto} es {capital}")

frase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eu arcu maximus, sagittis massa sit amet, varius ante. Donec rhoncus vestibulum aliquet. Proin tempus eget libero in maximus. Nullam fringilla, odio ac rutrum tristique, mi magna ultricies nibh, eu cursus neque nulla sit amet purus. Nullam blandit neque mi, vitae bibendum felis bibendum a. Duis tristique risus non nisl aliquam, ut tincidunt ante ullamcorper. Fusce commodo nibh tortor, nec ultricies felis placerat sit amet. Integer sagittis non sem quis euismod. Pellentesque elementum, lacus non dapibus gravida, leo nisl blandit lorem, sit amet imperdiet sapien tellus vel dui. Aenean volutpat odio erat, nec euismod erat tempor eget. Curabitur rhoncus consequat libero id pharetra. Aliquam condimentum leo magna, sed elementum magna imperdiet et."
print(len(frase))
cont_letras = dict()
for letra in frase.upper():
    if(letra in cont_letras.keys()):
      cont_letras[letra]+=1
    else:
      cont_letras[letra]=1 
print(cont_letras)       
