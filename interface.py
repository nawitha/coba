from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def luas(self):
        pass
    @abstractmethod
    def keliling(self):
        pass

class lingkaran(shape):
    def __init__(self,jari2): #constracter
        self.jari2=jari2
    def luas(self):
        return 3.14*self.jari2*self.jari2
    def keliling(self):
        return 2*3.14*self.jari2

L1=lingkaran(7)
print("luas lingkaran:",L1.luas())
print("keliling lingkaran:",L1.keliling())


