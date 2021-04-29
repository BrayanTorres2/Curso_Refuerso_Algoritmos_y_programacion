numero1=int(input("Digite Numero Uno: "))
numero2=int(input("Digite Numero Dos:  "))
operador=input(" * / + - %: ")
if(operador=="+"):
  funcion=lambda a,b: a+b
elif(operador=="-"):
  funcion=lambda a,b: a-b
elif(operador=="/"):
  funcion=lambda a,b:a/b
elif(operador=="*"):
  funcion=lambda a,b:a*b
elif(operador=="/"):
  funcion=lambda a,b:a/b
print("el resultado es: "+str(funcion(numero1,numero2)))