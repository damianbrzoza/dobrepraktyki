import os
from abc import ABC
from abc import abstractmethod



class    mojaBazowaKlasa(ABC):
    #To jest moja klasa bazowa
    def __init__(Self):
        Self.Moja_Lista = []
        print("INIT")
        
    def DodajDoListy(This, O):
        This.Moja_Lista.append(O)
    @abstractmethod
    def WYPISZLISTE(This):
        raise NotImplementedError

class MOJA_KLASA0(mojaBazowaKlasa):
    def __init__(Self):
        mojaBazowaKlasa.__init__(  Self)
        print("INIT2")
    def WYPISZLISTE(This):
        for I in               range(len(This.Moja_Lista)):
        
        
        
          print(This.Moja_Lista[I])

class MOJA_KLASA(mojaBazowaKlasa):
    def __init__(Self):
        mojaBazowaKlasa.__init__(  Self)
        print("INIT2")
    def WYPISZLISTE(This):
        print(", ".join(This.Moja_Lista))


class punkt():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
class kostka:
    def __init__(self,punktA, punktB, punktC, punktD):
        self.PunktA = punktA
        self.PunktB = punktB
        self.PunktC = punktC
        self.PunktD = punktD

    def oblicz(self):
        return  (self.PunktA.a + self.PunktA.b + self.PunktA.c) ** 2  + (self.PunktB.a+self.PunktB.b+self.PunktB.c) ** 2  + (self.PunktC.a + self.PunktC.b + self.PunktC.c) ** 2 + (self.PunktD.a + self.PunktD.b + self.PunktD.c) ** 2
    


MojaKlasa = MOJA_KLASA0()
MojaKlasa2 = MOJA_KLASA()

MojaKlasa.DodajDoListy(4)
MojaKlasa.DodajDoListy(5)
MojaKlasa.DodajDoListy(2)
MojaKlasa.DodajDoListy(10)
MojaKlasa.DodajDoListy(30)


 
MojaKlasa2.DodajDoListy('a')
MojaKlasa2.DodajDoListy(" ala ma kota")
MojaKlasa2.DodajDoListy('kolejny Element')
MojaKlasa2.DodajDoListy('wez')
MojaKlasa2.DodajDoListy('to popraw')     

MojaKlasa.WYPISZLISTE()
MojaKlasa2.WYPISZLISTE()

Kostka = kostka(punkt(1,2,3),punkt(2,2,2),punkt(3,3,3),punkt(2,3,1))

print(Kostka.oblicz()    )
        