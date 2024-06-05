class Manusia:
    def __init__(self, nama, umur) : 
        self.nama = nama
        self.umur = umur

    def sapa(self):
        print(f'Halo,nama saya {self.nama} dan saya berumur {self.umur}')

Manusia1 = Manusia("Mingyu",27)
Manusia2 = Manusia("S.Coups",30)

Manusia1.sapa()
Manusia2.sapa()