from dataclasses import dataclass

@dataclass
class Nodo:
    info: int
    sig = None

@dataclass
class NodoDoble(Nodo):
    ant = None

primero = Nodo(3)    
nodo2 = Nodo(7)
nodo3 = Nodo(9)
primero.sig = nodo2
nodo2.sig = nodo3

p = primero
while p != None:
    print(p.info)
    p = p.sig

cabeza = NodoDoble(20)
segundo = NodoDoble(70)
tercero = NodoDoble(80)
cuarto = NodoDoble(10)
cabeza.sig = segundo
segundo.ant = cabeza
segundo.sig = tercero
tercero.ant = segundo
tercero.sig = cuarto
cuarto.ant = tercero

# cabeza -> <- segundo -> <- tercero -> <- cuarto
p = cuarto
while p != None:
    print(p.info)
    p =p.ant
