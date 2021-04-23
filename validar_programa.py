import random
a=random.randint(0, 100)
c=0
intentos = 0
while True:
    numero = input("Ingrese un número entero: ")
    
    if (numero=="FIN"):
      break
    else:
      if(intentos==5):
        print("Demaciados intentos fuera de caracteres 🤡")
        break
      try:
          numero=int(numero)
          if(c==5):
            print("Demaciados intentos del rango establecido 🤡")
            break
          if(numero>=0 and numero<=100):          
            if(numero>a):
              print("es mayor")
            elif(numero<a):
              print("es menor")  
            else:
              print("Ganaste el numero es: "+str(a))
              break
          else:
            print("Numero fuera de rango")
            c+=1
      except:
        intentos += 1
        print("Error ingrese el valor entero❌")
