from dataclasses import dataclass
@dataclass
class Cuenta:
  numero: int
  saldo: int
banco=[Cuenta(6,50_000),Cuenta(3,60_000),Cuenta(1,150_000),Cuenta(9,90_000),Cuenta(10,250_000),Cuenta(11,850_000),Cuenta(2,20_000),Cuenta(4,10_000),Cuenta(20,900_000)]  
#Usando map y filter obtener los numeros de cuenta de aquellas cuentas que tengan menos de 50_000 de saldo
print(list(map(lambda x: x.numero,filter(lambda x:x.saldo<50000,banco))))
#obtener el saldo de nos numero de cuenta impar
print(list(map(lambda x: x.saldo,filter(lambda x: x.numero%2!=0,banco))))
#obtener el numero de cuentas que sean multiplos de 2
print(list(map(lambda x: x.numero,filter(lambda x: x.numero%2==0,banco))))
