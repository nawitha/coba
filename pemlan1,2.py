class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        pass #tidak dieksekusi

class Kucing(Hewan):
    def suara(self):
        return('meoww') #mengembalikan nilai
    
class Sapi(Hewan):
    def suara(self):
        return('mooooo')
    
class Ayam(Hewan):
    def suara(self): 
        return('petokpetok')
    
kucing = Kucing('momo')
sapi = Sapi('mimi')
ayam = Ayam('ciki')

print(f'{kucing.nama} bersuara {kucing.suara()}')
print(f'{sapi.nama} bersuara {sapi.suara()}')
print(f'{ayam.nama} bersuara {ayam.suara()}')