class Bunga:
    def __init__(self, jenis):
        self.jenis = jenis

    def warna(self):
        pass
    def asal(self):
        pass #tidak dieksekusi

class Matahari(Bunga):
    def warna(self):
        return('kuning') #mengembalikan nilai
    def asal(self):
        return('amerika')
    
class Sakura(Bunga):
    def warna(self):
        return('pink dan putih')
    def asal(self):
        return('jepang')
    
class Tulip(Bunga):
    def warna(self): 
        return('ungu')
    def asal(self):
        return('belanda')
    

    
matahari = Matahari('Matahari Helianthus')
sakura = Sakura('Sakura Musk')
tulip = Tulip('Tulip Angelique')

print(f'Bunga {matahari.jenis} berwarna {matahari.warna()} berasal dari negara {matahari.asal()}')
print(f'Bunga {sakura.jenis} berwarna {sakura.warna()} berasal dari negara {sakura.asal()} ')
print(f'Bunga {tulip.jenis} berwarna {tulip.warna()} berasal dari negara {tulip.asal()}')