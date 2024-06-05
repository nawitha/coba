from abc import ABC,abstractmethod

class Manusia(ABC):
    
    @abstractmethod
    def Menari(self):
        pass
    def Berkata(self):
        print("Aku Manusia")
    
class Jawa(Manusia):
    def Menari(self):
        print("Serimpi")
    def Berkata(self):
        super().Berkata()
        print("Aku orang suku jawa")

class Sunda(Manusia):
    def Menari(self):
        print("Jaipong")

paidi=Jawa()
paidi.Menari()
paidi.Berkata()

Nenden=Sunda()
Nenden.Menari()


