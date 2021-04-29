#Funciones de orden Superior
#funcion filter (funcion,lista)
frutas=["Manzana","Pera","Coco","Papaya","Durazno","Melon","Mango"]
#Usando Filter obtener cuantas flutas empiezan M       
def m(lista):
  if(lista[0]=="M"):
    return True
  else:
    return False   
print(len(list(filter(m,frutas))))
print(len(list(filter(lambda palabra:palabra[0]=="M",frutas ))))  

""""
#asi se hace a la antigua
copia=[]
for i in frutas:
  if(i[0]=="M"):
    copia.append(i)
    
print(len(copia))    
"""
