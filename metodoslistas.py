#Métodos de las listas
#append()
#clear()
#extend() une una lista con otra
#count()
#index()
#insert(posicion,elemento)
#pop()
#remove()
#reverse()
#sort()
#.sort(reverse=True)
#lista
#tuplas
frutas=["Mango","Coco","Banano","Manzana","Pera","Coco"]
numeros=[1,3,4,2,6,7,8,3,4]
fruta="Uva"
frutas.append(fruta)
#frutas.clear()
#frutas.extend(numeros)
#c=frutas.count("Coco")
#print(len(frutas))
p=frutas.index("Banano")
frutas.insert(0,"Fresa")
#frutas.pop(0)
#frutas.remove("Banano")
#numeros.remove(3)
#numeros.sort(reverse=True)
frutas_tupla=("Mango","Coco","Banano","Manzana","Pera","Coco")
frutas_tupla.sort()
print(frutas_tupla.count("Coco"))
