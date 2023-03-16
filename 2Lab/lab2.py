from warrior import warrior as W
from pehotinets import pehot as P
from matros import matros as M

class newClass1(W):

    def virtualMethod(self):
        print(self.warrior+' '+self.Warriorweapon)

class newClass2(P):

    def virtualMethod(self):
        print(self.pehotinets+' '+self.Pehotweapon)

class newClass3(M):

    def virtualMethod(self):
        print(self.matros+' '+self.Matrosweapon)


Class1 = newClass1(warrior=input('Возраст воина: '))
Class2 = newClass2(pehotinets=input('Возраст пехотинца: '))
Class3 = newClass3(matros=input('Возраст матроса: '))

Class1.virtualMethod()
Class2.virtualMethod()
Class3.virtualMethod()

        
