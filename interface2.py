from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def luas(self):
        pass
    @abstractmethod
    def keliling(self):
        pass

class persegi_panjang(shape):
    def __init__(self,panjang,lebar):
        self.panjang=panjang
        self.lebar=lebar
    def luas(self):
        return self.panjang*self.lebar
    def keliling(self):
        return 2*self.panjang + self.lebar

L1=persegi_panjang(7,8)
print("luas persegi panjang:",L1.luas())
print("keliling persegi panjang:",L1.keliling())


