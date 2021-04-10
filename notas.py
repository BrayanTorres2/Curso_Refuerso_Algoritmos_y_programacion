'''
Entradas
parcial1--->float
parcial2--->float
parcial3--->float
examenfinal--->float
trabajofinal---float
Salidas
notafinal--->nota-->float
'''
parcial1=float(input(""))
parcial2=float(input(""))
parcial3=float(input(""))
examenfinal=float(input(""))
trabajofinal=float(input(""))
nota= ((parcial1+parcial2+parcial3)/3)*0.55+(examenfinal*0.30)+(trabajofinal*0.15)
print("su nota final es: "+str(nota))