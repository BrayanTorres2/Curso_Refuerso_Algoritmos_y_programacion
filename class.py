"""
from dataclasses import dataclass
@dataclass
class Cuenta:
  numero: int
  saldo: int
banco=[Cuenta(6,50_000),Cuenta(3,60_000),Cuenta(1,150_000),Cuenta(9,90_000),Cuenta(10,250_000),Cuenta(11,850_000),Cuenta(2,20_000),Cuenta(4,10_000),Cuenta(20,900_000)] """

class Persona:
  def __init__(self,edad:int,nombre:str,peso:float,id:int):
     self.edad=edad
     self.nombre=nombre
     self.peso=peso
     self.id=id

  def dormir(self):
     print("esta durminedo",self.nombre)  
  def mayor_edad(self):
      if(self.edad>=18):  
        print("es mayor de edad",self.nombre) 
      else:
        print("es menor de edad",self.nombre)    

from dataclasses import dataclass
@dataclass
class Cuenta:
    numero: int
    saldo: float
    def consultar(self):
      print("este es tu saldo",self.saldo)
if __name__ == '__main__':
  """     
  leidy=Persona(18,"Leidy Johana",55.0,1234567)
  leidy.dormir()
  leidy.mayor_edad() 
  print(leidy.edad) 
  """
  banco=Cuenta(123,10000.0)
  banco.consultar()  
