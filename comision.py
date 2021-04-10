"""
Entradas
sueldobase-->float-->sb
venta1-->float--venta1
venda2-->flaot--->venta2
venta3-->float--->venta3
Salidas
comision-->float-->comsion
total-->float-->total
"""
#comentario una sola linea
sb=float(input("Digite sueldo base: "))
venta1=float(input("Digite venta1: "))
venta2=float(input("Digite venta2: "))
venta3=float(input("Digite venta3: "))
comision=(venta1+venta2+venta3)*0.10
total=sb+comision
print("La comision es: "+str(comision)," total de la nomina es: "+str(total))
