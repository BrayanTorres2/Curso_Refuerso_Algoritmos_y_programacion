intentos = 0
while True:
    valor = input("Ingrese un número entero: ")
    if(intentos==5):
      print("Demaciados intentos 🤡")
      break
    try:
        valor = int(valor)
        print(valor)
        break
    except:
      intentos += 1
      print("Error ingrese el valor entero❌")
        
